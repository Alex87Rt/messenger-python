from setuptools import setup
import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

setup(name="client_messenger",
      version="2.0",
      author="Alex_Pryakhin",
      author_email="alex@alex.ru",
      packages=["main"],
      description="A Simple Math Package",
      url="http://www.alex.org",
      options={"build_exe": build_exe_options},
      executables=[Executable("myscript.py")]
      )
