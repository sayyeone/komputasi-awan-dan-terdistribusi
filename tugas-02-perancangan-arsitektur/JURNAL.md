# Jurnal Proses — Tugas 2

## [Tanggal]
- Opsi arsitektur yang dipertimbangkan: ...
- Kenapa akhirnya pilih [SOA/Pub-Sub]: ...
- Revisi diagram (versi 1 → versi 2, apa yang berubah dan kenapa): ...

## Nomor 1 (Yolanda Elva Angelica - 103072400125)

### 1. Analisis Masalah Monolitik FoodGo

Analisis saat ini adalah semua komponen mulai dari pemesanan, pembayaran, notifikasi kurir hingg katalog resto berjalan di dalam satu server dalam aplikasi, sehingga muncul beberapa masalah seperti:

- Deploy, yaitu perubahan yang terjadi di dalam komponen yang menyebabkan aplikasi tersebut harus memasang ulang seluruh aplikasi baru lagi agar bisa digunakan.

- Downtime, yaitu kondisi dimana aplikasi tidak dapat digunakan sementara sehingga semua komponennya melakukan restart.

- Coupling tinggi, yaitu kondisi dimana bagian bagian komponen saling bergantungan sehingga dapat menyebabkan bug pada komponen lain.

- Skalabilitas yang tidak fleksibel, yaitu misalnya Ketika jam makan siang, komponen yang paling terbebani ialah pesanan tapi yang bisa di scale hanya seluruh aplikasi bukan hanya modul tertentu.

akar masalahnya ialah komponen yang tidak bisa terisolasi yang menyebabkan komponen saling bergantung dan bisa saja menyebabkan bug sewaktu Waktu apalagi Ketika pesanan sedang ramai, maka dari itu dibutuhkan arsitektur yang tiap komponennya terpisah dan juga independen serta di scale sendiri

### 2. Pemilihan Arsitektur

Pemilihan Arsitektur yang kami gunakan adalah Service-Oriented Architecture (SOA) sebagai gaya Utama dan Publsih-Subscribe sebagai pelengkap khusus alur notifikasi. Komponen ini dipecah menjadi server independent yaitu serice pesanan, service pembayaran, service notifikasi kurir, dan service katalog resto. service yang membutuhkan jawaban langsung (pesanan ke pembayaran) berkomunikasi melalui API/RPC. Notifikasi ke kurir dan resto dikirim asinkron melalui message broker.

### 3. Alasan Pemilihan

menggunakan kombinasi SOA dan Pub-Sub, karena kebutuhan FoodGo bukan hanya memisahkan komponen, tetapi juga membuat komunikasi antarkomponen lebih fleksibel. Dalam laporan, jelaskan bahwa pemisahan layanan memungkinkan deployment independen, sedangkan Pub-Sub membantu mengurangi ketergantungan langsung untuk pemberitahuan pesanan.

## Nomor 2 (Difa Auliya Andini Putri - 103072400112)
```mermaid
flowchart TD
    C["Pelanggan"]
    RC["Restaurant Catalog Service"]
    O["Order Service"]
    P["Payment Service"]
    B[("Message Broker")]
    R["Restaurant Order Handler"]
    N["Courier / Notification Service"]

    C -->|"1. HTTP sinkron: 
            melihat menu"| RC
    C -->|"2. HTTP sinkron:
            membuat pesanan"| O

    O -->|"3. API/RPC sinkron: 
            validasi menu dan harga"| RC

    O -->|"4. Request sinkron: 
            proses pembayaran"| P
    P -->|"5. Response sinkron: 
            status pembayaran"| O

    O -->|"6. Publish asinkron: 
            OrderPaid"| B
    B -->|"7. Subscribe asinkron: 
            OrderPaid"| R

    R -->|"8. Publish asinkron: 
            RestaurantAccepted"| B
    B -->|"9. Subscribe asinkron: 
            RestaurantAccepted"| N

    N -->|"10. Notifikasi penugasan 
            kurir"| C
```

## Nomor 3 - Alur Skenario End-to-End (Adisty Fatika Ardani - 103072400091)

