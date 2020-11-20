satuan = ['', 'satu', 'dua', 'tiga', 'empat','lima', 'enam', 'tujuh', 'delapan', 'sembilan']


def terbilang(n):
    if n % 1 > 0:
        cari_koma = str(n).find('.')
        angka_belakang_koma = str(n)[cari_koma+1:]
        angka_depan_koma = str(n)[0:cari_koma]
        int_angka_belakang_koma = int(angka_belakang_koma)
        int_angka_depan_koma = int(angka_depan_koma)

        return terbilang(int_angka_depan_koma)+" koma "+terbilang(int_angka_belakang_koma)
    elif n < 10:
        # satuan
        return satuan[int(n)]
    elif n >= 1_000_000_000:
        # milyar
        if n == 1_000_000_000:
            return ' satu milyar '
        elif n // 1_000_000 == 1:
            return ' satu milyar ' + terbilang(n % 1_000_000_000)
        else:
            return terbilang(n // 1_000_000_000) + ' milyar ' + terbilang(n % 1_000_000_000) 
    elif n >= 1_000_000:
        # juta
        if n == 1_000_000:
            return ' satu juta '
        elif n // 1_000_000 == 1:
            return ' satu juta' + terbilang(n % 1_000_000) 
        else:
            return terbilang(n // 1_000_000) + ' juta ' + terbilang(n % 1_000_000) 
    elif n >= 1000:
        #ribuan
        if n == 1000:
            return " seribu " 
        elif n // 1000 == 1:
            return " seribu " + terbilang(n % 1000) 
        else:
            return terbilang(n // 1000) + ' ribu ' + terbilang(n % 1000)       
    elif n >= 100:
        # ratusan
        if n == 100:
            return " seratus "
        elif n // 100 == 1:
            return " seratus " + terbilang(n % 100) 
        else:
            return terbilang(n // 100) + ' ratus ' + terbilang(n % 100) 
    elif n >= 20:
        # puluhan
        return terbilang(n // 10) + ' puluh ' + terbilang(n % 10) 
    else:
        # belasan
        if n == 10:
            return ' sepuluh'
        elif n == 11:
            return ' sebelas'
        else:
            return terbilang(n // 10) + ' belas'
    
    

n = float(input("Masukkan bilangan "))
print(f"{n if n%1>0 else int(n)} -> {terbilang(n)}")