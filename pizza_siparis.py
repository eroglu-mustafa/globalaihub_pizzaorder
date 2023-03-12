import csv
import datetime

class Pizza:
    
    def __init__(self, Type, component, cost):
        self.Type = Type
        self.component = component
        self.cost = cost


    def get_description(self):        
        return self.component
    
    
    def get_cost(self):
        return self.cost
    
    
    def __repr__(self):
        return self.Type 


class Sauice(Pizza):
    
    def __init__(self, Type, component, cost):
        super().__init__(Type, component, cost)
        self.component = component
        self.Type = Type


    def __repr__(self):
        return self.component


classic = Pizza("Klasik", "İnce Hamur, Pizza Sos, Mozarella Peyniri, Domates, Sucuk, Yeşil Biber", 75)
margherita = Pizza("Margherita", "İnce Hamur, Pizza Sos, Mozarella Peyniri, Dil Peyniri, Domates", 70)
turkpizza = Pizza("Türk", "İnce Hamur, Pizza Sos, Mozarella Peyniri, Sucuk, Pastırma, Köz Biber, Yöresel Baharatlar", 90)
plainpizza = Pizza("Sade", "İnce Hamur, Pizza Sos, Mozarella Peyniri, Domates, Yeşil Biber", 80)

olive = Sauice("Ek malzeme", "Zeytin", 5)
mushroom = Sauice("Ek malzeme", "Mantar", 5)
gcheese = Sauice("Ek malzeme", "Keçi Peyniri", 10)
beef = Sauice("Ek malzeme", "Et", 15)
onion = Sauice("Ek malzeme", "Soğan", 5)
corn = Sauice("Ek malzeme", "Mısır", 5)

total_order = 0
pizza_list = [classic, margherita, turkpizza, plainpizza]
sauice_list = [olive, mushroom, gcheese, beef, onion, corn]

s_list = []

def read_text():
    File = open("menu.txt", "r", encoding="utf-8")
    for line in File:
        print (line.strip())
        

def amount(piece, pizza, order):
    while True:
        name = input("\nLütfen İsim/Soyisim bilginizi giriniz: ")
        tckn = input("\nTCKN bilgisini giriniz: ")
        adress = input("\nAdres bilginizi ayrıntılı olarak giriniz: ")
        credit_no = input("\nÖdeme için geçerli bir kart numarası giriniz: ")
        password = input("Kart şifrenizi giriniz: ")
        if (name !="" and adress !="" and credit_no.isdigit()):
            break
        else:
            print("\nHatalı giriş yaptınız. İstenilen bilgileri lütfen tekrar giriniz: \n")
                
    confirm = input(f"\nSayın {name}, {order}.TL siparişiniz kredi kartınızdan tahsil edilecektir.\
 Onay için [E]vet ya da [H]ayır ")
    if confirm in ["E", "e"]:
        try:
            time = datetime.datetime.ctime(datetime.datetime.now())
                
            with open("Orders_Database.csv", "a+", newline = "", encoding="utf-8") as f:
                datafile = csv.writer(f)
                datafile.writerow([name,tckn, adress, credit_no, password, pizza, s_list, piece, order, time])
                
            print("\nSiparişiniz alınmıştır. Bizi tercih ettiğiniz için teşekkür ederiz. Afiyet olsun ! \n")
            input("\nDevam etmek için [Enter] ")
        except:
            input("\nKayıt işleminde hata oluştu. Dosyanın bir başka program tarafından kullanılmadığına emin olun.\
        Devam etmek için [Enter] ")
    else:
        input("\nSiparişiniz, isteğiniz üzerine iptal edilmiştir. Devam etmek için [Enter] ")
            

def read_csv():
    try:
        with open("Orders_Database.csv", "r", newline = "", encoding="utf-8") as f:
            datafile = csv.reader(f, delimiter=",")
            for line in datafile:
                print(", ".join(line))
    except:
        input("\nHata! Dosya konumunu ve bir başka program tarafından kullanılmadığını kontrol edin.")


def sauice_total(s_choice):
    s_choice = int(s_choice)
    return sauice_list[s_choice].get_cost()

def main():
    
    s_choice = 1
    print("\n"+"="*30+" AI PİZZA HUB "+ "="*30+"\n"+"-"*74)
    read_text()

    while True:
        print("\nHangi Pizzayı seçmek istiyorsunuz ?")
        p_choice = input("\nLütfen 1-4 arasından tercihinizi belirtin (Çıkış için Q/q) ")
        if (p_choice == "Q") or (p_choice == "q"):
            print("\nProgramdan çıkış yaptınız.\n")
            break
        elif p_choice in ["1", "2", "3", "4"]:
            p_choice = int(p_choice)-1
            
            print(f"\n{pizza_list[p_choice]} Pizza tercih ettiniz.")
            print(f"İçindekiler: {pizza_list[p_choice].get_description()}")
            piece = input("\nBir siparişte en fazla 3 adet pizza alabilirsiniz. Sipariş adediniz ? ")
            if piece in ["1", "2", "3"]:
                piece = int(piece)
                total_order = (pizza_list[p_choice].get_cost())*piece
                
                print("\nPizzanızı daha da lezzetlendirmek için ek malzemeler:\n")
                i = 0
                for i in range(1, (len(sauice_list)+1)):
                    print(i,f"{sauice_list[i-1]}",sauice_list[i-1].get_cost(),"TL","\t",end="")
                    i += 1
                    
                while (s_choice !="0"):
                    s_choice = input("\nPizzanıza ek malzeme için tercih yapınız. Siparişi tamamlamak için 0 tuşlayın : ")
                    if s_choice == "0":
                        break
                    elif s_choice in ["1", "2", "3", "4", "5", "6"]:
                        s_choice = int(s_choice)-1
                        if sauice_list[int(s_choice)] not in s_list:
                            print(f"\nEk malzeme olarak {sauice_list[s_choice]} seçtiniz.")
                            s_list.append(sauice_list[s_choice])
                            total_order += (sauice_total(s_choice)*piece)
                            
                        else:
                            print("\nBu ek malzemeyi seçmiştiniz.\n")
                    else:
                        print("\nSeçenekler arasından tercih yapmadınız.")
                        break
                
                print("\n"+"="*45+f"\nSipariş Özetiniz: {piece} adet {pizza_list[p_choice]} Pizza\n{pizza_list[p_choice].get_description()}")
                if len(s_list) != 0:
                    print("Pizzanıza ek malzemeler: ")
                    for i in s_list:
                        print(i," ",end="")
                print()
                print("-"*45+f"\nToplam tutar: {total_order}.TL")
                confirm = input("\nÖdeme yapmak ve siparişinizi tamamlamak istiyor musunuz ? E / H ")
                if confirm in ["E", "e"]:
                    amount(piece,pizza_list[p_choice], total_order)
                    
                    break
                else:
                    print("\nSipariş işlemi iptal edildi.\n")
                break
            
        else:
            print("\nGeçerli bir seçim yapmadınız.")

main()
