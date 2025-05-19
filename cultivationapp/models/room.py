from django.db import models
from django.db.models import Count


class PlantRoom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    width = models.PositiveIntegerField(help_text="Numnero de columnas (A, B, C...)")
    height = models.PositiveIntegerField(help_text="Numero de filas (1, 2, 3...)")
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    light_cycle_hours = models.PositiveIntegerField()

    def assign_ruleset_tag(self, tag):
        """Assign a RulesetTag to all plants in this room."""
        return self.plants.update(ruleset_tag=tag)

    def clear_rulesets(self):
        """Clear the RulesetTag for all plants in this room."""
        return self.plants.update(ruleset_tag=None)

    def get_ruleset_summary(self):
        """Returns how many plants have each ruleset tag in this room."""
        return self.plants.values('ruleset_tag__name').annotate(count=Count('id')).order_by('-count')

    def has_available_space(self):
        return self.plants.count() < self.max_capacity

    def __str__(self):
        return self.name

    @property
    def max_capacity(self):
        return self.width * self.height

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Plant Rooms"


class RoomCharacteristicType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('type', 'value')
        ordering = ['name']
        verbose_name_plural = "Room Characteristic Types"


class RoomCharacteristicValue(models.Model):
    room = models.ForeignKey('PlantRoom', on_delete=models.CASCADE, related_name='characteristics')
    type = models.ForeignKey('RoomCharacteristicType', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('room', 'type')
        ordering = ['type']
        verbose_name_plural = "Room Characteristic Values"

    def __str__(self):
        return f"{self.type.name}: {self.value} ({self.room.name})"
