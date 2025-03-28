# setup.py is responsible for creating my machine learning application as a package .
# we can install this setup.py package in our project 
# can also be used to deploy in pypi (python package index) and
# from there anybody can also do the installation and use it
# # we can also use setup.py to create a virtual environment

from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            

# command to give : pip install -r requirements.txt
# MLProject.egg-info will be created

setup(
    name='MLProject',
    version='0.0.1',
    author='Shri Kishan',
    author_email='punia21ashu@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)