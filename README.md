# Taller-biblioteca
# Inventario de Libros en Consola

Este proyecto es una aplicación de consola escrita en Python que permite **registrar, prestar, devolver, eliminar y listar libros** utilizando listas y diccionarios, sin necesidad de base de datos.

## Características principales

- Registrar libros con validaciones de datos.
- Listar todos los libros o filtrarlos por estado (Disponible / Prestado).
- Buscar libros por título, autor o categoría.
- Prestar libros (máximo 3 por persona).
- Devolver libros prestados.
- Mostrar libros actualmente prestados.
- Eliminar libros no prestados.
- Menú interactivo en español.

## Estructura del proyecto

```
├── Principal.py        # Menú principal e interacción del usuario
├── Funciones.py        # Lógica de negocio (funciones del sistema)
├── README.md           # Documentación del proyecto
```

## Requisitos

- Python 3.8 o superior

## Cómo ejecutar

1. Clona el repositorio o descarga los archivos.
2. Abre una terminal en el directorio del proyecto.
3. Ejecuta el archivo principal:

```bash
python Principal.py
```

## Archivos clave

- **`Principal.py`**: Controla el menú e interacción con el usuario.
- **`Funciones.py`**: Contiene las funciones `register_book`, `loan_book`, `search_books`, `show_books`, etc.
- **`books`**: Lista global que almacena los libros como diccionarios.

## Ejemplo de un libro registrado

```python
{
    "id": 1,
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "año": 1967,
    "categoria": "Ficción",
    "estado": "Disponible"
}
```

Si un libro es prestado, se agrega:

```python
"prestamo": {
    "nombre": "Juan Pérez",
    "fecha": "2025-05-19"
}
```

