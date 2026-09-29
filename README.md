# Template LaTeX Tugas Akhir — Program Studi Sistem Informasi (S1)

Template ini menyediakan kerangka lima bab beserta seluruh halaman legal,
daftar otomatis, dan galeri contoh elemen. Isinya dirancang agar mahasiswa
cukup mengganti teks contoh tanpa perlu menyentuh pengaturan tata letak.

---

## Cara memulai

1. **Isi `a0-identitas.tex`.** Ini satu-satunya berkas yang wajib diisi.
   Seluruh halaman sampul, persetujuan, pengesahan, dan pernyataan mengambil
   datanya dari sini.
2. **Ganti logo.** Timpa `gambar/logo-institusi.png` dengan logo institusi Anda.
   Rasio apa pun aman karena ukurannya diatur berdasarkan tinggi.
3. **Tulis naskah** pada `b1-bab1.tex` sampai `b5-bab5.tex`, mengikuti pola
   contoh yang sudah tersedia.
4. **Matikan galeri** sebelum naskah dikumpulkan. Beri tanda `%` pada baris
   `\include{zz-galeri-elemen}` di `laporan.tex`.

## Cara kompilasi

```
pdflatex laporan
bibtex   laporan
pdflatex laporan
pdflatex laporan
```

Atau cukup `latexmk -pdf laporan` (berkas `latexmkrc` sudah disertakan).
Di Overleaf, tekan **Recompile** — urutan di atas dijalankan otomatis.

Kompilasi perlu dijalankan **empat kali** karena daftar isi, daftar gambar,
daftar tabel, daftar lampiran, rujukan silang, dan daftar pustaka saling
bergantung. Jika ada rujukan yang masih tampil sebagai `??`, jalankan
`pdflatex` sekali lagi.

---

## Struktur berkas

### Lapis mesin — tidak perlu diubah

| Berkas | Isi |
|---|---|
| `laporan.tex` | Berkas induk, mengatur urutan bagian |
| `xx-preambles.tex` | Paket, margin, huruf, format bab, penomoran |
| `xx-sampul.tex`, `xx-sampuldalam.tex` | Halaman sampul |
| `xx-persetujuan.tex`, `xx-pengesahan.tex`, `xx-pernyataan.tex` | Halaman legal |
| `xx-daftar.tex` | Daftar isi, gambar, tabel, lampiran (otomatis) |
| `xx-daftarpustaka.tex` | Pembungkus daftar pustaka |
| `apalike-id.bst` | Gaya sitasi APA dengan kata sambung "dan" |

### Lapis konten — silakan diubah

| Berkas | Isi |
|---|---|
| `a0-identitas.tex` | **Data Anda + pilihan gaya sitasi** |
| `a2-abstrak.tex`, `a3-abstract.tex` | Abstrak dan abstract |
| `a4-persembahan.tex` | Persembahan (opsional) |
| `a5-katapengantar.tex` | Kata pengantar |
| `a6-daftarsingkatan.tex` | Daftar singkatan |
| `a7-pustaka.bib` | Basis data rujukan |
| `a8-lampiran.tex` | Lampiran A, B, C |
| `b1-bab1.tex` … `b5-bab5.tex` | Isi lima bab |
| `gambar/` | Berkas gambar |
| `kode/` | Berkas kode program untuk dilampirkan |
| `zz-galeri-elemen.tex` | **Galeri contoh — hapus sebelum dikumpulkan** |

---

## Benang merah rumusan masalah

Template ini menyediakan mekanisme agar rumusan masalah tertaut otomatis dari
Bab 1 sampai Bab 5.

**Menulis rumusan masalah** (Bab 1):

```latex
\begin{rumusanmasalah}
    \item Bagaimana tingkat kualitas layanan?\label{rq:kualitas}
    \item Bagaimana kesenjangannya?\label{rq:kesenjangan}
\end{rumusanmasalah}
```

**Merujuknya** dari bab mana pun: `\cref{rq:kualitas}` menghasilkan `RQ1`.
Bila urutan rumusan masalah diubah, seluruh rujukan menyesuaikan sendiri.

**Matriks keterkaitan** pada Bab 3 memetakan setiap rumusan masalah ke tujuan,
data, teknik analisis, dan subbab hasil. Matriks ini mencegah dua cacat yang
paling sering terjadi: bab hasil memuat pekerjaan yang tidak pernah ditanyakan,
dan kesimpulan menjawab pertanyaan yang tidak pernah diajukan.

