# -*- coding: utf-8 *-*
import os

try:
    from setuptools import setup
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

version = '0.0.1'


readme_content = ''
try:
    f = open('README.rst')
    readme_content = f.read()
    f.close()
except:
    pass

setup(
    name='wtforms-tornado',
    version=version,
    url='https://github.com/puentesarrin/wtforms-tornado',
    description='WTForms extensions for Tornado.',
    long_description=readme_content,
    author='Jorge Puente Sarrín',
    author_email='puentesarrin@gmail.com',
    packages=['wtforms_tornado'],
    keywords=['wtforms', 'tornado', 'validation'],
    install_requires=['tornado', 'wtforms'],
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)