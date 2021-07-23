from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.utils import timezone

class Category(models.Model):
    name=models.CharField(max_length=50)

    class Meta:
        verbose_name=('category')
        verbose_name_plural=('categories')

    def __str__(self):
        return self.name


class TodoList(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=100)
    created=models.DateField(default=timezone.now().strftime('%Y-%m-%d'))
    due_date=models.DateField(default=timezone.now().strftime('%Y-%m-%d'))
    category=models.ForeignKey(Category,on_delete=CASCADE)
