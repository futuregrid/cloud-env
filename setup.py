"""FutureGrid: Creating a SLURM virtual Cluster via euca2tools

This project creates a virtual cluster with the help of euca
tools. The cluster uses SLURM as resource manager. A simple MPI
program is included to test the functionality. of teh virtual cluster.
"""

from setuptools import setup, find_packages
import sys, os

version = '0.1'

classifiers = """\
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Science/Research
Development Status :: 3 - Alpha
Intended Audience :: Developers
License :: OSI Approved :: Apache Software License
Programming Language :: Python
Topic :: Database
Topic :: Software Development :: Libraries :: Python Modules
Operating System :: POSIX :: Linux
Programming Language :: Python :: 2.7
Operating System :: MacOS :: MacOS X
Topic :: Scientific/Engineering
Topic :: System :: Clustering
Topic :: System :: Distributed Computing
"""

if sys.version_info < (2, 7):
    _setup = setup
    def setup(**kwargs):
        if kwargs.has_key("classifiers"):
            del kwargs["classifiers"]
        _setup(**kwargs)

doclines = __doc__.split("\n")


setup(
    name='futuregrid.cloud.env',
    version=version,
    description = doclines[0],
    classifiers = filter(None, classifiers.split("\n")),
    long_description = "\n".join(doclines[2:]),
    keywords='FutureGrid OpenStack Eucalyptus management',
    maintainer='Koji Tanaka, Gregor von Laszewski',
    maintainer_email="laszewski@gmail.com",
    author='Koji Tanaka, Gregor von Laszewski',
    author_email='laszewski@gmail.com',
    url='https://github.com/futuregrid/cloud-env',
    license='Apache 2.0',
    package_dir = {'': '.'},
    packages = find_packages(exclude=['ez_setup', 'examples', 'tests']),
    
    #include_package_data=True,
    #zip_safe=True,
    #install_requires=[
    #    # -*- Extra requirements: -*-
    #],

    
    entry_points={
        'console_scripts': [
                'fg-cloud-env = futuregrid.cloud.env.FGEnvShell:main',
             ]},

    install_requires = [
             'setuptools',
             'pip'
             ],
             #'fabric',
             #'boto',

    )
