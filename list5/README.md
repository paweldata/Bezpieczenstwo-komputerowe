# Bezpieczenstwo-komputerowe
## Lista 5

Projekt banku pozwalający wysyłać przelewy.

### Użycie

Przykład instalacji oraz wywołania
```Shell
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip3 install -r requirements.txt
(venv) $ python3 bank/manage.py runserver
```

Wpisujemy w przeglądarce 'localhost:8000' <br>

Trzeba również stworzyć użytkownika i bazę danych w mysql według danych w bank/bank/settings.py:82-90.

### Podmiana numeru konta bankowego
w folderze plugin/ znajduje się kod w javascript, który podmienia numer konta, na który wykonujemy przelew.
