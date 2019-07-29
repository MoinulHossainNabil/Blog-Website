from django.contrib import admin
from .models import Author, Category, Posts, Comments
# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Posts)
admin.site.register(Comments)
