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

Usage
=====