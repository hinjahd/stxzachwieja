# Generated by Django 3.2.9 on 2021-11-27 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_books_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='num_of_pages',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
