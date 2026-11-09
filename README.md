# M450 LU04.A01 - Library

Erstelle die vollständigen Unittests für die Library-Applikation. Wende dabei
alles aus den Learning Units 03 und 04 an.

Wiki: <https://wiki.bzz.ch/modul/m450/learningunits/lu04/aufgaben/kombiniert>

## Ausgangslage

Die Applikation besteht aus den Klassen `Book`, `Customer`, `Librarian` und
`Library`. Zu jeder Klasse gibt es ein Testmodul:

| Klasse | Testmodul |
| --- | --- |
| `book.py` | `test_book.py` (Testfunktionen vorbereitet) |
| `library.py` | `test_library.py` |
| `customer.py` | `test_customer.py` |
| `librarian.py` | `test_librarian.py` |
| `main.py` | `main_test.py` (`test_main` vorbereitet) |

Der Programmcode ist vorgegeben und muss **nicht** verändert werden.

## Auftrag

1. Ergänze die Testfunktionen in `test_book.py` und schreibe die Tests für
   `Library` in `test_library.py` – die einzelnen Situationen sind im Wiki
   beschrieben. Prüfe nicht nur den korrekten Ablauf, sondern erzeuge auch
   Fehler und Exceptions. Objekte, die mehrere Tests brauchen, erstellst du in
   `fixture`s.
2. Definiere nach demselben System die Tests für `Customer` und `Librarian`.
3. Teste zuletzt die Funktion `main` in `main_test.py`.

## Lokal testen

```bash
pip install -r requirements.txt
pytest
python _run_pylint.py
```

## Bewertung

| Teil | Punkte |
| --- | --- |
| Unittests (`test_main` und die fünf Tests in `test_book.py`) | 6 |
| Linting der vier Testmodule `test_*.py` | 3 |
| **Total** | **9** |

## Abgabe

Die Abgabe erfolgt durch den Push ins GitHub-Repository. Jeder Push wird
automatisch bewertet.
