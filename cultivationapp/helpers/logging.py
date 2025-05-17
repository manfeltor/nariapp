from datetime import date
from django.forms.models import model_to_dict
from cultivationapp.models.logs import PlantEventLog, PlantStateLog, RoomStateLog


def log_plant_event(plant, event_type, occurred_at=None, value=None, notes=None, rule=None):
    occurred_at = occurred_at or date.today()

    # Flattened plant snapshot
    plant_snapshot = model_to_dict(plant)
    plant_snapshot["grid_label"] = plant.grid_label
    plant_snapshot["sex"] = plant.sex.name
    plant_snapshot["species"] = plant.species.name
    plant_snapshot["breed"] = plant.breed.name
    plant_snapshot["status"] = plant.status.name
    plant_snapshot["ruleset_tag"] = plant.ruleset_tag.name if plant.ruleset_tag else None
    plant_snapshot["room"] = plant.room.name
    plant_snapshot["created_by_snapshot"] = plant.created_by_snapshot

    # Rule snapshot
    rule_snapshot = None
    if rule:
        rule_snapshot = model_to_dict(rule, fields=['trigger_after_days', 'warning_lead_days', 'description'])
        rule_snapshot["event_type"] = rule.event_type.name
        rule_snapshot["ruleset_names"] = [r.tensname for r in rule.rulesets.all()]

    return PlantEventLog.objects.create(
        plant_code=plant.code,
        plant_identificator=plant.identificator,
        plant_name=plant.name,

        event_type_name=event_type.name,
        event_type_category=event_type.category,
        event_type_unit=event_type.unit,

        occurred_at=occurred_at,
        value=value,
        notes=notes,
        snapshot=plant_snapshot,
        rule_snapshot=rule_snapshot
    )


def log_plant_state(plant, change_type, notes=None):
    plant_snapshot = model_to_dict(plant)
    plant_snapshot["grid_label"] = plant.grid_label
    plant_snapshot["room"] = plant.room.name
    plant_snapshot["created_by_snapshot"] = plant.created_by_snapshot

    return PlantStateLog.objects.create(
        plant_code=plant.code,
        identificator=plant.identificator,
        change_type=change_type,
        snapshot=plant_snapshot,
        notes=notes
    )


def log_room_state(room, change_type, notes=None):
    room_snapshot = model_to_dict(room)
    room_snapshot["characteristics"] = {
        char.type.name: char.value
        for char in room.characteristics.all()
    }

    return RoomStateLog.objects.create(
        room_name=room.name,
        change_type=change_type,
        snapshot=room_snapshot,
        notes=notes
    )
