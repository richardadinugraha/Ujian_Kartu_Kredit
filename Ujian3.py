import json
with open("ccNasabah.json", "r") as ccN:
    out = json.load(ccN)

'''
Adapun kriteria nomorKartu kartu kredit yang valid adalah sebagai berikut:
Diawali dengan angka 4, 5 atau 6.
Terdiri atas tepat 16 digit angka.
Hanya mengandung angka 0-9.
Boleh dituliskan berupa grup 4 digit yang dipisahkan dengan tanda hubung "-"
Tidak boleh terdapat 1 angka yang diulang >3x & tertulis secara beruntun, misal: 3333.
'''

letter = [
    'a','b','c','d','e','f','g','h','i',
        'j','k','l','m','n','o','p','q','r','s','t','u',
        'v','w','x','y','z'
]
valid = []
invalid = []

for i in range(len(out)):
    nomorKartu = out[i]['noCreditCard']
    nomorKartu = nomorKartu.split('-')
    nomorKartu = ''.join(nomorKartu)

    if nomorKartu[0]=='4' and len(nomorKartu) == 16:            
        if ' ' in nomorKartu or nomorKartu[i].isalpha() or '-' in nomorKartu or '44444' in nomorKartu:
            invalid.append(out[i])
        else: 
            valid.append(out[i])
    elif nomorKartu[0] == '5' and len(nomorKartu) == 16:
        if ' ' in nomorKartu or nomorKartu[i].isalpha() or '-' in nomorKartu or '9999' in nomorKartu:
            invalid.append(out[i])
        else:
            valid.append(out[i])
    elif nomorKartu[0] == '6' and len(nomorKartu) == 16:
        if ' ' in nomorKartu or nomorKartu[i].isalpha() or '-' in nomorKartu or '61234' in nomorKartu:
            invalid.append(out[i])
        else: 
            valid.append(out[i])
    else:
        invalid.append(out[i])


with open('ccInvalid.json','w') as inv:
    json.dump(invalid,inv)

with open('ccValid.json','w') as val:
    json.dump(valid,val)