from django.db import models
from usersapp.models import CompanyScopedModel

class Sex(CompanyScopedModel):
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=3, help_text="Codigo corto como F, M, H")
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.abbreviation = self.abbreviation.upper()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Sexes"
        unique_together = ('company', 'name')

    def __str__(self):
        return self.name


class PlantStatus(CompanyScopedModel):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    phase_group = models.CharField(max_length=30, default="Default")

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Plant Statuses'
        unique_together = ('company', 'name')

    def __str__(self):
        return self.name

    
class Species(CompanyScopedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_by_snapshot = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Species'
        unique_together = ('company', 'name')

    def __str__(self):
        return self.name
    
    
class Breed(CompanyScopedModel):
    species = models.ForeignKey('Species', on_delete=models.CASCADE, related_name='breeds')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_by_snapshot = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Breeds'
        unique_together = ('company', 'name')

    def __str__(self):
        return self.name
    
    
class PlantPhase(CompanyScopedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        unique_together = ('company', 'name')

    def __str__(self):
        return self.name
