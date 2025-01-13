from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the
    list  of requirements after reading from file.
    '''
    requirements=[]
    with open(file_path) as file_object:
        requirements=file_object.readlines()
        requirements=[req.replace("\n","")  for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements



# meta data of package
setup(
name='Generic MLProject',
version='0.0.1',
author='Faizan Malik',
author_email='imuhammadfaizan38@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)