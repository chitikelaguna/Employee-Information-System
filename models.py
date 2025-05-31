from django.db import models

class employee2(models.Model):
    emp_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    salary = models.FloatField()
    contact = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='Active')

    def __str__(self):
        return f"{self.emp_id} - {self.name}"
