from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # nereye gidecek, hangi view fonk. çalışacak, kısayol adı
    # path(route, view, opt(kısayol ismi)

]
