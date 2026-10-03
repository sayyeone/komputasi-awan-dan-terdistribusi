# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** Awan Wawan

| Nama | NIM | Kontribusi |
|---|---|---|
| [nama 1] | [nim] | [pitfall/bagian yang dikerjakan] |
| [nama 2] | [nim] | [pitfall/bagian yang dikerjakan] |
| [nama 3] | [nim] | [pitfall/bagian yang dikerjakan] |
| Yolanda Elva Angelica | 103072400125 | Single Point of Failure / Monolitik |

## Pitfall 1: [nama pitfall] — ditulis oleh [nama]

**Bukti di skenario:** [kutip/paraphrase bagian skenario]

**Kenapa ini keliru:** [penjelasan]

**Dampak ke FoodGo:** [mekanisme kegagalan konkret]

**Solusi desain awal:** [usulan solusi]

**Trade-off:** [apa yang dikorbankan/risiko dari solusi ini]

---

## Pitfall 2: [nama pitfall] — ditulis oleh [nama]

(ulangi struktur di atas)

---

## Pitfall 3: [nama pitfall] — ditulis oleh [nama]

(ulangi struktur di atas)

---

## Pitfall 4: Single Point of Failure / Monolitik — ditulis oleh Yolanda Elva Angelica

**Bukti di skenario:** "Saat trafik naik, satu server yang menangani semua modul (pesanan, pembayaran, notifikasi kurir) kewalahan karena semuanya berjalan di satu proses monolitik yang sama."

**Kenapa ini keliru:** Alasannya adalah karena FoodGo berasumsi kalau satu server sudah cukup untuk melakukan semua pekerjaan dan tidak akan bermasalah. Kalau di dunia nyata, server bisa saja kewalahan atau mati apalagi saat pesanan sedang banyak dan ramai.

Ada dua masalah, yang pertama Single Point of Failure, yaitu Ketika semua fitur bergantung ke satu program, kalau program itu mati semuanya ikut mati. yang kedua tidak ada pemisah antar fitur, yaitu pesanan, pembayaran, dan notifikasi kurir menggunakan tenaga server yang sama (CPU, memori). kalau satu fitur kewalahan fitur fitur lainnya juga akan ikut terganggu.

**Dampak ke FoodGo:** waktu jam makan siang atau saat sedang promo, pesanan akan naik drastis. Modul pesanan dan pembayaran paling bekerja keras karena semua orang sedang order dan bayar. Masalahnya, semua modul akan jalan di dalam satu program yang sama, jadi CPU dan memori dipakai bersama sama. Jika pesanan dan pembayaran menghabiskan tenaga, maka modul lain yang dalam kondisi baik baik saja seperti notifikasi kurir akan menjadi lemot. Hal tersebut akan membuat program menjadi crash kemudian semua modul mati bersamaan. Dan karena tidak ada server cadangan atau restart otomatis, sistemnya akan tetap mati dan harus dinyalakan secara manual. Dampaknya ke FoodGo adalah pelanggan tidak bisa memesan dan outlet FoodGo tidak bisa menerima pesanan dan akan kehilangan pesanan.

**Solusi desain awal:** Solusi desainnya adalah FoodGo sebaiknya memisahkan fitur programnya sendiri sendiri (pesanan & pembayaran) supaya tidak menumpuk di satu fitur saja, lalu severnya juga di tambah cadangan & pasang load balancer untuk mengatur pesanan masuk ke server yang masih hidup, dan terakhir menambahkan pengecekan otomatis, jadi Ketika server mati server tersebut bisa menyala lagi sendiri tanpa tunggu orang.

**Trade-off:** Memisahkan fitur membuat system menjadi tahan lama, tapi hal tersebut lebih susah diurus dan program harus bicara lewat jaringan, jadi memungkinkan ada risiko lambat atau gagal. solusinya adalah dengan memisahkan secukupnya kemudian di beri timeout.

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
