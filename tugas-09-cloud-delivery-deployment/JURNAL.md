# Jurnal Proses — Tugas 9

## Diskusi deployment model
- Opsi yang dipertimbangkan ada empat: Private, Public, Hybrid, dan Community Cloud. Akhirnya kami pilih Private Cloud karena studi kasus meminta data kependudukan ada di infrastruktur yang dikendalikan penuh oleh negara.
- Public Cloud murni kami tolak karena infrastrukturnya dipakai bersama (multi-tenant) dan di luar kendali pemerintah, walaupun skalabilitasnya paling bagus.
- Kekurangan Private Cloud di skalabilitas kami atasi dengan capacity planning, auto-scaling, caching, dan DR site.

## Diskusi service model per komponen
- Kami pakai kombinasi IaaS dan PaaS, dengan SaaS hanya untuk hal-hal pendukung.
- Database dan penyimpanan biometrik pakai IaaS supaya pemerintah bisa mengatur enkripsi dan konfigurasi keamanannya sendiri.
- Aplikasi inti, API integrasi, dan dashboard pakai PaaS supaya tim pengembang tidak perlu mengurus seluruh infrastruktur.
- SaaS dipakai untuk kolaborasi internal dan helpdesk, yang tidak menyimpan data kependudukan.

## Pembagian kontribusi
- Bagian 1 (analisis karakteristik dan deployment model): Glory Leonthine Angi'
- Bagian 2 (service model): [Difa Aulia
- Bagian 3 (risiko dan mitigasi): Adisty Fatika Ardani
- Bagian 4 (analisis alternatif dan integrasi dokumentasi): Yolanda Elva Angelica

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
