from setuptools import setup,Extension
from Cython.Build import cythonize

ext_modules = [Extension("crc",sources=["crc.pyx"],language="c++")]

setup(ext_modules = cythonize(ext_modules))
