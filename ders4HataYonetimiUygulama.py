
import re #regular expression kutuphanesi import edilerek kontrol metodlari eklenir.

class PasswordCheck:
    def __init__(self,password):
        if(len(password)<7):
            raise Exception('parola 7 harften kucuk')
        elif re.findall("ş",password):
            raise Exception('turkce karakter iceremez')
        elif  re.search("[0-9]",password):
             raise Exception("parola harf icermeli")
        else:
           self.password=password
        

while True:
    try:  
     pw=input('parolayi gir: ')
     PasswordCheck(pw)
    except Exception as error:
        print(error)
    else:
        print('parola uygun')
        break       
    finally:
      print('blok calisti')


