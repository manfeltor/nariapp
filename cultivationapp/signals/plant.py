from django.db.models.signals import post_save
from django.dispatch import receiver
from cultivationapp.models.plant import Plant
from cultivationapp.helpers.logging import log_plant_state


# @receiver(post_save, sender=Plant)
# def auto_log_plant_change(sender, instance, created, **kwargs):
#     """
#     Automatically logs creation or updates of a Plant instance.
#     """
#     if created:
#         change_type = "created"
#     else:
#         change_type = "updated"

#     # Send to logging helper
#     log_plant_state(instance, change_type=change_type)
