# error -> hata
# error handling -> hata yonetimi

''' BU YONTEM PRATIK DEGIL
try:
 x=int(input('x: '))
 y=int(input('y: '))
 print(x/y)
except ZeroDivisionError: # hata oldugu zaman bize mesaj verir.
 print('y degeri sifir olamaz')
except ValueError:
 print('x ve y sayisal deger olmali')
'''

while True:
    try:
      x=int(input('x: '))
      y=int(input('y: '))
      print(x/y)
     ## asagidaki hatalar build-in hatalardir.python da gomulu hatalar yani. 
    except (ZeroDivisionError,ValueError) as error: # hatalar birlestirildi ve atama yapildi.
      print('hatali giris yapildi!')
      print(error)   
    finally:
       print('try except sonlandi!')
       



 








