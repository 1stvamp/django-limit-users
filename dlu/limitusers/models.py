from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User

def user_save_handler(sender, **kwargs):
    if not getattr(settings, 'DISABLE_USER_REGISTRATION_LIMIT', False):
        # Make sure we create a matching UserProfile instance whenever
        # a new User is created.
        user = kwargs['instance']
        if kwargs['created']:
            filters = {}
            if getattr(settings, 'LIMIT_USERS_IGNORE_ADMIN', True):
                filters['is_staff'] = False
                filters['is_superuser'] = False
            if User.objects.filter(**filters).count() > getattr(settings, 'MAX_USER_REGISTRATIONS'):
                user.is_active = False
                DisabledUser.objects.create(user=user)
            user.save()
        elif getattr(settings, 'CLEANUP_DISABLED_USER_MODELS', False):
            if not user.disabled:
                disabled = DisabledUser.objects.filter(user=user)
                if disabled:
                    disabled.delete()

post_save.connect(user_save_handler, User)

class DisabledUser(models.Model):
    user = models.ForeignKey(User)
