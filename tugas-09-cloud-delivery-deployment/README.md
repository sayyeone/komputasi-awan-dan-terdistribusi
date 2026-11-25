# Tugas 9 (Pekan 9) — Cloud Delivery & Deployment Model

**Materi terkait:** Karakteristik esensial cloud computing (NIST SP 800-145), Deployment Model (Public/Private/Hybrid/Community), Service Model (IaaS/PaaS/SaaS).

> Bagian 2 mata kuliah ini murni **analisis & desain di atas kertas** — tidak ada biaya cloud sama sekali, karena tugas berhenti di tahap rekomendasi, bukan implementasi nyata (implementasi baru mulai Tugas 11).

## Studi Kasus

Pemerintah ingin membangun **Sistem Data Kependudukan** (nama, NIK, alamat, data biometrik) yang:
- Sangat **rahasia** (data pribadi warga negara, diatur UU Perlindungan Data Pribadi).
- Diakses oleh **ribuan instansi** (dukcapil daerah, kepolisian, bank untuk verifikasi KYC) dengan pola akses yang **tidak rata** (lonjakan saat musim pemilu/pendaftaran sekolah).
- Butuh **skalabilitas** agar tidak downtime saat lonjakan akses, tapi **tidak boleh** datanya berada di infrastruktur yang tidak terkendali penuh oleh negara.

## Tugas Kelompok

# 1. Rekomendasikan Deployment Model - Glory Leonthine Angi'

(Public / Private / Hybrid / Community Cloud) yang paling tepat untuk sistem ini. Jelaskan alasannya berdasarkan **karakteristik NIST** (on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service) dikaitkan dengan kebutuhan kerahasiaan vs skalabilitas.

### 1.1 Analisis Karakteristik Sistem
Sistem Data Kependudukan memiliki beberapa karakteristik, yaitu:
- Menyimpan data pribadi yang bersifat rahasia, seperti nama, NIK, alamat, dan data biometrik.
- Diakses oleh ribuan instansi dengan kebutuhan dan hak akses yang berbeda.
- Mengalami lonjakan akses pada waktu tertentu, seperti musim pemilu dan pendaftaran sekolah.
- Membutuhkan kapasitas yang dapat disesuaikan dengan jumlah permintaan.
- Infrastruktur dan penyimpanan data harus berada di bawah kendali penuh pemerintah.

### 1.2 Rekomendasi Deployment Model
  Deployment model yang dipilih adalah Private Cloud karena sistem ini menyimpan data kependudukan yang bersifat rahasia. Dengan Private Cloud, pemerintah dapat mengendalikan infrastruktur, penyimpanan data, keamanan, serta hak akses setiap instansi. Untuk mengatasi lonjakan akses, pemerintah dapat menerapkan auto-scaling dan load balancing serta menyediakan kapasitas server cadangan. Dengan begitu, kebutuhan skalabilitas tetap dapat terpenuhi tanpa menggunakan infrastruktur di luar kendali pemerintah.

### 1.3 Analisis Berdasarkan Lima Karakteristik NIST
| Karakteristik NIST | Penerapan pada Sistem Data Kependudukan |
|---|---|
| **On-demand self-service** | Pengelola sistem dapat menambah sumber daya seperti server dan penyimpanan secara mandiri sesuai kebutuhan tanpa harus melalui proses manual setiap saat. |
| **Broad network access** | Instansi seperti Dukcapil, kepolisian, dan bank dapat mengakses layanan melalui jaringan yang aman sesuai hak akses masing-masing. |
| **Resource pooling** | Sumber daya seperti server, penyimpanan, dan jaringan dapat digunakan bersama serta dialokasikan sesuai kebutuhan setiap layanan tanpa mencampurkan hak akses data. |
| **Rapid elasticity** | Kapasitas server dapat ditambah ketika terjadi lonjakan akses, seperti saat pemilu dan pendaftaran sekolah, serta dikurangi kembali ketika jumlah akses menurun, selama kapasitas fisik masih tersedia. |
| **Measured service** | Penggunaan CPU, RAM, penyimpanan, dan jaringan dapat dipantau untuk mengetahui kebutuhan sumber daya serta menghindari penggunaan yang berlebihan. |

  Berdasarkan kelima karakteristik tersebut, Private Cloud dipilih karena dapat memenuhi kebutuhan kerahasiaan data, pengendalian infrastruktur, dan skalabilitas sistem, selama pemerintah menyediakan kapasitas infrastruktur yang memadai.



