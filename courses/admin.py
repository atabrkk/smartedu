from django.contrib import admin
from .models import Course


# Admin Decorator - Admin Paneli Kişiselleştirme
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'available',
    )  # admin sayfasında Courses içinde gözükecek sütunlar
    list_filter = (
        'available',
    )  # filtreleme yapmak için
    search_fields = (
        'name',
        'description',
    )  # arama yapmak için

