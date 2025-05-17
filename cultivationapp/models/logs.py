from django.db import models

class PlantEventLog(models.Model):
    # Free-text snapshot fields — not linked to anything dynamic
    plant_code = models.PositiveIntegerField()  # Still useful for searching, but not FK
    plant_identificator = models.CharField(max_length=10)
    plant_name = models.CharField(max_length=100)

    event_type_name = models.CharField(max_length=100)
    event_type_category = models.CharField(max_length=100, blank=True, null=True)
    event_type_unit = models.CharField(max_length=20, blank=True, null=True)

    occurred_at = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    snapshot = models.JSONField()  # Can contain full plant JSON or structured diff
    rule_snapshot = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-occurred_at']
        verbose_name_plural = 'Plant Event Logs'

    def __str__(self):
        return f"{self.plant_name} - {self.event_type_name} @ {self.occurred_at}"

class PlantStateLog(models.Model):
    plant_code = models.PositiveIntegerField()
    identificator = models.CharField(max_length=10)
    change_type = models.CharField(max_length=100)  # e.g. "created", "status update", "transplanted", etc.

    snapshot = models.JSONField()  # full current plant object flattened
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Plant State Logs"

    def __str__(self):
        return f"{self.change_type} - {self.identificator} ({self.plant_code})"

class RoomStateLog(models.Model):
    room_name = models.CharField(max_length=100)
    change_type = models.CharField(max_length=100)  # e.g. "initial config", "temp update", "resized"

    snapshot = models.JSONField()  # flattened PlantRoom + characteristics
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Room State Logs"

    def __str__(self):
        return f"{self.change_type} - {self.room_name}"

