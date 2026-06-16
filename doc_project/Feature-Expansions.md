# Feature Expansions & Ideas
**AI Resume Analyzer**

Dokumen ini berisi daftar ide fitur lanjutan untuk mengembangkan aplikasi AI Resume Analyzer menjadi produk yang lebih kaya fitur dan bernilai jual tinggi (*Killer Features*). Fitur-fitur ini direncanakan untuk dikerjakan setelah *Core MVP* selesai.

---

## 1. ✍️ Cover Letter Generator (Pembuat Surat Lamaran)
**Deskripsi:** Memberikan opsi kepada pengguna untuk men-generate *Cover Letter* (Surat Lamaran) yang sangat dikhususkan (tailored) berdasarkan Resume pengguna dan *Job Description* yang sedang dianalisis.

**Kebutuhan Backend:**
- Endpoint baru: `POST /api/v1/analysis/{id}/cover-letter`
- AI Prompt: Meminta AI untuk menulis surat lamaran profesional sepanjang 3-4 paragraf yang menyoroti kekuatan pengguna yang cocok dengan posisi yang dilamar.
- Schema DB: Menambahkan field `cover_letter` (teks) pada tabel `Analysis` (atau membuat tabel relasi baru).

**Kebutuhan Frontend:**
- Tombol aksi "Generate Cover Letter" di halaman *Result*.
- UI Modal atau halaman khusus (*text editor*) untuk melihat, mengedit secara manual, dan menyalin (Copy) teks *Cover Letter* yang dihasilkan AI.

---

## 2. 🎯 AI Resume Rewriter (Penyempurna Kalimat CV)
**Deskripsi:** AI tidak hanya memberikan saran, tetapi dapat menulis ulang (*rewrite*) poin-poin pengalaman kerja pengguna menjadi lebih profesional dan memiliki *impact* yang kuat (menggunakan *Action Verbs* dan format STAR - Situation, Task, Action, Result).

**Kebutuhan Backend:**
- Endpoint baru: `POST /api/v1/ai/rewrite-bullet`
- AI Prompt: Mengambil teks *bullet point* mentah dari pengguna, dan mengembalikan 3 variasi kalimat yang sudah dipoles.

**Kebutuhan Frontend:**
- Tool/UI khusus di mana pengguna bisa melakukan *paste* kalimat CV lama mereka, lalu menekan tombol "Optimize", dan melihat 3 opsi perbaikan dari AI yang bisa langsung di-*copy*.

---

## 3. 🎙️ Interview Prep (Simulasi Pertanyaan Wawancara)
**Deskripsi:** Menghasilkan prediksi pertanyaan wawancara yang kemungkinan besar akan ditanyakan oleh HRD/User berdasarkan *gap* (kekurangan) di CV pengguna saat dicocokkan dengan *Job Description*.

**Kebutuhan Backend:**
- Endpoint baru: `POST /api/v1/analysis/{id}/interview-prep`
- AI Prompt: Menghasilkan 5-7 pertanyaan (kombinasi teknikal dan *behavioral*) beserta panduan singkat cara pengguna harus menjawabnya.

**Kebutuhan Frontend:**
- *Tab* tambahan di halaman *Result* ("Interview Prep").
- Desain *Accordion* UI untuk menampilkan pertanyaan dan jawaban saran dari AI.

---

## 4. 📄 Export to PDF
**Deskripsi:** Fitur untuk mengunduh hasil analisis lengkap (Skor, Kekurangan, Saran) menjadi sebuah file PDF dengan desain yang rapi.

**Kebutuhan Backend / Frontend:**
- **Opsi A (Frontend-only):**t Menggunakan pustaka seperti `html2pdf.js` atau `jspdf` untuk me-render elemen DOM dari halaman *Result* langsung menjadi PDF di peramban pengguna.
- **Opsi B (Backend-only):** Menggunakan Python (`WeasyPrint` atau `pdfkit`) untuk meng-generate dokumen PDF standar dari data JSON.

---

## 5. 📁 Saved Profiles (Profil CV Tersimpan)
**Deskripsi:** Pengguna dapat menyimpan *Resume* utama mereka ke profil akun. Ke depannya, mereka tidak perlu mengunggah ulang file PDF/DOCX. Mereka cukup mem-*paste* tautan lowongan atau *Job Description*, dan sistem langsung menganalisisnya.

**Kebutuhan Backend:**
- Tabel DB baru: `Profile` atau relasi *One-to-One* dengan `User` yang menyimpan `base_resume_text`.
- Endpoint `PUT /api/v1/users/me/resume` untuk memperbarui *base resume*.
- Modifikasi di endpoint `POST /api/v1/analysis` untuk mengizinkan analisis tanpa file unggahan (menggunakan profil tersimpan).

**Kebutuhan Frontend:**
- Halaman "My Profile" untuk mengelola dan melihat ekstrak teks dari Resume tersimpan.
- Checkbox di halaman *New Analysis* untuk memilih "Gunakan Resume Tersimpan".

---

## 6. 📊 Analytics Dashboard
**Deskripsi:** Menampilkan grafik garis atau ringkasan historis mengenai progres skor lamaran pengguna dari waktu ke waktu.

**Kebutuhan Backend:**
- Endpoint statistik (misal: `GET /api/v1/analysis/stats`) yang mengembalikan rata-rata skor per minggu/bulan.

**Kebutuhan Frontend:**
- Integrasi *library* *Chart.js* atau *ApexCharts* pada halaman `Dashboard`.
- UI ringkasan: "Total Analisis: 15", "Rata-rata Skor: 75%".
