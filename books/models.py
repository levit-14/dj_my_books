from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    image = models.URLField(max_length=2000) # O models.ImageField si prefieres archivos locales
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    # Relación uno a muchos
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title