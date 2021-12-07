from django.db import models


# Create your models here.
class Group(models.Model):
    # id = models.BigAutoField
    group_name = models.CharField(max_length=64)
    group_theme = models.CharField(max_length=64)
    teacher = models.CharField(max_length=64)

    def get_group_info(self):
        return f"{self.id} {self.group_name} , {self.group_theme}, teacher = {self.teacher}"

    def __str__(self):
        return self.get_group_info()
