# Python vol 1

Na podstawie:
https://www.w3schools.com/python/default.asp

Rozdziały od `Comments` do `Functions`

## Konwencja 

Konwencje kodowania to zestawy wytycznych dla każdego konkretnego języka programowania z zaleceniami dotyczącymi różnych aspektów tworzenia oprogramowania w tym języku, w tym stylu kodowania, najlepszych praktyk i metod.

## Konwencje w Pythonie

### lower_case_with_underscores
Tzw. `snake_case`. Używany w nazewnictwie:


* Nazw funkcji/metod,

* Nazw parametrów,

* Nazw pakietów,

* Nazw modułów,

### CAPS lub CAPS_WITH_UNDERSCORE

Stosujemy w nazywaniu:

* Constów czyli stałych

* Zmiennych zadeklarowanych globalnie

### PascalCase

Używany do definiowania klas.

```python 
class BigDog:
    def bark(self):
        print('Hau Hau')
```

## Resources:
* Tuple vs List: https://www.geeksforgeeks.org/python-difference-between-list-and-tuple/

## PD

Napisz terminalową grę w zgadywanie liczby. Gra polega na tym że:
1. Gra w momencie startu losuje liczbę miedzy 1 a 100.
2. Gracz jest proszony o zgadnięcie jakiejś liczby miedzy 1 a 100
3. Jeśli gracz podał za dużą liczbę gra informuje o tym gracza i prosi o ponowne zgadnięcie
4. Analogicznie jesli gracz podał za małą liczbę gra informuje i prosi o ponowne zgadnięcie
5. Proces powtarza się do momentu aż gracz nie zgadnie wybranej na początu liczby. 
6. Wyświetla się informacja o wygranej rozgrywce
7. Zrób Pull request ze swoimi zmianami do tego repo.

Wymagania techniczne: 
1. Gra jest zaimplementowanw w conajmniej jednej funkcji. Na końcu pliku jest ona wywoływana.

Jak żyć?

1. Każdy problem jest składową mniejszych małych problemów. 
2. Jeśli nie wiesz jak coś zrobić zacznij od rozbicia na mniejsze problemy.Pomaga przy tym rozpisanie listy rzeczy do zrobienia. 
3. Kiedy masz już kilka mniejszych problemów, najpierw skup się na tych, które wiesz jak rozwiązać. 
4. Przy rozwiązywaniu miejszych problemów zbliżasz się do rozwiązania problemu ogólnego i jednocześnie nabywasz wiedzę o tym czego konkretnie nie rozumiesz lub nie wiesz. 
5. Kiedy wiesz już czego nie wiesz łatwo możesz zgobyć tą informację po prostu googlując, np: 'how to get user input in python?'.

