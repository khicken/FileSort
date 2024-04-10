import os
import shutil

import guard as g

"""
Sorts, moves and renames the given file.

Parameters
----------
srcPath : str
    Original path of file once was.
destPath: str
    New path of where file will be.
tag : str
    Keyword that's responsible for the actions bestowed upon this file.
file_ : str
    File to be operated upon.
folder : bool
    True for generating folders to sort files (default), False for throwing them in the destination path.
tagFirst : bool
    True for placing the keyword first in the renaming process (default), False otherwise.

Returns
-------
int
    Number of items moved and renamed.
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


"""
Replaces strings for all files found given a directory.

Parameters
----------
find : str
    String to select files.
replace : str
    String to replace all found strings.
path : str
    Directory path that will have operations bestowed upon thee.

Returns
-------
int
    Number of items renamed.
"""
def findAndReplace(find, replace, path):
    count = 0
    list_ = os.listdir(path)
    for file_ in list_:
        if os.path.isfile(path + '/' + file_):
            name, ext = os.path.splitext(file_)
            i = name.find(find)
            if i != -1:
                print('Found file: ' + file_)
                name =  name[0:i] + replace + name[(i+len(find))]
                os.rename(path + '/' + file_, path + '/' + name + ext)
                print('Renamed file from ' + file_ + " to " + name + ext)
    print('Items renamed: ' + count)
    return count