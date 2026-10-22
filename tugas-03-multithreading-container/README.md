# Tugas 3 (Pekan 3) — Efisiensi Proses & Kontainer

**Materi terkait:** Threading, Virtualization, Containers.

## Studi Kasus

Server FoodGo boros sumber daya karena setiap permintaan pesanan masuk diproses sebagai **proses baru yang berat** (mis. `fork()` proses OS penuh per request). Saat 100 pesanan masuk bersamaan, server kehabisan memori karena tiap proses membawa overhead-nya sendiri.

## Tugas Kelompok

1. Implementasikan **simulasi pesanan masuk** di Python (`src/order_simulator.py`) yang memproses banyak pesanan **secara konkuren memakai multithreading** (bukan multiprocessing, bukan sekuensial biasa).
2. Program harus mensimulasikan **race condition yang sengaja dibuat lalu diperbaiki** — buktikan pemahaman kalian tentang `Lock`/sinkronisasi dengan cara:
   - Jalankan dulu versi TANPA lock, tunjukkan hasil counter yang salah (screenshot/log).
   - Perbaiki dengan `threading.Lock()`, tunjukkan hasil counter yang benar.
   - Tulis perbandingan ini di `JURNAL.md`.
3. Paketkan program ke dalam **Docker container** (`Dockerfile` disediakan skeleton-nya, lengkapi bagian yang kosong).
4. Jalankan container di laptop, buktikan program tetap berjalan benar di dalam container (screenshot/video di `bukti/`).

## Skeleton yang Disediakan

- `src/order_simulator.py` — kerangka program dengan `# TODO` di bagian logika inti (worker function, penggunaan lock, agregasi hasil). **Kalian wajib mengisi bagian TODO sendiri** — ini bagian penilaian utama.
- `requirements.txt` — kosong/minimal (program ini sengaja hanya pakai standard library Python, tidak perlu dependency eksternal).
- `Dockerfile` — kerangka dengan beberapa baris `# TODO`, lengkapi agar image bisa di-build dan dijalankan.

## Cara Menjalankan (Setelah Skeleton Dilengkapi)

Tanpa Docker (langsung di laptop, untuk debugging cepat):
```bash
cd tugas-03-multithreading-container
python3 src/order_simulator.py
```

Dengan Docker (wajib untuk submission akhir):
```bash
cd tugas-03-multithreading-container
docker build -t foodgo-order-sim .
docker run --rm foodgo-order-sim
```

## Analisis Multithreading dan Race Condition

### 1. Race Condition pada Simulasi FoodGo

Race condition merupakan kondisi ketika beberapa thread mengakses dan mengubah data bersama secara bersamaan sehingga menghasilkan nilai yang tidak konsisten. Pada simulasi FoodGo, kondisi ini dapat terjadi ketika beberapa thread memproses pesanan dan memperbarui variabel `processed_count` secara bersamaan.

Variabel `processed_count` digunakan untuk menghitung jumlah pesanan yang berhasil diproses. Tanpa mekanisme penguncian, dua thread dapat membaca nilai penghitung yang sama sebelum keduanya menambahkan angka. Akibatnya, salah satu penambahan dapat tertimpa sehingga jumlah pesanan yang tercatat lebih sedikit daripada jumlah sebenarnya.

Pada pengujian tanpa lock, jumlah pesanan yang tercatat beberapa kali hanya mencapai 99, 97, 93, atau 94 dari total 100 pesanan. Hal ini menunjukkan bahwa race condition dapat menyebabkan ketidaksesuaian data.

### 2. Perbaikan Menggunakan `threading.Lock()`

Untuk mengatasi race condition, digunakan `threading.Lock()` pada bagian kode yang mengubah variabel `processed_count`. Lock memastikan bahwa hanya satu thread yang dapat menjalankan bagian kode tersebut pada satu waktu.

Dengan mekanisme ini, thread lain harus menunggu hingga thread yang sedang memegang lock selesai memperbarui penghitung. Setelah lock dilepaskan, thread berikutnya dapat melanjutkan prosesnya.

Hasil pengujian setelah penggunaan lock menunjukkan bahwa jumlah pesanan berhasil tercatat sebanyak 100 dari total 100 pesanan. Dengan demikian, penggunaan lock membantu menjaga konsistensi data ketika beberapa thread mengakses variabel bersama.

### 3. Alasan Menggunakan Multithreading

Multithreading dipilih karena simulasi FoodGo membutuhkan beberapa tugas pemrosesan pesanan berjalan secara bersamaan dalam satu proses aplikasi. Beberapa thread dapat berbagi memori yang sama, sehingga data pesanan dapat diakses tanpa harus menggunakan mekanisme komunikasi antarproses yang lebih kompleks.

Dibandingkan dengan multiprocessing atau pembuatan proses OS terpisah untuk setiap permintaan, multithreading dapat mengurangi overhead pembuatan proses dan penggunaan sumber daya untuk skenario simulasi ini. Namun, karena thread berbagi memori, akses terhadap data bersama perlu dikelola dengan benar menggunakan mekanisme sinkronisasi seperti `threading.Lock()`.

Pendekatan ini sesuai untuk memperbaiki simulasi FoodGo yang sebelumnya berisiko mengalami pemborosan sumber daya akibat pembuatan proses OS yang berat untuk setiap permintaan. Meskipun demikian, multithreading tidak otomatis lebih cepat untuk semua jenis pekerjaan; efektivitasnya bergantung pada karakteristik beban kerja dan kebutuhan aplikasi.

## Struktur Submission

```
tugas-03-multithreading-container/
├── README.md          # Analisis: race condition, perbaikan, kenapa threading (bukan multiprocessing/proses OS)
├── JURNAL.md           # Log sebelum/sesudah lock, error yang ditemui saat build Docker
├── Dockerfile
├── requirements.txt
├── src/
│   └── order_simulator.py
└── bukti/              # Screenshot/video: hasil counter salah (tanpa lock), hasil benar (dengan lock), container jalan
```

## Rubrik Penilaian (Tugas 3)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Implementasi multithreading benar | 30% | Worker benar-benar konkuren (bukan `time.sleep` yang menyamarkan sekuensial), pakai `threading` |
| Bukti race condition & perbaikan lock | 25% | Ada bukti nyata (log/screenshot) sebelum & sesudah, bukan cuma klaim di teks |
| Dockerfile & eksekusi container | 20% | Image ter-build, container jalan dan hasilkan output yang sama seperti tanpa Docker |
| Analisis (kenapa threading, bukan proses berat) | 15% | Mengaitkan balik ke masalah "server boros resource" di studi kasus |
| Proses & kontribusi kelompok | 10% | `JURNAL.md`, commit history |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya ke AI soal opsi umum menangani race condition (mis. "apa saja cara sinkronisasi thread di Python"); **tidak boleh** meminta AI menuliskan isi bagian `# TODO` di `order_simulator.py`/`Dockerfile`. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- Bagian `# TODO` di `order_simulator.py` dan `Dockerfile` sengaja dikosongkan — solusi yang identik persis antar kelompok (termasuk nama variabel, komentar) akan diperiksa lebih lanjut.
- `JURNAL.md` wajib menunjukkan bukti nyata percobaan **sebelum** (race condition muncul) dan **sesudah** (`Lock()` dipasang) — bukan cuma klaim tanpa data pembanding.
