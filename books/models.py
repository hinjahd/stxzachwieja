from django.db import models
import datetime

class Books(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, help_text="enter the title")
    author = models.CharField(max_length=200, help_text="name of the author")
    pub_date = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=200, help_text="isbn")
    num_of_pages = models.IntegerField(null=True, blank=True)
    image_link = models.CharField(max_length=200, help_text="link")
    language = models.CharField(max_length=200, help_text="pub lang")

    def __str__(self):
        return self.title