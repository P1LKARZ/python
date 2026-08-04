import json


# --- OPERACJE NA PLIKACH JSON ---

def WriteJson(produkty):
    with open("produkty.json", "w", encoding="utf-8") as plik:
        json.dump(produkty, plik, indent=4, ensure_ascii=False)


def ReadJsonProducts():
    try:
        with open("produkty.json", "r", encoding="utf-8") as plik:  
            return json.load(plik)
    except FileNotFoundError:
        return {}  


def ReadJsonUser():
    try:
        with open("pracownicy.json", "r", encoding="utf-8") as plik:
            return json.load(plik)
    except FileNotFoundError:
        return {}


# --- LOGIKA KONT I LOGOWANIA ---

def Login(worker):
    name = input("Podaj swoje imię: ")
    zalogowany = False
    zalogowany_user = None

    for p in worker:
        if p["imie"] == name:
            zalogowany_user = p
            while True:   
                password = input("Podaj hasło: ")
                if p["haslo"] == password:
                    zalogowany = True
                    break
                else:
                    print("Podaj prawidłowe hasło!")
            break

    return zalogowany, zalogowany_user


# --- SYSTEM UPRAWNIEŃ I MENU ---

def ShowMenu():
    print("\n--- MENU ---")
    print("1. Dodaj produkt")
    print("2. Wyświetl produkty")
    print("3. Usuń produkt")
    print("4. Zmień cenę")
    print("5. Podlicz wartość magazynu")
    print("6. Wyszukaj produkt")
    print("7. Wyjdź")


def MaDostep(rola, choice):
    """Sprawdza, czy dana rola ma dostęp do wybranej opcji w menu."""
    uprawnienia = {
        "Administrator": [1, 2, 3, 4, 5, 6, 7],
        "Manager": [2, 5, 6, 7],
        "Pracownik": [1, 3, 4, 6, 7],
        "Magazynier": [1, 3, 4, 6, 7]
    }
    dozwolone_opcje = uprawnienia.get(rola, [])
    return choice in dozwolone_opcje


def WykonajAkcje(choice, produkty):
    """Wywołuje odpowiednią funkcję na podstawie wyboru użytkownika."""
    if choice == 1:
        AddItem(produkty)
    elif choice == 2:
        ShowItem(produkty)
    elif choice == 3:
        DeleteItem(produkty)
    elif choice == 4:
        ChangePrice(produkty)
    elif choice == 5:
        OverrallPrice(produkty)
    elif choice == 6:
        SearchItem(produkty)


# --- OPERACJE NA PRODUKTACH ---

def AddItem(produkty):
    nazwaProduktu = input("Podaj nazwę produktu: ")
    iloscProduktu = int(input("Podaj ilość produktu: "))
    cenaProduktu = float(input("Podaj cenę produktu: "))  
    
    produkty[nazwaProduktu] = {
        "ilosc": iloscProduktu,
        "cena": cenaProduktu
    }    
    WriteJson(produkty)  
    print("Produkt został pomyślnie dodany.")


def ShowItem(produkty):
    if not produkty:
        print("Magazyn jest pusty!")
        return
        
    for nazwa, dane in produkty.items():
        print("--------------------")
        print("Produkt: " + nazwa)
        print("Ilość produktu: ", dane['ilosc'])
        print("Cena produktu: ", dane['cena'])


def DeleteItem(produkty):
    ItemToDelete = input("Który przedmiot chcesz usunąć? ")
    
    if ItemToDelete in produkty:
        del produkty[ItemToDelete]
        WriteJson(produkty) 
        print("Produkt usunięty.")
    else:
        print("Nie ma produktu w bazie.")      


def ChangePrice(produkty):
    ItemToChange = input("Którego produktu chcesz zmienić cenę? ")
    if ItemToChange in produkty:
        price = float(input("Podaj nową cenę: "))
        produkty[ItemToChange]["cena"] = price
        WriteJson(produkty)  
        print("Cena zaktualizowana.")
    else:
        print("Nie ma produktu w bazie.")  


def OverrallPrice(produkty):
    suma = 0
    for nazwa, dane in produkty.items():
        suma += dane["ilosc"] * dane["cena"]
    print(f"Magazyn jest warty {suma:.2f} PLN")


def SearchItem(produkty):
    item = input("Podaj produkt: ")
    if item in produkty:
        print(f"Produkt: {item}")
        print(f"Cena: {produkty[item]['cena']}")   
        print(f"Ilość: {produkty[item]['ilosc']}")  
    else:
        print("Nie ma produktu w bazie.")


# --- OBSŁUGA PĘTLI DLA ZALOGOWANEGO UŻYTKOWNIKA ---

def ObslugaMagazynu(zalogowany_user, produkty):
    rola = zalogowany_user.get("rola", "Pracownik")
    print(f"\nZalogowano jako {zalogowany_user['imie']} ({rola})")

    choice = 0
    while choice != 7:
        ShowMenu()
        choice = int(input("Co robimy? "))

        if choice == 7:
            break

        if MaDostep(rola, choice):
            WykonajAkcje(choice, produkty)
        else:
            print(f"\n[BŁĄD] Rola '{rola}' nie ma uprawnień do opcji numer {choice}!")


# --- GŁÓWNA FUNKCJA PROGRAMU ---

def Magazyn():
    produkty = ReadJsonProducts()
    users = ReadJsonUser()
    worker = users.get("pracownicy", [])

    zalogowany, zalogowany_user = Login(worker)

    if zalogowany:
        ObslugaMagazynu(zalogowany_user, produkty)
    else:
        print("Nie znaleziono takiego użytkownika lub wprowadzono błędne hasło.")

    print("\nDzięki za wizytę w magazynie!")


# Uruchomienie aplikacji
Magazyn()