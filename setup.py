#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pathlib
import re
from setuptools import setup, find_packages


def read_version():
    p = pathlib.Path(__file__)
    p = p.parent / "cfm_ospo_demo_project" / '__init__.py'
    with p.open('r') as f:
        for line in f:
            if line.startswith('__version__'):
                line = line.split('=')[1].strip()
                match = re.match(r"^['\"](\d+\.\d+\.\d+\w*)['\"]", line)
                if match:
                    return match.group(1)
    raise ValueError('Unable to compute version')


def read(fname):
    file_path = pathlib.Path(__file__).parent / fname
    with file_path.open('r', encoding='utf-8') as f:
        return f.read()


def get_requirements():
    requirements = pathlib.Path(__file__).parent / 'requirements.txt'
    with requirements.open('r', encoding='utf-8') as f:
        packages = f.readlines()
        packages.append('wheel')
    return list(set([i for i in packages])) 


setup(
    name='CFM OSPO Demo Project',
    version=read_version(),
    author='Florent Zara',
    author_email='fzara@henix.fr',
    maintainer='Florent Zara',
    maintainer_email='fzara@henix.fr',
    license='MIT',
    project_urls=dict(Source='https://github.com/CFMTech/CFM-OSPO-Demo-Project',
                      Tracker='https://github.com/CFMTech/CFM-OSPO-Demo-Project/issues'),
    url='https://CFM-OSPO-Demo-Project.readthedocs.io/',
    description='This a basic instanciation of CFM template for OSS projects',
    long_description=read('README.md'),
    packages=find_packages('.', exclude=('tests', 'example', 'docs')),
    python_requires='>=3.5',
    install_requires=get_requirements(),
    options={"bdist_wheel": {"universal": False}},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5', 
        'Programming Language :: Python :: 3.6', 
        'Programming Language :: Python :: 3.7', 
        'Programming Language :: Python :: 3.8', 
        'Programming Language :: Python :: 3.9', 
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={ 'console_scripts': [ 'cfm-ospo-demo-project=cfm_ospo_demo_project.cli:main', ], },
)
