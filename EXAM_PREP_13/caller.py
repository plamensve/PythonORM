import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import VideoGame, BillingInfo, Invoice, Technology, Project, Programmer

# Execute the "get_programmers_with_technologies" method for a specific project
specific_project = Project.objects.get(name="Web App Project")
programmers_with_technologies = specific_project.get_programmers_with_technologies()

# Iterate through the related programmers and technologies
for programmer in programmers_with_technologies:
    print(f"Programmer: {programmer.name}")
    for technology in programmer.projects.get(name="Web App Project").technologies_used.all():
        print(f"- Technology: {technology.name}")

# Execute the "get_projects_with_technologies" method for a specific programmer
specific_programmer = Programmer.objects.get(name="Alice")
projects_with_technologies = specific_programmer.get_projects_with_technologies()

# Iterate through the related projects and technologies
for project in projects_with_technologies:
    print(f"Project: {project.name} for {specific_programmer.name}")
    for technology in project.technologies_used.all():
        print(f"- Technology: {technology.name}")
