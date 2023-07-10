# Generated by Django 4.2.3 on 2023-07-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_category_course_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
    ]
