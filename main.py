import json

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
    WriteJson()  
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
    else:
            print("Nie ma produktu w bazie")         
    WriteJson()  
def ChangePrice(produkty):
    ItemToChange=input("Którego produktu chcesz zmienić cenę? ")
    if ItemToChange in produkty
        price=int(input("Podaj nową cenę"))
        produkty[ItemToChange]["cena"]=price
    else:
            print("Nie ma produktu w bazie")  
    WriteJson()  
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
    else:
        print("Nie ma produktu w bazie")
def WriteJson(produkty):
    with open("dane.json","w") as plik:
        json.dump(produkty,plik,indent=4)
def ReadJson():
    try:
        with open("dane.json","r",encoding="utf-8") as plik:  
            return json.load(plik)
    except FileNotFoundError:
        return "Nie znaleziono pliku"
    
def Magazyn():
    produkty=ReadJson()
   
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
            
    WriteJson(produkty)
    print("Dzięki za wizytę w magazynie")
Magazyn()