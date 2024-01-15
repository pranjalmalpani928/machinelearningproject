from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    with open(file_path) as new_file:
        requirements = new_file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='mlp_project',
    version = '0.0.1',
    author='pranjal',
    author_email='pranjal.malpani928@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)