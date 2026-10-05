# Jurnal Proses — Tugas 1

> Isi jurnal ini selama proses diskusi berlangsung, bukan ditulis ulang rapi di akhir. Tulis dengan gaya bebas — poin diskusi, kebuntuan, perubahan pikiran.

## 05/10/2026
- Peserta: Difa Auliya Andini Putri, Adisty Fatika Ardani, Yolanda Elva Angelica, Glory Leonthine Angi'
- Poin diskusi: ...
- Perbedaan pendapat (jika ada): ...

## [Tanggal diskusi 2]
- ...

## Review Silang
- Adisty mengomentari analisis Difa (Latency Is Zero):
  - Pitfall dan kutipan skenarionya sudah tepat, trade-off timeout terlalu singkat vs terlalu lama juga masuk akal.
  - Bagian "Kenapa ini keliru" masih terlalu generik. Sebaiknya ditambah bahwa latency berubah-ubah dan makin lama saat trafik tinggi (jam makan siang/promo).
## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 05/10/2026 | Claude | Menulis draft pitfall "Latency Is Zero" lalu minta dikoreksi | AI menyarankan fokus pitfall diganti ke asumsi "panggilan antar service instan", memberi pola 4 bagian (bukti, kenapa keliru, dampak, solusi+trade-off), dan menolak menuliskan versi jadinya | Draft ditulis ulang sendiri mengikuti pola tersebut, lalu direvisi (dampak dipecah, ditambah solusi pendukung) |