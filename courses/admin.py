from django.contrib import admin
from .models import Course, Category, Tag


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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)  # slug alanını name alanından alır ve otomatik slug oluşturur.
    }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)  # slug alanını name alanından alır ve otomatik slug oluşturur.
    }
