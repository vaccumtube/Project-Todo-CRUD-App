from django.db import models


# Create your models here.
class TodoApp(models.Model):
    input=models.CharField(max_length=100)
    complete=models.BooleanField(default=True)
    time=models.TimeField(auto_now=True)
    
    def __str__(self):
        return self.input

   



