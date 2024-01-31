from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15,null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10,null=True)
    type = models.CharField(max_length=15,null=True)
    def _str_(self):
        return self.user.username
 
class GraphicSoftware(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.name
    
    
# Model for categories
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    
#model for Cards
class Card(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    image = models.ImageField(upload_to='card_images/', blank=True, null=True)

    def __str__(self):
        return self.title


#model for feedback form
class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    site = models.URLField()
    image = models.ImageField(upload_to='feedback_images/', blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.email