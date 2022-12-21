from django.db import models

class Post(models.Model):
    item = models.CharField(max_length=100)
    price = models.TextField()
    desc= models.TextField()
    def __str__(self):
        return self.item

