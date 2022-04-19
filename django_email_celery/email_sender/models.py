from django.db import models


# Create your models here.

class employee_database(models.Model):
    Firstname = models.CharField(max_length=200, unique=True)
    Surname = models.CharField(max_length=200, unique=True)
    work = (
        ("IT", "IT"),
        ("FINANCE", "FINANCE"),
        ("HELP_DESK", "HELP_DESK"),
    )
    Department = models.CharField(choices=work, default='NONE', max_length=200)
    gend = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    Gender = models.CharField(choices=gend, default='None', max_length=200)

    def __str__(self):
        return self.Firstname


