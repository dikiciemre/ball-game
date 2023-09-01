
import random

ilk34sayi = range(1,35) #ilk 34 sayının listesini oluşturduk
sonBirsayi = range(1,15) #aşağıdaki 14 sayının listesini oluşturduk
print("ŞANS TOPU OYUNUNA HOŞ GELDİNİZ !!!!")


#Kazanan Sayılar
#ilkBesKazananSayi = [1,2,3,4,5]
ilkBesKazananSayi = random.sample(ilk34sayi,5) #Kazanan ilk beş sayıyı belirledik
#sonBirKazananSayi = [6]
sonBirKazananSayi = random.sample(sonBirsayi, 1)  #Kazanan son sayıyı belirledik

#Kullanıcının girdiği sayılar
kumarParasi = 500
print(kumarParasi)
while True:
    print("Hesaptaki paran",kumarParasi)
    secim = int(input("""
    1- Oyna
    2- Sonuç Getir
    3- Kazancımı ver ve kaç lira kazandığımı göster
    4- Oyundan Çık
    """))
    if secim == 1:
        kacLira = int(input("Kaç lira oynayacağını gir: "))
        sayi1 = int(input("1. sayıyı gir:(1-34) "))
        sayi2 = int(input("2. sayıyı gir:(1-34) "))
        sayi3 = int(input("3. sayıyı gir:(1-34) "))
        sayi4 = int(input("4. sayıyı gir:(1-34) "))
        sayi5 = int(input("5. sayıyı gir:(1-34) "))

        sayi6 = int(input("6. sayıyı gir:(1-14) "))

        kSayi1 = [sayi1, sayi2, sayi3, sayi4, sayi5] #kullanıcının oynadığı sayıları listeye çevirdik
        kSayi2 = [sayi6]

        kSayiKume1 = set(kSayi1) #kullanıcının oynadığı sayıları kümeye çevirdik, kesişim bulmak için
        kSayiKume2 = set(kSayi2)

        besKume = set(ilkBesKazananSayi) #kazanan sayıları kümeye çevirdik, kesişim bulmak için
        sonKume = set(sonBirKazananSayi)

        bilinenSayi5 = kSayiKume1.intersection(besKume) #kesişimi bulduk
        bilinenSayiSon = kSayiKume2.intersection(sonKume)

        #Kaç tane bildiğini belirledik
        kactaneBes = len(bilinenSayi5) #ilk beş sayı
        kactaneSon = len(bilinenSayiSon) #son bir sayı
        kumarParasi = kumarParasi - kacLira

    elif secim == 2:
        print("Bu oyun için",kacLira, "kadar harcadınız")
        if bilinenSayi5 == set():
            print("İlk beş sayıyı bilemediniz")
        else:
            print("Bilinen Sayılar",bilinenSayi5)


        if bilinenSayiSon == set():
            print("Son sayıyı bilemediniz")
        else:
            print("Bilinen Son Sayı", bilinenSayiSon)


        #konsola yazdırdık
        print(f"""
        Kazanan Beş sayı: {ilkBesKazananSayi}
        Kazanan Son sayı: {sonBirKazananSayi}
        """)
        print("Kazanan Sayılar: ",ilkBesKazananSayi, "+", sonBirKazananSayi)

        print("Sizin Sayılarınız", kSayi1, "+", kSayi2)

        #Kaç tane bildiğini konsola yazdırdık


        print(f"""
        {kactaneBes} + {kactaneSon} sayı bildiniz
        """)
    elif secim == 3:

        # Ne kadar kazandım, kaç lira kazandığı yazacak
        if kactaneBes == 0 and kactaneSon == 0:
            kumarParasi = kumarParasi - (kacLira * 3)
            print("Hiç para kazanamadın. Bugün şanssız günündesin :(")
            print(kumarParasi)
        elif kactaneBes == (1,6) or kactaneSon == 0:
            print("Paranız", kumarParasi)
            print(kactaneBes, "+", kactaneSon, "bildiniz")
            kumarParasi = kumarParasi + (kacLira * len(bilinenSayi5))
            print("Toplam paran", kumarParasi)
        elif kactaneBes == (1,6) or kactaneSon == 1:
            print("Paranız:",kumarParasi)
            print(kactaneBes, "+", kactaneSon, "bildiniz")
            kumarParasi = kumarParasi + (kacLira * len(bilinenSayi5)+100)
            print("Toplam paran", kumarParasi)



        """
        elif kactaneBes == 2:
            kumarParasi = kumarParasi + (kacLira * 2)
            print("Toplam paran", kumarParasi)
        elif kactaneBes == 3:
            kumarParasi = kumarParasi + (kacLira * 3)
            print("Toplam paran", kumarParasi)
        elif kactaneBes == 4:
            kumarParasi = kumarParasi + (kacLira * 4)
            print("Toplam paran", kumarParasi)
        elif kactaneBes == 5:
            kumarParasi = kumarParasi + (kacLira * 5)
            print("Toplam paran", kumarParasi)
        elif kactaneSon == 1:
            kumarParasi = kumarParasi + 500
        else:
            print("Neye bastın da buraya geldik")
         """



    elif secim == 4:
        print("Oyundan çıkıyorsunuz")
        break