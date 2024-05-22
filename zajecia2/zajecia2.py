import random


def guessing_game():
    random_number = random.randrange(100)
    while True:
        liczba = input("Jaka liczba twoim zdaniem została wylosowana? ")
        if liczba.isdigit():
            liczba = int(liczba)
            if liczba > 100:
                print("Liczba nie należy do przedziału od 0 do 100!")
            else:
                if liczba > random_number:
                    print("Wylosowana liczba jest mniejsza!")
                elif liczba < random_number:
                    print("Wylosowana liczba jest większa!")
                else:
                    print("Odgadłeś liczbę!")
                    break
        else:
            print("Należy wprowadzić wpisać liczbę naturalną!")
guessing_game()

