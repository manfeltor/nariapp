from django.db import models

class Sex(models.Model):
    name = models.CharField(max_length=20, unique=True)
    abbreviation = models.CharField(max_length=3, unique=True, help_text="Codigo corto como F, M, H")
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.abbreviation = self.abbreviation.upper()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Sexes"

    def __str__(self):
        return self.name


class PlantStatus(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)
    phase_group = models.CharField(max_length=30, default="Default")

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Plant Statuses'

    def __str__(self):
        return self.name

    
class Species(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Scientific or common
    description = models.TextField(blank=True, null=True)
    created_by_snapshot = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Species'

    def __str__(self):
        return self.name
    
class Breed(models.Model):
    species = models.ForeignKey('Species', on_delete=models.CASCADE, related_name='breeds')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_by_snapshot = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Breeds'

    def __str__(self):
        return self.name
    
class PlantPhase(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Plant Phases'

    def __str__(self):
        return self.name
