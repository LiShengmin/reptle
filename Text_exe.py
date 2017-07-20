#!/bin/bash
# 生成Exe
from distutils.core import setup
import py2exe
 
setup(console=["helloworld.py"])
