class Book:
    def __init__(self, title, author, category, isbn):
        """
        Inicializa un libro con los parámetros proporcionados: título, autor, categoría e ISBN.
        Se utilizan tuplas para el título y el autor, ya que estos son valores inmutables.
        """
        self.title = title
        self.author = author
        self.category = category
        self.isbn = isbn

    def __str__(self):
        """
        Genera una representación legible del libro para su impresión.
        """
        return f"'{self.title}' por {self.author} - Categoría: {self.category} (ISBN: {self.isbn})"


class Member:
    def __init__(self, name, user_id):
        """
        Inicializa un miembro con un nombre, ID único de usuario y una lista vacía de libros prestados.
        """
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def __str__(self):
        """
        Representación en cadena del miembro de la biblioteca.
        """
        return f"Miembro: {self.name} (ID: {self.user_id})"

    def borrow_book(self, book):
        """
        Permite al miembro tomar prestado un libro.
        """
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
            print(f"¡{self.name} ha tomado prestado '{book.title}'!")
        else:
            print(f"Ya has tomado '{book.title}' prestado, {self.name}.")

    def return_book(self, book):
        """
        Permite al miembro devolver un libro.
        """
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.name} ha devuelto '{book.title}'.")
        else:
            print(f"El libro '{book.title}' no está en tus libros prestados, {self.name}.")

    def list_borrowed_books(self):
        """
        Muestra todos los libros que el miembro tiene actualmente prestados.
        """
        if self.borrowed_books:
            print(f"{self.name} tiene los siguientes libros prestados:")
            for book in self.borrowed_books:
                print(f"- {book.title}")
        else:
            print(f"{self.name} no tiene libros prestados actualmente.")


class Library:
    def __init__(self):
        """
        Inicializa una biblioteca vacía, con diccionario para los libros y conjunto para los miembros.
        """
        self.books = {}
        self.members = set()

    def add_book(self, book):
        """
        Añade un libro a la colección de la biblioteca.
        """
        if book.isbn not in self.books:
            self.books[book.isbn] = book
            print(f"Libro '{book.title}' añadido a la biblioteca.")
        else:
            print(f"El libro '{book.title}' ya está en nuestra colección.")

    def remove_book(self, isbn):
        """
        Elimina un libro de la biblioteca según su ISBN.
        """
        if isbn in self.books:
            removed_book = self.books.pop(isbn)
            print(f"El libro '{removed_book.title}' ha sido eliminado de la biblioteca.")
        else:
            print("No se ha encontrado un libro con ese ISBN.")

    def register_member(self, member):
        """
        Registra un nuevo miembro en la biblioteca.
        """
        if member.user_id not in {m.user_id for m in self.members}:
            self.members.add(member)
            print(f"Miembro {member.name} registrado exitosamente.")
        else:
            print(f"Ya existe un miembro con el ID {member.user_id}.")

    def unregister_member(self, user_id):
        """
        Da de baja a un miembro de la biblioteca.
        """
        member_to_remove = None
        for member in self.members:
            if member.user_id == user_id:
                member_to_remove = member
                break

        if member_to_remove:
            self.members.remove(member_to_remove)
            print(f"Miembro {member_to_remove.name} dado de baja.")
        else:
            print("No se ha encontrado un miembro con ese ID.")

    def lend_book(self, user_id, isbn):
        """
        Presta un libro a un miembro de la biblioteca.
        """
        member = next((m for m in self.members if m.user_id == user_id), None)
        book = self.books.get(isbn)

        if member and book:
            member.borrow_book(book)
        else:
            print("No se ha encontrado el miembro o el libro.")

    def return_book(self, user_id, isbn):
        """
        Permite que un miembro devuelva un libro prestado.
        """
        member = next((m for m in self.members if m.user_id == user_id), None)
        book = self.books.get(isbn)

        if member and book:
            member.return_book(book)
        else:
            print("No se ha encontrado el miembro o el libro.")

    def search_books(self, search_type, query):
        """
        Busca libros en la biblioteca según un tipo de búsqueda (por título, autor o categoría).
        """
        result = []
        for book in self.books.values():
            if (search_type == 'title' and query.lower() in book.title.lower()) or \
               (search_type == 'author' and query.lower() in book.author.lower()) or \
               (search_type == 'category' and query.lower() in book.category.lower()):
                result.append(book)

        if result:
            print("Libros encontrados:")
            for book in result:
                print(book)
        else:
            print("No se han encontrado libros que coincidan con la búsqueda.")

    def list_all_borrowed_books(self):
        """
        Muestra todos los libros prestados por todos los miembros de la biblioteca.
        """
        for member in self.members:
            member.list_borrowed_books()


# Ejemplo de uso

# Crear una biblioteca
library = Library()

# Crear algunos libros
book1 = Book("Cien años de soledad", "Gabriel García Márquez", "Novela", "978-3-16-148410-0")
book2 = Book("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", "978-3-16-148411-7")
book3 = Book("1984", "George Orwell", "Distopía", "978-3-16-148412-4")

# Agregar los libros a la biblioteca
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Crear algunos miembros
member1 = Member("Ana Pérez", "M001")
member2 = Member("Luis Gómez", "M002")

# Registrar los miembros en la biblioteca
library.register_member(member1)
library.register_member(member2)

# Prestar libros a los miembros
library.lend_book("M001", "978-3-16-148410-0")
library.lend_book("M002", "978-3-16-148412-4")

# Buscar libros
library.search_books('title', '1984')

# Listar libros prestados
library.list_all_borrowed_books()

# Devolver libros
library.return_book("M001", "978-3-16-148410-0")

# Listar libros prestados después de la devolución
library.list_all_borrowed_books()
