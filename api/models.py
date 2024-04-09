from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    EDUCATIONAL_YEAR = [
        (2019, '2019'),
        (2020, '2020'),
        (2021, '2021'),
        (2022, '2022'),
        (2023, '2023')
    ]
    std_name = models.CharField(max_length=100)
    std_age = models.IntegerField()
    educational_year = models.IntegerField(choices=EDUCATIONAL_YEAR)
    courses = models.ManyToManyField(Course, related_name='students')

    # class Meta:
    #     unique_together = ['courses',]

    def __str__(self) -> str:
        return self.std_name + ' ' + str(self.educational_year)
