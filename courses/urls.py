from django.urls import path
from . import views


urlpatterns = [
    path('', views.course_list, name="courses"),  # nereye gidecek, hangi view fonk. çalışacak, kısayol adı (http://127.0.0.1:8000/courses/)
    path('<slug:category_slug>/<int:course_id>', views.course_detail, name="course_detail"),  # tekil course sayfasına yönlendirme. (http://127.0.0.1:8000/courses/category-name/course_id)(http://127.0.0.1:8000/courses/web-programming/3)
    path('categories/<slug:category_slug>', views.category_detail, name='courses_by_category')  # Category göre Course listeler. http://127.0.0.1:8000/courses/categories/web-programming

]
