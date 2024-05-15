# Validacja inputu od Usera

Programy które są zaprojektowane do interakcji z userem powinny być zabezpeczone przed głupotami, które user może zrobić.
Inaczej mówiąc input od Usera powinien być zwalidowany czyli sprawdzony przed dalszym wykonaniem jakielwiek operacji.

# Pure functions

Dobrą praktyką jest pisanie tzw. pure functions. Jest to funkcja, która spełnia obie poniższe cechy:

- Nie modyfikuje input’u, input jest tylko do odczytu.
- Jest deterministyczna — dla dowolnych danych zawsze zwraca te same wartości. Przykładowo funkcja dodawania jest deterministyczna, bo 2 + 2 zawsze zwróci 4, ale funkcja zwracająca obecny czas nie jest deterministyczna, bo czas zwrócony teraz jest inny niż czas zwrócony godzinę temu.

Oczywiście nie jest to reguła, ale bardziej wskazówka.

# Funkcja anonimowa - lambda

Lambda w pythonie to anonimowa (to znaczy nie nazwana) funkcja, która wykonuje jakąś operację. 
Jest bardzo przydatna, ponmieważ możemy ją podać jako argument do innej funkcji, np `map()`.

```python
lambda arg1,arg2: arg1+arg2
```

Przykład użycia lambdy jako argumentu w funkcji map:

```python
vals_in_meters = [1, 2, 3 ,4 ,5]

vals_in_centimeters = map(lambda a: a*100, vals_in_meters)

print(list(vals_in_centimeters))
```

1. Deklarujemy listę wartości w metrach
2. Funkcja map wywołuje funkcję-lambdę podaną jako pierwszy argument na każdym elemencie listy podanej jako drugi argument.
3. Return funkcji map jest przypisany do zmiennej `vals_in_centimeters`
4. `vals_in_centimeters` jest castowana jako lista i printowana funkcją print. 


# PD 

W naszej grze jest problem z inputem od usera. Należy przemyśleć co może pójść nie tak, np. user wpisze tekst zamiast liczby i zabezpieczyć nasz kod przed takimi zdarzeniami.
1. Przemyśl jakie inne błędy poza wpisaniem liter moze popełnić user
2. Zaimplementuj walidację - zabezpiecz program przed tym błędami.

# Do przeczytania
- map w pythonie W3 - https://www.w3schools.com/python/ref_func_map.asp
- map w pythonie tutorial -  https://www.programiz.com/python-programming/methods/built-in/map 
