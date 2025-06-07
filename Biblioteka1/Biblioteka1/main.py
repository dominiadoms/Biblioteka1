# -*- coding: utf-8 -*-
from books import add_book, list_books, edit_book, delete_book
from students import add_student, list_students, borrow_book, return_book, show_borrowed_report


def main():
    while True:
        print("=== MENU BIBLIOTEKI ===")
        print("1. Dodaj książkę")
        print("2. Wyświetl listę książek")
        print("3. Edytuj książkę")
        print("4. Usuń książkę")
        print("5. Dodaj studenta")
        print("6. Wyświetl studentów")
        print("7. Wypożycz książkę studentowi")
        print("8. Zwrot książki")
        print("9. Raport wypożyczeń")
        print("0. Wyjdź")


        choice = input("Wybierz opcję: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
             edit_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            add_student()
        elif choice == "6":
            list_students()
        elif choice == "7":
            borrow_book()
        elif choice == "8":
            return_book()
        elif choice == "9":
            show_borrowed_report()
        elif choice == "0":
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.\n")

if __name__ == "__main__":
    main()
