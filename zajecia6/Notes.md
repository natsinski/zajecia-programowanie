# Public i Private

## Public fields

Pole publiczne to takie pole, które go wartość można zmienić z dowolnego miejsca w programie.

```python 

class Car:
    colour = "red"  # To jest publiczne pole

my_car = Car()
print(my_car.colour) # Wyprintuje 'red'

my_car.color = "blue"
print(my_car.colour) # Wyprintuje 'blue' bo zmieniliśmy wartość fielda colour
```

## Private fields

Pola prywatne to pola, których można używać tylko wewnątrz klasy lub obiektu. W pythonie oznaczamu je przez dodanie `__` przed nazwaą pola.
Żeby dostać się do tych pól nalezy przygotować specjalne metody, które nazywamy getter i setter.

```python 

class Car:
    __engine = "V8"  # To jest prywatne pole

    def get_engine(self):
        return self.__engine

    def set_engine(self, new_engine):
        self.__engine = new_engine

my_car = Car()

print(my_car.__engine) # Wywali błąd

my_car.__engine = "vtec" # Wywali błąd

print(my_car.get_engine()) # Printuje "V8"

my_car.set_engine('vtec')
print(my_car.get_engine()) # Printuje 'vtec', bo zmieniliśmy go linikę wyżej
```

# PD
Zastanów się nad poniższym zadaniem. Przeanalizuj jakie wymagania są podane poniżej. Spróbuj rozbić podane wymagania na mniejsze problemy/zadania.
Postaraj się zrobić listę mniejszyczh zadań, po wykonaniu których poniższy program zadziala. Możesz też zacząć sam implementować poniższy program.

Do zrozumienia części o produktach przyda się znajomość dictionaries, o których przeczytasz tutaj: https://www.w3schools.com/python/python_dictionaries.asp

BTW zadanie jest trudne i bedziemy też razem nad nim pracować na zajęciach, więc jeśli coś nie jest jasne to też nie szkodzi.

## Zadanie 
Napisz program obsługujący prostą kasę fiskalną w terminalu.

1. Program obsługuje tylko konktetną listę produktów podaną poniżej
2. Po odpaleniu programu w terminalu ukazuje się poniższe menu główne:
    - User wybiera opcję 1 lub 2 poprzez wpisanie w terminal cyfry 1 lub 2. 
3. Funkcjonalność 1 podaje ilość pieniędzy w kasie w danym momencie. 
4. Funkcjonalność 2 pozwala na 'nabicie' produktów:
    - Program wyświetli listę dostępnych produktów oraz opcję zakończ
    - User wybiera produkt, który chce dodać do transakcji 
    - Program po każdym wyborze produktu dodaje wartość wybranych produktów i prezentuje ją userowi
    - Ponownie wyświetla menu z produktami i powtarza proces az user nie wybierze opcji zakończ.
    - gdy user zakonczy, wartość produktów jest dodana do ogólnego balansu kasy i nowy balans jest wyświetlany

```python
# lista produktów
products = [
    {
        "name": "banan",
        "price": 1.99,
    },
    {
        "name": "truskawka",
        "price": 1.10,
    },
    {
        "name": "pomarańcza",
        "price": 3.20,
    },
    {
        "name": "jagody",
        "price": 3.50,
    },
]

```

```bash
# menu główne
1) Wyświetl stan kasy
2) Dokonaj transakcji
```

## wymagania techniczne
1. Program składa się z co najmniej jednej klasy.
2. User może wybierać tylko dostępne opcje, w przeciwnym razie pokazuje się błąd.
3. Program działa cały czas i zawsze wraca do menu głównego po zakonczeniu funkcjonalnosci 1 lub 2.
4. Balans startowy to 500
