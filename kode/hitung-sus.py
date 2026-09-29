"""Menghitung skor System Usability Scale (SUS)."""

# Butir bernomor ganjil bersifat positif
BUTIR_POSITIF = [1, 3, 5, 7, 9]


def hitung_sus(jawaban):
    """Skor SUS (0-100) dari 10 jawaban skala 1-5."""
    if len(jawaban) != 10:
        raise ValueError("Jawaban harus 10 butir")

    total = 0
    for nomor, nilai in enumerate(jawaban, start=1):
        if nomor in BUTIR_POSITIF:
            total += nilai - 1
        else:
            total += 5 - nilai
    return total * 2.5


if __name__ == "__main__":
    contoh = [4, 2, 5, 1, 4, 2, 5, 2, 4, 3]
    print(f"Skor SUS: {hitung_sus(contoh):.1f}")
