from django.shortcuts import render


# Create your views here.

# İlgili isteklere buradaki oluşturacağımız fonksiyonlarla beraber geri dönüş yapıyoruz.
# neye karşılık render edeceğiz? = request'e karşılık
# neyi render etmek istiyoruz? = ilgili html sayfası. örnek: index.html
# uygulama içinde index html nasıl bulanacak? = uygulama içi uygulamaadi/templates/uygulamadı/index.html
def index(request):
   return render(request, 'index.html')