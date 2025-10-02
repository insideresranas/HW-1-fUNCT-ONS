"""
50 soruluk, 4 yanlışın 1 doğruyu götürdüğü sınavda öğrencinin inputlarla girilen doğru yanlış sayısına göre aldığı puanı hesaplayan programı yazınız.

Ogrenci isimli bir sınıf tanımlayınız.

Bu sınıfın içinde ogrenci_adi, ogrenci_soyadi, ogrenci_sinif’ı değişkenleri bulunacaktır. Bu sınıftan nesne oluşturulurken bu bilgiler parametre olarak verilecektir.

Soru diye bir sınıfınız olacaktır. Bu sınıfın net_sayisi ve hesapla isimli iki fonksiyon olacaktır.

net_sayisi fonksiyonu doğru ve yanlış sayısını parametre olarak alıp öğrencinin kaç neti olduğunu bulacaktır.

hesapla fonksiyonu net sayısını parametre olarak alıp öğrencinin puanını hesaplayacaktır. Her net 2 puan olacak şekilde öğrenci bilgileri ve puanı console ekranında gösterilecektir. """

class Ogrenci:
    def __init__(self, adi, soyadi, sinif):
        self.ogrenci_adi = adi
        self.ogrenci_soyadi = soyadi
        self.ogrenci_sinif = sinif

class Soru:
    def net_sayisi(self, dogru, yanlis):

        net = dogru - (yanlis / 4)
        return max(0, net)

    def hesapla(self, net):

        puan = net * 2
        return puan


adi = input("Öğrencinin adı: ")
soyadi = input("Öğrencinin soyadı: ")
sinif = input("Öğrencinin sınıfı: ")

dogru = int(input("Doğru sayısı: "))
yanlis = int(input("Yanlış sayısı: "))


ogrenci = Ogrenci(adi, soyadi, sinif)
sinav = Soru()

net = sinav.net_sayisi(dogru, yanlis)
puan = sinav.hesapla(net)


print("\n--- Sınav Sonucu ---")
print(f"Adı: {ogrenci.ogrenci_adi}")
print(f"Soyadı: {ogrenci.ogrenci_soyadi}")
print(f"Sınıfı: {ogrenci.ogrenci_sinif}")
print(f"Net Sayısı: {net}")
print(f"Puan: {puan}")

""""
Insan isimli bir sınıf tanımlayınız.

Bütün constructor parametreleri default değerlere sahip olacak, default contructor (__init__) içinde belirlenecektir. 

Bu değerler; ad, soyad, yas, ulke, sehir olacaktır.Ek olarak yetenekler isimli bir boş dizi init fonksiyonu içinde tanımlanacaktır.

kisi_bilgileri isimli fonksiyon ile init fonksiyonu içinde belirlenen kisi bilgileri return’le döndürülecektir.

yetenek_ekle isimli fonksiyon ile init fonksiyonu içinde belirlenen yetenekler dizisine yetenekler eklenecektir.

Bu classtan belirtilen bilgileri içeren bir nesne tanımlayınız.

Tanımlanan nesneye yetenek ekleyiniz. (Bisiklete binmek, Python vs.)

kisi_bilgileri fonksiyonu ile bu bilgileri console ekranında gösteriniz."""

class Insan:
    def __init__(self, ad="Ayse", soyad="Yılmaz", yas=35, ulke="Turkiye", sehir="Ankara"):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        return {
            "Ad": self.ad,
            "Soyad": self.soyad,
            "Yaş": self.yas,
            "Ülke": self.ulke,
            "Şehir": self.sehir,
            "Yetenekler": self.yetenekler
        }

    def yetenek_ekle(self, yetenek):
        self.yetenekler.append(yetenek)



ad = input("Adınız: ")
soyad = input("Soyadınız: ")
yas = int(input("Yaşınız: "))
ulke = input("Ülkeniz: ")
sehir = input("Şehir: ")


kisi = Insan(ad, soyad, yas, ulke, sehir)


yetenekler = input("Yetenekleriniz (Virgül ile ayırınız): ")
yetenek_listesi = [y.strip() for y in yetenekler.split(",")]

for y in yetenek_listesi:
    kisi.yetenek_ekle(y)

bilgiler = kisi.kisi_bilgileri()
print("\n--- Kişi Bilgileri ---")
for anahtar, deger in bilgiler.items():
    print(f"{anahtar}: {deger}")
