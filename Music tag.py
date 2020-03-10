# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:41:24 2019

@author: Tijesunimi.Adebiyi
"""
import os
import shutil
from pathlib import Path # because to iterate files in folder
from mutagen.id3 import ID3

p = "C:\\Users\\tijesunimi.adebiyi\\Documents\\Python Scripts\\Test2"
myfolder = os.path.normpath(p)
#audio = ID3('Matt Redman  Songs In The Night.mp3') #path: path to file


pathlist = Path(p).glob('**/*.mp3')
for path in pathlist:
    audio = ID3(path) #path: path to file
    #Get music details
    artiste = audio.get('TPE1')
    album = audio.get('TALB')

    #Check if file has artist tag. Create folder accordingly
    if(artiste):
        #print(artiste.text[0].title())
        
        newFolder = os.path.join(myfolder,artiste.text[0].title())
        os.makedirs(newFolder, exist_ok = True)
        
        
    else:
        newFolder = os.path.join(myfolder,"Unknown")
        os.makedirs(newFolder, exist_ok = True)
        
    
    #move file to folder
    fileNameList = str(path).split('\\')
    fileName = fileNameList[len(fileNameList)-1]
    print(fileName)
    shutil.move(path,  os.path.join(newFolder,fileName))

