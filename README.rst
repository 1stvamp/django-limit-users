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