# Mean-Variance-Standard Deviation Calculator

Solusi proyek freeCodeCamp *Data Analysis with Python* — Mean-Variance-Standard Deviation Calculator.

## Struktur

| File | Keterangan |
|------|-----------|
| `mean_var_std.py` | Implementasi fungsi `calculate()` (Numpy) |
| `main.py` | Entry point: contoh perhitungan + menjalankan unit test |
| `test_module.py` | Unit test (unittest) |
| `requirements.txt` | Dependensi (`numpy`) |

## Cara Pakai

```bash
pip install -r requirements.txt
python main.py
```

## Spesifikasi

`calculate(list_input)` menerima list berisi 9 angka, membentuk matriks 3x3, lalu
mengembalikan dict berisi `mean`, `variance`, `standard deviation`, `max`, `min`, `sum`
untuk `axis=0`, `axis=1`, dan matriks flattened.

- Melempar `ValueError("List must contain nine numbers.")` bila panjang list != 9.
- Semua nilai dikembalikan sebagai `list` Python (bukan array Numpy).

## Contoh

```python
from mean_var_std import calculate

calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
# => {
#   'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
#   'variance': [[6.0, 6.0, 6.0], [0.666..., 0.666..., 0.666...], 6.666...],
#   'standard deviation': [[2.449..., 2.449..., 2.449...], [0.816..., 0.816..., 0.816...], 2.581...],
#   'max': [[6, 7, 8], [2, 5, 8], 8],
#   'min': [[0, 1, 2], [0, 3, 6], 0],
#   'sum': [[9, 12, 15], [3, 12, 21], 36]
# }
```

## Hasil Test

```
Ran 4 tests in 0.002s
OK
```
