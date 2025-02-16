from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of requirements.
    """
    requirements = []
    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Strip spaces and newlines
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name="Back pack project",
    version="0.0.1",
    author="Sudipto K",
    author_email="sudiptokumarmahato@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
