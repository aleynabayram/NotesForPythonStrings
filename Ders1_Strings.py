######### DERS1: STRING #########

print("Merhaba Dünya!") # Çift tırnak kullanılabilir
print('Merhaba Dünya!') #Tek tırnak kullanılabilir

# print('Ali's Home') Bu durumda sadece iki tek tırnak arası string olarak sayılacağı için hatalı bir kullanım olur
print('Ali\'s Home')  # \ kullandığımızda bu karakterden sonra gelen karakter özel karakter olamktan çıkar

print("""Merhaba
Dünya""")  # Alt alta yazılmasını sağlar 

print("""Merhaba

Dünya""")  # Arasında bir satır boşluk bırakır.Yani üç tırnak arasına ne yazılırsa çıktısı da birebir aynısı olur. 

print("Merhaba\nDünya") # \n bir alt satıra geçmesini sağlar

print("Merhaba\tDünya") # \t aralarında bir tab boşluk olmasını sağlar

mesaj = "Merhaba Dünya"
print(mesaj) # mesaj değişkenine atadığımız kelimeyi yazdırır. 

mesaj1 = "Merhaba"
mesaj2 = "Dünya"
print(mesaj1 + mesaj2) # iki değişkeni de ardarda aralarında herhangi bir boşluk olmadan yazdırır
print(mesaj1 + " "+ mesaj2) # manuel olarak araya iki tırnak arasına boşluk koyabiliriz

print(mesaj [0]) # Mesaj değişkeni içerisindeki sıfırıncı elemanı yazdırır yani M
print(mesaj [1]) # Mesaj değişkeni içerisindeki birinci elemanı yazdırır yani e
print(mesaj [-2]) # Sondan bir önceki harfi yazdırır yani y

print(mesaj [0:4] ) # 0. karakter ile 4. karakter arasını yazdırır. 0 dahil 4 dahil değil
print(mesaj [::2]) # 2 ve 2 nin katları olan harfleri yanyana yazdırır yani MraaDna
print(mesaj [::-1]) # Metini tersten yazdırır

print(mesaj.upper()) # Metinin bütün harflerini büyük harf şeklinde yazdırır

mesaj = mesaj.upper() # Mesaj değişkeninin bütün harflerini büyük yapar ve yeni hali bu olur
mesaj = mesaj.lower() # Mesaj değişkeninin bütün harflerini küçük yapar ve yeni hali bu olur
mesaj = mesaj.capitalize() # Sadece ilk kelimenin baş harfini büyütür

print(mesaj.startswith("me")) # Mesaj değişkeni me harfleriyle başlamıyorsa False çıktısını verir
print(mesaj.endswith("a")) # Mesaj değişkeni a harfiyle bitiyorsa true olaak döner
print(len(mesaj)) # Karakter uzunluğunu gösterir bu uzunluğa boşluk karakteri de dahildir
print(len(mesaj1 + mesaj2)) # İki değişkeni toplayarak aralarında boşluk olmadan karakter uzunluğunu gösterir

print("Merhaba"*10) # Yanyana 10 tane aralarında boşluk olmadan Merhaba yazar

isim = "Ali"
yaş = "20"
print("{} , {} yaşındadır".format(isim,yaş)) # Küme parantezi içerisine otomatik olarak değişkenleri yazdırmayı sağlar
print("{} {} dedi".format(isim,mesaj1)) # Ali Merhaba dedi şeklinde bir çıktı alınır
print(f"{isim} {mesaj1} dedi") # fstring yaparak bu şekilde bir kullanım sağlayabiliriz yine Ali Merhaba dedi çıktısı elde edilir

