# AI Resume Analyzer & Job Optimizer 🚀

AI Resume Analyzer adalah platform web modern berbasis kecerdasan buatan (AI) yang dirancang untuk membantu pelamar kerja mengoptimalkan resume mereka terhadap deskripsi pekerjaan (Job Description) tertentu menggunakan model **Google Gemini AI**.

Platform ini dibangun menggunakan arsitektur monorepo dengan frontend **Nuxt 4** yang responsif dan backend **FastAPI** asinkron yang berkinerja tinggi.

---

## ✨ Fitur Utama

1. **ATS Match Score & Gap Analysis**
   * Menganalisis kecocokan resume terhadap deskripsi pekerjaan dalam hitungan detik.
   * Menampilkan skor persentase kelayakan (ATS Score).
   * Mendeteksi kata kunci (*missing keywords*) penting yang tidak ada dalam resume Anda.
   * Memberikan saran perbaikan (*actionable suggestions*) yang spesifik untuk meningkatkan skor resume Anda.

2. **Job Description Auto-Import via URL (Scraping + AI Parser)**
   * Cukup masukkan link/URL lowongan kerja (dari LinkedIn, Jobstreet, Kalibrr, atau situs karir lainnya).
   * Backend akan mengunduh konten web secara asinkron, memangkas elemen sampah (CSS/JS/Footer), dan memanfaatkan Gemini AI untuk menyaring judul pekerjaan serta deskripsi utama secara terstruktur dan mengisi formulir secara otomatis (*autofill*).

3. **AI Cover Letter Generator**
   * Membuat surat lamaran (*cover letter*) profesional (3-4 paragraf) yang disesuaikan secara khusus antara resume Anda dan syarat pekerjaan.
   * Modal editor interaktif untuk mengedit hasil generate sebelum diunduh.
   * Fitur salin ke clipboard cepat dan unduh sebagai file `.txt`.

4. **Print-Optimized PDF Report**
   * Ekspor hasil analisis resume ke dalam format dokumen PDF berukuran A4 yang rapi dan profesional menggunakan logika **jsPDF**.
   * Output didesain bersih dan diformat khusus untuk cetak, bebas dari potongan layout layar web (*viewport clipping*).

5. **Profile Resume & Dashboard History**
   * Menyimpan resume utama di server sehingga Anda tidak perlu mengunggah ulang file resume untuk setiap lowongan kerja yang dianalisis.
   * Riwayat pencarian (*dashboard history*) dengan label kustom dan fitur hapus (*soft delete*).

---

## 🛠️ Tech Stack

