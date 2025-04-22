from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=200)
    student_id = models.CharField(max_length=200,default= "231400000")
    is_staff= models.BooleanField()
    is_superuser = models.BooleanField()

    def __str__(self):
        return self.name









