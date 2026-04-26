from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    # Cambiado para aceptar archivos
    image = models.ImageField(upload_to='book_covers/') 
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title