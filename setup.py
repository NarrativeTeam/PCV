# coding=utf-8
from setuptools import setup, find_packages

setup(name="pcv",
      version="0.1.0",
      author="Jan Erik Solem",
      url="https://github.com/jesolem/PCV",
      packages=find_packages(),
      license="BSD",
      platforms="Posix; MacOS X; Windows",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Topic :: Multimedia :: Graphics",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: BSD License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          ],
      install_requires=[
          "PIL>=1.1.7",
          "numpy>=1.6.1",
          "scipy>=0.10.1",
          "matplotlib>=1.1.0",
          ])
