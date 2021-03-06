# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import Profile

class FamilyHistoryStats(models.Model):
    generations = models.IntegerField(blank=True, default=0)
    names = models.IntegerField(blank=True, default=0)
    indexed = models.IntegerField(blank=True, default=0)
    memories = models.IntegerField(blank=True, default=0)

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Family History Stats'
        verbose_name_plural = 'Famlily History Stats Records'

    def __str__(self):
        if self.profile.first_name:
            return '{0} {1}'.format(self.profile.first_name, self.profile.last_name)
        else:
            return self.profile.user.username

@receiver(post_save, sender=Profile)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        FamilyHistoryStats.objects.create(profile=instance)

@receiver(post_save, sender=Profile)
def save_user_profile(sender, instance, **kwargs):
    instance.familyhistorystats.save()


class FamilyName(models.Model):
    name = models.CharField(max_length=180)
    owner = models.ForeignKey(FamilyHistoryStats, on_delete=models.CASCADE)

