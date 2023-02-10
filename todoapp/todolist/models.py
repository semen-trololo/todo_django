from django.db import models

# Create your models here.

class todo_model(models.Model):
    title = models.CharField('Название заданий', max_length=500)
    is_complete = models.BooleanField('Завершено', default=False)

    def __str__(self):
        return self.title