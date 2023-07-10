from django.db import models

# Course ve Category Arasındaki İlişki
"""
Her Category'de birden daha fazla Course olabilir.
Ancak bir Course yalnızca bir Category içerisinde bulunacaktır.
Buna One To Many(Many To One) ilişkisi denir.
"""


# Parent Class
class Category(models.Model):
    name = models.CharField(max_length=50, null=True)  # null=True -> boş olsada hata verme demektir. sonradan Category model oluşturduğumuz için bunu ayarladık.
    slug = models.SlugField(max_length=50, unique=True, null=True)  # slug URL'de görünen ifadenin daha anlamlı görünmesi için kullandığımız bir alandır.

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name


# Child Class
class Course(models.Model):
    name = models.CharField(max_length=200, unique=True)  # verbose_name: admin alanında gözükürken nasıl gözükeceği. help_text: admin kısmında kullancığa açıklayıcı bilgi.
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)  # Category silindiği zaman Course olduğu gibi kalsın birşey yapılmasın.
    tags = models.ManyToManyField(Tag, blank=True, null=True)  # Course model içinde tagler diye alan oluşturduk. Bu tags Tag modelindekileri gösterecektir.
    description = models.TextField(blank=True)  # blank:True-> son kullanıcı açısından boş olabilir. null:True-> dev açısından boş olabilir.
    image = models.ImageField(upload_to="courses/%Y/%m/%d/", default="courses/default_course_image.jpg")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name