**Skenario:** pelanggan melihat menu, membuat pesanan, membayar, resto menyetujui pesanan, lalu kurir ditugaskan.

Nomor langkah di bawah sama dengan nomor panah pada diagram di bagian 2.

| No | Dari → Ke | Jenis Komunikasi | Penjelasan |
|----|-----------|------------------|------------|
| 1 | Pelanggan → Restaurant Catalog Service | Sinkron, HTTP request-response | Pelanggan membuka daftar menu dan langsung menerima datanya. |
| 2 | Pelanggan → Order Service | Sinkron, HTTP request-response | Pelanggan mengirim pesanan ke Order Service. |
| 3 | Order Service → Restaurant Catalog Service | Sinkron, API/RPC | Order Service memvalidasi menu dan harga. Hasilnya harus diketahui dulu sebelum lanjut, sehingga sinkron. |
| 4 | Order Service → Payment Service | Sinkron, request | Order Service meminta pembayaran diproses. |
| 5 | Payment Service → Order Service | Sinkron, response | Payment Service mengembalikan status pembayaran. Pesanan hanya dilanjutkan jika pembayaran berhasil. |
| 6 | Order Service → Message Broker | Asinkron, publish event | Setelah pembayaran berhasil, Order Service mempublikasikan event **OrderPaid** tanpa menunggu respons. |
| 7 | Message Broker → Restaurant Order Handler | Asinkron, subscribe event | Broker meneruskan **OrderPaid** ke Restaurant Order Handler, yang menerima dan memproses informasi pesanan baru. |
| 8 | Restaurant Order Handler → Message Broker | Asinkron, publish event | Setelah restoran benar-benar menyetujui pesanan, Restaurant Order Handler menerbitkan event **RestaurantAccepted**. Menerima informasi pesanan belum berarti menyetujuinya. |
| 9 | Message Broker → Courier/Notification Service | Asinkron, subscribe event | Courier/Notification Service menerima **RestaurantAccepted** dan memulai proses penugasan kurir. |
| 10 | Courier/Notification Service → Pelanggan | Notifikasi (push) | Setelah kurir berhasil ditemukan dan penugasan dikonfirmasi, pelanggan diberi tahu bahwa kurir sudah ditugaskan. |

### Komunikasi Sinkron (Langkah 1-5)
Dipakai untuk proses yang butuh jawaban langsung sebelum alur berlanjut, yaitu melihat menu, validasi menu dan harga, serta pembayaran. Pesanan tidak boleh dilanjutkan jika menu tidak valid atau pembayaran gagal.

### Komunikasi Asinkron (Langkah 6-9)
Dipakai setelah pembayaran berhasil, melalui Message Broker dengan pola Pub-Sub. Order Service cukup mempublikasikan event tanpa tahu siapa yang akan menerimanya.

Jika Restaurant Order Handler atau Courier/Notification Service sedang tidak tersedia, Message Broker dapat menyimpan event untuk diproses ketika layanan kembali aktif, asalkan broker dan konsumennya dikonfigurasi untuk mendukung penyimpanan pesan (durable) dan pemrosesan ulang (acknowledgment dan retry). Dengan demikian, gangguan pada satu layanan tidak harus langsung menghentikan layanan lainnya.

### Langkah 10: Notifikasi ke Pelanggan
Langkah 10 adalah kelanjutan proses, yaitu pengiriman notifikasi oleh Courier/Notification Service ke pelanggan. Diagram saat ini belum menunjukkan apakah notifikasi dikirim melalui broker atau langsung oleh service tersebut, sehingga langkah ini tidak dikategorikan sebagai bagian Pub-Sub. Notifikasi hanya dikirim setelah penugasan kurir berhasil dikonfirmasi.

### Kesesuaian dengan Diagram
- **Langkah 1-5:** komunikasi langsung request-response sesuai rancangan SOA (Pelanggan, Order Service, Restaurant Catalog Service, Payment Service).
- **Langkah 6-9:** komunikasi event melalui Message Broker sesuai pola Pub-Sub (Order Service, Restaurant Order Handler, Courier/Notification Service).
- **Langkah 10:** pengiriman notifikasi oleh Courier/Notification Service ke pelanggan.


## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
