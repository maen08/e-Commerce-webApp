from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()
    description = models.TextField()
    
    def __str__(self):
        return self.name
    

