program na zaliczenie laboratorium z podstaw programowania

program włącza się z index.py

Podzieliłem projekt na kilka folderów dzięki temu index.py, calculator.py oraz filebrowser.py nie ma wiele kodu i jest schludniejszy 
wszystkie funkcje są w folderze logic i są segregowane na tryby programu aby mięc do nich łatwiejszy dostęp. 

przy rozpoczęciu programu, przechodzeniu do trybu, wychodzeniu oraz wpisaniu złej komendy w terminalu wyświetla się lista komend które urzytkownik może wpisać, uzyskałem to za pomocą wywoływania fukncji która ma w sobie print z listą komend

w kalkulatorze sprawdzam za pomocą try except czy wartości podane przez użytkownika to numery oraz podczas dzielenia czy użytkownik podzielił przez zero jeżeli tak użytkownik ponownie musi wybrać operacje i liczby

w filebrowser podczas funckji cd sprawdzam czy plik istnieje oraz czy jest katalogiem w funckji head sprawdzam czy plik istnieje.

Poprawa:
odzieliłem każdą funkcje dwiema spacjami by kod był bardziej czytelny, 

zmieniłem nazwy zmiennych sum ponieważ jest to słowo kluczowe w python

zmieniłem również nazwy innych zmiennych by łatwiej było się domyślić co przedstawiają 

Dodałem historie w kalkulatorze oraz silnie.

dodałem funkcje get_numbers() aby zminiejszyć powtarzalność kodu w logic/calculator.py

dodałem error handlers takie jak : PermissionError, OSError, UnicodeDecodeError w funckjach przeglądarki 

do nazywania zmiennych oraz funkcji których nazwa składa się z więcej niz jednego słowa używam lower_case_with_underscores
(w dokumentacji PEP8 w jednym miejscu piszą o tym żeby używać camelCase a w roździale funckje i zmienne piszą by używać "_" pomiedzy słowami wybrałem używanie "_")

do pustych return dodałem none aby składnia zwracania była spójna

do każdego inputu użytkownika dodałem strip() oraz lower() wyjątkiem jest input filebrowser tam strip nie jest potrzebny ponieważ 
split() usunie zbędne spacje (dodałem lower do input w przeglądarce ponieważ wyczytałem że ścieżki plików nie są case Sensitive przetestowałem to u mnie zadziałało)

w filebrowser.py zmieniłem nazwe comand na operation aby było spójnie z kalkulatorem i index
używam absolutnych importów tak jak PEP8 sugeruje

do poprawy używałem :
https://peps.python.org/pep-0008/
https://www.w3schools.com
https://www.geeksforgeeks.org