# Funkcja Map

Funkcja map w Pythonie 3 bierze dwie rzeczy: funkcję i listę. Zastosowuje funkcję do każdego elementu na liście. 
Wyobraź sobie, że masz listę jabłek i maszynę, która zmienia każde jabłko w sok jabłkowy. 

Funkcja map działa podobnie. Jeśli masz listę [1, 2, 3] i funkcję, która podwaja liczby, map tworzy nową listę [2, 4, 6]. To sposób na szybkie zmienienie wszystkich elementów na liście jednym poleceniem.

Przykładowa implementacja funkcji map (obsługuje tylko listę):

```python
def map(callback, my_list): 
    result = [] 
    for i in my_list: 
        result.append(callback(i)) 
    return result
```

Więcej o map(): https://realpython.com/python-map-function/

# Lambada


W Pythonie lambda to szybki sposób na stworzenie drobnej funkcji bez nazwy. Coś w stylu narzędzia jednorazowego użytku.
Jeśli chcesz dodać dwie liczby, normalnie napisałbyś funkcję:

```python 
def add(x, y):
    return x+y
```

Z lambda robisz to w jednej linijce: 

```python
lambda x,y: x+y
```

Na przykład, jeśli chcesz podwoić liczbę, możesz napisać:

```python
lambda x: x*2
```

Jest używana, gdy nie chcesz pisać pełnej funkcji, na przykład podając ją jako argument do innej funkcji.


# PD

## Do przeczytania

Funkcja `filter()`: https://ioflood.com/blog/python-filter-function-guide-with-examples/

## Zadanie

Napisz program, który na podstawie listy cen w dolarach stworzy nową listę z poprawnie sformatowanymi zapisami cen i wyprintuje ją do konsoli.

Przykład:

```python
# Przykładowa lista cen w dollarach
prices_in_dollars = [2.40, 999, 34.21, 150, 1001]

# Przykładowa lista wyprintowana do konsoli po odpaleniu programu
['$2.40', '$999', '$34.21', '$150', '$1001']

```

Warunki do spełnienia:
1. Program nie modyfikuje pierwszej listy. Należy użyć funkcji map.
2. Program printuje do konsoli listę
3. Nie trzeba zabespieczać programu przed userem debilem. Ćwiczenie służy do zapoznania się z funkcją map.

-----Podpowiedzi poniżej-----

Step by step:

1. Zadeklaruj swoją listę `prices_in_dollars` (możesz skopiować stąd)
2. Napisz funkcję, która przyjmuje numer i zwraca go jako string z $ na początku. np. przyjmuje 3.38, zwraca '$3.38'.
3. Zadeklaruj zmienną `result`
4. Po znaku `=` możesz od razu użyć funkcji map
5. Podaj odpowiednie argumenty do funkcji map.
6. Wyprintuj result do konsoli.
