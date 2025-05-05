from django.db import models

# Create your models here.
class PlantRoom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    width = models.PositiveIntegerField(help_text="Number of columns (A, B, C...)")
    height = models.PositiveIntegerField(help_text="Number of rows (1, 2, 3...)")
    max_capacity = models.PositiveIntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    light_cycle_hours = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class RoomCharacteristicType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
    
class RoomCharacteristicValue(models.Model):
    room = models.ForeignKey('PlantRoom', on_delete=models.CASCADE, related_name='characteristics')
    type = models.ForeignKey('RoomCharacteristicType', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('room', 'type')

    def __str__(self):
        return f"{self.type.name}: {self.value} ({self.room.name})"

class Plant(models.Model):
    room = models.ForeignKey(PlantRoom, on_delete=models.CASCADE, related_name='plants', default="1")
    column = models.PositiveIntegerField()  # 0 = A, 1 = B, etc.
    row = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    species = models.CharField(max_length=200)

    class Meta:
        unique_together = ('room', 'column', 'row')

    def grid_label(self):
        col_label = chr(65 + self.column)
        row_label = str(self.row + 1)
        return f"{col_label}{row_label}"
    
class PlantCharacteristicType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

class PlantCharacteristicValue(models.Model):
    plant = models.ForeignKey('Plant', on_delete=models.CASCADE, related_name='characteristics')
    type = models.ForeignKey('PlantCharacteristicType', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('plant', 'type')

    def __str__(self):
        return f"{self.type.name}: {self.value} ({self.plant})"