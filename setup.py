from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Read the requirements from a file and return them as a list."""
    requirements_list:list[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # read lines from the file 
            lines=file.readlines()
            #process each line 
            for line in lines:
                requirement=line.strip() 
                #ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")

    return requirements_list

setup(
    name='networksecurity',
    version='0.0.1',
    author='Daksh',
    author_email='xyz@example.com',
    packages=find_packages(),
    install_requires=get_requirements()

)
    