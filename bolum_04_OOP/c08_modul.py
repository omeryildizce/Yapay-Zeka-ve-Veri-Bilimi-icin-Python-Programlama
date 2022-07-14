def hesapla_maas(maas ,zam_orani = 0):
    "maas -> sayısal deger olmalıdır. Zam oranı 0-100 arasında olmalıdır."
 
    try: 
        yeni_maas = maas + (maas * zam_orani / 100)
        print(yeni_maas) 
    except :
        print("Hatalı değer girdiniz. İşleminiz iptal edildi.")
        print("Girilen değerler: ")
        print(f"maas = str{maas}, zam_orani = str{zam_orani} ")
