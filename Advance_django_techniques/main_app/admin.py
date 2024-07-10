from django.contrib import admin
from main_app.models import RestaurantReview


# Register your models here.
@admin.register(RestaurantReview)
class AuthorAdmin(admin.ModelAdmin):
    pass
