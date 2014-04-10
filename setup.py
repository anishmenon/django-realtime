from setuptools import setup, find_packages

setup(
    name='django-realtime',
    version='1.1',
    author='Anish menon',
    author_email='anish@inzane.in',
    description='an iShout.js client for Django',
    url='https://bitbucket.org/inzane/django-realtime',
    license='MIT',
    packages=find_packages(),
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django'
    ]
)
