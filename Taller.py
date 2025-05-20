#from Funcions import *
import os
import time
os.system("cls" if os.name == "nt" else "clear")
def imprimir_con_retraso(texto, delay=0.1):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(delay)
    print()

def show_library():
    print("\n°°° Library °°°\n")
    print("1. Agregar libro")
    print("2. Ver todos los libros")  
    print("3. Buscar libro")
    print("4. Prestar un libro")
    print("5. Ver libros prestados")
    print("6. Devolver un libro")
    print("7. Eliminar libro")
    print("8. Salir de la biblioteca")

while True:
    show_library()
    option = input("Selecciona una opción (1-8): ")

    if option == "1":
        register_book()

    elif option == "2":
        flag = True
        while flag:
            try:
                print("1. Mostrar todos los libros.")
                print("2. Filtrar por estado (Disponible)")
                print("3. Filtrar por estado (Prestado)")
                filter_opt = int(input("Elija una opción: ").strip())
                if filter_opt == 1:
                    show_books(books)
                    flag = False
                elif filter_opt == 2:
                    show_books(books, "Disponible")
                    flag = False
                elif filter_opt == 3:
                    show_books(books, "Prestado")
                    flag = False
                else:
                    print("\nError: Ingresa una opción entre 1 y 3.\n")
            except ValueError:
                print("\nError: Debes ingresar un número.\n")

    elif option == "3":
        query = input("Ingrese título, autor o categoría a buscar: ")
        search_books(books, query)

    elif option == "4":
        loan_book()

    elif option == "5":
        show_loan_books(books)

    elif option == "6":
        to_return_a_book()

    elif option == "7":
        delete_book()

    elif option == "8":
        imprimir_con_retraso("Saliendo de la biblioteca......", 0.1)
        break

    else:
        print("Opción inválida. Intenta de nuevo.")
