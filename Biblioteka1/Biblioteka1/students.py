# -*- coding: utf-8 -*-
import json
import os
from books import list_books, load_books, save_books

STUDENTS_FILE = "data/students.json"

def load_students():
    if not os.path.exists(STUDENTS_FILE) or os.path.getsize(STUDENTS_FILE) == 0:
        return []
    with open(STUDENTS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_students(students):
    with open(STUDENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4, ensure_ascii=False)

def add_student():
    students = load_students()
    if len(students) >= 15:
        print("⚠️ Osiągnięto limit 15 studentów.")
        return

    name = input("Podaj imię i nazwisko studenta: ")
    students.append({
        "imie": name,
        "wypozyczone": []
    })
    save_students(students)
    print("✅ Student dodany.\n")

def list_students():
    students = load_students()
    if not students:
        print("Brak studentów.\n")
        return
    for i, s in enumerate(students, 1):
        print(f"{i}. {s['imie']} – wypożyczone: {len(s['wypozyczone'])}")
    print()

def borrow_book():
    students = load_students()
    books = load_books()
    if not students:
        print("Brak studentów.\n")
        return

    list_students()
    try:
        student_index = int(input("Podaj numer studenta: ")) - 1
        if student_index < 0 or student_index >= len(students):
            print("Błędny numer studenta.\n")
            return
    except ValueError:
        print("Nieprawidłowy numer.\n")
        return

    student = students[student_index]

    if len(student["wypozyczone"]) >= 5:
        print("⚠️ Ten student wypożyczył już 5 książek.")
        return

    list_books()
    try:
        book_index = int(input("Podaj numer książki do wypożyczenia: ")) - 1
        if book_index < 0 or book_index >= len(books):
            print("Błędny numer książki.\n")
            return
    except ValueError:
        print("Nieprawidłowy numer.\n")
        return

    if int(books[book_index]["ilosc"]) <= 0:
        print("❌ Brak dostępnych egzemplarzy.")
        return

    if book_index in student["wypozyczone"]:
        print("📛 Ten student już wypożyczył tę książkę.")
        return

    student["wypozyczone"].append(book_index)
    books[book_index]["ilosc"] = str(int(books[book_index]["ilosc"]) - 1)

    save_students(students)
    save_books(books)
    print(f"📗 Wypożyczono książkę '{books[book_index]['tytul']}' studentowi {student['imie']}\n")

def return_book():
    students = load_students()
    books = load_books()

    if not students:
        print("Brak studentów.\n")
        return

    list_students()
    try:
        student_index = int(input("Podaj numer studenta: ")) - 1
        if student_index < 0 or student_index >= len(students):
            print("Nieprawidłowy numer studenta.\n")
            return
    except ValueError:
        print("Nieprawidłowy numer.\n")
        return

    student = students[student_index]

    if not student["wypozyczone"]:
        print("Ten student nie ma wypożyczonych książek.\n")
        return

    print(f"\nWypożyczone książki przez {student['imie']}:")
    for i, book_index in enumerate(student["wypozyczone"], 1):
        print(f"{i}. {books[book_index]['tytul']}")

    try:
        return_index = int(input("Podaj numer książki do zwrotu: ")) - 1
        if return_index < 0 or return_index >= len(student["wypozyczone"]):
            print("Nieprawidłowy wybór.\n")
            return
    except ValueError:
        print("To nie jest liczba.\n")
        return

    book_id = student["wypozyczone"].pop(return_index)
    books[book_id]["ilosc"] = str(int(books[book_id]["ilosc"]) + 1)

    save_students(students)
    save_books(books)
    print("✅ Książka została zwrócona.\n")

def show_borrowed_report():
    students = load_students()
    books = load_books()

    print("\n📋 RAPORT – wypożyczone książki:\n")
    empty = True
    for student in students:
        if student["wypozyczone"]:
            empty = False
            print(f"{student['imie']}:")
            for i, book_index in enumerate(student["wypozyczone"], 1):
                print(f"  {i}. {books[book_index]['tytul']} ({books[book_index]['autor']})")
            print()

    if empty:
        print("Brak wypożyczonych książek.\n")
