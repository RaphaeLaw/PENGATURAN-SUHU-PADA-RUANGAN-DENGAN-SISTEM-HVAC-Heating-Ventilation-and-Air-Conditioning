"Tugas Besar Fuzzy Logic"
"Metode Sugeno"

print("PENGATURAN SUHU PADA RUANGAN DENGAN SISTEM HVAC")
suhu=int(input("Masukan Nilai Suhu saat ini (C) : "))
orang=int(input("Banyak Orang pada Ruangan : "))

#Fuzzifikasi Suhu
if suhu <= 15 :
    value_dingin = 1
    value_panas = 0
elif suhu > 15 and suhu < 25 :
    value_dingin = (25-suhu)/(25-15)
    value_panas = (suhu-15)/(25-15)
elif suhu >= 25 :
    value_dingin = 0
    value_panas = 1

#Fuzzifikasi Orang
if orang <= 30 :
    value_sedikit = 1
    value_banyak = 0
elif orang > 30 and orang < 70 :
    value_sedikit = (70-orang)/(70-30)
    value_banyak = (orang-30)/(70-30)
elif orang >= 70 :
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
indexes = [[0, 0.2], [0, 0.4], [0, 0.6], [0, 0.8]]

#Diisi Titik 25
def fungsiinferensisangatrendah(value_suhu, value_orang):
    if value_suhu!=0 :
       if value_orang!=0:
           hasil_fungsi = min(value_suhu, value_orang)
           indexes[0] = [hasil_fungsi,0.2]
def fungsiinferensiagakrendah(value_suhu, value_orang):
    if value_suhu!=0 :
       if value_orang!=0:
           hasil_fungsi = min(value_suhu, value_orang)
           indexes[1] = [hasil_fungsi,0.4]
def fungsiinferensiagakkencang(value_suhu, value_orang):
    if value_suhu!=0 :
       if value_orang!=0:
           hasil_fungsi = min(value_suhu, value_orang)
           indexes[2] = [hasil_fungsi,0.6]
def fungsiinferensisangatkencang(value_suhu, value_orang):
    if value_suhu!=0 :
       if value_orang!=0:
           hasil_fungsi = min(value_suhu, value_orang)
           indexes[3] = [hasil_fungsi,0.8]

fungsiinferensisangatrendah(value_dingin, value_sedikit)
fungsiinferensiagakrendah(value_panas, value_sedikit)
fungsiinferensiagakkencang(value_dingin, value_banyak)
fungsiinferensisangatkencang(value_panas, value_banyak)

x1 = 0
x2 = 0
for index in indexes:
   x1 = x1 + (index[0] * index[1]) 
   x2 = x2 + index[0]

print("Bobot kecepatan Sangat Rendah: ", indexes[0][0])
print("Bobot kecepatan Agak Rendah: ", indexes[1][0])
print("Bobot kecepatan Agak Kencang: ", indexes[2][0])
print("Bobot kecepatan Sangat Kencang: ", indexes[3][0])
print()
decision_index = x1 / x2
print("Crisp Decision Index : {:.4f}".format(decision_index))

fuzzy_decision = [0, 0, 0, 0]
if(decision_index <= 0.2):
    fuzzy_decision[0] = 1
if(decision_index > 0.2 and decision_index <= 0.4):
    x2 = decision_index - 0.2
    x1 = 0.4 - decision_index 
    x3 = x1 + x2
    fuzzy_decision[0] = x1 / x3
    fuzzy_decision[1] = x2 / x3
if(decision_index > 0.4 and decision_index <= 0.6):
    x2 = decision_index - 0.4
    x1 = 0.6 - decision_index
    x3 = x1 + x2
    fuzzy_decision[1] = x1 / x3
    fuzzy_decision[2] = x2 / x3
if(decision_index > 0.6 and decision_index <= 0.8):
    x2 = decision_index - 0.6
    x1 = 0.8 - decision_index
    x3 = x1 + x2
    fuzzy_decision[2] = x1 / x3
    fuzzy_decision[3] = x2 / x3
if(decision_index > 0.8):
    fuzzy_decision[3] = 1

print("Fuzzy Decision Index : ")
if(fuzzy_decision[0] > 0):
    print("{:.2f}% Sangat Rendah".format(fuzzy_decision[0] * 100), end=" ")
if(fuzzy_decision[1] > 0):
    print("{:.2f}% Agak Rendah".format(fuzzy_decision[1] * 100), end=" ")
if(fuzzy_decision[2] > 0):
    print("{:.2f}% Agak Kencang".format(fuzzy_decision[2] * 100), end=" ")
if(fuzzy_decision[3] > 0):
    print("{:.2f}% Sangat Kencang".format(fuzzy_decision[3] * 100))
print()
