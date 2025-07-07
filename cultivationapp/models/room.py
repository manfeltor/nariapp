from django.db import models
from django.db.models import Count
from usersapp.models import CompanyScopedModel


class PlantRoom(CompanyScopedModel):
    name = models.CharField(max_length=100)
    width = models.PositiveIntegerField(help_text="Número de columnas (A, B, C...)")
    height = models.PositiveIntegerField(help_text="Número de filas (1, 2, 3...)")
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    light_cycle_hours = models.PositiveIntegerField()

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Plant Rooms"
        unique_together = ('company', 'name')

    def __str__(self):
        return self.name

    @property
    def max_capacity(self):
        return self.width * self.height

    def has_available_space(self):
        return self.plants.count() < self.max_capacity

    def assign_ruleset_tag(self, tag):
        """Assign a RulesetTag to all plants in this room."""
        return self.plants.update(ruleset_tag=tag)

    def clear_rulesets(self):
        """Clear the RulesetTag for all plants in this room."""
        return self.plants.update(ruleset_tag=None)

    def get_ruleset_summary(self):
        """Returns how many plants have each ruleset tag in this room."""
        return self.plants.values('ruleset_tag__name').annotate(count=Count('id')).order_by('-count')


class RoomCharacteristicType(CompanyScopedModel):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Room Characteristic Types"
        unique_together = ('company', 'name')

    def __str__(self):
        return self.name


class RoomCharacteristicValue(models.Model):
    room = models.ForeignKey(PlantRoom, on_delete=models.CASCADE, related_name='characteristics')
    type = models.ForeignKey(RoomCharacteristicType, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('room', 'type')
        ordering = ['type']
        verbose_name_plural = "Room Characteristic Values"

    def __str__(self):
        return f"{self.type.name}: {self.value} ({self.room.name})"
