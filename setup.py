from pathlib import Path

from setuptools import setup


setup(
    name='wtforms-tornado',
    version='0.1.0.dev0',
    url='https://github.com/puentesarrin/wtforms-tornado',
    description='WTForms extensions for Tornado.',
    long_description=Path('README.rst').read_text(encoding='utf-8'),
    long_description_content_type='text/x-rst',
    author='Jorge Puente Sarrín',
    author_email='puentesarrin@gmail.com',
    packages=['wtforms_tornado'],
    keywords=['wtforms', 'tornado', 'validation'],
    install_requires=['Tornado>=6.4,<7', 'WTForms>=3.1,<4'],
    python_requires='>=3.11',
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
