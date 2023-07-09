from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # ilgili url dosyasına gönderir.
    path('courses/', include('courses.urls'))  # url kısmına courses yazıldığı zaman courses.urls içerisine gider.

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # media'ya yüklenen(media klasörü app dışı olacaktır) url'lere ulaşmak için
