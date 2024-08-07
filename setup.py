'''
- With setup.py, you can package your entire machine learning application, making it installable for others via PyPI. 
- This allows anyone to easily install and use your package in their projects. 
- The setup.py script handles the configuration for building and distributing your package.
'''


from setuptools import find_packages,setup
from typing import List

hypen_e_dot = '-e .'
'''this function will return the list of requiremnts'''
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    
    return requirements

'''metadata info of the entire project'''
setup(
name='mlproject',
version='0.0.1',
author="Arshiya",
author_email="arshiyanaheed98@gmail.com",
packages=find_packages(),
install_requires = get_requirements('requirements.txt'),

)
