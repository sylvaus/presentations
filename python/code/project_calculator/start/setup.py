from setuptools import setup, find_packages


def read_readme(filepath):
    return open(filepath).read()


def read_requirement(filepath):
    return open(filepath).read().splitlines()


setup(
    name="Calculator Project",
    version='',
    # Use this commented line to define your entry_point
    # py_modules=["entry_point"],
    packages=find_packages(exclude=['tests']),
    url='',
    description='',
    long_description=read_readme('readme.md'),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    install_requires=[],
    tests_require=['pytest'],
    # Use this to register your entry point
    # entry_points={'gui_scripts': ['read_text=entry_point:main', ], },
)
