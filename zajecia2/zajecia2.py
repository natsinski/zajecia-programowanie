import random


def guessing_game():
    random_number = random.randrange(100)
    while True:
        liczba = input("Jaka liczba twoim zdaniem została wylosowana? ")
        liczba = int(liczba)
        if liczba > random_number:
            print("Wylosowana liczba jest mniejsza!")
        elif liczba < random_number:
            print("Wylosowana liczba jest większa!")
        else:
            print("Odgadłeś liczbę!")
            break
guessing_game()

