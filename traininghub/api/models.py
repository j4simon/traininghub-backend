from django.db import models

# Create your models here.

# class User(models.Model):
#      first_name = models.CharField(max_length=50)
#      last_name = models.CharField(max_length=50)
#      employee_number = models.IntegerField()
#      company = models.CharField(max_length=50)
#      department = models.CharField(max_length=50)
#      title = models.CharField(max_length=50)
    
class Training(models.Model):
     title = models.CharField(max_length=50)
     description = models.CharField(max_length=100)
     category = models.CharField(max_length=50)
     training_link = models.URLField(max_length=200)
    #  users = ManyToManyField(User)
     
    # def __str__(self):
    #     return self.name