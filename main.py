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
clean = True # clean from the following extensions listed below
cleanExts = ['asd']

# UPDATE KEYWORDS IF NECESSARY
drumKeywords = ['Kick', 'Snare', 'Hihat', 'Ride', 'Crash', 'Tom', 'Cymbal', 'Drum', 'Clap']
docKeywords = ['Transcript', 'Resume', 'Card', 'Letter', 'ID', 'Final', 'Book']

# UPDATE THESE PATHS IF NECESSARY
# path = '/Users/%s/Downloads' %(user)
path = '/Users/%s/Desktop/Music/Samples' %(user)
samplesPath = '/Users/%s/Music/Ableton/User Library/Samples' %(user)
docPath = '/Users/%s/Documents' %(user)
photoPath = '/Users/%s/Pictures' %(user)

''' Code you don't have to look at commences forth here '''
import os, shutil

import clean as f
import guard as g

list_ = os.listdir(path)

# main function
for file_ in list_:
    name, ext = os.path.splitext(file_)
    ext = ext[1:].lower()
    # folders and unknown files
    if ext == '':
        continue
    # samples (music)
    if ext == 'wav' or ext == 'mp3': # for music
        if name.__contains__(' - '): # track
            if(name.lower().__contains__('acapella')):
                g.ckdir(samplesPath + 'Acapellas')
                shutil.move(path + '/' + file_, samplesPath + '/Acapellas/' + file_)
            else:
                g.ckdir(samplesPath + '/Tracks')
                shutil.move(path + '/' + file_, samplesPath + '/Tracks/' + file_)
            print('Moving track: ' + file_)
            continue
        for drumTag in drumKeywords: # drum
            if name.lower().__contains__(drumTag.lower()):
                g.ckdir(samplesPath + '/Drums')
                f.filter(path, samplesPath + '/Drums', drumTag, file_)
                break
        if name.__contains__('bpm'): # loop
            g.ckdir(samplesPath + '/Loops')
            shutil.move(path + '/' + file_, samplesPath + '/Loops/' + file_)
        print("Can't sort this music sample chief")
    # documents
    elif ext == 'pdf' or ext == 'doc' or ext == 'docx': # for documents
        g.ckdir(docPath)
        moved = False
        for docTag in docKeywords:
            if name.lower().__contains__(docTag.lower()):
                g.ckdir(docPath)
                f.filter(path, docPath, docTag, file_, False, False)
                print('Moved document: ' + file_)
                moved = True
                break
        if not moved: # means keyword hasn't been found
            os.remove(path + '/' + file_)
            print('Deleted file: ' + file_)
    # images
    elif ext == 'heic' or ext == 'jpg' or ext == 'png':
        g.ckdir(photoPath)
        shutil.move(path + '/' + file_, photoPath + '/' + file_)
        print('Moved photo: ' + file_)
    # samples (music)
    elif clean:
        for e in cleanExts:
            if e == ext:
                os.remove(path + '/' + file_)
                print('Deleted file: %s' %(path + '/' + file_))