from setuptools import find_packages, setup
from typing import List 


def get_requirement(filepath:str)-> List[str]:
    "getting package from requirement text file"
    requirement = []
    with open(filepath, 'r') as f:
        requirement = f.readlines()
        requirement = [ele.replace(r'\n', '') for ele in requirement]
        
        if "-e ." in requirement:
            requirement = requirement.remove('-e .')
            
    return requirement
         
    


setup(
    name='Machine Learning Project',
    version='1.0',
    author='Dhilip Maharish',
    description='An end to end machine learning applications',
    packages=find_packages(),
    install_requires= get_requirement("requirements.txt")
)