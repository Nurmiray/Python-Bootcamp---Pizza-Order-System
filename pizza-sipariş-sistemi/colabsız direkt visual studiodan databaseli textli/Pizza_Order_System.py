#kütüphaneler
import csv
from datetime import datetime 


#Menu.txt dosyasnı değişken adı menupizza olarak açılır 
def menugösterimi():
    with open("Menu.txt", "w") as menupizza: 
        # w parametresi ile o dosya yoksa oluştutur ve yazmaya işlemi gerçekleşir. Varsa üzerine yazar.        
        menuicerik = """*Lütfen Bir Pizza Tabanı Seçiniz:
1: Klasik
2: Margarita
3: TürkPizza
4: Sade Pizza
* ve seçeceğiniz sos:
11: Zeytin
12: Mantarlar
13: Keçi Peyniri
14: Et
15: Soğan
16: Mısır
*Teşekkür ederiz!"""
        
        menupizza.write(menuicerik) 
        menupizza.close() 


#Menu.txt için fonksiyon çağırma
menugösterimi() 


#Pizza sınıfı tanımlanır 
class Pizza:
    def __init__(self, description, cost): 
        self.description = description 
        self.cost = cost 

    def get_description(self):
        return self.description 

    def get_cost(self):
        return self.cost 


#Pizza sınıfından miras alan alt sınıflar tanımlanır
class klasikPizza(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza", 90.00)

class margaritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza", 95.00)

class turkPizza(Pizza):
    def __init__(self):
        super().__init__("Türk Pizza", 100.00)

class sadePizza(Pizza): 
    def __init__(self):
        super().__init__("Sade Pizza", 80.00)


#decorator sınıfı tanımlanır
class Decorator(Pizza):
    def __init__(self, component, description, cost):
        self.component = component
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.component.get_description() + " --- Ekstra: " + Pizza.get_description(self)

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_saucecost(self):
        return self.cost
    
    def get_saucedescription(self):
        return self.description


#decorator (miras alma/inheritance) kalıtılan soslar
class zeytin(Decorator):
    def __init__(self, component):
        super().__init__(component, "Zeytin", 5.00)

class mantar(Decorator):
    def __init__(self, component):
        super().__init__(component, "Mantar", 8.00)

class kecipeyniri(Decorator):    
    def __init__(self, component):
        super().__init__(component, "Keçi Peyniri", 10.00)

class et(Decorator):
    def __init__(self, component):
        super().__init__(component, "Et", 12.00)

class sogan(Decorator):       
    def __init__(self, component):
        super().__init__(component, "Soğan", 8.00)    

class misir(Decorator):
    def __init__(self, component):
        super().__init__(component, "Mısır", 9.00)
        
class ekstrasiz(Decorator):   
    def __init__(self, component):
        super().__init__(component, "Extrasız", 0.00)


#ID number için
def IDvalid(id_number):
    id_number = str(id_number) 
    if not len(id_number) == 11: #11 karakter olup olmadığı kontrol eder
        return False
    
    if not id_number.isdigit(): #sadece rakam olup olmadığına bakar
        return False

    if int(id_number[0]) == 0: #ID number 0 ile başlayamaz
        return False

    return True


#kredi kartı için
def kredikart(debitNo): 
    if not debitNo.isdigit(): #sadece rakam olup olmadığına bakılır
        return False
    
    if len(debitNo) == 16: # kredi kartı 16 Hanelidir 
        return True   
    

#Menu.txt göster
def show_menu(): 
    with open('Menu.txt', 'r') as file:
        #Bir dosyayı okuma kipinde açmak için ise “r” harfini kullanırız.
        pMenu = file.read()
        print(pMenu)


#Main fonksiyon tanımla
def main():
    show_menu()
    
    while(True):
        pizzaseçimi = int(input("\nPizzanızı seçiniz [1-4]: ")) #Pizza Tabanı Seçtirilir
        if pizzaseçimi == 1:
            pizza = klasikPizza()
            break
        elif pizzaseçimi == 2:
            pizza = margaritaPizza()
            break
        elif pizzaseçimi == 3:
            pizza = turkPizza()
            break
        elif pizzaseçimi == 4:
            pizza = sadePizza()
            break
        else:
            print("Yanlış seçim aralığı yaptınız! Lütfen (1-4) arası tekrar seçim yapınız.")
            
    orderBase = pizza #Pizza orderBase degiskenine kaydedilir.
    
    while(True):
        pizzasosu = int(input("Eklenecek ekstra malzemeyi seçiniz [11-16] (ekstra istemiyorsanız 00 tuşlayın): ")) 
        if pizzasosu == 11:
            pizza = zeytin(pizza) 
            break
        elif pizzasosu == 12:
            pizza = mantar(pizza)
            break
        elif pizzasosu == 13:
            pizza = kecipeyniri(pizza)
            break
        elif pizzasosu == 14:
            pizza = et(pizza)
            break
        elif pizzasosu == 15:
            pizza = sogan(pizza)
            break
        elif pizzasosu == 16:
            pizza = misir(pizza)
            break
        elif pizzasosu == 00:
            pizza = ekstrasiz(pizza)
            break
        else:
            print("Yanlış seçim aralığı yaptınız! Lütfen (11-16) arası tekrar seçim yapınız.")

          
    ad = input("Adınız: ")
    id_number = input("Kimlik No: ")
    
    while(True):
        if IDvalid(id_number): 
            break
        else:
            print("Burada bir hata var. ID No, 11 haneli rakamlardan oluşmalıdır ve '0' ile başlayamaz. Tekrar Dene.")
            id_number = input("Kimlik No: ")
    
    print("\nSiparişiniz: ")
    print("Pizza: " + orderBase.get_description() + ' --- ' + 'Ekstra: ' + pizza.get_saucedescription()) 
    totalCost = orderBase.get_cost() + pizza.get_saucecost()
    print("Toplam Tutar: " + f"{totalCost} ₺" )
    
    kredikartino = input("Ödeme için Kredi Kart No Giriniz: ")
    
    while(True):
        if kredikart(kredikartino):
            break
        else:
            print("Burada bir hata var. Kredi Kartı No, 16 haneli rakamlardan oluşmalıdır. Tekrar Dene.")
            kredikartino = input("Ödeme için Kredi Kart No Giriniz: ")
            
    geçerlikredikarti = input("Şifrenizi Giriniz: ")
    
    description = pizza.get_description()
    cost = pizza.get_cost()
    now = datetime.now()
    dateTime = now.strftime("%d/%m/%Y, %H:%M:%S")
    
    print("\nTeşekkürler")
    print("\nSipariş detayları:")
    print("AD: " + ad)
    print("ID No: " + id_number)
    print("Sipariş: " + description)
    print("Cost:" + f"{cost} ₺")
    print("Sipariş Zamanı: " + dateTime)
 
    with open("Orders_Database.csv", "a") as siparisbilgisi: #CSV Database oluşturma
        # Dosyayı açarken "a" modu ile açarsam. Dosyama ekleme işlemi ( append ) yapabilirim.
        database = csv.writer(siparisbilgisi) 
        database.writerow([ad, id_number, kredikartino, description, cost, dateTime, geçerlikredikarti])
                

main() #main fonksiyon çağırma
