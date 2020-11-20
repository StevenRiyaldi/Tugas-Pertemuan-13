satuan = ['', 'one', 'two', 'three', 'four','five', 'six', 'seven', 'eight', 'nine']


def terbilang(n):
    if n % 1 > 0:
        cari_koma = str(n).find('.')
        angka_belakang_koma = str(n)[cari_koma+1:]
        angka_depan_koma = str(n)[0:cari_koma]
        int_angka_belakang_koma = int(angka_belakang_koma)
        int_angka_depan_koma = int(angka_depan_koma)

        return terbilang(int_angka_depan_koma)+' point '+terbilang(int_angka_belakang_koma)
    elif n < 10:
        # satuan
        return satuan[int(n)]
    elif n >= 1_000_000_000:
        # milyar
        if n == 1_000_000_000:
            return ' one billion '
        elif n // 1_000_000_000 == 1:
            return ' one billion ' + terbilang(n % 1_000_000_000) 
        else:
            return terbilang(n // 1_000_000_000) + ' billion ' + terbilang(n % 1_000_000_000) 
    elif n >= 1_000_000:
        # juta
        if n == 1_000_000:
            return ' one million '
        elif n // 1_000_000 == 1:
            return ' one million ' + terbilang(n % 1_000_000) 
        else:
            return terbilang(n // 1_000_000) + ' million ' + terbilang(n % 1_000_000) 
    elif n >= 1000:
        #ribuan
        if n == 1000:
            return " a thousand "
        elif n // 1000 == 1:
            return " a thousand " + terbilang(n % 1000) 
        else:
            return terbilang(n // 1000) + " thousand " + terbilang(n % 1000)       
    elif n >= 100:
        # ratusan
        if n == 100:
            return ' a hundred '
        elif n // 100 == 1:
            return " a hundred " + terbilang(n % 100)
        else:
            return terbilang(n // 100) + " hundred " + terbilang(n % 100) 
    elif n >= 20:
        # puluhan
        if n // 10 == 2:
            return ' twenty '+ terbilang(n%10)
        elif n // 10 == 3:
            return ' thirty '+ terbilang(n%10)
        elif n // 10 == 4:
            return ' forty '+ terbilang(n%10)
        elif n // 10 == 5:
            return ' fifty '+ terbilang(n%10)
        elif n // 10 == 8:
            return ' eighty '+ terbilang(n%10)
        else:
            return terbilang(n//10)+ 'ty'
        
    else:
        # belasan
        if n == 10:
            return ' ten '
        elif n == 11:
            return ' eleven '
        elif n == 12:
            return ' twelve '
        elif n == 13:
            return ' thirteen '
        elif n == 15:
            return ' fifteen '
        elif n == 18:
            return ' eighteen '
        else:
            return terbilang(n % 10) + 'teen'
    
    

n = float(input("Masukkan bilangan "))
print(f"{n if n%1>0 else int(n)} -> {terbilang(n)}")