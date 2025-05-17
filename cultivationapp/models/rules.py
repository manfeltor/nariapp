from django.db import models


class PlantEventType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Event Types'

    def __str__(self):
        return self.name
    
class Rule(models.Model):
    event_type = models.ForeignKey('PlantEventType', on_delete=models.PROTECT)
    trigger_after_days = models.PositiveIntegerField()
    warning_lead_days = models.PositiveIntegerField(default=2)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['event_type']
        verbose_name_plural = 'Rules'

    def __str__(self):
        return f"{self.event_type.name} every {self.trigger_after_days}d"

class Ruleset(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    rules = models.ManyToManyField('Rule', related_name='rulesets')

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Rulesets'

    def __str__(self):
        return self.name
    
class RulesetTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Ruleset Tags'

    def __str__(self):
        return self.name

class RulesetAssignment(models.Model):
    tag = models.ForeignKey('RulesetTag', on_delete=models.CASCADE, related_name='assignments')
    ruleset = models.ForeignKey('Ruleset', on_delete=models.CASCADE, related_name='assignments')
    phase = models.ForeignKey('PlantPhase', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('tag', 'phase')  # One ruleset per phase per tag
        ordering = ['tag', 'phase']
        verbose_name_plural = 'Ruleset Assignments'

    def __str__(self):
        return f"{self.tag.name} → {self.phase.name} = {self.ruleset.name}"