from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from .models import Employee


# Replace an old image with the new image
@receiver(pre_save, sender=Employee)
def delete_old_image(sender, instance, **kwargs):
    try:
        old_image = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return

    new_image = instance.image
    if not old_image == new_image and old_image != 'images/default.png':
        if old_image:
            old_image.delete(save=False)


# Deletes the image when the user is deleted
@receiver(pre_delete, sender=Employee)
def delete_image(sender, instance, using, **kwargs):
    if instance.image != 'images/default.png':
        instance.image.delete(save=False)
