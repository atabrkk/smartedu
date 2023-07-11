from django.shortcuts import render
from .models import Course, Category, Tag  # modelleri içeri aktardık


# Tüm Kurslar
def course_list(request):
    courses = Course.objects.all().order_by('-date')  # tüm kursları getirdik. date göre sıraladık. '-date': en son geleni en once getirir.
    categories = Category.objects.all()  # tüm Category'leri getirdik
    tags = Tag.objects.all()
    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags

    }  # farklı bilgileride courses.html'de kullanmamız için sözlük içine atarız ve sözlük olarak göndeririz.
    return render(request, 'courses.html', context)  # courses.html yönlendirir


# Tekil Kurs
def course_detail(request, category_slug, course_id):  # ekstra iki parametre daha alacaktır
    course = Course.objects.get(category__slug=category_slug, id=course_id)
    # Course modelinden category_slug ulaşmak için. category__slug (iki alt çizgi koyma sebebi: Course modeli içindeki category'nin (F.K'deki Category) slug'a ilerlemek için iki alt çizgi koyarız.
    # course.category.slug = category__slug (query sette __ (iki alt çizgi) kullanılır.
    # Category: Parent class / Course: Child class. child classtan parent classa ulaşmak için iki alt çizgi kullanılır.
    # id: Course tablosuna ait olan id'dir.
    context = {
        'course': course
    }
    return render(request, 'course.html', context)  # course.html yönlendirir


def category_list(request, category_slug):  # category_slug:URL'den gelen slug
    courses = Course.objects.all().filter(category__slug=category_slug)  # Course tablosundan Categoryye ulaştık.
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'courses.html', context)  # courses.html gidip courseları getirir.


def tag_list(request, tag_slug):
    courses = Course.objects.all().filter(tags__slug=tag_slug)  # Course tablosundan Tag'e ulaşştık
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'courses.html', context)  # courses.html gidip courseları getirir.