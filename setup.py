"""Installer for django-limit-users"""

try:
        from setuptools import setup, find_packages
except ImportError:
        from ez_setup import use_setuptools
        use_setuptools()
        from setuptools import setup, find_packages
setup(
        name='django-limit-users',
        description='Installable Django application to limit the number of enabled user registrations',
        version='1.0.0',
        author='Wes Mason',
        author_email='wes@1stvamp.org',
        url='http://github.com/1stvamp/django-limit-users',
        packages=find_packages(exclude=['ez_setup']),
        setup_requires=(
                'django>=1.1',
        ),
        provides=(
                'dlu',
        ),
        license='Apache License 2.0'
)
