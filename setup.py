import setuptools

from os import path

# To produce the source distribution
#    python setup.py sdist

inloco = path.abspath(path.dirname(__file__))

with open(path.join(inloco,'README.md'),encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
      name="reschpc", 
      version="0.0.1.dev0",
      packages=setuptools.find_packages(),

      # Installation requirements
      install_requires = ['requests>=2.10.0'] ,
      python_requires='>=3.6',

      # Description
      description="CHPC package to submit jobs on the Rescale Cloud",
      long_description=long_description,
      long_description_content_type="text/markdown",

      author="Wim R.M. Cardoen",
      author_email="wcardoen@gmail.com",
   
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
)
