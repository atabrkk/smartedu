from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200, unique=True)  # verbose_name: admin alanında gözükürken nasıl gözükeceği. help_text: admin kısmında kullancığa açıklayıcı bilgi.
    description = models.TextField(blank=True)  # blank:True-> son kullanıcı açısından boş olabilir. null:True-> dev açısından boş olabilir.
    image = models.ImageField(upload_to="courses/%Y/%m/%d/", default="courses/default_course_image.jpg")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name