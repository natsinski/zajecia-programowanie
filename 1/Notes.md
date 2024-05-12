# GIT i Github

Omówiliśmy czym jest git i github i jak posługiwać się repozytoriami.

## Git

System kontroli wersji. Pozwala na zapisywanie zmian w plikach i utrzymanie historii zmian.

### Podstawy używania gita
Aby stworzyć repozytorium w danym folderze używamy
    
```
git init

```
Aby zacząć trackować zmodyfikowane pliki w repozytorium używamy

```
git add .

```
Aby dodać commit czyli zapisać zmiany w historii używamy

```
git commit -m "moje zmiany"

```
Aby przełączać się miedzy branchami

```
git switch nazwa_brancha

```
Aby stworzyć nowy branch 

```
git switch -c nazwa-nowego-brancha

```

## Github

Serwis internetowy do przechowywania repozytoriów. Repozytoria mogą być prywatne i publiczne (open source).
Alternatywami dla Githuba są serwisy takie jak gitlab, bitbucket, gitea. 

### Pull Request
Pull request jest żądaniem o sprawdzenie oraz zatwierdzenie zmian wprowadzonych przez programistę do istniejącego repozytorium kodu. Pozwala na utrzymanie porzątku i wysokiej jakość kodu.

Aby wystawić PR należy:

1. Stworzyć nowy branch lokalnie (na swoim komputerze)
2. Dodać swoje zmiany w kodzie
3. Zacommitować swoje zmiany
4. Użyć komendy `git push`, która wypchnie nasz lokalny branch do repozytorium na GitHub.
5. Na GH kliknąć przycisk Add Pull Request i wypełnić formularz
6. Poczekać na Code Review i Approve
7. Klinąć Merge changes

# Resources do nauki

Dokumentacja

* https://www.easypythondocs.com/
* https://www.w3schools.com/python/python_reference.asp -> lista słów kluczowych i metod
* Jest też oficjalna dokumentacja pythona ale jest turbo nieczytelna

Tutoriale:

* https://www.w3schools.com/python/default.asp -> przyjemny tutorial pythona na którym będziemy się opierać
* https://dev.to/milu_franz/git-explained-the-basics-igc Post Milu na temat podstaw gita. (tylko 1 part)

Misc.

* https://www.youtube.com/@Fireship Krótkie filmiki tłumaczące konkretne technologie i newsy
* https://www.youtube.com/@programmingwithmosh/videos dużo różności z poradami i tutoriale
* https://www.youtube.com/@bigboxSWE Brainrot i dobre rady


# PD

Jako że codecademy jest za paywallem to zamiast tego przejdź proszę przez ten tutorial maksymalnie do rozdziału Python Functions.

https://www.w3schools.com/python/default.asp 

Nie ma parcia, tutorial dość rozwięzły więc nie szkodzi jak nie dojdziesz do funkcji.

