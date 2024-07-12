import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.core.exceptions import ValidationError

from main_app.models import Book

# from django.core.exceptions import ValidationError
#
# from main_app.models import Customer
#
# customer = Customer(
#     name="Svetlin Nakov1",
#     age=1,
#     email="nakov@example",
#     phone_number="+35912345678",
#     website_url="htsatps://nakov.com/"
# )
#
# try:
#     customer.full_clean()
#     customer.save()
#
# except ValidationError as e:
#     print('\n'.join(e.messages))
# book = Book(
#     title="Short Title",
#     description="A book with a short title.",
#     genre="Fiction",
#     author="A",
#     isbn="1234"
# )
#
# try:
#     book.full_clean()
#     book.save()
#
# except ValidationError as e:
#     print("Validation Error for Book:")
#     for field, errors in e.message_dict.items():
#         print(f"{field}: {', '.join(errors)}")
