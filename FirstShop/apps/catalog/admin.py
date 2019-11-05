from django.contrib import admin

from apps.catalog.models import Genre, Book, Author, Language

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Language)
