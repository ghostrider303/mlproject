from setuptools import find_packages,setup
from typing import List


hypen_e_dot='-e .'
def get_req(file_path:str)->List[str]:
    """
    this fn will return list of requirements
    """
    with open(file_path) as fo:
        req=fo.readlines()
        req=[r.replace('\n','') for r in req]


        if hypen_e_dot in req:
            req.remove(hypen_e_dot)

    return req



setup(

    name='mlproject',
    version='0.0.1',
    author='ghostrider303',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')
    
)