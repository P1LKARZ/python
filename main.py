def ShowMenu():
    print("1. Dodaj produkt")
    print("2. Wyświetl produkty")
    print("3. Usuń produkt")
    print("4. Zmień cenę")
    print("5. Podlicz wartość magazynu")
    print("6. Wyszukaj produkt")
    print("7. Wyjdź")
def AddItem(produkty):
    nazwaProduktu=input("podaj nazwe produktu")
    iloscProduktu=int(input("podaj ilosc produktu"))
    cenaProduktu=int(input("podaj cene produktu"))
    produkty[nazwaProduktu]={
        "ilosc":iloscProduktu,
        "cena":cenaProduktu
        }      
def ShowItem(produkty):
    for nazwa,dane in produkty.items():
        print("--------------------")
        print("Produkt: " + nazwa)
        print("Ilość produktu: " , dane['ilosc'] )
        print("Cena produktu: " , dane['cena'])
def DeleteItem(produkty):
    ItemToDelete=input("Który przedmiot chcesz usunąć?")
    
    if ItemToDelete in produkty:
        del produkty[ItemToDelete]
def ChangePrice(produkty):
    ItemToChange=input("Którego produktu chcesz zmienić cenę? ")
    price=int(input("Podaj nową cenę"))
    produkty[ItemToChange]["cena"]=price
def OverrallPrice(produkty):
    suma = 0
    for nazwa, dane in produkty.items():
        suma += dane["ilosc"] * dane["cena"]
    print(f"Magazyn jest warty {suma} pln")
def SearchItem(produkty):
    item=input("Podaj produkt: ")
    if item in produkty:
        print(f"Produkt: {item} ")
        print(f"Cena: {produkty[item]["cena"]} ")
        print(f"Ilość: {produkty[item]["ilosc"]} ")  
    
    
    
def Magazyn():
    produkty={
        "mleko":{
            "ilosc":15,
            "cena":10,
        },
        "chleb":{
            "ilosc":2,
            "cena":7,
        }
    }
    choice=0

    while choice!=7:
        ShowMenu()
        choice=int(input("Co robimy "))
        
        if choice==1:
            AddItem(produkty)
        elif choice==2:
            ShowItem(produkty)
        elif choice==3:
            DeleteItem(produkty)
        elif choice==4:
            ChangePrice(produkty)
        elif choice==5:
            OverrallPrice(produkty)
        elif choice==6:
            SearchItem(produkty)

    print("Dzięki za wizytę w magazynie")
Magazyn()