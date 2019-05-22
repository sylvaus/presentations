from setuptools import setup, find_packages

def read_requirement(filepath):
    return open(filepath).read().splitlines()

setup(
    name = '',                                 # Name of the project
    version='',                                # Version of the project
    packages=find_packages(exclude=['tests']), # Will find all the packages in this folder
    url='',                                    # Wiki or Tuleap or Jira page
    # license='',                              # Optional: License
    # author='',                               # Optional: Code Author
    # author_email='',                         # Optional: Email of the author
    description='Small project example',       # Short Description of the project
    long_description=open('readme.md').read(),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4', # Optional: Restricts the version
    install_requires=[''],                     # Optional: List of dependencies required for installation    
    # Optional: List of dependencies required for installation from a text file    # 
    # install_requires=read_requirement("requirements.txt"),   
    tests_require=['coverage'],                 # Optional: List of extra dependencies required for tests    
    # Optional: List of extra dependencies required for testing from a text files
    # tests_require=read_requirement("test_requirements.txt"),
    # Optional Entry point for a console line interface
    # entry_points={'console_scripts': ['say_hello=entry_point:main',],},
)
