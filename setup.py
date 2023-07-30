from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME='requirements.txt'
HYPHEN_E_NOT ="-e ."


def get_requirement()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list=requirement_file.readlines()
    requirement_list=[requirement_name.replace("\n","") for requirement_name in requirement_list]

    if HYPHEN_E_NOT in requirement_list:
        requirement_list.remove(HYPHEN_E_NOT)
    return requirement_list


setup(
    name="sensor",
    version="0.0.2",
    author="Deepak Kumar",
    author_email="kumardeepakg92@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement(),
)