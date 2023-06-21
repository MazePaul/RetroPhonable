from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
class Player(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    id = 1
    #xp = models.IntegerField(default=0)
    def __str__(self):
        return "%s's profile" % self.user.username
    def id_player(self):
        return self.id

    #def nb_xp(self):
        #return self.xp
        # def create_user_profile(sender, instance, created, **kwargs):
        #     if created:
        #         profile, created = UserProfile.objects.get_or_create(user=instance)
        #     post_save.connect(create_user_profile, sender=User) #in settings.py
        #     AUTH_PROFILE_MODULE = 'YOURAPP.UserProfile'