from django.db import models

# Create your models here.

PRIORITY = {('danger','high'),('info','normal'),('success','low')}

class TodoModel(models.Model):
    # https://qiita.com/nachashin/items/f768f0d437e0042dd4b3
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = PRIORITY
    )
    duedate = models.DateField()

    def __str__(self):
        return self.title
