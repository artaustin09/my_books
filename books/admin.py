from django.contrib import admin
from .models import Book, Category

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')
    search_fields = ['title', 'author']
    list_filter = ['category', 'created_at']

admin.site.register(Book, BookAdmin)
admin.site.register(Category)