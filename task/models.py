from django.db import models
from category.models import Category
# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateTimeField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
