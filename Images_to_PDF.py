import os
path = "C:/Users/anand/OneDrive/Desktop/Data Science/Python Programs/R Programming/"
files = os.listdir(path)
'''
# Renaming the files according to the reauirement
# This is for removing paranthesis in screenshots folder
for j in range(len(files)):
    fileName = files[j]
    newName = ""
    for i in range(len(fileName)):
        exceptions = ["(", ")"]
        if (fileName[i] not in exceptions):
            newName += fileName[i]
        else:
            newName = newName
    files[j] = newName
    # Renamig the files
    os.rename(path+fileName, path+newName)
'''

from PIL import Image

imageList = []

for file in files:
    imageList.append((Image.open(r'{}{}'.format(path,file))).convert('RGB'))
imageList[0].save(r'{}Converted.pdf'.format(path), save_all = True, append_images = imageList)
