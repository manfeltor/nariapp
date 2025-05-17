from django.db import models
from cultivationapp.models.room import PlantRoom
from cultivationapp.models.meta import Species, Breed, Sex, PlantStatus

class Plant(models.Model):
    code = models.AutoField(primary_key=True)
    identificator = models.CharField(max_length=4, default="0001")
    name = models.CharField(max_length=100)
    
    sex = models.ForeignKey(Sex, on_delete=models.PROTECT)
    species = models.ForeignKey(Species, on_delete=models.PROTECT)
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT)
    status = models.ForeignKey(PlantStatus, on_delete=models.PROTECT)
    ruleset_tag = models.ForeignKey(
        'RulesetTag',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='plants'
    )
 
    room = models.ForeignKey(PlantRoom, on_delete=models.CASCADE, related_name='plants')
    column = models.PositiveIntegerField()  # 0 = A, 1 = B, ...
    row = models.PositiveIntegerField()     # 0-based, adds 1 for display

    generation = models.PositiveIntegerField(default=1)

    created_by_snapshot = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    mother_code = models.IntegerField(null=True, blank=True)
    father_code = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('room', 'column', 'row')
        ordering = ['code']
        verbose_name_plural = "Plants"

    def __str__(self):
        return f"{self.name} ({self.grid_label})"

    @property
    def grid_label(self):
        col_label = chr(65 + self.column)  # A-Z
        row_label = str(self.row + 1)
        return f"{col_label}{row_label}"


class PlantCharacteristicType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Plant Characteristic Types"

    def __str__(self):
        return self.name


class PlantCharacteristicValue(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='characteristics')
    type = models.ForeignKey(PlantCharacteristicType, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('plant', 'type')
        ordering = ['type']
        verbose_name_plural = "Plant Characteristic Values"

    def __str__(self):
        return f"{self.type.name}: {self.value} ({self.plant})"
