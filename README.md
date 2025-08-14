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

<div style="display: flex; align-items: center; gap: 15px;">
  <img src="logo.png" alt="Icon" width="70">
  <div style="display: flex; align-items: center; gap: 10px;">
    <span>netdark_1966</span>
    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
      <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
    </svg>
    <a href="mailto:netdark_1966@op.pl">netdark_1966</a>
    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
    </svg>
    <a href="https://github.com/Darek1966">GitHub — Darek1966</a>
  </div>
</div>

---
