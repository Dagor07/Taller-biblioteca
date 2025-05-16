# Funcion para imprimir con retraso
import time
def imprimir_con_retraso(texto, delay=0.1):
    for letter in texto:
        print(letter, end='', flush=True)
        time.sleep(delay)
    print()

# Cambio solicitado
def show_library():
    print("\n°°° Library °°°\n")
    print("1. Agregar libro")
    print("2. Ver todos los libros")  
    print("3. Buscar libro")
    print("4. Prestar un libro")
    print("5. Devolver un libro")
    print("6. Ver libros prestados")
    print("7. Eliminar libro")
    print("8. Salir de la biblioteca")
    
# Funcion case 3
def menu_search_book():
    print("Buscar libro por autor")
    print("Buscar libro por titulo")
    print("Buscar libro por categoria")




while True:
    show_library()
    option = input("Selecciona una opción (1-8): ")
    if option == "3":
        menu_search_book
        
    if option == "8":
        imprimir_con_retraso("Saliendo de la biblioteca......", 0.1)
        break
    else:
        print("Opción no válida.")