---

## Gaya sitasi

Diatur lewat satu baris pada `a0-identitas.tex`:

| Nilai | Keterangan |
|---|---|
| `apalike-id` | **Bawaan.** APA nama-tahun, kata sambung "dan". Berkas `.bst` disertakan. |
| `apalike` | Sama, tetapi kata sambungnya "and" (bawaan LaTeX). |
| `apacite` | APA lebih ketat. Perlu paket `apacite` — tersedia di Overleaf dan MiKTeX penuh, tidak pada semua instalasi. Bila dipakai, aktifkan juga `\usepackage{apacite}` pada `xx-preambles.tex` bagian 11. |

Bentuk sitasi: `\citep{kunci}` menghasilkan (Nama, 2020), `\citet{kunci}`
menghasilkan Nama (2020). Contoh lengkap ada di galeri.

`apalike-id.bst` adalah turunan dari `apalike.bst` karya Oren Patashnik.
Lisensi aslinya mengizinkan modifikasi sepanjang berkas hasilnya diganti nama,
dan syarat tersebut dipenuhi. Satu-satunya perubahan adalah kata sambung
antarpenulis dari "and" menjadi "dan".

---

## Galeri elemen

Berkas `zz-galeri-elemen.tex` memuat contoh siap salin untuk:

- **Tabel** — biasa, gaya booktabs, bersambung antarhalaman (`longtable`),
  bersel gabung (`multirow`), berkolom otomatis (`tabularx`), bercatatan kaki
  (`threeparttable`), terlalu lebar (`adjustbox`), dan lanskap.
- **Gambar** — tunggal, bersumber, dua berdampingan (a)(b), tinggi satu
  halaman, dan lanskap.
- **Persamaan** — dalam baris, bernomor, bertingkat (`align`), dan matriks.
- **Kode program** — Python, SQL, Java, PHP, dibaca langsung dari berkas
  (`\lstinputlisting`), serta pseudocode (`algorithm2e`).
- **Sitasi** — seluruh bentuk `natbib`, kutipan blok, dan katalog tipe entri
  `.bib`.

Galeri diberi nomor bab **G** agar jelas terpisah dari naskah. Begitu
dimatikan, entri katalog `.bib` juga hilang sendiri dari daftar pustaka.

---

## Catatan teknis

**Halaman lanskap** memakai `pdflscape`, sehingga halamannya ikut diputar pada
berkas PDF — pembaca tidak perlu memiringkan layar.

**Baris kode** sebaiknya tidak lebih dari sekitar 60 karakter agar tidak
meluber ke tepi halaman.

**Logo sampul** diatur dengan `height`, bukan `width`. Ini disengaja: logo
berbentuk memanjang akan jauh lebih tinggi daripada logo bujur sangkar pada
lebar yang sama, dan itu dapat mendorong baris terakhir sampul ke halaman
berikutnya. Dengan `height`, tinggi sampul tetap sama untuk rasio logo apa pun.

**Bahasa.** Paket `babel` bahasa Indonesia diganti pengaturan istilah manual
(BAB, Gambar, Tabel, Lampiran) agar template dapat dikompilasi di lingkungan
mana pun. Karena pemenggalan kata memang dimatikan, tidak ada fitur yang
hilang. Cara mengaktifkan `babel` dijelaskan pada komentar di
`xx-preambles.tex` bagian 1.

**Keterangan tabel** diletakkan di atas tabel, **keterangan gambar** di bawah
gambar, sesuai konvensi penulisan ilmiah Indonesia.

---

## Peringatan tentang isi contoh

Seluruh teks pada `b1-bab1.tex` sampai `b5-bab5.tex` adalah **contoh berjalan**
bertema WebQual 4.0. Angka, tabel, dan temuannya **fiktif**.

Pada `a7-pustaka.bib`, entri bertanda `[CONTOH FIKTIF]` **bukan sumber nyata**
dan harus dihapus. Entri bertanda `[NYATA]` adalah rujukan sungguhan
(Barnes & Vidgen, 2002; Martilla & James, 1977) dan boleh dipertahankan bila
memang Anda gunakan.

---

## Bahasa naskah

Sebagian mahasiswa menulis Tugas Akhir dalam Bahasa Inggris. Template ini
menyediakan sakelar pada `a0-identitas.tex`:

