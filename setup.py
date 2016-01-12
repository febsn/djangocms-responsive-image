from setuptools import setup
setup(
    name = 'djangocms_responsive_image',
    packages = ['djangocms_responsive_image'],
    version = '0.0.4',
    description = 'Django CMS plugin implementing html5 responsive images',
    author = 'Fabian Lehner',
    author_email = 'fl@makonis.net',
    url = 'https://github.com/febsn/djangocms-responsive-image',
    download_url = 'https://github.com/febsn/djangocms-responsive-image/tarball/0.0.4',
    install_requires = [
       'django-filer>=1.0.4',
       'jsonfield>=1.0.3',
       'django-appconf>=1.0.1',
    ],
    keywords = ['responsive', 'image', 'django'],
    classifiers = [],
)
