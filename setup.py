from setuptools import setup
setup(
    name = 'djangocms_responsive_image',
    packages = ['djangocms_responsive_image'],
    version = '0.0.1',
    description = 'Django CMS plugin implementing html5 responsive images',
    author = 'Fabian Lehner',
    author_email = 'fl@makonis.net',
    url = 'https://github.com/febsn/djangocms-responsive-image',
    download_url = 'https://github.com/febsn/djangocms-responsive-image/tarball/0.0.1',
    install_requires = [
       'django-filer',
       'jsonfield',
       'django-appconf',
    ],
    keywords = ['responsive', 'image', 'django'],
    classifiers = [],
)
