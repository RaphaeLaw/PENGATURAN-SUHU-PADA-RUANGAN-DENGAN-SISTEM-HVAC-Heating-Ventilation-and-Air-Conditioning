"Tugas Besar Fuzzy Logic"
"Metode Sugeno"

print("PENGATURAN SUHU PADA RUANGAN DENGAN SISTEM HVAC")
suhu=int(input("Masukan Nilai Suhu yang diinginkan (C) : "))
orang=int(input("Banyak Orang pada Ruangan : "))

#Fuzzifikasi Suhu
if suhu <= 15 :
    value_dingin = 1
    value_panas = 0
if suhu > 15 and suhu < 25 :
    value_dingin = (25-suhu)/(25-15)
    value_panas = (suhu-15)/(25-15)
if suhu >= 25 :
    value_dingin = 0
    value_panas = 1

#Fuzzifikasi Orang
if orang <= 30 :
    value_sedikit = 1
    value_banyak = 0
if orang > 30 and orang < 70 :
    value_sedikit = (70-orang)/(70-30)
    value_banyak = (orang-30)/(70-30)
if orang >= 70 :
    value_sedikit = 0
    value_banyak = 1

print(".........................")
print("Hasil Proses Fuzzifikasi")
print("Hasil derajat keanggotaan Suhu")
print("Nilai Dingin = ", value_dingin)
print("Nilai Panas = ", value_panas)
print(".........................")
print("Hasil derajat Keanggotaan Orang")
print("Nilai Sedikit = ", value_sedikit)
print("Nilai Banyak = ", value_banyak)

#Rules Evaluation
print(".........................")
print("Sistem inferensi dengan menyesuaikan Aturan yang telah dibuat")
speed=[]
speed.clear()

#Diisi Titik 25
def fungsiinferensisangatrendah(value_suhu, value_orang):
    if value_suhu!=0 :
       if value_orang!=0:
           hasil_fungsi = min(value_suhu, value_orang)
           speed.append([hasil_fungsi,25])
def fungsiinferensiagakrendah(value_suhu, value_orang):
    if value_suhu!=0 :
       if value_orang!=0:
           hasil_fungsi = min(value_suhu, value_orang)
           speed.append([hasil_fungsi,40])
def fungsiinferensiagakkencang(value_suhu, value_orang):
    if value_suhu!=0 :
       if value_orang!=0:
           hasil_fungsi = min(value_suhu, value_orang)
           speed.append([hasil_fungsi,60])
def fungsiinferensisangatkencang(value_suhu, value_orang):
    if value_suhu!=0 :
       if value_orang!=0:
           hasil_fungsi = min(value_suhu, value_orang)
           speed.append([hasil_fungsi,80])

fungsiinferensisangatrendah(value_dingin, value_sedikit)
fungsiinferensiagakrendah(value_panas, value_sedikit)
fungsiinferensiagakkencang(value_dingin, value_banyak)
fungsiinferensisangatkencang(value_panas, value_banyak)