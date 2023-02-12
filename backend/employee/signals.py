from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Employee


@receiver(pre_save, sender=Employee)
def delete_old_image(sender, instance, **kwargs):
    try:
        old_image = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return

    new_image = instance.image
    if not old_image == new_image:
        if old_image:
            old_image.delete(save=False)
