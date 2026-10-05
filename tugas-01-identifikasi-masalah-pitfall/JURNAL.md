# Jurnal Proses — Tugas 1

> Isi jurnal ini selama proses diskusi berlangsung, bukan ditulis ulang rapi di akhir. Tulis dengan gaya bebas — poin diskusi, kebuntuan, perubahan pikiran.

## 05/10/2026
- Peserta: Difa Auliya Andini Putri, Adisty Fatika Ardani, Yolanda Elva Angelica, Glory Leonthine Angi'
- Poin diskusi: membahas hasil analisis dari masing-masing pitfall dan kesesuaiannya pada skenario FoodGo, membahas solusi yang dapat digunakan untuk mengatasi masalah komunikasi antarservice dan ketergantungan sistem pada satu server, dan membahas trade-off dari setiap solusi.
- Perbedaan pendapat (jika ada)

## [Tanggal diskusi 2]
- ...

## Review Silang
- Adisty mengomentari analisis Difa (Latency Is Zero):
  - Pitfall dan kutipan skenarionya sudah tepat, trade-off timeout terlalu singkat vs terlalu lama juga masuk akal.
  - Bagian "Kenapa ini keliru" masih terlalu generik. Sebaiknya ditambah bahwa latency berubah-ubah dan makin lama saat trafik tinggi (jam makan siang/promo).

- Yolanda mengomentari analisis Adisty (Transport Cost Is Zero):
  - Rantai sebab-akibatnya jelas. Kemudian untuk Trade-off-nya juga nyata: antrean dan batching membuat sistem lebih rumit dan notifikasi bisa terlambat.
  - Klaim "bandwidth habis" bertentangan dengan skenario. Karena modul monolitik saling panggil di dalam satu program, bukan lewat jaringan

- Glory mengomentari analsis Yolanda (Single Point of Failure / Monolitik):
  - Pitfall, kutipan skenario, dan dampaknya sudah sesuai dengan skenario.
  - Solusi yang diusulkan sudah sesuai. Namun, bagian trade off perlu menjelaskan bahwa menambah server cadangan membutuhkan biaya tambahan, sedangkan mengelola beberapa layanan dan server membuat pemeliharaan sistem lebih rumit.

- Difa mengomentari analisis Glory (Network Is Always Reliable):
    - Pitfall dan kutipan skenario yang digunakan sudah sesuai.
    - Penjelasan mengenai jaringan yang dapat mengalami gangguan dan respons yang tidak sampai sudah cukup jelas.
    - Dampak dan solusi timeout serta retry sudah sesuai dengan masalah yang terjadi pada FoodGo.
    - Bagian trade-off sudah baik karena menjelaskan bahwa retry dapat menambah beban server dan membuat pengguna menunggu lebih lama.
## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 05/10/2026 | Claude | Menulis draft pitfall "Latency Is Zero" lalu minta dikoreksi | AI menyarankan fokus pitfall diganti ke asumsi "panggilan antar service instan", memberi pola 4 bagian (bukti, kenapa keliru, dampak, solusi+trade-off), dan menolak menuliskan versi jadinya | Draft ditulis ulang sendiri mengikuti pola tersebut, lalu direvisi (dampak dipecah, ditambah solusi pendukung) |
