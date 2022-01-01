# Analiza wpływu jakości wideo na skuteczność automatycznej identyfikacji obiektów


Repozytorium zawiera pliki z poleceniami oraz kodem, które wykorzystano podczas realizacji tematu pracy. Pominięto dodawanie plików wideo i plików detektorów, jako że są bardzo duże (kilka GB w sumie). Wszystkie pliki można znaleźć na moim dysku Google Drive (dostęp z tylko konta w domenie Politechniki Wrocławskiej): https://drive.google.com/drive/folders/1P25c80ImJ73fyvyhB2-BlwGymvxEEh6K?usp=sharing

Aby moć w pełni odwzorować czynności zaprezentowane w napisanej pracy, nleży pobrać udostępniony wyżej folder autora, a następnie przesłać pliki do własnej usługi Google Drive. Ze względu na duży rozmiar niektórych plików, można pominąć pobieranie zawartości następujących folderów: `wideo/logi`, `wideo/skompresowane`, `wideo/wyniki` oraz `detektor/wagi`. Struktura pobrancyh folderów i plików powinna zostać jednak zachowana. 

W originalnej strukturze projektu znajdują się następujące pliki z rozszerzeniem `.ipynb`:
<ul>
    <li>"przygotowanie-zbiorów.ipynb" - zawierający komendy służące pobraniu własnego zbioru do trenowania modelu, jak i do walidacji. Pobrane zbiory są kompresowane i przesyłane na dysk Google Drive,
    <li> "trenowanie-modelu.ipynb" - plik odpowiedzialny za trenowanie modelu  detektora (koniecznym jest wybór GPU jako akceleratora sprzętowego),
    <li> "kompresja.ipynb" - plik odpowiedzialny za kompresję plików referencyjnych do wybranych wartości BR (bitrate) oraz za ocenę jakości plików skompresowanych,
    <li> "detekcja.ipynb" - plik odpowiedzialny za przeprowadzenie detekcji na plikach skompresowanych (koniecznym jest wybór GPU jako akceleratora sprzętowego). Detekcja przeprowadzona może być dla  samodzielnie wytrenowanego lub gotowego modelu detektora (folder pre-trained).
</ul>

Opisane pliki wystarczą do realizacji każdej z opisanych w pracy zadań. Problem stanowić mogą jedynie ograniczenia czasowe narzucone przez środowisko Google Colab.
