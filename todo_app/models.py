from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50,null=False)
    todo = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.title