| Nilai | Istilah struktural |
|---|---|
| `id` | **Bawaan.** BAB, Gambar, Tabel, DAFTAR ISI, DAFTAR PUSTAKA |
| `en` | CHAPTER, Figure, Table, TABLE OF CONTENTS, BIBLIOGRAPHY |

Halaman legal (persetujuan, pengesahan, pernyataan keaslian) tetap Bahasa
Indonesia pada kedua pilihan, karena merupakan dokumen resmi institusi.
Untuk naskah berbahasa Inggris, disarankan memakai `\gayasitasi` bernilai
`apalike` (kata sambung "and"), bukan `apalike-id`.

## Dua perintah bantu

**`\gambarbelumada{Keterangan}{fig:label}`** menghasilkan kotak bergaris
putus-putus bertuliskan "BERKAS GAMBAR BELUM TERSEDIA". Gambar tetap terdaftar
pada Daftar Gambar dan dapat dirujuk `\cref`, sehingga naskah tetap dapat
dikompilasi sebelum seluruh gambar tersedia. Ganti dengan `\includegraphics`
biasa setelah berkasnya siap.

**`\belumdiisi{N}`** menghasilkan teks merah tebal dalam kurung siku untuk
menandai data yang belum diisi, sehingga mustahil terlewat saat naskah dibaca
ulang.

Keduanya wajib dihapus sebelum naskah dikumpulkan.

---

## Halaman legal: dua versi

Template menyediakan dua versi halaman legal. **Pilih salah satu**, lalu beri
tanda `%` pada blok yang tidak dipakai di `laporan.tex`.

### Versi A — Formulir resmi FR-UAJ

| Berkas | Kode formulir |
|---|---|
| `xx-form-pembimbing.tex` | FR-UAJ-07-39/R0 Pernyataan Pembimbing |
| `xx-form-selesai.tex` | FR-UAJ-07-40/R0 Pernyataan Tanda Selesai |
| `xx-form-pengesahan.tex` | FR-UAJ-07-46/R0 Pengesahan Tugas Akhir |
| `xx-form-keaslian.tex` | FR-UAJ-07-47/R0 Pernyataan Keaslian |

Keempatnya memakai kop `gambar/kop-uaj.png` dan mengambil data dari
`a0-identitas.tex`, sehingga tidak perlu diketik ulang.

Posisi dan ukuran kop diatur lewat tiga panjang pada `xx-preambles.tex`:

| Panjang | Bawaan | Fungsi |
|---|---|---|
| `\kopnaik` | 2,25 cm | seberapa jauh kop ditarik ke atas |
| `\kopkiri` | 1,6 cm | seberapa jauh kop digeser ke kiri |
| `\koplebar` | 4,6 cm | lebar gambar kop |

Ketiganya diperlukan karena halaman formulir mewarisi margin buku (kiri 4 cm,
atas 3 cm) yang membuat kop terdorong ke tengah. Nilai bawaan menempatkan kop
di 2,56 cm dari kiri dan 1,27 cm dari atas, sehingga posisi vertikalnya sama
dengan formulir asli. Margin isi formulir tidak ikut berubah, tetap 4 cm agar
aman saat dijilid. Halaman ini sengaja
tidak diberi nomor agar tampilannya sama dengan formulir aslinya, tetapi
penghitung halaman tetap berjalan sehingga penomoran sesudahnya tidak bergeser.

Data tambahan yang perlu diisi khusus untuk formulir ini: `\stid`,
`\kotaformulir`, `\tglujian`, `\periodeujian`, dan `\tglkoreksi`.

Pada FR-UAJ-07-39 dan FR-UAJ-07-40, judul Tugas Akhir dipecah manual menjadi
beberapa baris berikut garis isian, mengikuti bentuk formulir aslinya.
Sesuaikan pemenggalannya dengan judul Anda.

Formulir Pernyataan Keaslian memerlukan meterai. Tempatnya disediakan sebagai
kotak putus-putus; ganti dengan `\includegraphics` bila memakai e-meterai.

### Versi B — Halaman legal versi template

`xx-persetujuan.tex`, `xx-pengesahan.tex`, dan `xx-pernyataan.tex`. Bentuknya
lebih umum dan tidak terikat kode formulir, cocok bila program studi tidak
mensyaratkan formulir FR-UAJ.

---

## Bila kompilasi tiba-tiba gagal setelah mengubah `\include`

Menonaktifkan sebuah `\include` dapat menyisakan berkas `.aux` lama yang
membuat bibtex gagal dengan pesan `I found no \citation commands`. Solusinya
bersihkan artefak lebih dulu:

