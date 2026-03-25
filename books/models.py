from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    cover_image = models.ImageField(upload_to='book_covers/',null=True,blank=True)

    def __str__(self):
        return self.title

