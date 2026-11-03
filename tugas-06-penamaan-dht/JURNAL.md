# Jurnal Proses — Tugas 6

## Implementasi find_successor
- Kesalahan pertama yang ditemui (mis. lupa wrap-around di ring): ...
- Cara memperbaikinya: ...

## Skenario join/leave
- Hasil sebelum & sesudah node baru bergabung: Sebelum node baru bergabung, kurir-012 (hash=116) ditangani node 136. Setelah node-medan-1 (id=123) bergabung, kurir-012 berpindah ke node 123. Mapping kurir lain tidak berubah, misalnya kurir-001 tetap ditangani node 102 dan IP-nya tetap 192.168.1.10.
- Hasil sebelum & sesudah node keluar: Sebelum node-jakarta-1 (id=177) keluar, kurir-005 (hash=175) ditangani node 177. Setelah node keluar, kurir-005 berpindah ke node 40 (successor berikutnya, karena ring berputar kembali ke awal). Lookup kurir-001 dan kurir-002 tetap mengarah ke node dan IP yang sama.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
