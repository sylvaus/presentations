from setuptools import setup, find_packages

import text_reader


def read_readme(filepath):
    return open(filepath).read()


def read_requirement(filepath):
    return open(filepath).read().splitlines()


setup(
    name="text_reader",
    version=text_reader.__version__,
    packages=find_packages(exclude=['tests']),
    url='',
    description='Text Reader Project',
    long_description=read_readme('readme.md'),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    install_requires=['pyttsx3'],
    tests_require=['pytest'],
    entry_points={'console_scripts': ['read_text=text_reader.entry_point:main', ], },
)
