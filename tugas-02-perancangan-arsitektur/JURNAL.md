# Jurnal Proses — Tugas 2

## [Tanggal]
- Opsi arsitektur yang dipertimbangkan: ...
- Kenapa akhirnya pilih [SOA/Pub-Sub]: ...
- Revisi diagram (versi 1 → versi 2, apa yang berubah dan kenapa): ...

## Jawaban Yolanda (Orang 1)

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
flowchart ID
    C["Pelanggan"]
    RC["Restaurant Catalog Service"]
    O["Order Service"]
    P["Payment Service"]
    B[("Message Broker")]
    R["Restaurant Order Handler"]
    N["Courier / Notification Service"]

    C -->|"HTTP: melihat menu"| RC
    C -->|"HTTP: membuat pesanan"| O

    O <-->|"API/RPC sinkron"| P

    O -->|"Publish: OrderPaid"| B
    B -->|"Subscribe: OrderPaid"| R
    B -->|"Subscribe: OrderPaid"| N
```

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
