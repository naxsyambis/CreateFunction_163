import math #Liblary untuk operasi matematika

luas_lingkaran = lambda r: math.pi * r*r
#lamda : cara cepat membuat fungsi dalam 1 baris, rumus: π × r²

#contoh penggunaanya masukkan nilai jari2 = 7
jari_jari = 7
#area : memanggil fungsi luas_lingkaran dengan nilai jari2 = 7
area = luas_lingkaran(jari_jari)
#Mencetak hasil dengan format 2 angka dibelakang koma (.2f)
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")