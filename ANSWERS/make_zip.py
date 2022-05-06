#!/usr/bin/env python
"""

@author: jstrick
Created on Thu Mar 21 00:20:43 2013

"""
from zipfile import ZipFile

with ZipFile('potus.zip','w') as zfile:
    zfile.write('save_potus_info.py')
    zfile.write('read_potus_info.py')
    zfile.write('potus.pic')

with ZipFile('potus.zip') as zfile_in:
    print(zfile_in.namelist())
