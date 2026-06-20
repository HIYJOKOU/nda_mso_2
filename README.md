# NDA_MSO-2

Prosty projekt Python przygotowany w ramach ćwiczenia dotyczącego organizacji repozytorium, testów, lintowania oraz GitHub Actions.

## Wymagania

* Python 3.11+
* Git

## Instalacja

Utworzenie środowiska i instalacja zależności:

```bash
python scripts/create_venv.py
```

Aktywacja środowiska (Windows):

```powershell
.\.venv\Scripts\activate
```

## Testy

```bash
python scripts/test.py
```

## Formatowanie kodu

Formatowanie:

```bash
python scripts/format.py
```

Sprawdzenie formatowania:

```bash
python scripts/format_check.py
```

## Lint

```bash
python scripts/lint.py
```

## Czyszczenie projektu

```bash
python scripts/clean.py
```

## CI

Projekt wykorzystuje GitHub Actions.

Pipeline automatycznie:

* instaluje zależności,
* sprawdza formatowanie kodu,
* uruchamia linting,
* uruchamia testy.

Workflow uruchamia się przy pushach oraz Pull Requestach do gałęzi `main` i `develop`.
