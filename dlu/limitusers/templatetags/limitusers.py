from django import template
from django.conf import settings
from dlu.limitusers.models import User, DisabledUser


register = template.Library()

class RegsAvailableNode(template.Node):
    def __init__(self, available, var_name = 'registrations_available'):
        self.available = available
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = self.available
        return ''

def regs_available(parser, token):
    filters = {}
    if getattr(settings, 'LIMIT_USERS_IGNORE_ADMIN', True):
        filters['is_staff'] = False
        filters['is_superuser'] = False
    remaining = getattr(settings, 'MAX_USER_REGISTRATIONS') - User.objects.filter(**filters).count()
    if remaining < 0:
        remaining = 0
    return RegsAvailableNode(remaining)

register.tag('regs_available', regs_available)

class RegsAllowedNode(template.Node):
    def __init__(self, allowed, var_name = 'registrations_allowed'):
        self.allowed = allowed
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = self.allowed
        return ''
        
def regs_allowed(parser, token):
    filters = {}
    if getattr(settings, 'LIMIT_USERS_IGNORE_ADMIN', True):
        filters['is_staff'] = False
        filters['is_superuser'] = False
    allowed = getattr(settings, 'MAX_USER_REGISTRATIONS')
    return RegsAllowedNode(allowed)

register.tag('regs_allowed', regs_allowed)

@register.simple_tag
def regs_disabled():
    return DisabledUser.objects.all().count()

class ActiveUsersNode(template.Node):
    def __init__(self, active, var_name = 'active_users'):
        self.active = active
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = self.active
        return ''
        
def active_users(parser, token):
    filters = {'is_active':True}
    if getattr(settings, 'LIMIT_USERS_IGNORE_ADMIN', True):
        filters['is_staff'] = False
        filters['is_superuser'] = False
    active = User.objects.filter(**filters).count()
    return ActiveUsersNode(active)

register.tag('active_users', active_users)
