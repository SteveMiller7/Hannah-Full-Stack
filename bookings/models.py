from django.db import models
from cloudinary.models import CloudinaryField


class Technician(models.Model):
    title = models.CharField(max_length=40, unique=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)

def __str__(self):
    return self.title
