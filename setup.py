from setuptools import find_packages, setup
from typing import List 

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
  """_summary_

  Args:
      file_path (str): requirements.txt file

  Returns:
      List[str]: List of strings
  """
  requirements = []
  with open(file_path) as file_obj:
    requirements=file_obj.readlines()
    requirements=[req.replace('\n', "") for req in requirements]
  
  return requirements



setup(
  name="mlproject",
  version='0.0.1',
  author='shivamkc01',
  author_email = "shivam.11712711@gmail.com",
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt')
  )