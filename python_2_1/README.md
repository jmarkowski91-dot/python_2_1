# Ćwiczenia praktyczne 1 – eksperymenty z kontekstem

## Struktura

```
.
├── main.py                  # uruchamia wszystkie ćwiczenia
├── pyproject.toml
├── src/
│   └── kontekst/
│       ├── __init__.py
│       ├── logger.py        # 1. Logger
│       ├── file_writer.py   # 2-3. FileWriter
│       └── safe_division.py # 4. SafeDivision
└── tests/
    └── test_kontekst.py
```

## Uruchomienie

```bash
python src/main.py
```

## Testy

```bash
pip install pytest
pytest
```
