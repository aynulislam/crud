from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name




class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=20)
    religion = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=20, unique=True)
    company = models.ForeignKey(Company, on_delete= models.CASCADE, blank=True, null=True,)
    department = models.ForeignKey(Department, on_delete= models.CASCADE, blank=True, null=True,)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, blank=True, null=True)

    created_by = models.IntegerField()
    modified_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name
