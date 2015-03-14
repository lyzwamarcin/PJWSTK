1. Uruchomienie programu.
    1.
        - w katalogu data należy wymienić zawartość pliku text.txt
        - program uruchamiamy komendą z katalogu main: python Main.py
    2.
        - aby zmienić ścieżki dla pliku źródłowego i wynikowego należy zmienić wartości zmiennych (__TEXT_SOURCE_FILE__, __OUTPUT_FILE_PATH__)w pliku Main.py
        - uruchomienie: python Main.py

2. Struktura katalogów
    1. main - katalog zawiera pliki z implementacją poszczególnych funkcjonalności programu.
    2. data - katalog w którym znajdują się pliki z listą skrótów, plik źródłowy do analizy oraz xml wynikowy.

3. Wykorzystane biblioteki zewnętrzne do NLP
    W pierwszej programu korzystałem z biblioteki nltk do tokenizacji tekstu źródłowego. W ostatecznej wersji nie wykorzystuję bibliotek do NLP.

4. Opis zaimplementowanej metody
    Zliczanie zdań oparte jest głównie na szukaniu kropek w poszczególnych tokenach oraz ich analiza. Sprawdzanie czy token zawiera kropkę odbywa sie przez
    wyrażenie regularne. Następnie wykonywane jest sprawdzanie, czy dany token znajduje sie w bazie skrótów. Cytaty traktowane są jako jedno całe zdanie.
