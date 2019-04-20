from setuptools import setup
import immortalmodel
setup(
    name='django-immortalmodel',
    version=immortalmodel.__version__,
    author='20Tab S.r.l.',
    author_email='info@20tab.com',
    description='A django model, manager and queryset implementing undeletable models',
    url='https://github.com/20tab/django-immortalmodel',
    packages=['immortalmodel'],
    license='MIT License',
    install_requires=[
        'Django >=2.1',
    ],
)
