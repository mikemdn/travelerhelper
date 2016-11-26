from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) #make a link between Auth model and Profile Model
    licence = models.BooleanField(default=False)
    card = models.BooleanField(default=False)
    navigo = models.BooleanField(default=False)
    velibPass = models.BooleanField(default=False)
    car = models.BooleanField(default=False)
    bike = models.BooleanField(default=False)

# Enabling one to one link with the User authentification and the User Profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()