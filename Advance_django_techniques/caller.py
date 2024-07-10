import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


# from main_app.models import Restaurant, RestaurantReview
# from django.core.exceptions import ValidationError
#
# restaurant1 = Restaurant.objects.create(name="Restaurant A", location="123 Main St.", description="A cozy restaurant", rating=4.88)
# restaurant2 = Restaurant.objects.create(name="Restaurant B", location="456 Elm St.",  description="Charming restaurant", rating=3.59)
#
# RestaurantReview.objects.create(reviewer_name="Bob", restaurant=restaurant1, review_content="Good experience overall.", rating=4)
# RestaurantReview.objects.create(reviewer_name="Aleks", restaurant=restaurant1, review_content="Great food and service!", rating=5)
# RestaurantReview.objects.create(reviewer_name="Charlie", restaurant=restaurant2, review_content="It was ok!", rating=2)
#
# duplicate_review = RestaurantReview(reviewer_name="Aleks", restaurant=restaurant1, review_content="Another great meal!", rating=5)
#
# try:
#     duplicate_review.full_clean()
#     duplicate_review.save()
# except ValidationError as e:
#     print(f"Validation Error: {e}")
#
#
# print("All Restaurant Reviews:")
# for review in RestaurantReview.objects.all():
#     print(f"Reviewer: {review.reviewer_name}, Rating: {review.rating}, Restaurant: {review.restaurant.name}")



