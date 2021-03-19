from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import Image
import fnmatch


root = tk.Tk()
# getting screen's height in pixels 
# screenHeight = root.winfo_screenheight()/2
  
# getting screen's width in pixels 
# screenWidth = root.winfo_screenwidth()/2
# Creating a Canvas
canvas1 = tk.Canvas (root, width = 600, height = 400, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

# Creating a heading
heading = tk.Label(root, text = 'Images to PDF Conversion Tool', bg = 'lightsteelblue2')
heading.config(font = ('helvetica',20, 'bold'))
canvas1.create_window(300, 40, window = heading)

# Select folder path Label
selectPath = tk.Label(root, text = 'Select the Folder Path : ', bg = 'lightsteelblue2')
selectPath.config(font = ('helvetica', 14))
canvas1.create_window(200, 100, window = selectPath)

# Function for getting directory path from browse input
def getDirectoryPath():
    global imageName
    global import_file_path
    import_file_path = filedialog.askdirectory()
       
    # Displaying the selected path
    global selectedPath
    selectedPath = tk.Label(root, text = '{}'.format(import_file_path), bg = 'lightsteelblue2')
    selectedPath.config(font = ('helvetica', 9))
    canvas1.create_window(300, 140, window = selectedPath)


# Browse or selecting the path button
browseButton = tk.Button(root, text = "    Browse    ", command = getDirectoryPath, bg = 'green', fg = 'white', font = ('helvetica', 12, 'bold'))
canvas1.create_window(400, 100, window = browseButton)    

# Input file name Label
inputFileNameLabel = tk.Label(root, text = 'Enter the output filename : ', bg = 'lightsteelblue2')
inputFileNameLabel.config(font = ('helvetica', 14))
canvas1.create_window(200, 180, window = inputFileNameLabel)

# Taking fileneame from user to save pdf file
outputFileNameStr = tk.StringVar()
outputFileName = tk.Entry(root, textvariable = outputFileNameStr, bg = 'white', relief= 'raised', font=('helvetica', 14))
canvas1.create_window(450,180, window = outputFileName)

# Function to convert thse given images to pdf
def convertToPDF():
    # Taking path to the directory
    path = import_file_path
    files = os.listdir(path)
    imageList = []
    
    # Converting the images to pdf file
    # The Heart of the program
    for file in files:
        if ((fnmatch.fnmatch(file, '*.png')) or (fnmatch.fnmatch(file, '*.jpg')) or (fnmatch.fnmatch(file, '*.jpeg'))):
            imageList.append((Image.open(r'{}/{}'.format(path,file))).convert('RGB'))
    imageList[0].save(r'{}/{}.pdf'.format(path,outputFileNameStr.get()), save_all = True, append_images = imageList)
    
    # Task started
    taskStartedMessage = tk.messagebox.showinfo('Processing...','Your files are being converted...' )
    
    # Task Complete Message
    taskCompletedMessage = tk.messagebox.showinfo('Completed','Successfully conveted to PDF...' )
    
    # Calling resetLayout function
    resetLayout()

def resetLayout():
    # Emptying the inputs
    outputFileName = tk.Entry(root, textvariable = "", bg = 'white', relief= 'raised', font=('helvetica', 14))
    canvas1.create_window(450,180, window = outputFileName)
    
    # Resetting the selected path
    selectedPath.destroy()
    
    # selectedPath = tk.Label(root, text = "", bg = 'lightsteelblue2')
    # selectPath.config(font = ('helvetica', 14))
    # canvas1.create_window(300, 140, window = selectedPath)
   

# Save as Button 
convertToPDFButton = tk.Button(root, text = ' Convert to PDF ', command = convertToPDF, bg = 'green', fg = 'white', font = ('helvetica', 12, 'bold'))
canvas1.create_window(300, 250, window = convertToPDFButton)

# Exiting the application
def exitApplication():
    messageBox = tk.messagebox.askquestion('Exit Application','Are you sure, you want to exit the application?', icon = 'warning')
    if messageBox == 'yes':
        root.destroy()
exitButton = tk.Button(root, text = 'Exit Application', command = exitApplication, bg = 'brown', fg = 'white', font = ('helvetica', 12, 'bold'))
canvas1.create_window(300, 350, window = exitButton)


root.mainloop()