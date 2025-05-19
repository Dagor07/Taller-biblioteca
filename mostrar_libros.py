
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
            title = str(book["titulo"]).capitalize()
            author = str(book["autor"]).title()
            year = str(book["año"])
            category = str(book["categoria"]).capitalize()
            condition = str(book["estado"]).capitalize()
            print(f"{id.center(10)}|{title.center(25)}|{author.center(25)}|{year.center(20)}|{category.center(15)}|{condition.center(15)}")
            print("-"*115)
    if not found and filter:
        print(f"\nNo se encontraron libros con estado '{filter}'.\n")
    elif not found and filter is None:
         print("No hay libros registrados.")




def search_book(books, search):
    
    print("*"*115)
    print(f"\n{"ID".center(10)}|{"Titulo del libro".center(25)}|{"Autor".center(25)}|{"Año".center(20)}|{"Categoria".center(15)}|{"Estado".center(15)}")
    print("*"*115)
    found  = False
    search = search.lower()
    for book in books:
        title = book["titulo"]
        author = book["autor"]
        category = book["categoria"]
        if search in title or search in author or search in category:
            found  = True
            id = str(book["id"])
            title = str(book["titulo"]).capitalize()
            author = str(book["autor"]).title()
            year = str(book["año"])
            category = str(book["categoria"]).capitalize()
            condition = str(book["estado"]).capitalize()
          
            print(f"{id.center(10)}|{title.center(25)}|{author.center(25)}|{year.center(20)}|{category.center(15)}|{condition.center(15)}")
            print("-"*115)
    if not found:
        print("No se encontraron libros que coincidan con la búsqueda.")
        
