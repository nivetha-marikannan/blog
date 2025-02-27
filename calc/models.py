from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField() 
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Image Upload Field
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title


    
