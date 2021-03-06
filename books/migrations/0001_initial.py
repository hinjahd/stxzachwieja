# Generated by Django 3.2.9 on 2021-11-23 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='enter the title', max_length=200)),
                ('author', models.CharField(help_text='name of the author', max_length=200)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('ISBN', models.CharField(help_text='isbn', max_length=200)),
                ('num_of_pages', models.IntegerField()),
                ('image_link', models.ImageField(blank=True, null=True, upload_to='')),
                ('language', models.CharField(help_text='pub lang', max_length=200)),
            ],
        ),
    ]
