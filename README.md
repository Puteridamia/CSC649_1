# CSC649 Setup

## Description
Program ini menerima satu ayat daripada pengguna dan mengira jumlah perkataan dan aksara (termasuk ruang). Ia juga menyemak jika input adalah kosong.

## How to Run
1. Pastikan persekitaran maya Python (`.venv`) aktif.
2. Jalankan skrip menggunakan terminal: `python main.py` atau tekan butang Run.
3. Masukkan ayat apabila diminta.

## Test Results
- Normal sentence: "Hello world" -> Word count: 2, Character count: 11
- Empty input: "" -> "You did not enter a sentence."
- Extra spaces: "   Hello   world   " -> Word count: 2, Character count: 19

## Limitation
Logik pengiraan menggunakan `.split()`, yang akan mengira apa-apa rentetan aksara sebagai perkataan selagi ia dipisahkan oleh ruang (space), termasuklah tanda baca (punctuation).