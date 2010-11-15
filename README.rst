About
=====
*django-limit-users* is an installable Django application to quickly limit the
number of user registrations at any time, especially useful during beta periods
when you want to test with a limited number of users.

*dlu*, rather than take the blocking approach to limiting registrations, actually
allows users to continue creating new accounts, but when the maximum limit has been
reached, any new accounts are automatically disabled.

Management scripts, which allow you to open registrations up in batches and
enabling existing registrations (that were registered after the limit was
reached, and so are disabled), are included.

Installation
============
From source using ``setup.py``::

    cd dlu
    python setup.py install # perhaps ^sudo if you're not in a virtualenv

From pypi::

    easy_install django-limit-users
    # or using the virtualenv friendly pip
    pip install django-limit-users

Configuration
=============
Add ``limitusers`` to the ``INSTALLED_APPS`` tuple in your ``settings.py`` file,
and run ``syncdb`` (using ``manage.py`` or equivalent, depending on your Django
setup).

You'll also want to add the following config values to ``settings.py``:

 * ``MAX_USER_REGISTRATIONS`` (required): maximum number of registrations to enable.
 * ``CLEANUP_DISABLED_USER_MODELS`` (optional): whether or not to delete orphaned
    instances of ``limitusers.models.DisabledUser``. Default: False.
 * ``LIMIT_USERS_IGNORE_ADMIN`` (optional): if True, ignore admin users in counts. Default: True.
 * ``DISABLE_USER_REGISTRATION_LIMIT`` (optional): if True, registrations will not be
    limited and everything works is as if *django-limit-users* isn't installed. Default: False.

Usage
=====
If for example you have your ``MAX_USER_REGISTRATIONS`` value set to ``1000``,
and you've reached 1000 users, in fact you've got 1215 users (215 of which are
disabled), after a period of testing you might increase that to ``2000``.

To enable the next batch of available users (like an invite system) you can run::

    python manage.py enableusers -e

(If your Django deployment doesn't use the ``manage.py`` script just replace
``python manage.py`` above with your management path, e.g. ``bin/django`` for
buildout).

The ``enableusers`` command, with the ``-e``, will enable the 215 disabled users,
and print out their email addresses, so that you can send out a "Welcome" email
of some sort to inform these new lucky beta testers that their accounts are active.

You can also use the ``-i`` option to export a list of IDs, and the option ``-c``
will display lists of emails and IDs as a comma-seperated list, making sendin
bulk emails out a bit easier (or using the IDs in model queries).


A similar comand, ``enableuser``, is provided if you need to specifically enable
a particular user.

Some template tags are also provided  in ``limitusers.templatetags.limitusers``
for handy functionality in templates, such as switching based on available
registrations, or displaying counts of registrations/enabled users etc.