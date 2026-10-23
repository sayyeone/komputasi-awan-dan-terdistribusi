# Tugas 5 (Pekan 5) Koordinasi & Konsensus

**Materi terkait:** Physical/Logical Clock, Election Algorithm (Bully/Raft).

## Studi Kasus

Terjadi konflik urutan waktu pada pesanan FoodGo (dua server mencatat urutan pesanan berbeda karena jam tidak sinkron), dan sistem membutuhkan satu **"Node Leader"** untuk mengelola antrean pesanan pusat agar tidak terjadi konflik pemrosesan ganda.

## Tugas Kelompok

Implementasikan simulasi **Bully Algorithm** untuk memilih leader di antara **5 node virtual** yang berjalan sebagai 5 proses Python terpisah di laptop yang sama (tiap node = satu proses di port berbeda, komunikasi lewat TCP socket di `localhost`).

Skeleton yang disediakan (`src/node.py`) sudah menangani bagian **infrastruktur jaringan** (membuka socket, menerima & mengirim pesan antar node) bagian **algoritma Bully sendiri sengaja dikosongkan** (`# TODO`), karena itu inti pembelajaran tugas ini.

### Aturan Bully Algorithm yang harus diimplementasikan

1. Node yang mendeteksi leader tidak merespons (atau saat start pertama kali) mengirim pesan `ELECTION` ke semua node dengan ID **lebih besar** darinya.
2. Jika ada node ber-ID lebih besar yang merespons `OK`, node yang memulai election **berhenti mencalonkan diri** dan menunggu pesan `COORDINATOR`.
3. Jika **tidak ada** node ber-ID lebih besar yang merespons dalam batas waktu tertentu, node tersebut menjadi leader dan mem-broadcast `COORDINATOR` ke semua node lain.
4. Semua node mencatat siapa leader saat ini.

### Cara Menjalankan

Buka 5 terminal terpisah (satu per node):
```bash
python3 src/node.py --id 1 --port 5001 --peers 5002,5003,5004,5005
python3 src/node.py --id 2 --port 5002 --peers 5001,5003,5004,5005
python3 src/node.py --id 3 --port 5003 --peers 5001,5002,5004,5005
python3 src/node.py --id 4 --port 5004 --peers 5001,5002,5003,5005
python3 src/node.py --id 5 --port 5005 --peers 5001,5002,5003,5004
```

### Skenario Wajib Diuji & Dicatat

1. **Start normal**: nyalakan node 1–5 hampir bersamaan, catat siapa yang terpilih jadi leader (harusnya node ber-ID tertinggi, yaitu node 5).
2. **Leader mati**: matikan (Ctrl+C) proses node leader (node 5), amati node lain mendeteksi leader hilang dan memicu election baru. Catat leader baru yang terpilih (harusnya node 4).
3. Simpan log terminal (screenshot atau `> log_nodeX.txt` redirect) dari kedua skenario ke folder `bukti/`.

## Analisis Implementasi

### 1. Leader pada Sistem FoodGo

Membantu mengoordinasikan pemrosesan pesanan agar setiap node memiliki informasi yang sama mengenai pihak yang bertanggung jawab mengelola antrean pesanan pusat. Tanpa koordinasi, beberapa node dapat bertindak sebagai pengelola secara bersamaan sehingga berpotensi menimbulkan konflik pemrosesan atau duplikasi pesanan, ini juga berkaitan dengan perbedaan urutan waktu yang dicatat oleh beberapa server akibat jam yang tidak sinkron. Leader membantu menentukan satu node yang bertanggung jawab dalam koordinasi, tetapi tidak secara langsung menyelesaikan jam fisik yang tidak sinkron.

### 2. Alasan Menggunakan Bully Algorithm dibandingkan Raft

Karena mekanismenya relatif sederhana untuk disimulasikan menggunakan lima node virtual. Setiap node memiliki ID, dan node dengan ID tertinggi yang masih aktif berpeluang menjadi leader. Ketika sebuah node memulai election, node tersebut mengirim pesan `ELECTION` kepada node dengan ID lebih tinggi. Jika menerima pesan `OK`, node menunggu pengumuman leader. Jika tidak ada respons dari node yang lebih tinggi, node dapat menyatakan dirinya sebagai leader dan mengirim pesan `COORDINATOR` kepada node lainnya. Dibandingkan dengan Raft, Bully Algorithm lebih mudah dipahami untuk mempelajari proses pemilihan leader berdasarkan prioritas ID. Sementara itu, Raft menggunakan mekanisme pemilihan leader berbasis term dan pertukaran pesan antarnode, dan memiliki mekanisme replikasi log untuk menjaga konsistensi sistem, di sini menggunakan Bully Algorithm agar proses election dan pergantian leader dapat diamati dengan lebih sederhana. Tetapi Bully Algorithm memiliki keterbatasan karena bergantung pada komunikasi antarnode dan penentuan apakah sebuah node masih aktif. Algoritma ini juga tidak menyediakan mekanisme replikasi log seperti Raft, sehingga pemilihan leader saja belum cukup untuk menjamin konsistensi seluruh data pesanan dalam sistem terdistribusi.

