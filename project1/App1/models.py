from django.db import models

# Create your models here.
# import the standard Django Model
# from built-in library

from datetime import datetime

class GeeksModel(models.Model):

    # Field Names
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to="images/%Y/%m/%d")

    # rename the instances of the model
    # with their title name
    def __str__(self) -> str:
        return self.title
    



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, null = True)  # New field with default value
    summary = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title



