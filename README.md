
# Udostępnianie danych informacyjnych o regionalnych dyrekcjach lasów państwowych i nadleśnictwach w geoportalu
Niniejsze repozytorium zawiera skrypty będące częścią pracy inżynierskiej.

Autor: Kinga Rozmuszyńska

Uczelnia: Szkoła Główna Gospodarstwa Wiejskiego

Warszawa, 30 Czerwca 2020 roku

## Uruchomienie skryptów on-line
W celu przetestowania kodu zawartego w tym repozytorium (oraz ewentualnej modyfikacji) możesz skorzystać ze strony [repl.it](https://repl.it/). Jest to najprostszy sposób, żeby bez konieczności instalacji jakiegokolwiek oprogramowania wygenerować własny geoportal. Poniżej jest instrukcja krok po kroku co trzeba zrobić:

1. Otwórz stronę [repl.it](https://repl.it/).
2. Wybierz `Start <coding>` (możesz też utworzyć konto ale nie jest to wymagane).
3. W wyświetlonym panelu wybierz `Import from GitHub`
4. Wklej adres tego repozytorium `https://github.com/krozmuszynska/geoportal` i kliknij Import
5. Zobaczysz, że do on-line edytora zostanie wczytane repozytorium kodu, powinieneś zobaczyć ten plik z instrukcją.
6. Kliknij `Run`, teraz rozpocznie się instalacja wymaganych bibliotek a po jej ukończeniu skrypt na podstawie przykładowego pliku `data.xlsx` wygeneruje gotowy geoportal zawierający dane o siedzibach administracji LP wraz z danymi kontaktowymi i zdjęciami budynków. 
7. Jeżeli w oknie terminala po prawej zobaczysz komunikat  `Geoportal is ready to use, please open geoportal/index.html to see how it looks like` portal wygenerował się poprawnie. Wygenerowane pliki znajdują się w katalogu `geoportal`, który zobaczysz w drzewie repozytorium po lewej stronie.
8. Żeby pobrać pliki na dysk komputera kliknij w podglądzie drzewa projektu na trzy pionowe kropki `...` i wybierz `Download as zip`.
9. Pobrane archiwum rozpakuj w dowolne miejsce
10. Wejdź do katalogu gdzie rozpakowałeś plik, dalej do `geoportal` i otwórz plik `index.html`
11. W domyślnej przeglądarce pojawi się wygenerowany geoportal wraz z warstwami i punktami, które były w pliku Excel `rdlp_gps.xlsx`
12. Zawartość katalogu `geoportal` możesz komuś posłać, albo skopiować na dowolny hosting i udostępnić całemu światu :)
13. Niech moc będzie z Tobą!


## Uruchomienie skryptów w lokalnym środowisku
W celu uruchomienia skryptów lokalnie (na swoim komputerze) należy wykonać poniższe kroki. W tym celu będziesz potrzebował zainstalowanego Pythona 3, szczegóły znajdziesz tutaj [python.org](https://www.python.org/downloads/). Potrzebujesz również `git`-a, żeby ściągnąć repozytorium na dysk, szczegóły znajdziesz tutaj [git-scm.com](https://git-scm.com/). Dalej za pomocą polecenia `pip` musisz zainstalować biblioteki `geojson` (do obsługi formatu GeoJSON), `openpyxl` (do odczytania plików Excel) oraz `jinja2` (do odczytania szablonów strony geoportalu).

W skrócie, po zainstalowaniu Python-a i Git-a wykonaj poniższe polecenia w terminalu:
```
$ git clone <GitHub address>
$ cd <projName>
$ virtualenv .venv --python=python3
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

Twoje środowisko jest gotowe i możesz uruchomić kod z repozytorium:

```
$ python3 main.py
```

W pliku `main.py` zauważysz zakomentowaną sekcję kodu na samym początku, w tej sekcji znajduje się obsługa argumentów podawanych z linii poleceń w celu automatyzacji przetwarzania danych wejściowych. Jeżeli potrzebowałbyś wygenerować więcej portali na podstawie różnych zbiorów sanych wejściowych możesz odkomentować tą sekcję i zautomatyzować pracę.

## Pliki w repozytorium
- main.py - główny skrypt generujący geoportal
- helper.py - plik zawierający pomocnicze funkcje
- sheet_types.py - plik zawierający klasy reprezentujące poszczególne arkusze
- index.html.jinja - szablon strony geoportalu
- data.xlsx - szablon danych wejściowych i konfiguracyjnych z przykładami (punkty, opisy, podkłady mapowe, warstwy wms, znaczniki)
- requirements.txt - lista bibliotek z których korzysta skrypt

## Struktura pliku danych informacyjnych `data.xlsx`
Plik `data.xlsx` zawiera dane informacyjne służące do wygenerowania geoportalu. Plik zawiara informacje takie jak:
I. Lista obiektów (`data`), które będą prezentowane na podkładach mapowych.
II. Lista podkładów mapowych (`tiles`), które użytkownik może dowolnie wybierać.
III. Lista warstw usługi mapowej (`wms`), która pozwala na prezentowanie dodatkowych warstw na mapie.
IV. Lista znaczników (`markers`), która pozwala na graficzne oznaczenie różnych typów obiektów (Point).

### I. Arkusz zawierający listę obiektów o nazwie `data` posiada następujące kolumny:
1. ID - unikalny identyfikator obiektu
2. Latitude [N] - szerokość geograficzna punktu podawana w formie dziesiętnej (np. 52.200105)
3. Longitude [E] - długość geograficzna punktu podawana w formie dziesiętnej (np. 20.967855)
4. Marker ID - przyporządkowany do punktu identyfikator znacznika (zgodnie z id podanym w zakładce `markers`)
5. Name - tekstowa nazwa punktu, może zawierać kod HTML
6. Description - tekstowy opis punktu, może zawierać kod HTML
7. Search key - tekst po który zostanie użyty w wyszukiwarce punktów (np. słowa kluczowe opisujące punkt, miejscowość, identyfikator)
8. Street - nazwa ulicy, tekst
9. Building no - numer budynku, tekst (znaki, cyfry)
10. Local no - numer lokalu, tekst (znaki, cyfry)
11. ZIP - kod pocztowy
12. City - nazwa miejscowości
13. Country - nazwa kraju
14. Telephone - numer tlefonu
15. E-mail - adres email
16. Web - adres strony www
17. Image URL - adres URL obrazka, który pojawi się w opisie punktu na mapie

### II. Arkusz zawierający listę podkładów mapowych o nazwie `tiles` posiada następujące kolumny:
1. ID - unikalny identyfikator podkładu mapowego
2. Name - nazwa podkładu mapowego, pojawia się w panelu konfiguracyjnym użytkownika geoportalu
3. URL - adres URL podkładu mapowego (np. `http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png`)
4. Tile size - rozmiar kafelka (np. `512` oznacza kafelki w rozmiarze 512x512 px)
5. Zoom offset - wartość przesunięcia powiększenia zastosowana w adresach URL kafelków
6. Max zoom - maksymalne możliwe powiększenie na danym podkładzie mapowym
7. Attribution - informacje autorskie lub komentarze do podkładu mapowego, widoczne dla użytkownika

### III. Arkusz zawierający listę podkładów mapowych o nazwie `wms` posiada następujące kolumny:
1. ID - unikalny identyfikator warstwy
2. Name - nazwa warstwy, pojawia się w panelu konfiguracyjnym użytkownika geoportalu
3. URL - adres URL serwera WMS (np. `https://mapserver.bdl.lasy.gov.pl/ArcGIS/services/WMS_BDL/mapserver/WMSServer?`)
4. Layer name - nazwa warstwy, zgodnie z informacjami w GetCapabilities serwera WMS
5. Format - format danych przesyłanych przez serwer (np. `image/png`)
6. Transparent - czy pobrane obrazy mają być transparentne, wartość boolowska (np. `true`, `false`) 
7. Attribution - informacje autorskie lub komentarze do warstw, widoczne dla użytkownika

### IV. Arkusz zawierający listę znaczników o nazwie `markers` posiada kolumny, które tworzą dwie grupy.
A. kolumy 1-7 które służą do konfigurowania znacznika w formie łezki, np. wskazania jego koloru oraz ikony jaka się ma na nim pojawić
B. kolumny 11-17 które służą do konfigurowania własnego znacznika, np. link do obrazu znacznika, jego wielkość, cieniowanie, pozycja dymka informacji względem znacznika 
Domyślne oznaczenie punktu jest realizowane przez grupę kolumn (A). W przypadku gdy użytkownik uzupełni obie grupy, skrypt jako preferowany użyje własny znacznik użytkownika (B).

Znaczenie poszczególnych kolumn w arkuszu jest następujące:
1. (A) ID - unikalny identyfikator znacznika, wykorzystywany w arkuszu `data`
2. (A) Name - nazwa grupy znaczników, pojawia się w panelu konfiguracyjnym, żeby użytkownik mógł włączyć/wyłączyć wszystkie znaczniki danego typu
3. (A) Icon name - nazwa ikony z biblioteki wskazanej w kolumnie `Prefix` (np. `star` dla biblioteki `fa`)
4. (A) Prefix - oznaczenie biblioteki ikon znacznika, dostępne biblioteki to `fa` dla stylu Font-Awesome, `glyphicon` dla stylu Bootstrap 3, `ion` dla stylu IOnic Fonts
5. (A) Marker color - kolor znacznika łezki, dostępne wartości kolorów to `red`, `darkred`, `orange`, `green`, `darkgreen`, `blue`, `purple`, `darkpurple`, `cadetblue`
6. (A) Icon color - kolor ikony na znaczniku, dostępne wartości kolorów to `white`, `black` lub kod css (hex, rgba)
7. (A) Spin - czy ikona ma się kręcić wokół swojej osi 
8. Zoom min - minimalna wartość powiększenia dla której widoczna jest ikona znacznika
9. Zoom max - maksymalna wartość powiększenia dla której widoczna jest ikona znacznika
10. Extra classes - dodatkowe klasy CSS które zostaną dodane do znacznika
11. (B) Icon URL - adres URL ikony znacznika
12. (B) Shadow URL - adres URL cienia znacznika (opcjonalne dla stworzenia efektu 2.5D)
13. (B) Icon size - rozmiar ikony znacznika na mapie podany w pikselach w postaci listy `[X,Y]` (np. `[20,20]`)
14. (B) Shadow size - rozmiar cienia znacznika na mapie podany w pikselach w postaci listy `[X,Y]` (np. `[20,20]`)
15. (B) Icon anchor - miejsce wyświetlenia ikony względem lokalizacji na mapie (użytkownik może podać przesunięcie wzglem punktu na mapie), wartość podana w postaci listy `[X,Y]`, gdzie wartości X i Y są przesunięciem w pikselach (np. `[-10,8]`)
16. (B) Shadow anchor - miejsce wyświetlenia cienia ikony względem lokalizacji na mapie (użytkownik może podać przesunięcie wzglem punktu na mapie), wartość podana w postaci listy `[X,Y]`, gdzie wartości X i Y są przesunięciem w pikselach (np. `[-40,20]`)
17. (B) Popup anchor - miejsce wyświetlenia dymka z informacjami o punkcie względem lokalizacji na mapie (użytkownik może podać przesunięcie wzglem punktu na mapie), wartość podana w postaci listy `[X,Y]`, gdzie wartości X i Y są przesunięciem w pikselach (np. `[20,20]`)

## Jakie dane są dostępne w usługach WMS, WMTS serwera
W celu sprawdzenia jakie dane sa dostępne na serwerze udostępniającym usługi WMS lub WMTS, które możemy wykorzystać w naszym geoportalu, należy skorzystać z parametru o nazwie `GetCapabilities` oraz wskazać jaką usługę chcemy sprawdzić - parametr `services`. Przykład zapytania skonstruowanego na podstawie adresu serwera oraz parametrów wygląda tak:
[https://wfs.bdl.lasy.gov.pl/geoserver/BDL/ows?request=GetCapabilities&service=WMS](https://wfs.bdl.lasy.gov.pl/geoserver/BDL/ows?request=GetCapabilities&service=WMS)

Jeżeli klikniesz powyższy link powinieneś zobaczyć w przeglądarce odpowiedź serwera w postaci pliku XML. W pliku możesz wyszukać dostępne formaty kafelek (`<GetMap><Format>...</Format></GetMap>`), dostępne układy współrzędnych (`<Layer><CRS>...</CRS></Layer>`), czy nazwy dostępnych warstw i ch konfiguracji (`<Layer><name>...</Name></Layer>`).


## Biblioteki wykorzystane w skrypcie Python-a
1. [Geojson](https://pypi.org/project/geojson/) - do obsługi formatu GeoJSON
2. [Openpyxl](https://pypi.org/project/openpyxl/) - do odczytania plików Excel
3. [Jinja2](https://pypi.org/project/Jinja2/) - do odczytania szablonów strony geoportalu

## Biblioteki wykorzystane przez geoportal
1. [JQuery](https://jquery.com/) - do obsługi zapytań JQuery
2. [Leafletjs](https://leafletjs.com/) - do obsługi wyświetlania geoportalu
3. [Leaflet MinMap](https://github.com/Norkart/Leaflet-MiniMap) - do wyświetlania minimapy
4. [Leaflet fusesearch](https://github.com/naomap/leaflet-fusesearch) - do wyszukiwania na podstawie słów kluczowych (`search key`)
5. [Leaflet grouped layer control](https://github.com/ismyrnow/leaflet-groupedlayercontrol) - do wyświetlania panelu grupującego warstwy WMS i znaczniki
6. [Leaflet awsome markers](https://github.com/lvoogdt/Leaflet.awesome-markers) - do obsługi znaczników
7.  [Font Awsome](https://fontawesome.com/v4.7.0/icons/) - zestaw stylów ikon `fa`
8. [IOnic Font](https://ionicons.com/) - zestaw stylów ikon `ion`
9. [Bootstrap 3](https://icons.getbootstrap.com/) - zestaw stylów ikon `glyphicon`

## Dane informacyjne geoportalu (plik `geojson.js`)
Dane informacyjne wyświetlane w geoportalu są przechowywane w pliku `geojson.js`. Dane te pochodzą z arkusza `data`, który po przetworzeniu przez skrypt generujący portal zostały umieszczone w strukturze [geoJSON](https://geojson.org/). Wprowadzono niewielką modyfikację pliku geoJSON przez dodanie tekstu `var jsonData = ` na początku pliku. Taki zabieg jest celowy i pozwala użytkownikowi na wyświetlenie geoportalu lokalnie na dowolnym systemie wyposażonym w przeglądarkę internetową. W przeciwnym przypadku próba odczytania pliku geoJSON przez skrypty JavaScript na lokalnej maszynie zostałaby zablokowana (ze względu na polityki bezpieczeństwa nowych przeglądarek).
Struktura pliku geoJSON w sekcji `properties` zawiera dane informacyjne o punktach oraz w pod-sekcji `marker` informacje o znaczniku jaki ma się wyświetlić. Zawarcie wszystkich danych informacyjnych w sekcji `properties` zapewnia pełną zgodność ze standardem geoJSON i uniknięciem problemów z ewentualnym importem danych do innych zastosowań w przyszłości (np. wczytaniem danych na geoserwerach).
Przykładowy punkt prezentowany w geoportalu jest zapisany w formacie geoJSON w następujący sposób:
```
    {
            "geometry": {
                "coordinates": [
                    20.967855,
                    52.200105
                ],
                "type": "Point"
            },
            "properties": {
                "address": "Grójecka 127, 02-124 Warszawa, Polska",
                "description": "",
                "email": "sekretariat@lasy.gov.pl",
                "image": "https://www.lasy.gov.pl/++theme++lasy/cache/img/static_151745856382/cab4c4b4-56e8-4c4b-b35b-c8985e4a96d4.jpeg",
                "marker": {
                    "extraClasses": "",
                    "icon": "star",
                    "iconAnchor": "",
                    "iconColor": "white",
                    "iconSize": "",
                    "iconUrl": "",
                    "id": "general",
                    "markerColor": "red",
                    "name": "Dyrekcja generalna",
                    "popupAnchor": "",
                    "prefix": "fa",
                    "shadowAnchor": "",
                    "shadowSize": "",
                    "shadowUrl": "",
                    "spin": true,
                    "zoom_max": 20,
                    "zoom_min": 4
                },
                "name": "Dyrekcja Generalna Lasów Państwowych",
                "phone": "22 589 81 00",
                "search": "Warszawa",
                "website": "http://www.lasy.gov.pl/pl"
            },
            "type": "Feature"
        }
```
W sekcji `geometry` można użyć innych typów jak okrąg, elipsę, trójkąt czy wielokąt (poligon). Więcej na ten temat można przeczytać w [załaczniku A](https://geojson.org/geojson-spec.html#appendix-a-geometry-examples)  standardu geoJSON. Takie rozwiązanie pozwala na pokazywanie dowolnie złożonych punktów w geoportalu. W chwili obecnej skrypt generujący geoportal ogranicza się jedynie do interpretacji punktów z podanymi współrzędnymi (proste tabelaryczne zestawienie danych wejściowych), ale jeżeli użytkownik dostarczy dane w formacie geoJSON z innej aplikacji (np. QGis) to może je wyświetlić podmieniając plik `geojson.js`. 


## Zasada działania geoportalu
Geoportal wygenerowany dzięki skryptom Python-a wykorzystuje szkielet strony w HTML5 oraz biblioteki JavaScript do wyświetlania a) podkładów mapowych, b) warstw z serwisów WMS, c) danych informacyjnych. 

Geoportal umożliwia użytkownikowi na podstawową konfigurację dynamicznie wyświetlanej zawartości. Użytkownik ma dostępne funkcje takie jak 
a) powiększenie
b) skala
c) wyszukiwanie znaczników (po słowach kluczowych)
d) wybór wyświetlanego podkłdu mapowego
e) wybór wyświetlanych warstw WMS
f) wybór wyświetlanych grup znaczników
g) podgląd orientacyjny na minimapie ogólnej

Geoportal do swojego działania wykorzystuje m.in. bibliotekę LeafJS, która umożliwia odczytanie podkładów mapowych z podanych adresów URL serwerów. Na podkłady mapowe są następnie nakładane dane pobrane z serwisów WMS w formie warstw. Dalej wyświetlane są znaczniki punktów podane w pliku z danymi (`geojson.js`). Każdy punkt jest umieszczony na mapie zgodnie ze swoimi współrzędnymi i reprezentowany jest w formie znacznika. Punkty mogą mieć przyporządkowane różne znaczniki. Znaczniki danego typu (ID) tworzą grupę, którą użytkownik może włączać/wyłączać jak warstwy na mapie. Znaczniki mają ponadto przypisane dane, które są wyświetlane po kliknięciu na znacznik. Dane zawierają podstawowe informacje teleadresowe punktu, nazwę, obrazek i opis. W przypadku nie podania danych adresowych zostaną one pominięte w widoku, dzięki temu można ograniczyć informacje podawane o punkcie do tytułu i opisu (treść może zawierać kod HTML). 
Takie rozwiązanie pozwala na uniwersalne zastosowanie arkusza do wyświetlania dowolnych danych informacyjnych w opisie punktu. Dane prezentowane w geoportalu znajdują się w pliku `geojson.js`, który jest zgodny z formatem geoJSON.  Użytkownik może zawsze wykorzystać wygenerowany plik geoJSON (po usunięciu wspomnianego tekstu na jego początku) np. do obróbki danych w aplikacjach takich jak ArcGIS, QGis. Zgodność danych geoportalu z formatem geoJSON gwarantuje kompatybilność z szeregiem innych zastosowań danych i pozostawia stworzone rozwiązanie jako otwarte na dalszą integrację.


Geoportal dzięki otwartym technologiom pozwala na dalsze modyfikacje przez użytkownika końcowego. Możliwa jest integracja z istniejącą stroną, portalem, czy aplikacją desktopową, serwerową lub mobilną (opartą o wyświetlanie zawartości HTML). Również zawartość interfejsu użytkownika może zostać dostosowana w zależności od potrzeb odbiorcy, można np. dodać opcje pomiaru na mapie, zaznaczania obszarów, zapisywania własnych warstw, itp. Ponadto przygotowane rozwiązanie jest w pełni skalowalne. W przypadku umieszczenia geoportalu na serwerze hostingowym można wykonać skalowanie pionowe przez dodanie większej ilości zasobów (procesor, pamięć ram, dysk, ilość IOPS). W przypadku większych potrzeb odbiorcy końcowego możliwe jest wykonanie skalowania poziomego poprzez umieszczenie HAProxy (rozdziela ruch na poszczególne serwery) na wejściu ruchu sieciowego a dalej na osobnych serwerach należy umieścić kopię geoportalu. Takie rozwiązanie zapewni wysoką dostępność rozwiązania. Możliwe jest też zwiększenie dostępności geoportalu na poziomie światowym poprzez umieszczenie kopii danych i strony na serwerach CDN (duży, rozproszony system dostarczania treści do wielu centrów danych i punktów wymiany ruchu w Internecie). Ostatnie proponowane rozwiązanie wydaje się być efektywne ekonomicznie. Sama architektura rozwiązania jest w dużej mierze oparta o wykorzystanie zasobów własnych odbiorcy końcowego rozwiązania, tj. po wczytaniu danych strony głównej `index.html` oraz pobraniu pliku danych `geojson.js` wszystkie operacje wykonywane są po stronie klienta, co znacząco ogranicza koszty transferu dla usług hostingowych. Wąskim gardłem rozwiązania staje się jedynie dostępność podkładów mapowych oraz usług WMS. Ten problem można rozwiązać poprzez skorzystanie z profesjonalnych dostawców podkładów takich jak Google Maps, ArcGis, MapBox. 