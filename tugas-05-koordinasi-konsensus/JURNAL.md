# Jurnal Proses — Tugas 5

## Implementasi Bully
- Kendala saat mengisi TODO 1-4: ...

## Skenario 1: Start normal (Yolanda Elva Angelica - 103072400125)
- Leader yang terpilih: Node 5
- Log/observasi: Node 1 sampai 4 mengirim ELECTION ke node ber-ID lebih tinggi dan menerima OK. Node 5 tidak punya node ber-ID lebih tinggi, jadi langsung menjadi LEADER dan mengirim COORDINATOR ke node 1 sampai 4. Semua node mencatat “Leader sekarang: node 5”.

## Skenario 2: Leader dimatikan (Yolanda Elva Angelica - 103072400125)
- Leader baru yang terpilih: Node 4
- Berapa lama waktu sampai leader baru terdeteksi: Node 5 dimatikan dengan Ctrl+C. Node 1 sampai 4 mendeteksi bahwa leader node 5 tidak merespons, lalu memulai election ulang. Node 4 menjadi LEADER dan mengirim COORDINATOR ke node 1, 2, dan 3.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
