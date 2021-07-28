"""
Tipe Data Dictionary sekedar menghubungkan Key dengan Value
KVP - Key Value Pair
Dictionary=Kamus
"""
print('Contoh Dictionary Pertama')

kamus_in_eng={}
kamus_in_eng['anak']= 'son'
kamus_in_eng['istri']= 'wive'
kamus_in_eng['ayah']= 'father'
kamus_in_eng['ibu']= 'mother'
print(kamus_in_eng)

print('-'*10)

print('Contoh Dictionary kedua')

kamus_in_eng= {'anak': 'son', 'istri': 'wive', 'ayah': 'father', 'ibu': 'mother'}
print(kamus_in_eng)

print('-'*10)

print('Data dari server gojek')
data_server_gojek={
    'tanggal':'2021-07-28',
    'driver_list':[{'nama':'Kiki','jarak':10},
                   {'nama':'Sopi','jarak':89},
                   {'nama':'Anggi','jarak':35},
                   {'nama':'Dera','jarak':100},
                   {'nama':'Disa','jarak':44}]
}

print(f'\nData Dari Server Gojek {data_server_gojek}')
print(f"Driver Disekitar anda dengan jarak {data_server_gojek['driver_list']}")
print(f"Driver Disekitar anda tanpa jarak "
      f"{data_server_gojek['driver_list'][0]['nama']},"
      f"{data_server_gojek['driver_list'][1]['nama']},"
      f"{data_server_gojek['driver_list'][2]['nama']},"
      f"{data_server_gojek['driver_list'][3]['nama']},"
      f"{data_server_gojek['driver_list'][4]['nama']},")
print(f"Driver #1 {data_server_gojek['driver_list'][0]['nama']}"),
print(f"Driver #3 {data_server_gojek['driver_list'][2]['nama']}")

print(f"\nDriver dengan jarak terdekat saat ini {data_server_gojek['driver_list'][0]['jarak']} KM")
print(f"\nDriver dengan jarak terdekat saat ini {data_server_gojek['driver_list'][0]['nama']} ")
print(f"\n{data_server_gojek['driver_list'][0]['nama']}")