### Frontend (Nuxt Application)
* **Framework:** [Nuxt 4](https://nuxt.com/) (Vue 3, Composition API)
* **State Management:** [Pinia](https://pinia.vuejs.org/)
* **Styling:** [Tailwind CSS](https://tailwindcss.com/) dengan SaaS-aesthetic (Glassmorphism, Slate & Indigo palettes)
* **Icons:** [Material Symbols Outlined](https://fonts.google.com/icons)
* **Libraries:** `jsPDF` (PDF Generation), `@vueuse/core`

### Backend (FastAPI Service)
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Python 3.13)
* **Database & ORM:** PostgreSQL & [SQLAlchemy](https://www.sqlalchemy.org/) (Asyncio)
* **Migrations:** [Alembic](https://alembic.otexts.org/)
* **AI Engine:** Google GenAI SDK (`gemini-2.5-flash` model dengan *Structured Outputs*)
* **Rate Limiting:** [SlowAPI](https://github.com/laurentS/slowapi) (Membatasi panggilan API secara pintar)
* **Parsing:** `PyMuPDF` (PDF) & `python-docx` (Word) untuk mengekstrak teks resume

---

## 📂 Struktur Direktori

```bash
├── backend/            # Aplikasi Backend FastAPI
│   ├── app/            # Kode utama (Routers, Schemas, Services, Models, dll)
│   ├── data/           # Tempat penyimpanan lokal (Profil resume tersimpan)
│   ├── requirements.txt# Dependensi Python
│   └── alembic/        # Skrip migrasi database
├── frontend/           # Aplikasi Frontend Nuxt 4
│   ├── app/            # Halaman (Pages), Komponen (Components), Composables, Stores
│   ├── public/         # Aset statis publik
│   └── nuxt.config.ts  # Konfigurasi Nuxt
└── docker-compose.yml  # Layanan Docker untuk PostgreSQL local
```

---

## 🚀 Cara Cepat Menjalankan Aplikasi (Local Development)

Untuk menjalankan seluruh platform secara lokal, ikuti 3 langkah mudah berikut di terminal Anda:

### Langkah 1: Jalankan Database (Docker)
Di root direktori proyek, jalankan PostgreSQL menggunakan Docker:
```bash
docker-compose up -d
```

### Langkah 2: Jalankan Server Backend (FastAPI)
Buka terminal baru, masuk ke folder `backend`, aktifkan virtual environment, dan jalankan server:
```bash
cd backend
source venv/bin/activate      # Untuk Windows: venv\Scripts\activate
uvicorn app.main:app --reload --port 8000
```
*Backend kini aktif di: `http://localhost:8000` (Dokumentasi API interaktif di: `http://localhost:8000/docs`)*

### Langkah 3: Jalankan Aplikasi Frontend (Nuxt)
Buka terminal baru lainnya, masuk ke folder `frontend`, dan jalankan server dev Nuxt:
```bash
cd frontend
npm run dev
```
*Aplikasi frontend kini aktif di: `http://localhost:3000`*

---

## ⚙️ Instalasi & Persiapan Pertama Kali (Setup)

Jika Anda baru pertama kali mengunduh repositori ini, lakukan konfigurasi awal berikut:

### Prasyarat
* Python 3.10 ke atas (direkomendasikan Python 3.13)
* Node.js v18 ke atas & NPM
* Docker (untuk PostgreSQL lokal)

### Setup Backend (Pertama Kali)
1. Masuk ke folder backend: `cd backend`
2. Buat virtual environment: `python3 -m venv venv`
3. Aktifkan venv: `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
4. Install dependensi: `pip install -r requirements.txt`
5. Salin `.env.example` menjadi `.env` dan lengkapi konfigurasinya:
   ```ini
   DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/resume_analyzer
   SECRET_KEY=ganti_dengan_key_rahasia_acak
   GEMINI_API_KEY=AIzaSy... # Dapatkan key di Google AI Studio
   ```
6. Jalankan migrasi database: `alembic upgrade head`

### Setup Frontend (Pertama Kali)
1. Masuk ke folder frontend: `cd frontend`
2. Install dependensi npm: `npm install`
3. Buat file `.env` di dalam folder `frontend` untuk mengarahkan ke API backend:
   ```ini
   API_BASE_URL=http://localhost:8000/api/v1
   ```

---

## 📝 Alur Penggunaan Aplikasi
1. Buka `http://localhost:3000` di browser.
2. Daftar akun baru (**Register**) dan masuk (**Login**).
3. Buka menu **Manage Profile** untuk mengunggah resume utama Anda (PDF/DOCX). Resume ini akan disimpan secara aman di folder `backend/data/profiles/{user_id}.txt`.
4. Klik tombol **New Analysis** di Dashboard:
   - Pilih opsi **Use Saved Profile** (atau unggah resume baru khusus untuk analisis ini).
   - Masukkan deskripsi pekerjaan: salin teks manual ATAU klik **Import from URL** untuk menempelkan link lowongan kerja dan mengambil detailnya secara otomatis.
5. Klik **Analyze Resume** untuk melihat skor ATS, daftar keyword yang hilang, serta saran perbaikan dari AI.
6. Unduh laporan hasil dengan menekan **Download PDF**, atau buat surat lamaran kerja terpersonalisasi melalui fitur **Cover Letter**.
