# Tugas 9 (Pekan 9) — Cloud Delivery & Deployment Model

**Materi terkait:** Karakteristik esensial cloud computing (NIST SP 800-145), Deployment Model (Public/Private/Hybrid/Community), Service Model (IaaS/PaaS/SaaS).

> Bagian 2 mata kuliah ini murni **analisis & desain di atas kertas** — tidak ada biaya cloud sama sekali, karena tugas berhenti di tahap rekomendasi, bukan implementasi nyata (implementasi baru mulai Tugas 11).

## Studi Kasus

Pemerintah ingin membangun **Sistem Data Kependudukan** (nama, NIK, alamat, data biometrik) yang:
- Sangat **rahasia** (data pribadi warga negara, diatur UU Perlindungan Data Pribadi).
- Diakses oleh **ribuan instansi** (dukcapil daerah, kepolisian, bank untuk verifikasi KYC) dengan pola akses yang **tidak rata** (lonjakan saat musim pemilu/pendaftaran sekolah).
- Butuh **skalabilitas** agar tidak downtime saat lonjakan akses, tapi **tidak boleh** datanya berada di infrastruktur yang tidak terkendali penuh oleh negara.

## Tugas Kelompok

1. **Rekomendasikan Deployment Model** (Public / Private / Hybrid / Community Cloud) yang paling tepat untuk sistem ini. Jelaskan alasannya berdasarkan **karakteristik NIST** (on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service) dikaitkan dengan kebutuhan kerahasiaan vs skalabilitas.

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



2. **Rekomendasikan Service Model** (IaaS / PaaS / SaaS) yang tepat untuk komponen-komponen berbeda dari sistem ini (boleh berbeda service model untuk komponen berbeda, mis. database inti vs portal publik untuk pengecekan status).

## 2. Rekomendasi Service Model

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
4. Bandingkan singkat dengan **satu alternatif yang kalian tolak** — kenapa alternatif itu kurang tepat (mis. kenapa Public Cloud murni ditolak, atau kenapa Private Cloud murni dianggap kurang skalabel).

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
