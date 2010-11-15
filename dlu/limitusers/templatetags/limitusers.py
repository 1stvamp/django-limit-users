from django import template
from django.conf import settings
from dlu.limitusers.models import User, DisabledUser


register = template.Library()

@register.simple_tag
def regs_available():
    filters = {}
    if settings.get('LIMIT_USERS_IGNORE_ADMIN', True):
        filters['is_stuff'] = False
        filters['is_superuser'] = False
    remaining = settings.get('MAX_USER_REGISTRATIONS') - User.objects.filter(**filters).count()
    if remaining < 0:
        remaining = 0
    return remaining

@register.simple_tag
def regs_disabled():
    return DisabledUser.objects.all().count()

@register.simple_tag
def active_users():
    return Users.objects.filter(disabled=False).count()
