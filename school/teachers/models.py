from django.db import models


# Create your models here.

class Teacher(models.Model):
    # id = models.BigAutoField
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    theme = models.CharField(max_length=64)

    def get_teacher_info(self):
        return f"{self.id} {self.first_name} {self.last_name}, theme = {self.theme}"

    def __str__(self):
        return self.get_teacher_info()
