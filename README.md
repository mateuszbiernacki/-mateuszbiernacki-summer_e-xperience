# summer_e-xperience
Aplikacja zwraca listę repozytoriów (wraz z odpowiadającą liczbą gwiazdek) na podstawie nazwy użytkownika w postaci dokumentu html lub json.

Aplikacja została napisana w języku Python 3.8.
Python 3.8 lub wyższy jest wymagany do poprawnego działania aplikacji.

Zostały wykorzystana następujące frameworki:

 - requests
 - flask
 
Należy je zainstalować przed uruchomieniem aplikacji.

    pip install requests
    pip install flask

Zostały zaimplementowane dwa warianty aplikacji. Jeden z wariantów korzysta z tokenów githuba w celu autoryzacji zapytań. Bez autoryzacji użytkownik, na konkretny adres IP, może wykonać tylko 60 zapytań na godzinę. Z autoryzacją 5000. Jest to ograniczenie githuba. 

Aplikacja wykonuje 1 zapytanie na każde 100 repozytoriów które użytkownik posiada + 1 zapytanie na sprawdzenie ile repozytoriów ma dany użytkownik. Takie rozwiązanie jest spowodowane tym, że GitHub ogranicza liczbę repozytoriów do maksymalnie 100 na stronę (domyślnie 30).

Aby uruchomić aplikację z wiersza poleceń:
(bez tokena)

    python stars_counter.py 

(z tokenem)

    python stars_counter_with_auth.py
Odpowiedni token wygenerowany wcześniej ([link do wygenerowania tokena](https://github.com/settings/tokens)) należy umieścić w pliku **auth.json** obok swojej nazwy użytkownika. Przy generowaniu tokena należy zaznaczyć opcję **read:user**. 

Aplikacja uruchamia się na adresie 127.0.0.1 na porcie 5000 (URL: http://127.0.0.1:5000/ ).

Aby uruchomić aplikację na innym adresie należy zmienić ostatnią linijkę kodu w następujący sposób:
  

    flask_app.run(
        host="0.0.0.0",
        port=5000
    )

Można skorzystać z aplikacji przez przeglądarkę - wchodząc na podany wcześniej adres URL, albo uzystać te dane w JSON np. za pomocą Postmana (GET http://127.0.0.1:5000/json/numbers_of_star/allegro ).

 
