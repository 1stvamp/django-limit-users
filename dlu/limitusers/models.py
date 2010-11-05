from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User

def user_save_handler(sender, **kwargs):
    # Make sure we create a matching UserProfile instance whenever
    # a new User is created.
    if kwargs['created']:
        user = kwargs['instance']
        filters = {}
        if settings.get('LIMIT_USERS_IGNORE_ADMIN', True):
            filters['is_stuff'] = False
            filters['is_superuser'] = False
        if User.objects.filter(**filters).count() >= settings.get('MAX_USER_REGISTRATIONS'):
            user.disabled = True
            user.save()
            DisabledUser.objects.create(user=user)
post_save.connect(user_save_handler, User)

class DisabledUser(models.Model):
    user = models.ForeignKey(User)
