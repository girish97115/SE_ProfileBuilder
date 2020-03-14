from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import FacultyProfile, StudentProfile

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_teacher:
            profile = FacultyProfile.objects.create(user=instance)
        else:
            profile = StudentProfile.objects.create(user=instance)

#
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     if instance.is_teacher:  # access the field of instance
#         profile = instance.FacultyProfile.save()
#
#     else:
#         profile = instance.StudentProfile.save()
