from django.db import models

# Create your models here.

class Employees(models.Model):
    
    full_name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    mobile = models.CharField(max_length = 15)
    date_of_birth = models.DateField()
    photos = models.ImageField(upload_to='employee_photos/', blank=True, null=True)
    
    def __str__(self):
        return self.full_name