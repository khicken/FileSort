import os

# directory safeguard, nothing else hahahahaha
def ckdir(path):
    if(os.path.exists(path)):
        return
    os.mkdir(path)
    print('Created new directory: ' + path)