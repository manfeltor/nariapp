from django.db import models
from django.contrib.auth.models import AbstractUser


# CustomUser model
class CustomUser(AbstractUser):
    MANAGER = 'Manager'
    EMPLOYEE = 'Empleado'
    ADMIN = 'Admin'

    ROLE_CHOICES = [
        (MANAGER, 'Manager'),
        (EMPLOYEE, 'Empleado'),
        (ADMIN, 'Admin'),
    ]

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=EMPLOYEE)

    def __str__(self):
        return self.username

    @property
    def is_management(self):
        return self.role in {self.MANAGER, self.ADMIN}
