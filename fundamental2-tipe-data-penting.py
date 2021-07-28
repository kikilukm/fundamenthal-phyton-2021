print('Tipe data Skalar / tipe data sederhana ')

anak1 = 'Kiki'
anak2 = 'Anggi'
anak3 = 'Sopi'
anak4 = 'Dera'
anak5 = 'Disa'

print('Hai Anaku', anak1)
print('Hai Anaku', anak2)
print('Hai Anaku', anak3)
print('Hai Anaku', anak4)
print('Hai Anaku', anak5)

print('\nTipe Data List/Daftar/Array')

anak = ['Kiki', 'Anggi', 'Sopi', 'Dera', 'Disa']
print(anak)
anak.append('Kamal')  # menambahkan data kedalam list
print(anak)

print('\nSapa Anak ke Dua')
print(f'Hai anakku {anak[1]}!')

print('\nPanggil semua anak')
for a in anak:
    print(f'Hai Anakku {a}!')

print('\nSapa semua anak cara rumit')

for a in range(0,len(anak)):
    print(f'{a+1}. Hai anakku {anak[a]}!')