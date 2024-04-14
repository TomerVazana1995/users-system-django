from django.db import models

# Create your models here.
class User(models.Model):
    fullName = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('worker', 'Worker')], default='worker', null=True)

    def __str__(self):
        return self.fullName
    
class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    role = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('worker', 'Worker')], default='worker')
    
    def __str__(self):
        return f'{self.user.fullName} - {self.role}'