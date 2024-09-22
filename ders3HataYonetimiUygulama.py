'''
liste=["1","2","5a","10b","abc","10","50"]

#1 liste elemanlari icindeki sayisal degerleri bulunuz.
for x in liste:
    try:
     result=int(x)
     print(result)
    except ValueError:
       print("deger sayi degil")
       continue #hatali indexi atlar ve devam eder.

#2 kullanici q degerini girmedikce alinan her inputun sayi olup
#olmadigindan emin olunuz.

while True:
   sayi=input('sayi: ')
   if (sayi=='q'):
      break
   
   try:
      result2=float(sayi)
      print('giris basarili')
   except ValueError:
      print('gecersiz giris hatasi')
      continue
   

#3 girilen parola icinde turkce karakter hatasi veriniz.
def passwordCheck(password):
 
 turkceKarakter=['ğ','ş','ı','Ğ','İ','ş']
 for i in password:
    if (i in turkceKarakter):
     raise TypeError('turkce karakter kullanmayiniz.')
    else:
       pass

password=input('parolayi giriniz: ')
 
try:
  passwordCheck(password)
except TypeError as error:
  print(error)
     
 
'''
#4 faktoriyel fonksiyonu olusturun.
# gelen degerlere gore hata mesajları olusturun.

def faktoriyel (sayi):
    if sayi==0:
        return 1
    elif sayi<0:
        raise Exception('sayi negatif olmaz')
    elif type(sayi)==float:
        raise Exception('sayi ondalikli olamaz')
    elif type(sayi)==str:
        raise Exception('sayi karakter olamaz')
    else:
        return sayi*(faktoriyel(sayi-1))

while True:
   try:
       sayi=int(input('faktoriyeli alinacak sayiyi giriniz: '))
   except Exception as error:
       print(error) 
       continue
   else:
       sonuc=faktoriyel(sayi)
       print(f'sonuc: {sonuc}')
       break
   finally:
      print('faktoriyel fonksiyonu calisti.')
