# Object Oriented Programming

Szkoła programowania opierająca się o koncept obiektu. Popularnymi rodzajami OOP jest Class based OOP (Python, C#, Ruby) i Prototype based OOP (JavaScript)

## Obiekt i Klasy

Obiekt to kolekcja danych (data) i funkcji, które mogą przeprowadzać jakieś operacje. Funkcje obecne na instancji obiektu nazywamy metodami (method).

Klasa jest szablonem, na podstawie którego tworzymy nowe instancje obiektów.

```python
class Dog:
    def bark(self):
        print('Wow wow')

# instancja obiektu 👇
burek = Dog()

# druga instancja 👇
reks = Dog()
```

## Konstruktor

Konstruktor to funkcja, która jest wywoływana jak tylko powstaje nowa instancja obiektu. W Pythonie nazywamy ją `__init__`.
W Pythonie funkcja ta, jak kazda* inna metoda w tym języku, jako pierwszy parametr przyjmuje referencję do obiektu.
Najczęsciej ten parametr nazywany jest self.

```python
class Dog:
    def __init__(self, pet_name):
        self.name = pet_name

    def bark(self):
        print('Wow wow')

# instancja obiektu 👇
burek = Dog('Burek')
print(burek.name) # Printuje: Burek
```

## Class Properties 
Pola (properties) klasy mogą być:

- nie-statyczne -> dostępne na instancji obiektu.
    - nie statyczne metody
    - nie statyczne zmienne

- statyczne -> definiowane na klasie i dostępne z poziomu klasy
    - statyczne metody
    - statyczne zmienne

```python
class Dog:
    def __init__(self, pet_name):
        # 👇Tworzenie nie-statycznej zmiennej name
        self.name = pet_name

    # 👇Tworzenie nie-statycznej metody
    def bark(self):
        print('Wow wow')

    # 👇Tworzenie statycznej zmiennej
    latin_name = "Canis familiaris"

    # 👇Tworzenie statycznej metody. Używamy do tego dekoratora @staticmethod. 
    #   Nie przyjmuje self jako argumentu, bo jest obecna na klasie a nie na obiekcie.
    @staticmethod
    def get_dog_name(dog):
        print(dog.name)
```

# PD
Tylko przeczytać:
- Dziedziczenie w Pythonie: https://www.w3schools.com/python/python_inheritance.asp
- 4 filaty OOP: https://backend.turing.edu/module1/lessons/four_pillars_of_oop
