from setuptools import setup, find_packages
setup(
    name = 'djangocms-responsive-image',
    packages = find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    license='MIT License',
    version = '0.1.0',
    description = 'Django CMS plugin implementing html5 responsive images',
    author = 'Fabian Lehner',
    author_email = 'fl@makonis.net',
    url = 'https://github.com/febsn/djangocms-responsive-image',
    download_url = 'https://github.com/febsn/djangocms-responsive-image/tarball/0.1.0',
    install_requires = [
       'django-filer>=1.0.4',
       'jsonfield>=1.0.3',
       'django-appconf>=1.0.1',
    ],
    keywords = ['responsive', 'image', 'django'],
    classifiers = [],
)
