from django.forms import ModelForm
from .models import Books


class booksForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        help_texts = {
            'title': '',
            'author':'',
            'pub_date':'',
            'ISBN':'',
            'num_of_pages':'',
            'image_link':'',
            'language':'',
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if not title:
            return title

        if not title[0].isupper():
            self.add_error("title", "Should start with an uppercase letter")

        if title.endswith("."):
            self.add_error("title", "Should not end with a full stop")

        if "&" in title:
            self.add_error("title", "Use 'and' instead of '&'")

        return title