#### 2.1 Mengapa Bully Algorithm Selalu Memilih ID Tertinggi?
 
Pemilihan ID tertinggi bukan hasil pengacakan, melainkan konsekuensi langsung dari aturan pengiriman pesan:
 
- Node yang memulai election hanya mengirim `ELECTION` kepada node ber-ID **lebih besar** dari dirinya.
- Node ber-ID lebih besar yang masih aktif membalas `OK`, sehingga pengirim berhenti mencalonkan diri. Node yang membalas tersebut kemudian memulai election sendiri ke node di atasnya.
- Proses ini berulang naik ke ID yang lebih tinggi sampai ada node yang tidak mendapat `OK` dari siapa pun dalam batas waktu `ELECTION_TIMEOUT`. Node itu pasti node aktif dengan ID tertinggi, lalu mengumumkan diri melalui `COORDINATOR`.
Contohnya, node 2 tidak akan menjadi leader selama node 3, 4, atau 5 masih aktif karena node 2 akan menerima `OK` dari salah satunya dan berhenti. Jika node 5 mati, node 4 tidak lagi menerima `OK` dari ID yang lebih tinggi sehingga node 4 menjadi leader. Aturan ini berasal dari prioritas ID, bukan dari kapasitas komputasi node.
 
#### 2.2 Kelebihan Bully Algorithm
 
- **Sederhana** hanya tiga jenis pesan (`ELECTION`, `OK`, `COORDINATOR`), sehingga mudah diimplementasikan dan diamati.
- **Deterministik** hasil election dapat diprediksi: node aktif dengan ID tertinggi selalu menang.
- **Pemulihan otomatis** ketika leader mati, node lain dapat memulai election ulang tanpa campur tangan manual.
- **Mudah diuji** skenario seperti start normal dan leader dimatikan dapat dilihat langsung pada log.
#### 2.3 Kekurangan Bully Algorithm
 
1. **Jumlah pesan dapat mencapai $O(n^2)$.** Pada kondisi terburuk, node ber-ID rendah memulai election saat seluruh node aktif. Setiap node mengirim `ELECTION` ke semua node di atasnya, dan penerima juga memulai election sendiri. Dengan $n$ sebagai jumlah node, total pesan dalam satu proses election dapat mencapai orde $n^2$. Jumlah aktual bergantung pada kondisi jaringan, waktu respons, dan apakah beberapa election berjalan bersamaan.
2. **Ada jeda tanpa leader (SPOF sementara).** Selama leader mati dan leader baru belum terpilih, operasi yang membutuhkan koordinasi leader dapat tertunda. Pada implementasi ini, `monitor_leader()` memeriksa leader dengan `PING` setiap 3 detik, lalu `ELECTION_TIMEOUT` menunggu respons selama 2 detik. Jadi kegagalan tidak langsung terdeteksi, dan jeda total sekitar 3 detik interval `PING` ditambah 2 detik *timeout*. Node lain tetap berjalan, tetapi operasi yang bergantung pada leader harus menunggu.
3. **Rentan split-brain saat partisi jaringan.** Bully Algorithm mengasumsikan node yang tidak merespons berarti mati. Jika jaringan terpecah, kedua sisi partisi dapat saling menganggap node di sisi lain mati, lalu masing-masing memilih leader sendiri. Akibatnya, dua leader dapat aktif bersamaan dan mengelola antrean pesanan secara terpisah.
4. **Tidak mempertimbangkan kondisi node.** Pemilihan hanya berdasarkan ID, bukan CPU, beban kerja, latensi jaringan, atau kesehatan layanan, sehingga leader terpilih belum tentu kandidat paling optimal.
5. **Tidak ada replikasi log.** Bully hanya menentukan siapa leader. Tidak ada kesepakatan mayoritas atau replikasi data, sehingga pemilihan leader saja belum menjamin konsistensi seluruh data pesanan.
#### 2.4 Perbandingan Bully Algorithm dan Raft
 