2. **Rekomendasikan Service Model**

(IaaS / PaaS / SaaS) yang tepat untuk komponen-komponen berbeda dari sistem ini (boleh berbeda service model untuk komponen berbeda, mis. database inti vs portal publik untuk pengecekan status).

## 2. Rekomendasi Service Model - Difa Aulia

Berdasarkan deployment model yang dipilih, yaitu **Private Cloud**, Sistem Data Kependudukan menggunakan kombinasi service model IaaS dan PaaS, serta SaaS secara terbatas. Pemilihan ini disesuaikan dengan kebutuhan pengendalian data, pengelolaan aplikasi, dan akses oleh berbagai instansi.

### 2.1 Pemetaan Service Model

| Komponen Sistem | Service Model | Alasan Pemilihan |
|---|---|---|
| Infrastruktur server dan jaringan | **IaaS** | Memberikan kendali kepada pemerintah dalam mengelola server virtual, jaringan, sistem operasi, dan konfigurasi keamanan. |
| Database kependudukan dan penyimpanan biometrik | **IaaS** | Memungkinkan pemerintah mengatur penyimpanan, konfigurasi database, enkripsi, dan keamanan data sensitif. |
| Aplikasi pengelolaan data kependudukan | **PaaS** | Menyediakan platform untuk menjalankan dan mengembangkan aplikasi tanpa harus mengelola seluruh infrastruktur server secara langsung. |
| API integrasi antarinstansi | **PaaS** | Memudahkan pengembangan dan pengelolaan API yang menghubungkan Dukcapil, kepolisian, dan bank dengan mekanisme autentikasi serta otorisasi. |
| Dashboard monitoring dan administrasi | **PaaS** | Mendukung pemantauan penggunaan sistem, aktivitas akses, dan kondisi layanan. |
| Aplikasi kolaborasi internal dan helpdesk | **SaaS** | Digunakan untuk kebutuhan pendukung yang tidak memproses atau menyimpan data kependudukan sensitif. |

### 2.2 Alasan Pemilihan Service Model 

**1. Infrastructure as a Service (IaaS)**

IaaS digunakan untuk menyediakan infrastruktur dasar, seperti server virtual, jaringan, dan penyimpanan data. Model ini dipilih untuk komponen yang membutuhkan kendali tinggi, khususnya database kependudukan dan data biometrik. Pemerintah dapat mengatur sistem operasi, konfigurasi keamanan, serta mekanisme penyimpanan sesuai kebijakan yang berlaku.

**2. Platform as a Service (PaaS)**

PaaS digunakan untuk menjalankan aplikasi kependudukan, API integrasi, dan dashboard administrasi. Model ini memungkinkan tim pengembang berfokus pada pengembangan aplikasi tanpa harus mengelola seluruh infrastruktur dasar. PaaS juga mendukung pengembangan layanan yang dapat disesuaikan dengan kebutuhan akses berbagai instansi.

**3. Software as a Service (SaaS)**

SaaS digunakan secara terbatas untuk layanan pendukung, seperti aplikasi kolaborasi internal dan pengelolaan tiket bantuan teknis. Model ini tidak direkomendasikan untuk sistem inti yang mengolah data kependudukan karena pemerintah membutuhkan kendali tinggi terhadap pengolahan dan penyimpanan data sensitif.

### 2.3 Kesimpulan

Kombinasi IaaS dan PaaS menjadi pilihan utama karena memberikan kendali terhadap infrastruktur dan data sensitif sekaligus mempermudah pengembangan serta pengelolaan aplikasi. Sementara itu, SaaS dapat dimanfaatkan secara terbatas untuk layanan pendukung yang tidak berkaitan langsung dengan data kependudukan. Seluruh layanan tetap harus ditempatkan dalam lingkungan Private Cloud yang berada di bawah kendali pemerintah.

3. Jelaskan **minimal 2 risiko spesifik** dari pilihan kalian dan mitigasinya (mis. jika Hybrid Cloud dipilih: risiko sinkronisasi data antara private & public segment).

## 3. Analisis Risiko dan Mitigasi - Adisty

Pada Private Cloud yang dipilih, pemerintah memegang kendali penuh atas infrastruktur. Konsekuensinya, pemerintah juga menanggung seluruh tanggung jawab keamanan dan kapasitas. Berikut tiga risiko spesifik pada Sistem Data Kependudukan.

### 3.1 Risiko Kebocoran Data NIK dan Biometrik

