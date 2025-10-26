#!/usr/bin/env python3

from distutils.core import setup, Extension
import os
import shutil
import subprocess
import sys

def check_output(*args):
    """subprocess.check_output, for Python 2.6 compatibility"""
    p = subprocess.Popen(*args, stdout=subprocess.PIPE)
    out, err = p.communicate()
    exitstatus = p.poll()
    if exitstatus:
        raise subprocess.CalledProcessError(exitstatus, args[0])
    return out.decode('utf-8')

fmbt_utils_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)),os.getenv("VPATH",""))
fmbt_dir = os.path.join(fmbt_utils_dir, "..")

version = (open(os.path.join(fmbt_dir, "configure.ac"), "r")
           .readline()
           .split(",")[1]
           .replace(' ','')
           .replace('[','')
           .replace(']',''))

lines = [line.replace("\\","").strip()
         for line in open(os.path.join(fmbt_utils_dir, "Makefile.am"))
         if not "=" in line]

modules = [module.replace(".py","")
           for module in lines[lines.index("# modules")+1:
                               lines.index("# end of modules")]]

scripts = lines[lines.index("# scripts")+1:
                lines.index("# end of scripts")]

setup(name         = 'fmbt-python',
      version      = version,
      description  = 'fMBT Python tools and libraries',
      author       = 'Antti Kervinen',
      author_email = 'antti.kervinen@gmail.com',
      py_modules   = modules,
      scripts      = scripts,
  )
