from optparse import make_option
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from dlu.limitusers.models import DisabledUser

class Command(BaseCommand):
        args = ''
        help = 'Enable a batch of users'
        option_list = BaseCommand.option_list + (
            make_option('-e', '--emails',
                        action='store_true',
                        dest='emails',
                        default=False,
                        help='Show email addresses of enabled users'),
            make_option('-i', '--ids',
                        action='store_true',
                        dest='ids',
                        default=False,
                        help='Show IDs of enabled users'),
            make_option('-c', '--commalist',
                        action='store_true',
                        dest='comma',
                        default=False,
                        help='Output email/ID lists as comma separated lists'),
        )

        def handle(self, *args, **options):
            limit = settings.get('MAX_USER_REGISTRATIONS')
            limit = limit - User.objects.all().count()
            if limit > 0:
                # Get the oldest registered users that are disabled
                disabled = DisabledUser.objects.all().order_by('user__created')[:(limit-1)]
                users = disabled.user_set
                user_set.update(disabled=False)

                if options['comma']:
                    sep = ","
                else:
                    sep = "\n"

                emails = []
                if options['emails']:
                    print "IDs:"
                    print sep.join(email for obj.email in users.all())

                ids = []
                if options['ids']:
                    print "Emails:"
                    print sep.join(id for obj.id in users.all())

                disabled.delete()
                print "%d users enabled." % (limit,)
            else:
                print "No users to enable.\nEither all users are enabled, or settings.MAX_USER_REGISTRATIONS is too low."
