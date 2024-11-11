from django.db import models


class Category(models.Model):
    image = models.ImageField(upload_to='category-images/')
    name = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return f"Category - {self.name}"
    
    
class Author(models.Model):
    image = models.ImageField(upload_to='author-images/')
    full_name = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return self.full_name
    
class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=128)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.CharField(max_length=128)
    email = models.EmailField()
    text = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.username