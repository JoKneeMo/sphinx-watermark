#!/usr/bin/env python3
# coding: utf-8
'''sphinx-watermark setup file.'''

from io import open
from setuptools import setup
from sphinx_watermark import __version__, __author__, __email__, __license__, __keywords__

setup(
    name='sphinx-watermark',
    version=__version__,
    url='https://github.com/JoKneeMo/sphinx-watermark',
    project_urls = {
        'repository': 'https://github.com/JoKneeMo/sphinx-watermark',
        'homepage': 'https://jokneemo.github.io/sphinx-watermark',
        'documentation': 'https://jokneemo.github.io/sphinx-watermark',
        'issues': 'https://github.com/JoKneeMo/sphinx-watermark/issues'
    },
    author=__author__,
    author_email=__email__,
    license=__license__,
    description='A Sphinx extension that enables watermarks for HTML output.',
    long_description=open('README.rst', encoding='utf-8').read(),
    long_description_content_type='text/x-rst',
    platforms='any',
    keywords=__keywords__,
    packages=['sphinx_watermark'],
    package_data={
        'sphinx_watermark': [
            'fonts/*',
        ],
    },
    python_requires='>=3',
    install_requires=open('requirements.txt', 'r').readlines(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Writers',
        'Topic :: Documentation :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ]
)