```
latexmk -C
latexmk -pdf laporan
```

Di Overleaf, gunakan menu **Logs and output files → Clear cached files**.

---

## Logo

| Berkas | Dipakai pada | Asal |
|---|---|---|
| `gambar/logo-institusi.png` | Sampul luar dan sampul dalam | Lambang perisai, dipotong dari `kop-uaj.png` |
| `gambar/kop-uaj.png` | Kop keempat formulir FR-UAJ | Berkas kop resmi |

Lambang pada sampul berukuran 195x322 piksel, yang setara 256 DPI bila dicetak
setinggi 3,2 cm. Angka itu memadai untuk gambar garis, tetapi bila tersedia
berkas logo resmi beresolusi lebih tinggi, sebaiknya timpa saja berkasnya
dengan nama yang sama.

Ukuran logo sampul diatur dengan `height`, bukan `width`, sehingga rasio logo
apa pun tidak akan membuat sampul meluber ke halaman berikutnya.

---

## Mengganti label RQ dan T

Awalan label pada daftar rumusan masalah dan tujuan diatur lewat dua baris di
`a0-identitas.tex`:

```latex
\newcommand{\labelrq}{RQ}      % menghasilkan RQ1, RQ2, ...
\newcommand{\labeltujuan}{T}   % menghasilkan T1, T2, ...
```

Mengubah kedua baris ini akan mengganti label di **seluruh** naskah sekaligus:
daftar rumusan masalah di Bab 1, matriks keterkaitan di Bab 3, kesimpulan di
Bab 5, serta setiap rujukan `\cref` di mana pun. Tidak ada tempat lain yang
perlu disunting.

Contoh: mengganti menjadi `P` dan `TJ` menghasilkan P1, P2, P3 dan TJ1, TJ2,
TJ3. Kerataan label terhadap nomor subbab tetap terjaga karena label
dirata-kirikan di dalam kotaknya, bukan bergantung pada lebar teksnya.

Jika label yang dipakai lebih panjang daripada sekitar empat karakter, misalnya
`RUMUS1.`, lebarkan juga kotak labelnya pada `xx-preambles.tex` agar teks
tidak terdorong:

```latex
\setlength{\labelwidth}{2.4em}   % lebarkan bila label lebih panjang
\setlength{\leftmargin}{3.0em}   % harus selalu = labelwidth + labelsep
```

## Dua naskah dalam satu template: Tugas Akhir dan Proposal

Template ini punya **dua berkas master tipis** yang berbagi berkas konten yang sama:

- `laporan.tex` — naskah **Tugas Akhir** (lima bab, lengkap dengan halaman legal FR-UAJ).
- `proposal.tex` — naskah **Proposal Tugas Akhir** (tiga bab, Lembar Persetujuan).

Keduanya diatur satu sakelar di baris atas masing-masing master:

```latex
\newcommand{\jenisnaskah}{ta}        % pada laporan.tex
\newcommand{\jenisnaskah}{proposal}  % pada proposal.tex
```

Sakelar ini otomatis: mengubah label sampul ("TUGAS AKHIR" / "PROPOSAL TUGAS
AKHIR"), memilih halaman legal yang sesuai, menampilkan sistematika 3 bab pada
proposal, dan menyembunyikan Daftar Lampiran pada proposal. **Bab 1 dan Bab 2
dipakai bersama** oleh kedua naskah, sehingga apa yang dijanjikan pada proposal
persis menjadi yang dibuktikan pada Tugas Akhir. Bab 3 proposal memakai
`b3-proposal.tex` (rancangan penelitian + jadwal), sedangkan Tugas Akhir memakai
`b3-bab3.tex` (metode penelitian).

### Jumlah pembimbing (1 atau 2)

Diatur di `a0-identitas.tex`:

```latex
\newcommand{\jumlahpembimbing}{2}   % 1 atau 2
\newcommand{\pembimbingdua}{...}    % diisi bila 2 pembimbing
\newcommand{\NIPpembimbingdua}{...}
\newcommand{\tglpersetujuandua}{...}
```

Sakelar ini mengatur blok tanda tangan pada Lembar Persetujuan dan formulir
FR-UAJ secara otomatis.

### Kompilasi

- Overleaf: set **Main document** ke `proposal.tex` atau `laporan.tex`, lalu Recompile.
- Lokal: `latexmk -pdf proposal` atau `latexmk -pdf laporan`.
