# -*- coding: utf-8 -*-
"""This is a custom local plugin to add extra functionality to the site."""

# Third party imports
from setuptools import setup


requirements = [
   'Lektor',
   'unidecode',
]


setup(
    name='lektor-python-colombia-plugin',
    author='Gonzalo Peña-Castellanos',
    author_email='goanpeca@gmail.com',
    url='https://github.com/colombiapython/sitio-web/tree/lektor/packages/lektor_python_colombia_plugin',
    version='0.1',
    license='MIT',
    py_modules=['lektor_python_colombia_plugin'],
    install_requires=requirements,
    entry_points={
        'lektor.plugins': [
            'python-colombia-plugin = lektor_python_colombia_plugin:PythonColombiaPlugin',
        ]
    }
)
