__author__ = "isaerenc"

while True:
    istek = input("Çevresini Hesaplamak istediğiniz şekli seçiniz.:\n 1.Kare\n 2.Dikdörtgen\n 3.Üçgen\n 4.Daire\n 5.Paralel Kenar.:\n")
    if istek=="1":
        # Karenin Çevresini Hesaplama
        kkenar = float(input("Karenin bir kenarını giriniz:"))
        print("Karenin Çevresi....:", kkenar*4)
    elif istek=="2":
         # Dikdörtgen Çevresini Hesaplama
        dkisakenar = float(input("Dikdörtgenin kısa kenar uzunluğunu giriniz:"))
        duzunkenar = float(input("Dikdörtgenin uzun kenar uzunluğunu giriniz:"))
        print("Dikdörtgenin Çevresi....:", dkisakenar*2 + 2*duzunkenar)
    elif istek=="3":
        # Üçgenin Çevresini Hesaplama
        ukenar1 = float(input("Üçgenin birinci kenar uzunluğunu giriniz:"))
        ukenar2 = float(input("Üçgenin ikinci kenar uzunluğunu giriniz:"))
        ukenar3 = float(input("Üçgenin üçüncü kenar uzunluğunu giriniz:"))
        print("Üçgenin Çevresi....:", float(ukenar1 + ukenar2 + ukenar3))
    elif istek=="4":
        # Dairenin Çevresini Hesaplama
        dyaricap = float(input("Dairenin yarıçap uzunluğunu giriniz:"))
        pi = float(input("Belirtilen pi (π) sayısını giriniz:"))
        print("Dairenin Çevresi....:", (dyaricap * dyaricap) * pi)
    elif istek=="5":
        # Paralel kenarın Çevresini hesaplama
        pkisakenar = float(input("Paralel Kenarın kısa kenar uzunluğunu giriniz:"))
        puzunkenar = float(input("Paralel Kenarın uzun kenar uzunluğunu giriniz:"))
        print("Paralel Kenarın Çevresi....:", pkisakenar*2 + puzunkenar*2)
    else:
        print("Yanlış Giriş Yaptınız lütfen yukarıda verilen 1-2-3-4-5 sayılarından birini giriniz.")
