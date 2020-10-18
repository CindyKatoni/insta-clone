from django.db import models

# Create your models here.
class Profile(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True)