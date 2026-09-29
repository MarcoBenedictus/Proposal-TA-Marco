# Konfigurasi latexmk
# Jalankan cukup dengan:  latexmk -pdf laporan
$pdf_mode        = 1;      # gunakan pdflatex
$bibtex_use      = 2;      # jalankan bibtex dan bersihkan .bbl saat -C
$max_repeat      = 5;      # ulangi sampai rujukan silang stabil
$clean_ext       = "lap bbl blg run.xml synctex.gz";
