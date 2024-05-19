from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.BigIntegerField()
    image = models.ImageField(upload_to='fastfood')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['category']
    
class Saved(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)

  
class Comment(models.Model):   
    author = models.ForeignKey(User, on_delete=models.CASCADE)    
    body = models.CharField(max_length=150)
    date  = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return "Comment of " + str(self.author.username)
