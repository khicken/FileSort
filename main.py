import os
import shutil

path = '/Users/kaleb/Downloads'
list_ = os.listdir(path)

# for sound filtering
musicPath = '/Users/kaleb/Music/Ableton/User Library/Samples'
drumList = ['Kick', 'Snare', 'Hihat', 'Ride', 'Crash', 'Tom', 'Cymbal', 'Drum']

def drumFilter(name, ext, file_):
    # format the goofy drum sample name first
    file_, capitalizeNext, currWord = drumTag, False, ''
    for i in name:
        if i == ' ' or i == '-' or i == '_':
            if currWord.lower() != drumTag.lower():
                file_ += ' ' + currWord
            currWord = ''
            capitalizeNext = True
            continue
        if capitalizeNext:
            currWord += i.upper()
            capitalizeNext = False
        else:
            currWord += i.lower()
    file_ += currWord + '.' + ext

    # sort into respective drum folder then rename
    src = musicPath + '/Drums'
    dest = musicPath + '/Drums/' + drumTag
    oldName = name + '.' + ext

    if os.path.exists(dest):
        print('moved!')
        shutil.move(path + '/' + oldName, dest + '/' + oldName)
    else:
        print('moved!')
        os.mkdir(dest)
        shutil.move(path + '/' + oldName, dest + '/' + oldName)
    os.rename(dest + '/' + oldName, dest + '/' + file_)

for file_ in list_:
    name, ext = os.path.splitext(file_)
    ext = ext[1:]
    if ext == "": # it's a folder...
        continue
    if ext == 'wav' or ext == 'mp3': # for music
        if name.__contains__(' - ') and os.path.exists(musicPath + '/Tracks'): # track
            print('Moving track: ' + file_)
            shutil.move(path + '/' + file_, musicPath + '/Tracks/' + file_)
            continue
        for drumTag in drumList: # drum
            if name.lower().__contains__(drumTag.lower()) and os.path.exists(musicPath + '/Drums'):
                print('Moving drum sample: ' + file_)
                drumFilter(name, ext, file_)
                continue
        print("damn can't sort this one chief")
    elif ext == 'pdf': # for documents
        shutil.move(path + '/' + file_, '/Users/kaleb/Documents/' + file_)