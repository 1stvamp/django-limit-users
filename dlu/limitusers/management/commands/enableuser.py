from optparse import make_option
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from dlu.limitusers.models import DisabledUser

class Command(BaseCommand):
        args = '<id>'
        help = 'Enable a single user, regardless of settings.MAX_USER_REGISTRATIONS'
        option_list = BaseCommand.option_list + (
            make_option('-e', '--email',
                        dest='email',
                        default=False,
                        help='Enable user matching email rather than ID'),
        )

        def handle(self, *args, **options):
            id = None
            if len(args):
                id = args[0]
            email = options.get('email', None)
            if not id and not email:
                raise CommandError('''Please provide either a numeriuc ID as the
first argument, or pass the --email
argument.''')
            filters = {}
            if id:
                filters['user__pk'] = id
            else:
                filters['user__email'] = email
            try:
                user = DisabledUser.objects.get(**filters)
            except DisabledUser.DoesNotExist:
                raise CommandError('User matching "%s" not found.' %
                        (str(filters),))
            else:
                # Re-enable the auth models User, and remove the DisabledUser
                user.user.disabled = False
                user.user.save()
                user.delete()
                print "User enabled."
