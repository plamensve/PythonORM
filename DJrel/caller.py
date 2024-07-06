import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book


def show_all_authors_with_their_books():
    authors = Author.objects.all().order_by('id')

    result = []

    for a in authors:
        books = a.book_set.all()

        if not books:
            continue

        books_title = [b.title for b in books]
        result.append(f"{a.name} has written - {', '.join(books_title)}!")

    return '\n'.join(result)


def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()


# # Create authors
# author1 = Author.objects.create(name="J.K. Rowling")
# author2 = Author.objects.create(name="George Orwell")
# author3 = Author.objects.create(name="Harper Lee")
# author4 = Author.objects.create(name="Mark Twain")
#
# # Create books associated with the authors
# book1 = Book.objects.create(
#     title="Harry Potter and the Philosopher's Stone",
#     price=19.99,
#     author=author1
# )
# book2 = Book.objects.create(
#     title="1984",
#     price=14.99,
#     author=author2
# )
#
# book3 = Book.objects.create(
#     title="To Kill a Mockingbird",
#     price=12.99,
#     author=author3
# )
#
# Display authors and their books
authors_with_books = show_all_authors_with_their_books()
print(authors_with_books)

# Delete authors without books
delete_all_authors_without_books()
print(Author.objects.count())
