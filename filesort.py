import os
import shutil
path = ((os.path.dirname(os.path.realpath(__file__)))+"/")
print(path)
names = os.listdir(path)
print(names)
folder = ['Images', 'Documents', 'Videos', 'Audio']
for i in range(0, 4):
    if not os.path.exists(path+folder[i]):
        os.makedirs(path+folder[i])
images = ['.png', '.jpg', '.bmp', ' .gif', '.tiff', '.dng', '.bmp']
documents = ['.txt', '.pdf', '.doc', '.xls', '.ppt', '.xml', '.odt', '.ods', '.odp']
videos = ['.avi', '.mp4', '.wmv', '.flv', '.mov']
audio = ['.mp3', '.ogg', '.aac', '.flac', '.wav', '.3gp']
for files in names:
    for i in images:
        if i in files.lower() and not os.path.exists(path+'Images/'+files):
            shutil.move(path+files, path+'Images/'+files)
    for i in documents:
        if i in files and not os.path.exists(path+'Documents/'+files):
            shutil.move(path+files, path+'Documents/'+files)
    for i in videos:
        if i in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(path+files, path+'Videos/'+files)
    for i in audio:
        if i in files and not os.path.exists(path+'Audio/'+files):
            shutil.move(path+files, path+'Audio/'+files)

