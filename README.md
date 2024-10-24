# Lab4 - ASI

### by s24916

## Opis

Aplikacja Flask przewidująca wynik końcowy studenta na podstawie danych wejściowych. Model przewiduje wynik na podstawie
zestawu cech z pliku `CollegeDistance.csv`, który został wyczyszczony i znormalizowany w poprzednim zadaniu.

## Wymagania

- Docker
- Python 3.9

## Klonowanie repozytorium

Aby sklonować repozytorium, wykonaj poniższe polecenia:

```bash
git clone https://github.com/pncqq/Lab4_s24916.git
cd s24916_flask_app
```

## Uruchomienie aplikacji lokalnie

1. Zainstaluj wymagane zależności:

```bash
pip install -r requirements.txt
```

2. Uruchom aplikację:

```bash
python app.py
```

3. Aplikacja będzie działać pod adresem `http://127.0.0.1:5000`.

## Uruchomienie aplikacji z wykorzystaniem Dockera

1. Zbuduj obraz Dockera:

```bash
docker build -t s24916_flask_app .
```

2. Uruchom aplikację w kontenerze:

```bash
docker run -p 5000:5000 s24916_flask_app
```

3. Aplikacja będzie dostępna pod adresem `http://127.0.0.1:5000`.

## Korzystanie z obrazu z Docker Huba

1. Pobierz obraz z Docker Hub:

```bash
docker pull s24916/s24916_flask_app:v1
```

2. Uruchom aplikację:

```bash
docker run -p 5000:5000 s24916/s24916_flask_app:v1
```

3. Aplikacja będzie dostępna pod adresem `http://127.0.0.1:5000`.

## Wysyłanie danych do API

Aby wysłać dane do API, należy przesłać zapytanie POST z danymi w formacie JSON pod adres
`http://127.0.0.1:5000/predict`.

### Struktura danych:

API oczekuje danych wejściowych w postaci znormalizowanych wartości liczbowych, które są cechami pochodzącymi z pliku
`CollegeDistance.csv`. Te dane zostały wcześniej wyczyszczone i przekształcone w ramach inżynierii cech w poprzednim
zadaniu. Model został wytrenowany na tych znormalizowanych danych, dlatego wymagane są one jako input do przewidywań.

#### Przykładowe dane wejściowe:

Przykład danych wejściowych w formacie JSON:

```json
{
    "features": [-1.21388, 0.13288, -0.74027, 0.83021, 0.11071, 2.23148, -0.48129, -0.90890, -0.50404, -0.39381,
                 0.47630, -0.55063, -1.61145, -0.50527, -0.72657, 0.82038, -1.32694, -0.61237, 0.04556]
}
``` 

### Wysyłanie zapytania:

Dane należy wysłać jako body zapytania POST z odpowiednimi nagłówkami (`Content-Type: application/json`),  
np:

```python
import requests
import json

url = 'http://127.0.0.1:5000/predict'

data = {
    "features": [-1.21388, 0.13288, -0.74027, 0.83021, 0.11071, 2.23148, -0.48129, -0.90890, -0.50404, -0.39381,
                 0.47630, -0.55063, -1.61145, -0.50527, -0.72657, 0.82038, -1.32694, -0.61237, 0.04556]
}

headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)

print("Parsed response:", response.json())
```

### Odpowiedź z API:

Odpowiedzią z serwera będzie wynik predykcji w formacie JSON, na przykład:

```json
{
  "prediction": [
    47.92
  ],
  "message": "Predicted score for the input data is 47.92."
}
```

Wynik predykcji jest wartością przewidzianą przez model na podstawie dostarczonych cech.