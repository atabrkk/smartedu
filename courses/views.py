from django.shortcuts import render
from .models import Course  # Course modeli içeri aktardık


def course_list(request):
    courses = Course.objects.all().order_by('-date')  # tüm kursları getirdik. date göre sıraladık. '-date': en son geleni en once getirir.
    context = {
        'courses': courses

    }  # farklı bilgileride courses.html'de kullanmamız için sözlük içine atarız ve sözlük olarak göndeririz.
    return render(request, 'courses.html', context)  # courses.html yönlendirir