"""
Quick renaming fix for my pdf files without an extension in my documents folder
"""

import os

path = '/Users/kaleb/Documents'
list_ = os.listdir(path)

for file_ in list_:
    if os.path.isfile(path + '/' + file_):
        name, ext = os.path.splitext(file_)
        if ext == '.' or ext == '':
            os.rename(path + '/' + file_, path + '/' + name + '.pdf')