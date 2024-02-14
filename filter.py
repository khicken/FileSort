import os
import shutil

import guard as g

"""
Sorts, moves and renames the given file.

Parameters
----------
srcPath : str
    Original path of file once was
destPath: str
    New path of where file will be
tag : str
    Keyword that's responsible for the actions bestowed upon this file
file_ : str
    File to be operated upon
folder : bool
    True for generating folders to sort files, False for throwing them in the destination path
tagFirst : bool
    True for placing the keyword first in the renaming process (default), False otherwise

Returns
-------
None
"""
def filter(srcPath, destPath, tag, file_, folder=True, tagFirst=True):
    name, ext = os.path.splitext(file_)

    # renaming, the goofy way
    file_ = ''
    if tagFirst:
        file_ = tag
    capitalizeNext, foundTag = True, False
    curr = ''
    for i in name:
        if i == ' ' or i == '-' or i == '_' or i == '+':
            if tagFirst and not foundTag:
                if curr.lower() == tag.lower(): # tag found, don't duplicate it
                    foundTag = True
                    continue
            # for all the other cases, keep adding words
            file_ += ' ' + curr
            capitalizeNext = True
            curr = ''
            continue
        if capitalizeNext:
            curr += i.upper()
            capitalizeNext = False
        else:
            curr += i.lower()
    file_ += ' ' + curr + ext if not tagFirst or foundTag else ext # append last word and extension if not a tag when tagFirst is off 

    if folder:
        destPath += '/' + tag
    oldName = name + ext

    g.ckdir(destPath)
    shutil.move(srcPath + '/' + oldName, destPath + '/' + oldName)
    print('Moved file %s from %s to %s' %(oldName, srcPath, destPath))

    os.rename(destPath + '/' + oldName, destPath + '/' + file_)
    print('Renamed file from %s to %s' %(oldName, file_))