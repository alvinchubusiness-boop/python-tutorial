class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def check_out(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        if not self.available:
            self.available = True
            return True
        return False

    def __str__(self):
        status = "Available" if self.available else "Checked out"
        return f'"{self.title}" by {self.author} [{status}]'

class LibraryCatalogue:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        return True

    def list_books(self):
        if not self.books:
            return "No books in the catalogue."
        return "\n".join(f"{i+1}. {book}" for i, book in enumerate(self.books))

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

def main():
    library = LibraryCatalogue()

    library.add_book("Harry Potter", "J.K. Rowling")
    library.add_book("Pride and Prejudice", "Jane Austen")

    print("Initial Catalogue:")
    print(library.list_books())
    print()

    book_to_checkout = library.find_book_by_title("Pride and Prejudice")
    if book_to_checkout:
        if book_to_checkout.check_out():
            print(f'Checked out: {book_to_checkout.title}')
        else:
            print(f'Cannot check out (already checked out): {book_to_checkout.title}')
    print()

    print("Catalogue After Checkout:")
    print(library.list_books())
    print()

    if book_to_checkout:
        if book_to_checkout.return_book():
            print(f'Returned: {book_to_checkout.title}')
        else:
            print(f'Cannot return (already available): {book_to_checkout.title}')
    print()

    print("Final Catalogue:")
    print(library.list_books())

main()