**Risiko:** Karena seluruh data kependudukan terpusat, satu celah (misalnya serangan siber, kebocoran kredensial administrator, atau orang dalam yang menyalahgunakan akses) dapat membocorkan data jutaan warga sekaligus. NIK dan biometrik sangat berbahaya jika bocor, terutama biometrik karena tidak dapat diganti seperti password. Data yang bocor dapat dipakai untuk pencurian identitas dan penipuan KYC di bank. Kebocoran juga berpotensi melanggar UU Perlindungan Data Pribadi.

**Mitigasi:**
- Enkripsi data saat disimpan (*at rest*, misalnya AES-256) dan saat dikirim (*in transit*, TLS), dengan kunci dikelola di HSM (*Hardware Security Module*) milik pemerintah.
- Data biometrik disimpan terpisah dari data identitas (NIK, nama, alamat) di segmen jaringan berbeda, serta dipetakan menggunakan token/pseudonim.
- Autentikasi multi-faktor (MFA) dan prinsip *least privilege* untuk semua administrator.
- Audit log yang tidak dapat diubah (*immutable*) dan deteksi anomali, misalnya pengunduhan data dalam jumlah besar.
- Backup terenkripsi yang disimpan offline dan diuji pemulihannya secara berkala.

### 3.2 Risiko Akses Tidak Sah oleh Instansi

**Risiko:** Ribuan instansi (Dukcapil daerah, kepolisian, bank) memiliki kebutuhan dan hak akses berbeda. Ada risiko instansi mengakses data di luar kewenangannya, misalnya bank menarik data biometrik padahal hanya perlu verifikasi KYC. Selain itu, kredensial atau API key milik instansi yang kurang aman dapat disalahgunakan pihak ketiga. Ini juga berkaitan dengan karakteristik *broad network access* yang membuka banyak titik akses.

**Mitigasi:**
- Kontrol akses berbasis peran dan atribut (RBAC/ABAC) per instansi, sehingga bank hanya mendapat jawaban verifikasi (cocok/tidak cocok), bukan data mentah.
- API Gateway dengan autentikasi dan otorisasi per instansi (OAuth2/mutual TLS), pembatasan laju permintaan (*rate limiting*), serta pembatasan alamat IP yang diizinkan.
- Pencatatan setiap permintaan data (siapa, kapan, data apa, untuk tujuan apa) dan peninjauan audit berkala.
- Rotasi API key/sertifikat secara berkala serta pencabutan akses segera jika terjadi penyalahgunaan.

### 3.3 Risiko Lonjakan Akses dan Gangguan Layanan

**Risiko:** Pada Private Cloud, kapasitas dibatasi oleh perangkat fisik milik pemerintah. Saat lonjakan akses (pemilu, pendaftaran sekolah) *rapid elasticity* hanya berjalan sampai batas kapasitas fisik tersedia. Jika permintaan melebihi kapasitas, layanan melambat atau down, sehingga verifikasi identitas oleh instansi dan bank terhenti. Lonjakan juga dapat menyerupai serangan DDoS sehingga sulit dibedakan.

**Mitigasi:**
- Perencanaan kapasitas (*capacity planning*) berdasarkan data lonjakan tahun-tahun sebelumnya, dengan cadangan kapasitas (*buffer*) di atas puncak beban.
- *Auto-scaling* dan *load balancing* yang dikonfigurasi sebelum musim puncak (*pre-scaling*).
- Menggunakan *caching* dan antrian permintaan (*queue*) untuk meredam beban pada database inti.
- Pemisahan beban baca dan tulis (*read replica*) serta penerapan prioritas layanan untuk instansi kritis.
- Perlindungan DDoS dan *rate limiting*, serta pusat data cadangan (*disaster recovery site*) di lokasi berbeda yang tetap berada di bawah kendali pemerintah.
- Pemantauan (*measured service*) dengan peringatan dini saat penggunaan CPU/RAM mendekati batas.

### 3.4 Ringkasan Risiko dan Mitigasi

| Risiko | Dampak | Mitigasi Utama |
|---|---|---|
| Kebocoran data NIK dan biometrik | Pencurian identitas, pelanggaran UU PDP, hilangnya kepercayaan publik | Enkripsi + HSM, pemisahan data biometrik, MFA, audit log |
| Akses tidak sah oleh instansi | Penyalahgunaan data di luar kewenangan | RBAC/ABAC, API Gateway, pembatasan data per instansi, audit akses |
| Lonjakan akses dan gangguan layanan | Layanan verifikasi down saat pemilu/pendaftaran sekolah | Capacity planning, auto-scaling, caching, DR site, perlindungan DDoS |

