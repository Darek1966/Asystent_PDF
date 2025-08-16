# Asystent PDF

Aplikacja do analizy dokumentów PDF z wykorzystaniem sztucznej inteligencji. Pozwala na wgranie dokumentów PDF i zadawanie pytań dotyczących ich zawartości.

## Funkcjonalności

- Wgrywanie wielu dokumentów PDF jednocześnie
- Ekstrakcja tekstu z dokumentów PDF
- Przetwarzanie tekstu na wektory przy użyciu OpenAI Embeddings
- Przeszukiwanie dokumentów przy użyciu FAISS
- Konwersacyjny interfejs do zadawania pytań o zawartość dokumentów
- Odpowiedzi generowane przez model językowy OpenAI

## Wymagania

- Python 3.x
- Klucz API OpenAI

## Instalacja

1. Sklonuj repozytorium:

```
git clone [adres-repozytorium]
cd Asystent\ PDF
```

2. Zainstaluj wymagane pakiety:

```
pip install -r requirements.txt
```

3. Utwórz plik `.env` na podstawie `.env.example` i dodaj swój klucz API OpenAI:

```
OPENAI_API_KEY=twój-klucz-api
```

## Uruchomienie

Uruchom aplikację za pomocą Streamlit:

```
streamlit run application.py
```

Aplikacja będzie dostępna w przeglądarce pod adresem: http://localhost:8501

## Jak korzystać

1. Wgraj dokumenty PDF za pomocą przycisku w panelu bocznym
2. Kliknij przycisk "Process" aby przetworzyć dokumenty
3. Zadawaj pytania w polu tekstowym na dole ekranu
4. Otrzymuj odpowiedzi oparte na zawartości wgranych dokumentów

## Technologie

- Streamlit - interfejs użytkownika
- LangChain - framework do budowy aplikacji opartych na LLM
- OpenAI - model językowy i embeddingi
- FAISS - biblioteka do efektywnego wyszukiwania podobieństwa wektorów
- PDFPlumber - ekstrakcja tekstu z PDF

## Struktura projektu

- `application.py` - główny plik aplikacji
- `requirements.txt` - lista zależności
- `.env.example` - przykładowy plik konfiguracyjny

---

## Kontakt

[![Email](https://img.shields.io/badge/Email-Napisz%20do%20mnie-blue?style=for-the-badge&logo=gmail&logoColor=white)](mailto:netdark_1966@op.pl)

[![GitHub](https://img.shields.io/badge/GitHub-Darek1966-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Darek1966)

## Licencja
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ten projekt jest licencjonowany na licencji MIT - zobacz plik [LICENSE](LICENSE).

---
