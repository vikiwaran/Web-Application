from django.contrib import admin
from .models import Faculty_information
from faculty.models import Book_published
from faculty.models import Chapters
from faculty.models import Conference
from faculty.models import Journals

# Register your models here.
admin.site.register(Faculty_information)
admin.site.register(Journals)
admin.site.register(Conference)
admin.site.register(Book_published)
admin.site.register(Chapters)
