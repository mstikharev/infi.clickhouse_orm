#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "A Python library for working with the ClickHouse database"

setup(
    name='infi.clickhouse_orm',
    version='2.0.0',
    author='Infinidat',
    author_email='',
    url='https://github.com/Infinidat/infi.clickhouse_orm',
    license='BSD',
    description='A Python library for working with the ClickHouse database',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database"
    ],
    
    install_requires=[
        'iso8601 >= 0.1.12',
        'pytz',
        'requests',
        'setuptools'
    ],
    
    namespace_packages=['infi'],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    
    entry_points={
        'console_scripts': [],
        'gui_scripts': [],
    },
)
