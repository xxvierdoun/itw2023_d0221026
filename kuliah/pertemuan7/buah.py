# Harga buah per kilogram
harga_apel_per_kg = 5000
harga_anggur_per_100g = 3000
harga_jeruk_per_3_kg = 45000

# Berat yang harus dibeli
berat_apel = 20
berat_anggur = 18
berat_rambutan = 17
berat_jeruk = 29

# Harga total buah tanpa diskon
total_harga_apel = (berat_apel * 1000) * harga_apel_per_kg
total_harga_anggur = (berat_anggur * 10) * harga_anggur_per_100g
total_harga_jeruk = (berat_jeruk / 3) * harga_jeruk_per_3_kg

# Hitung total bonus untuk masing-masing buah
bonus_apel = (berat_apel // 5) * 0.5
bonus_anggur = (berat_anggur // 5) * 0.5
bonus_jeruk = (berat_jeruk // 5) * 0.5

# Total bonus keseluruhan
total_bonus = (bonus_apel * 1000 * harga_apel_per_kg) + (bonus_anggur * 10 * harga_anggur_per_100g) + (bonus_jeruk / 3 * harga_jeruk_per_3_kg)

# Hitung berat total
berat_total = berat_apel + berat_anggur + berat_rambutan + berat_jeruk

# Hitung diskon jika berat total melebihi 20 kg
diskon = 0
if berat_total > 20:
    diskon = (total_harga_apel + total_harga_anggur + total_harga_jeruk) * 0.002

# Hitung harga total dengan diskon
harga_total = (total_harga_apel + total_harga_anggur + total_harga_jeruk) - diskon + total_bonus

# Output program
print(f"Harga apel: {total_harga_apel} rupiah")
print(f"Harga anggur: {total_harga_anggur} rupiah")
print(f"Harga jeruk: {total_harga_jeruk} rupiah")
print(f"Total diskon: {diskon} rupiah")
print(f"Total bonus: {total_bonus} rupiah")
print(f"Total harga yang harus dibayar oleh Ucup: {harga_total} rupiah")
