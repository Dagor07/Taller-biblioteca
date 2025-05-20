import datetime

books = []
id_counter = 1
loans_per_person = {}

def generate_id():
    global id_counter
    new_id = id_counter
    id_counter += 1
    return new_id

def validate_entry(texto, tipo=int, condiciones=None):
    while True:
        valor = input(texto)
        if not valor.strip():
            print("El campo no puede estar vacío.")
            continue
        try:
            if tipo == int:
                valor = int(valor)
            if condiciones and not condiciones(valor):
                print("Valor fuera de rango o inválido.")
                continue
            return valor
        except:
            print("Formato inválido.")

def register_book():
    titulo = input("Título: ").strip().lower()
    autor = input("Autor: ").strip().lower()
    año = validate_entry("Año de publicación: ", int, lambda x: 1500 <= x <= datetime.date.today().year)
    categoria = input("Categoría Exactamente (Ficción, No Ficción, Infantil, Educativo): ").strip()
    if categoria not in ['Ficción', 'No Ficción', 'Infantil', 'Educativo']:
        print("Categoría inválida.")
        return
    libro = {
        "id": generate_id(),
        "title": titulo,
        "author": autor,
        "year": año,
        "category": categoria,
        "status": "Disponible"
    }
    books.append(libro)
    print(" Libro registrado correctamente.")



def loan_book():
    id_libro = validate_entry("ID del libro a prestar: ")
    book = next((l for l in books if l["id"] == id_libro), None)
    if not book:
        print("Libro no encontrado.")
        return
    if book["status"] == "Prestado":
        print("El libro ya está prestado.")
        return
    nombre = input("Nombre de quien presta: ").strip()
    if loans_per_person.get(nombre, 0) >= 3:
        print("No puede prestar más de 3 libros.")
        return
    book["status"] = "Prestado"
    book["prestamo"] = {
        "nombre": nombre,
        "fecha": str(datetime.date.today())
    }
    loans_per_person[nombre] = loans_per_person.get(nombre, 0) + 1
    print(" Libro prestado correctamente.")
    
def show_books(books, filter = None):
    print(f"{"****Listado de libros****"}".rjust(60))
    print("*"*115)
    print(f"\n{"ID".center(10)}|{"Titulo del libro".center(25)}|{"Autor".center(25)}|{"Año de publicacion".center(20)}|{"Categoria".center(15)}|{"Estado".center(15)}")
    print("*"*115)
    found = False
    for book in books:
        if filter is None or book["estado"] == filter:
            found = True

            id = str(book["id"])
            title = str(book["title"]).capitalize()
            author = str(book["author"]).title()
            year = str(book["year"])
            category = str(book["category"]).capitalize()
            condition = str(book["status"]).capitalize()
            print(f"{id.center(10)}|{title.center(25)}|{author.center(25)}|{year.center(20)}|{category.center(15)}|{condition.center(15)}")
            print("-"*115)
    if not found and filter:
        print(f"\nNo se encontraron libros con estado '{filter}'.\n")
    elif not found and filter is None:
         print("No hay libros registrados.")





def search_books(book_list, query):
    print("*" * 115)
    print(f"\n{'ID'.center(10)}|{'Título'.center(25)}|{'Autor'.center(25)}|{'Año'.center(20)}|{'Categoría'.center(15)}|{'Estado'.center(15)}")
    print("*" * 115)
    found = False
    query = query.lower()
    for book in book_list:
        title = book["title"].lower()
        author = book["author"].lower()
        category = book["category"].lower()
        if query in title or query in author or query in category:
            found = True
            id_str = str(book["id"])
            title = book["title"].capitalize()
            author = book["author"].title()
            year = str(book["year"])
            category = book["category"].capitalize()
            status = book["status"].capitalize()
            print(f"{id_str.center(10)}|{title.center(25)}|{author.center(25)}|{year.center(20)}|{category.center(15)}|{status.center(15)}")
            print("-" * 115)
    if not found:
        print("No se encontraron libros que coincidan con la búsqueda.")
        
def show_loan_books(books):
    print("\n--- Libros Actualmente Prestados ---")
    if not books:
        print("No hay libros registrados.")
        return
    
    print("*"*115)
    print(f"\n{"ID".center(10)}|{"Titulo del libro".center(25)}|{"Autor".center(25)}|{"Año de publicacion".center(20)}|{"Categoria".center(15)}|{"Estado".center(15)}|{"Prestamo".center(25)}")
    print("*"*115)

    for book in books:
        if book["status"] == "prestado":
            for loan in book:
                if "prestamo" in loan:                   
                    id = str(book["id"])
                    title = str(book["title"]).capitalize()
                    author = str(book["author"]).title()
                    year = str(book["year"])
                    category = str(book["category"]).capitalize()
                    condition = str(book["status"]).capitalize()
                    print(f"{id.center(10)}|{title.center(25)}|{author.center(25)}|{year.center(20)}|{category.center(15)}|{condition.center(15)}{str(book['prestamo']['nombre']).center(25)}|{str(book['prestamo']['fecha']).center(25)}")
                    print("-"*115)
            if book["status"] != "prestado":
                print("No hay libros actualmente prestados.")
                return
        
def to_return_a_book():
    if not loan_book:
        print("No tienes libros para devolver.")
        return
    print("\nLibros que puedes devolver:")
    show_books(loan_book)
    try:
        opcion = int(input("Elige el número del libro que deseas devolver: ")) - 1
        if 0 <= opcion < len(loan_book):
            libro = loan_book.pop(opcion)
            libro["disponible"] = True
            print(f"Has devuelto: '{libro['title']}'")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Entrada no válida.")
        
def delete_book(books, title):
    if not books:
        print("La lista de libros está vacía.")
        return
    
    if not title:
        print("Debes ingresar el título del libro a eliminar.")
        return
    
    found_book = next((book for book in books if book['title'].lower() == title.lower()), None)
    
    if found_book:
        books.remove(found_book)
        print(f"Libro '{title}' eliminado con éxito.")
    else:
        print(f"No se encontró el libro '{title}' en la lista.")
