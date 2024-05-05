from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField for automatic primary key generation
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title
