# -*- coding: utf-8 -*-
import json
import os

BOOKS_FILE = "data/books.json"

def load_books():
    if not os.path.exists(BOOKS_FILE) or os.path.getsize(BOOKS_FILE) == 0:
        return []
    with open(BOOKS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

def add_book():
    title = input("Tytuł: ")
    author = input("Autor: ")
    year = input("Rok wydania: ")
    pages = input("Ilość stron: ")
    quantity = input("Ilość egzemplarzy: ")

    book = {
        "tytul": title,
        "autor": author,
        "rok": year,
        "strony": pages,
        "ilosc": quantity
    }

    books = load_books()
    books.append(book)
    save_books(books)
    print("📚 Książka dodana!\n")

def list_books():
    books = load_books()
    if not books:
        print("Brak książek w bazie.\n")
        return
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['tytul']} – {book['autor']} ({book['rok']}), {book['strony']} stron, dostępnych: {book['ilosc']}")
    print()
    
def edit_book():
    books = load_books()
    list_books()

    if not books:
        return

    try:
        index = int(input("Podaj numer książki do edycji: ")) - 1
        if index < 0 or index >= len(books):
            print("Nieprawidłowy numer.\n")
            return
    except ValueError:
        print("To nie jest liczba.\n")
        return

    book = books[index]

    print(f"\nEdycja książki: {book['tytul']}")

    book["tytul"] = input(f"Nowy tytuł [{book['tytul']}]: ") or book["tytul"]
    book["autor"] = input(f"Nowy autor [{book['autor']}]: ") or book["autor"]
    book["rok"] = input(f"Nowy rok wydania [{book['rok']}]: ") or book["rok"]
    book["strony"] = input(f"Nowa liczba stron [{book['strony']}]: ") or book["strony"]
    book["ilosc"] = input(f"Nowa ilość egzemplarzy [{book['ilosc']}]: ") or book["ilosc"]

    save_books(books)
    print("📘 Książka zaktualizowana!\n")
    
def delete_book():
    books = load_books()
    list_books()

    if not books:
        return

    try:
        index = int(input("Podaj numer książki do usunięcia: ")) - 1
        if index < 0 or index >= len(books):
            print("Nieprawidłowy numer.\n")
            return
    except ValueError:
        print("To nie jest liczba.\n")
        return

    confirm = input(f"Czy na pewno chcesz usunąć '{books[index]['tytul']}'? (t/n): ")
    if confirm.lower() == "t":
        removed = books.pop(index)
        save_books(books)
        print(f"❌ Usunięto książkę: {removed['tytul']}\n")
    else:
        print("Anulowano.\n")

