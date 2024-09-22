
def checkPassword(pw):
    import re
    if len(pw)<8:
     raise Exception('parola 8 karakterden az olamaz')
    elif  re.search("[a-z]",pw):
     raise Exception("parola kucuk harf icermeli")
    elif  re.search("[0-9]",pw):
     raise Exception("parola harf icermeli")
    else:
      print("gecerli parola") #parola gecerli olunca calisir.


password="12345689" #parola gecerli 

try:
  checkPassword(password)
except Exception as ex:
  print(ex)


class Person:
  def __init__(self,name,year):
    
    self.year=year
    if len(name)>10: 
      raise Exception("isim alani fazla karakter iceriyor")
    else:
      self.name=name
    

p1=Person("ahmetuop1",1990)       