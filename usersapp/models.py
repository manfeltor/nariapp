from django.db import models
from django.contrib.auth.models import AbstractUser

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    mail = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    

class CompanyScopedModel(models.Model):
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        related_name='%(class)ss'
    )

    class Meta:
        abstract = True


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return self.username