#bölüm 1
#kullanıcıdan iki sayı alıyoruz
#ondalıklı sayı yazma ihitmaline karşı float kullandım
sayi1 = float(input("İlk sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))

print("Toplam",sayi1 + sayi2)
print("Çıkar",sayi1 - sayi2)
print("Çarp",sayi1 * sayi2)
print("böl",sayi1 / sayi2)
print("üs",sayi1 ** sayi2)
print("mod",sayi1 % sayi2)

#bölüm2
#kullanıcıdan bir sayı alıyoruz
sayi = int(input("Bir sayı girin: "))
toplam = 0

for i in range(1, sayi + 1):
    toplam += i

print(f"1'den {sayi}'a kadar olan sayıların toplamı: {toplam}")

#bölüm3
#1 ile 100 arasındaki çift sayıları ekrana yazdırma
for i in range(1,101): #1 den 100 e kadar satıları yazdırma
    if i % 2 == 0 : #2 ye bölümünden kalan 0 olması için
         print(i) 

#bölüm4
# Kullanıcıdan bir metin al
metin = input("Bir metin yazınız: ")

#metni ters çevir
ters_metin = ""
for harf in metin :
     ters_metin = harf + ters_metin #ters metnin nasıl olacağını tanımlıyoruz
     print("metnin tersi: ", ters_metin)