## 4. Perbandingan dengan Alternatif yang Ditolak - Yolanda Elva Angelica

Bandingkan singkat dengan **satu alternatif yang kalian tolak** — kenapa alternatif itu kurang tepat (mis. kenapa Public Cloud murni ditolak, atau kenapa Private Cloud murni dianggap kurang skalabel).

Alternatif yang kami tolak adalah Public Cloud murni. Kelebihan Public Cloud ada di skalabilitas, karena penyedia layanannya punya kapasitas yang sangat besar. Waktu akses melonjak saat pemilu atau pendaftaran sekolah, sumber daya bisa ditambah dengan cepat dan biayanya mengikuti pemakaian. Tapi untuk sistem yang menyimpan NIK dan data biometrik seluruh warga, kelebihan itu belum cukup.

Dari sisi keamanan, Public Cloud itu multi-tenant, jadi infrastruktur fisiknya dipakai bersama oleh banyak pelanggan. Pemerintah juga cuma mengendalikan sebagian lapisan, sisanya dipegang penyedia, jadi tanggung jawab keamanan terbagi dan pemerintah tidak bisa memastikan sendiri semua lapisannya aman. Soal kendali infrastruktur, lokasi server, kebijakan penyedia, dan akses staf penyedia semuanya di luar kendali pemerintah. Ini bertentangan langsung dengan syarat studi kasus bahwa data tidak boleh berada di infrastruktur yang tidak dikendalikan penuh oleh negara. Apalagi biometrik tidak bisa diganti seperti password, jadi kalau bocor dampaknya permanen.

Perbandingan Private Cloud dan Public Cloud murni dapat dilihat pada tabel berikut.

| Aspek | Private Cloud (dipilih) | Public Cloud murni (ditolak) |
|---|---|---|
| Kendali infrastruktur dan lokasi data | Sepenuhnya di tangan pemerintah | Sebagian dipegang penyedia layanan |
| Keamanan data sensitif | Isolasi dan kunci enkripsi (HSM) dikelola sendiri | Infrastruktur dipakai bersama pelanggan lain |
| Skalabilitas | Terbatas kapasitas fisik, tapi bisa dimitigasi | Hampir tidak terbatas |
| Kesesuaian dengan syarat studi kasus | Memenuhi | Tidak memenuhi syarat kendali penuh oleh negara |

Private Cloud memang punya kelemahan di skalabilitas karena dibatasi kapasitas fisik milik pemerintah. Tapi kelemahan ini masih bisa ditutup lewat capacity planning, pre-scaling sebelum musim puncak, caching, dan DR site seperti yang sudah dibahas di bagian 3.3. Kelemahan Public Cloud di kendali data tidak bisa ditutup selama modelnya tetap Public. Jadi alasan kami memilih Private Cloud adalah karena kekurangannya masih bisa dimitigasi, sedangkan kekurangan Public Cloud mengenai syarat paling utama dari sistem ini.


## Struktur Submission

```
tugas-09-cloud-delivery-deployment/
├── README.md      # Analisis lengkap (isi dengan poin 1-4 di atas)
├── JURNAL.md
└── bukti/          # (opsional) diagram pendukung
```

## Rubrik Penilaian (Tugas 9)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Ketepatan rekomendasi deployment model | 30% | Argumen berbasis karakteristik NIST, bukan sekadar "private cloud lebih aman" tanpa detail |
| Ketepatan rekomendasi service model | 25% | Pemetaan komponen sistem ke IaaS/PaaS/SaaS masuk akal |
| Analisis risiko & mitigasi | 25% | Risiko spesifik ke konteks data kependudukan (bukan risiko generik) |
| Perbandingan dengan alternatif yang ditolak | 20% | Argumen penolakan jelas dan berdasar |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya ke AI gambaran umum karakteristik NIST/deployment model untuk brainstorming; **tidak boleh** meminta AI menuliskan rekomendasi/analisis akhir yang tinggal ditempel ke `README.md`. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- Jawaban yang terasa seperti "template" (bisa dipakai untuk sistem cloud apa saja tanpa menyebut spesifik kependudukan/data pribadi/regulasi) akan dinilai rendah pada komponen ketepatan rekomendasi.
- `README.md` wajib membahas minimal satu skenario tandingan yang kalian buat sendiri (mis. "bagaimana jika instansi daerah tidak punya infrastruktur private cloud sendiri?") beserta jawabannya.
