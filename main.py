""""
3 tane parametre alan bolunen_sayi_bulma isimli bir fonksiyon tanımlayınız.

Bu fonksiyon; min_sayi, max_sayi, bolen_sayi isimli parametreleri alsın.

Fonksiyon dışardan aldığı bu parametre değerlerini kullanarak, min_sayi ve max_sayi aralığındaki bolen_sayi değerine bölünen sayıları tam_bolunenler adlı bir diziye atayıp, listelesin.

tam_bolunenler dizisi ile min_sayi ve max_sayi arasındaki değerlerin sayısını return ile döndürsün.
"""

def bolunen_sayi_bulma(min_sayi, max_sayi, bolen_sayi):

    tam_bolunenler = []
    i = min_sayi
    while i <= max_sayi:
        if i % bolen_sayi == 0:
            tam_bolunenler.append(i)
        i += 1
    return len(tam_bolunenler)

Count = bolunen_sayi_bulma(10, 50, 7)
print(Count)


""""
sayi_atama ve sayi_okunusu isimli 2 tane fonksiyon tanımlayınız.

Bu fonksiyonlardan sayi_atama fonksiyonu 2 basamaklı bir sayıyı parametre olarak alsın ve fonksiyon içinde bu değer bir değişkene atansın.

Daha sonra sayi_atama fonksiyonu içinde sayi_okunusu isimli fonksiyon çağırılarak değişkene atanan sayının okunuşu string olarak verilsin.

sayi_atama fonksiyonu 2 basamaktan daha az yada daha fazla sayıyı kabul etmeyecektir.  """

def sayi_okunusu(sayi):
    onlar_basamagi = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
    birler_basamagi = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]

    return f"{onlar_basamagi[sayi//10]} {birler_basamagi[sayi%10]}"


def sayi_atama(iki_basamakli_sayi):
    if (iki_basamakli_sayi<100 and iki_basamakli_sayi>9) :
        x=iki_basamakli_sayi
        okunus=sayi_okunusu(x)
        print(okunus)
    else:
            print("Girdiğiniz sayı iki basamaklı bir sayı değil")

sayi_atama(101)


"""Kullanıcının girdiği vize1, vize2, final notlarına göre harf notunu hesaplayınız.

-vize1 toplam notun %30'una etki edecektir.

-vize2 toplam notun %30'una etki edecektir.

-final toplam notun %40'ına etki edecektir.

Bu değerler 0-100 arası kabul edilmelidir!

    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF """

def vize_notu_hesaplama(vize1, vize2, final):
    if 0 <= vize1 <= 100 and 0 <= vize2 <= 100 and 0 <= final <= 100:
        toplam_not = vize1*0.3 + vize2*0.3 + final*0.4
    else:
        return "Geçersiz not!"

    if toplam_not >= 90:
        harf = "AA"
    elif toplam_not >= 85:
        harf = "BA"
    elif toplam_not >= 80:
        harf = "BB"
    elif toplam_not >= 75:
        harf = "CB"
    elif toplam_not >= 70:
        harf = "CC"
    elif toplam_not >= 65:
        harf = "DC"
    elif toplam_not >= 60:
        harf = "DD"
    elif toplam_not >= 55:
        harf = "FD"
    else:
        harf = "FF"

    return f"Notunuz: {harf}"


print(vize_notu_hesaplama(100, 30, 80))

