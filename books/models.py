from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title