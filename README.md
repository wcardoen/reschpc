## reschpc: An Initial CHPC Interface to the Rescale Cloud

reschpc
Package to create jobs, submit jobs, download files on Rescale.com
Currently LAMMPS, VASP but easily extendible to all other packages installed on Rescale.

#### Installation
There are 2 requirements:
* python >= 3.6
* requests>=2.10.0

There are several (installation) options:
* Local installation: 
  pip install .

* Development mode: (useful when developing the package)
  pip install -e .

* Using setup.py:
  python3 setup.py build
  python3 setup.py install --prefix=$DIR
  (The last set will give you an error => set corresponding PYTHONPATH)

#### Creation of a source distro
python3 setup.py sdist --formats=bztar
The distro (tar.bz format) is within sdist subdirectory

#### Simple Tests (AFTER installation)
sleipnir@ragnarok:~$ python3
Python 3.7.4 (default, Aug 13 2019, 20:35:49) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import reschpc
>>> reschpc.__file__
'/home/sleipnir/develcode/python/rescale/reschpc/__init__.py'
>>> reschpc.__version__
'0.0.1.dev0'
>>> reschpc.__author__
'Wim R.M. Cardoen'

I haven't created tests in tests (under construction)

#### Examples
An example can be found in the examples subdirectory
The ReScale job submission goes through THREE steps:
1. Upload a ZIP file (e.g. input.zip containing my input file:
                           "in.lj.fixed"
2. Create a Job (using in.lj.fixed)
3. Submit the Job

Once the job is done you can retrieve the output files => 
e.g. test_retrieval.py 

NOTE:
For ALL operations a KEY (I call it token is required).
A projectID is required to submit the job
The current KEY is my own Key
The projectid is the TCO projectID.

#### What about Other Packages?
I have included a module info.py (see examples/test_info.py)
which queries ReScale's REST API:
* analyses:
  returns info/keywords w.r.t 'analysis' section (json) (see e.g. lammps)
* coretypes:
  returns info/keywords w.r.t. 'hardware' section (json) (see e.g. lammps)


Wim
