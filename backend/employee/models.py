from django.db import models
from company.models import Company


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()
    department = models.CharField(max_length=255)
    salary_per_hour = models.DecimalField(decimal_places=2, max_digits=20)
    hours_per_week = models.IntegerField()
    image = models.ImageField(upload_to='images/', default='images/default.png')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # gets the image for the frontend
    def get_image(self):
        return 'http://127.0.0.1:8000' + self.image.url

    # calculates the total salary from the employee
    def get_absolute_salary(self):
        return (self.salary_per_hour * self.hours_per_week) * 52