| Aspek | Bully Algorithm | Raft |
|---|---|---|
| Dasar pemilihan leader | Node aktif dengan ID tertinggi | Kandidat yang memperoleh dukungan mayoritas |
| Mekanisme election | `ELECTION` → `OK` → `COORDINATOR` | *Term*, permintaan suara (*request vote*), dan voting |
| Jumlah pesan | Dapat mencapai $O(n^2)$ pada kondisi terburuk | Bergantung pada jumlah node, jaringan, dan jumlah percobaan; tidak selalu lebih sedikit |
| Penanganan kegagalan leader | Node yang mendeteksi kegagalan memulai election ulang | Node memulai election ketika leader dianggap tidak tersedia |
| Partisi jaringan | Rentan split-brain (dua leader dapat muncul) | Hanya partisi yang memegang mayoritas yang dapat memilih leader |
| Konsistensi data | Tidak menjamin konsistensi data | Replikasi log dengan aturan mayoritas |
| Jeda tanpa leader | Ada jeda selama deteksi dan election | Ada jeda selama election; bergantung pada mayoritas yang tersedia |
| Kompleksitas implementasi | Relatif sederhana | Lebih kompleks (term, voting, log, aturan konsistensi) |
 
Raft tidak menghilangkan kebutuhan akan leader. Ketika leader gagal, election baru tetap diperlukan. Perbedaan utamanya terletak pada jaminan konsensus dan konsistensi data, bukan pada jumlah pesan semata. Untuk FoodGo skala kecil, Bully cukup untuk mempelajari dasar pemilihan leader. Jika FoodGo membutuhkan konsistensi antrean dan replikasi data yang lebih kuat, Raft lebih relevan untuk dipertimbangkan.

### 3. Analisis Skenario Pengujian

#### Skenario 1: Start Normal

Pada skenario ini, lima node dijalankan hampir bersamaan. Setiap node memulai proses election dan mengirim pesan `ELECTION` kepada node yang memiliki ID lebih tinggi. Node dengan ID lebih tinggi akan merespons menggunakan pesan `OK` dan melanjutkan proses election jika diperlukan.

Berdasarkan hasil pengujian yang dicatat dalam `JURNAL.md`, node 5 terpilih sebagai leader karena memiliki ID tertinggi di antara lima node. Node 5 kemudian mengirim pesan `COORDINATOR` kepada node lainnya, sehingga node 1 sampai 4 mengetahui bahwa node 5 merupakan leader saat ini.

Hasil tersebut sesuai dengan mekanisme Bully Algorithm, yaitu node aktif dengan ID tertinggi menjadi leader setelah proses election selesai.

#### Skenario 2: Leader Dimatikan

Pada skenario ini, proses node 5 dihentikan menggunakan `Ctrl+C`. Node lain yang sebelumnya mengetahui node 5 sebagai leader akan memeriksa responsnya melalui pesan `PING`. Ketika node 5 tidak merespons, node yang mendeteksi kegagalan akan memulai election baru.

Berdasarkan hasil yang dicatat dalam `JURNAL.md`, node 4 terpilih sebagai leader baru setelah node 5 dimatikan. Node 4 kemudian mengirim pesan `COORDINATOR` kepada node 1, 2, dan 3 untuk mengumumkan perubahan leader.

Pergantian ini menunjukkan bahwa sistem dapat melakukan pemilihan leader kembali ketika leader sebelumnya tidak tersedia. Berdasarkan konfigurasi program, pemeriksaan leader dilakukan setiap tiga detik dan waktu tunggu respons election adalah dua detik. Waktu aktual pemilihan leader tetap bergantung pada waktu deteksi kegagalan dan respons komunikasi antarnode.

Kedua skenario menunjukkan bahwa Bully Algorithm dapat digunakan untuk mensimulasikan pemilihan leader awal dan pergantian leader ketika terjadi kegagalan pada node yang sedang memimpin.


## Struktur Submission

```
tugas-05-koordinasi-konsensus/
├── README.md      # Analisis: kenapa perlu leader, kenapa Bully (vs Raft), hasil 2 skenario
├── JURNAL.md
├── src/
│   └── node.py
└── bukti/          # Log/screenshot skenario start normal & leader mati
```

## Rubrik Penilaian (Tugas 5)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Implementasi Bully Algorithm benar | 35% | Election, OK, COORDINATOR message bekerja sesuai aturan algoritma |
| Bukti skenario leader mati → re-election | 30% | Log jelas menunjukkan leader baru terpilih otomatis |
| Analisis (kenapa perlu leader, trade-off Bully vs Raft) | 20% | Dikaitkan ke masalah urutan pesanan di skenario FoodGo |
| Proses & kontribusi kelompok | 15% | `JURNAL.md`, commit history |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya ke AI tentang gambaran umum algoritma election; **tidak boleh** meminta AI menuliskan isi `# TODO` di `src/node.py` (logika `on_message`, `start_election`, `declare_leader`, `monitor_leader`). Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- `README.md` wajib menjelaskan kenapa Bully Algorithm selalu memilih node ber-ID tertinggi yang masih hidup, dan apa kelemahannya dibanding algoritma lain (mis. jumlah pesan yang dikirim saat election, single point of failure sebelum leader baru terpilih) bukan sekadar definisi generik.
