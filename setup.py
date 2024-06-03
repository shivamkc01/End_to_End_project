from setuptools import find_packages, setup
from typing import List 

def get_requirements(file_path:str)->List[str]:
  """_summary_

  Args:
      file_path (str): _description_

  Returns:
      List[str]: _description_
  """
  requirements = []
  with open(file_path) as file_obj:
    requirements=file_obj.readlines()
    requirements=[req.replace('\n', "") for req in requirements]
  
  return requirements



setup(
  name="mlproject",
  version='0.0.1',
  author='shivam',
  author_email = "shivam.11712711@gmail.com",
  packages=find_packages(),
  install_requires=['numpy', 'pandas']
  )