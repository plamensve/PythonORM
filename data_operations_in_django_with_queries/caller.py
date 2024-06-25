import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Run and print your queries

from main_app.models import Student

"""
FC5204	John	Doe	15/05/1995	john.doe@university.com
FE0054	Jane	Smith	null	jane.smith@university.com
FH2014	Alice	Johnson	10/02/1998	alice.johnson@university.com
FH2015	Bob	Wilson	25/11/1996	bob.wilson@university.com

"""


def add_students():
    student1 = Student(
        student_id='FC5204',
        first_name='John',
        last_name='Doe',
        birth_date='1995-05-15',
        email='john.doe@university.com'
    )
    student1.save()

    student2 = Student(
        student_id='FE0054',
        first_name='Jane',
        last_name='Smith',
        birth_date=None,
        email='jane.smith@university.com'
    )
    student2.save()

    student3 = Student(
        student_id='FH2014',
        first_name='Alice',
        last_name='Johnson',
        birth_date='1998-02-10',
        email='alice.johnson@university.com'
    )
    student3.save()

    Student.objects.create(
        student_id='FH2015',
        first_name='Bob',
        last_name='Wilson',
        birth_date='1996-11-25',
        email='bob.wilson@university.com'
    )


# add_student()
for n in Student.objects.all():
    print(n.first_name)
