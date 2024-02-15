'''

FileSorter for MacOS.
Intended for you who keeps dropping everything in your Downloads folder.
Change the user to yours (from 'kaleb'), as well as respective keywords in the lists if necessary.

Features (made specifically for kaleb but maybe for you as well):
- Selects tracks if ' - ' is contained in the file name
- Sorts drum samples into respective folders by name and cleans each name
- Migrates and deletes documents if not containing a keyword or has a size >50 MB

For questions or wanting to say that this is a totally-awesome-and-not-low-effort-program, email kaleb@case.edu.

'''

# UPDATE THIS LINE TO YOUR USER
user = 'kaleb'

# UPDATE THESE VARIABLES IF NECESSARY
delDocs = True # deletes document if it doesn't contain any of the keywords

# UPDATE KEYWORDS IF NECESSARY
drumKeywords = ['Kick', 'Snare', 'Hihat', 'Ride', 'Crash', 'Tom', 'Cymbal', 'Drum']
docKeywords = ['Transcript', 'Resume', 'Card', 'Letter', 'ID', 'Final', 'Book']

# UPDATE THESE PATHS IF NECESSARY
path = '/Users/%s/Downloads' %(user)
musicPath = '/Users/%s/Music/Ableton/User Library/Samples' %(user)
docPath = '/Users/%s/Documents' %(user)
photoPath = '/Users/%s/Pictures' %(user)

''' Code you don't have to look at commences forth here '''
import os, shutil

import filter as f
import guard as g

list_ = os.listdir(path)

# main function
for file_ in list_:
    name, ext = os.path.splitext(file_)
    ext = ext[1:]
    # folders and unknown files
    if ext == '':
        continue
    # samples (music)
    if ext == 'wav' or ext == 'mp3': # for music
        if name.__contains__(' - '): # track
            g.ckdir(musicPath + '/Tracks')
            print('Moving track: ' + file_)
            shutil.move(path + '/' + file_, musicPath + '/Tracks/' + file_)
            continue
        for drumTag in drumKeywords: # drum
            if name.lower().__contains__(drumTag.lower()):
                g.ckdir(musicPath + '/Drums')
                f.filter(path, musicPath + '/Drums', drumTag, file_)
                break
        print("Can't sort this music sample chief")
    # documents
    elif ext == 'pdf' or ext == 'doc' or ext == 'docx': # for documents
        g.ckdir(docPath)
        moved = False
        for docTag in docKeywords:
            if name.lower().__contains__(docTag.lower()):
                g.ckdir(docPath)
                f.filter(path, docPath, docTag, file_, False)
                print('Moved document: ' + file_)
                moved = True
                break
        if not moved: # means keyword hasn't been found
            os.remove(path + '/' + file_)
            print('Deleted file: ' + file_)
    # images
    elif ext.lower() == 'heic' or ext.lower() == 'jpg' or ext.lower() == 'png':
        g.ckdir(photoPath)
        shutil.move(path + '/' + file_, photoPath + '/' + file_)
        print('Moved photo: ' + file_)