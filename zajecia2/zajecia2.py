import random
x = random.randrange(100)

def user():

    while True:
        liczba = input("Jaka liczba twoim zdaniem została wylosowana? ")
        liczba = int(liczba)
        print(liczba)
        if liczba > x:
            print("Wylosowana liczba jest mniejsza!")
        elif liczba < x:
            print("Wylosowana liczba jest większa!")
        else:
            print("Odgadłeś liczbę!")
            break
user()

#Wykonałem, ale nie mam pojęcia czemu to działa