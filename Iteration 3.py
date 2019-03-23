#Image Manipulation modules

from tkinter import *
from PIL import Image, ImageEnhance, ImageOps, ImageTk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile

#-----------------------
# INITIALISING VARIABLES
#-----------------------

imageOriginal = Image.new('RGB', (500, 500),'white')#creates the image imageOriginal
imageReset = Image.new('RGB', (500, 500),'white')#creates the image imageReset
imageOriginalsize = imageOriginal.size #calculates the image's dimensions

#------------------------
#------------------------

#-----------------------
# MODULES (SUBROUTINES)
#-----------------------

#-----------------------
# OPEN IMAGE SUBROUTINE
#-----------------------

def open_image():
    fullfilename = filedialog.askopenfilename(initialdir="/",
                                                      title="Open a file",
                                                      filetypes=[("Image files", "*.jpg; *.png"),
                                                      ("All Files","*.*")]) #allows the user to open a png or jpg image file from the directory
     
    if(fullfilename != ''): #conditional statement to ensure that a file has actually been chosen
        global imageOriginal #brings the global variable imageOriginal into the scope of the subroutine
        global imageOriginalsize #brings the global variable imageOriginalsize into the scope of the subroutine
        global imageReset #brings the global variable imageResize into the scope of the subroutine
        imageOriginal = Image.open(fullfilename).convert('RGB') #opens the image, passing the filename as the parameter
        imageReset = Image.open(fullfilename).convert('RGB') #opens a copy of the image and stores it in imageReset
        imageOriginal.thumbnail((500,500)) #creates a thumbnail image of imageOriginal to display it in the window
        imageReset.thumbnail((500,500)) #creates a copy of the thumbnail image
        imageDisplay = ImageTk.PhotoImage(imageOriginal) #creates a new variable imageDisplay which converts imageOriginal into a Tkinter readable format
        labelphoto.config(image = imageDisplay)
        labelphoto.photo_ref = imageDisplay #keep a reference
        labelphoto.grid()
        sizeLabel = Label(window,text=(imageOriginalsize[0],'x', imageOriginalsize[1]),fg="white",bg="gray25") #creates a label widget to display the image's size
        sizeLabel.grid(column=0,row=9,padx=10,pady=10) #positions the sizeLabel label widget

#-----------------------
# SAVE IMAGE SUBROUTINE
#-----------------------

def save_image():
    global imageOriginal #brings the global variable imageOriginal into the scope of the subroutine
    filename = filedialog.asksaveasfilename(initialdir = "/",
                                                  title = "Save file",
                                                  filetypes = (("JPEG files","*.jpg"),("All files","*.*")),
                                                  defaultextension=".jpg") #allows the user to save the edited image file into the directory
    imageOriginal.save(filename) #runs the in-built save function, passing the file name specified as the parameter

#------------------------------
# HELP FUNCTIONALITY SUBROUTINE
#------------------------------

def help_message():
    aboutWindow=Tk() #creates a new window, aboutWindow
    aboutWindow.geometry("500x200") #sets dimensions for the window
    aboutWindow.configure(background="gray22") #sets the colour as 'gray22'
    aboutWindow.title("Help") #title for the help functionality window
    aboutLabel = Label(aboutWindow,text="This is the Image Editor. To use, please enter the input corresponding to the desired editing option in the input box. Then, press 'Submit' to run the process. If you wish to close the Editor, please press 'Exit' in the top menu.",wraplength=400,bg="gray24",fg="white")
    aboutLabel.pack() #positions the label widget aboutLabel automatically
    OKButton = Button(aboutWindow,text="OK",width=10,command=openImage,bg="gray25",fg="white").pack() #creates and positions a button called 'OK' that will shut the window when pressed
    aboutWindow.mainloop()

#------------------------
# BRIGHTEN/DIM SUBROUTINE
#------------------------

def brightness_image():
    global imageOriginal
    en=ImageEnhance.Brightness(imageOriginal) #enables change in brightness
    #image_enhanced = en.enhance(float(input("Enter a value between 0 and 10: ")))
    if float(brightnessval.get()) < 0 or float(brightnessval.get()) > 10: #checks input is in range
        messagebox.showinfo("Error","Values outside of the range 0 to 10 are not permitted.") #if not, error message is output
    else: #if it's valid, program goes down 'else' route and carries out the procedure to edit the image
        imageOriginal = en.enhance(float(brightnessval.get()))
        #asks user for input of how bright the image should be
        imageDisplay = ImageTk.PhotoImage(imageOriginal)
        labelphoto.config(image = imageDisplay)
        labelphoto.photo_ref = imageDisplay #keep a reference
        labelphoto.grid() 
    
#------------------------
# CONTRAST SUBROUTINE
#------------------------

def contrast_image():
    global imageOriginal
    en=ImageEnhance.Contrast(imageOriginal) #enables contrasting
    #image_enhanced = en.enhance(float(input("Enter a value between 0 and 10: ")))
    if float(contrastval.get()) < 0 or float(contrastval.get()) > 10: #checks input is in range
      messagebox.showinfo("Error","Values outside of the range 0 to 10 are not permitted.") #if not, error message is output
    else: #if it's valid, program goes down 'else' route and carries out the procedure to edit the image
        imageOriginal = en.enhance(float(contrastval.get()))
        #asks user for input on how much to contrast the image by
        imageDisplay = ImageTk.PhotoImage(imageOriginal)
        labelphoto.config(image = imageDisplay)
        labelphoto.photo_ref = imageDisplay #keep a reference
        labelphoto.grid()

#------------------------
# SATURATE SUBROUTINE
#------------------------

def saturate_image():
    global imageOriginal
    en=ImageEnhance.Color(imageOriginal) #enables saturation
    imageOriginal = en.enhance(float(saturateval.get()))
    #asks user for input of how much saturation they would like
    imageDisplay = ImageTk.PhotoImage(imageOriginal)
    labelphoto.config(image = imageDisplay)
    labelphoto.photo_ref = imageDisplay #keep a reference
    labelphoto.grid()

#------------------------
# BLUR SUBROUTINE
#------------------------

def blursharpen_image():
    global imageOriginal
    en=ImageEnhance.Sharpness(imageOriginal) #enables blur/sharpening
    #image_enhanced = en.enhance(float(input("Enter a value between -10 and 10: ")))
    if int(blurval.get()) < -10 or int(blurval.get()) > 10: #checks input is in range
      messagebox.showinfo("Error","Values outside of the range -10 to 10 are not permitted.") #if not, error message is output
    else: #if it's valid, program goes down 'else' route and carries out the procedure to edit the image
        imageOriginal = en.enhance(float(blurval.get()))
        #asks user for input on how sharp/blurred they want the image
        imageDisplay = ImageTk.PhotoImage(imageOriginal)
        labelphoto.config(image = imageDisplay)
        labelphoto.photo_ref = imageDisplay #keep a reference
        labelphoto.grid() 

#------------------------
# FILTER SUBROUTINE
#------------------------

#colours that can be used:
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
RED = (236,11,31)
BLUE = (17, 95, 251)
GREEN = (62, 180, 42)
ORANGE =(255,128,0)
PINK = (255,51,255)
TURQUOISE = (0,255,255)
FUCHSIA = (255,0,127)

def filter_image():
    global imageOriginal
    imageGrayscale = ImageOps.grayscale(imageOriginal)
    imageOriginal = ImageOps.colorize(imageGrayscale,filterval.get(),filterval1.get())
    #colorizes the image as per the user's input
    imageDisplay = ImageTk.PhotoImage(imageOriginal)
    labelphoto.config(image = imageDisplay)
    labelphoto.photo_ref = imageDisplay #keep a reference
    labelphoto.grid() 


#------------------------
# FLIP SUBROUTINE
#------------------------

def flip_horizontal():
    global imageOriginal
    imageOriginal = imageOriginal.transpose(Image.FLIP_LEFT_RIGHT) #transposes the image vertically
    imageDisplay = ImageTk.PhotoImage(imageOriginal)
    labelphoto.config(image = imageDisplay)
    labelphoto.photo_ref = imageDisplay #keep a reference
    labelphoto.grid() 

def flip_vertical():
    global imageOriginal
    imageOriginal = imageOriginal.transpose(Image.FLIP_TOP_BOTTOM) #transposes the image horizontally
    imageDisplay = ImageTk.PhotoImage(imageOriginal)
    labelphoto.config(image = imageDisplay)
    labelphoto.photo_ref = imageDisplay #keep a reference
    labelphoto.grid() 

def flip_input():
    #flip_orientation = input("How would you like to flip your image? For Left-Right, type 1, for Top-Bottom, type 2: ")
    flip_orientation = flipval.get() #asks user for input of how to flip the image
    #carries out user's request using conditional statements
    if flip_orientation == "1": #checks input is either 1 or 2
      print(flip_horizontal())
    elif flip_orientation == "2":
      print(flip_vertical())
    else:
      messagebox.showinfo("Error","Please type 1 or 2, other values are not permitted.") #if not, error message is output

#------------------------
# RESIZE SUBROUTINE
#------------------------

def resize_image():
    global imageOriginal
    xval = int(imageOriginal.size[0])
    yval = int(imageOriginal.size[1])
    if int(resizexval.get()) < 0 or int(resizexval.get()) > xval+1000: #checks input is in range
        messagebox.showinfo("Error","Invalid width input. Width input must be less than " + str(xval+1000) + ".") #if not, error message is output
    elif int(resizeyval.get()) < 0 or int(resizeyval.get()) > yval+1000: #checks input is in range
        messagebox.showinfo("Error","Invalid height input. Height input must be less than " + str(yval+1000) + ".") #if not, error message is output
    else: #if it's valid, program goes down 'else' route and carries out the procedure to edit the image
        imageOriginal = imageOriginal.resize((int(resizexval.get()),int(resizeyval.get())))
        #asks user for input on width and height
        sizeLabel = Label(window,text=(int(resizexval.get()),'x', int(resizeyval.get())),fg="white",bg="gray25").grid(column=0,row=9,padx=10,pady=10)
        imageDisplay = ImageTk.PhotoImage(imageOriginal)
        labelphoto.config(image = imageDisplay)
        labelphoto.photo_ref = imageDisplay #keep a reference
        labelphoto.grid()

#------------------------
# ROTATE SUBROUTINE
#------------------------

def rotate_image():
    global imageOriginal
    if int(rotateval.get()) < 0 or int(rotateval.get()) > 360: #checks input is in range
      messagebox.showinfo("Error","Values outside of the range 0 to 360 are not permitted.") #if not, error message is output
    else: #if it's valid, program goes down 'else' route and carries out the procedure to edit the image
      #image_rotated = image.rotate(int("Enter a degree to rotate by: ")),expand=True)
      imageOriginal = imageOriginal.rotate(360-int(rotateval.get()),expand=True) 
      #asks user for angle input, 'expand' makes sure that the new image fits
      imageDisplay = ImageTk.PhotoImage(imageOriginal)
      labelphoto.config(image = imageDisplay)
      labelphoto.photo_ref = imageDisplay #keep a reference
      labelphoto.grid()

#------------------------
# CROP SUBROUTINE
#------------------------

def crop_imageops():
    global imageOriginal
    #cropped_image = ImageOps.crop(image,border=int(input("Enter a number to crop by: ")))
    imageOriginal = ImageOps.crop(imageOriginal,border=int(cropval.get()))
    #asks user for input of pixels to crop the image by, in both dimensions
    imageDisplay = ImageTk.PhotoImage(imageOriginal)
    labelphoto.config(image = imageDisplay)
    labelphoto.photo_ref = imageDisplay #keep a reference
    labelphoto.grid()

#------------------------
#------------------------

#-----------------------
# DEVELOPING A NEW WINDOW
#-----------------------

window = Tk() #initialises a new window as 'window' using tkinter
window.geometry("1600x1150") #sets dimensions for the window
window.state("zoomed") #makes the window take up the full space of the screen on load-up
window.title("Image Editor v1.9")#title for the application window

window.resizable(True, True) #allows user to resize the window
window.configure(background = "gray22") #sets the colour as 'gray22'

#Below are the variables as 'StringVar()' data type for use in the algorithms in back-end. They are taken from entry fields:

imageDisplay = ImageTk.PhotoImage(imageOriginal)
brightnessval = StringVar()
resizexval = StringVar()
resizeyval = StringVar()
rotateval = StringVar()
blurval = StringVar()
flipval = StringVar()
contrastval = StringVar()
saturateval= StringVar()
cropval = StringVar()
filterval = StringVar()
filterval.set("BLACK")
filterval1 = StringVar()
filterval1.set("WHITE")

menu = Menu(window) #Creates a menubar at the top of the window to display 'Open', 'Save' and 'Exit'
window.config(menu=menu)

file = Menu(menu)

window.config(menu=file)

file.add_command(label = 'Open', command = open_image) #creates a new menu item to open the image, passing the open_image subroutine as the command
file.add_command(label = 'Save', command = save_image) #creates a new menu item to save the image, passing the save_image subroutine as the command
file.add_command(label = "Help", command = help_message) #creates a new menu item to activate the help functionality, passing the help_message subroutine as the command
file.add_command(label = 'Exit', command = lambda:exit()) #creates a new menu item to close the window and stop running the program

labelphoto = Label(window,image=imageDisplay) #Creates a label widget to allow display of the image in the window
labelphoto.imageDisplay = imageDisplay #keeps a reference
labelphoto.grid(column=2,row=9,padx=10,pady=10) #places the label widget in a specified location on the window, using a grid

#------------------------
#------------------------

#-----------------------
# DEVELOPING MAIN UI
#-----------------------

#-----------------------

brightnessLabel = Label(window,text="Brightness",bg="gray24",fg="white") #creates a label widget to identify the Brightness function
brightnessLabel.grid(row = 0, column = 0, padx = 10, pady=10) #sets dimensions of the label widget
brightnessSlider = Scale(window,bg="gray25",fg="white",from_=0,to=5,tickinterval=1,variable=brightnessval,
                         orient=HORIZONTAL,length=500,troughcolor="gray30",highlightbackground="gray25",resolution=0.1,width=7,sliderlength=35) #creates a slider to adjust the brightness
brightnessSlider.grid(row=0,column=2,padx=5,pady=1) #sets dimensions of the scale widget
brightnessSubmit = Button(window,text="Submit",width=10,command=brightness_image,bg="gray25",fg="white").grid(row=0,column=5,padx=5,pady=5)
#creates button that runs the Brightness function, passing the value of the slider as the input

#-----------------------

contrastLabel = Label(window,text="Contrast",bg="gray24",fg="white") #creates a label widget to identify the Contrast function
contrastLabel.grid(row = 1, column = 0, padx = 10, pady=10) #sets dimensions of the label widget
contrastSlider = Scale(window,bg="gray24",fg="white",from_=0,to=5,tickinterval=1,variable=contrastval,
                       orient=HORIZONTAL,length=500,troughcolor="gray30",highlightbackground="gray24",resolution=0.1,width=7,sliderlength=35) #creates a slider to adjust the contrast
contrastSlider.grid(row=1,column=2,padx=5,pady=1) #sets dimensions of the scale widget
contrastSubmit = Button(window,text="Submit",width=10,command=contrast_image,bg="gray25",fg="white").grid(row=1,column=5,padx=5)
#creates button that runs the Contrast function, passing the value of the slider as the input

#-----------------------

saturateLabel = Label(window,text="Saturate",bg="gray24",fg="white") #creates a label widget to identify the Saturate function
saturateLabel.grid(row = 2, column = 0, padx = 10, pady=10) #sets dimensions of the label widget
saturateSlider = Scale(window,bg="gray24",fg="white",from_=0,to=5,tickinterval=1,variable=saturateval,
                       orient=HORIZONTAL,length=500,troughcolor="gray30",highlightbackground="gray24",resolution=0.1,width=7,sliderlength=35) #creates a slider to adjust the saturation
saturateSlider.grid(row=2,column=2,padx=5,pady=1) #sets dimensions of the scale widget
saturateSubmit = Button(window,text="Submit",width=10,command=saturate_image,bg="gray25",fg="white").grid(row=2,column=5,padx=5)
#creates button that runs the Saturate function, passing the value of the slider as the input

#-----------------------

blurLabel = Label(window,text="Sharpen/Blur",bg="gray24",fg="white") #creates a label widget to identify the Blur/Sharpen function
blurLabel.grid(row = 3, column = 0, padx = 10, pady=10) #sets dimensions of the label widget
blurSlider = Scale(window,bg="gray24",fg="white",from_=-5,to=5,tickinterval=1,variable=blurval,
                   orient=HORIZONTAL,length=500,troughcolor="gray30",highlightbackground="gray24",resolution=1,width=7,sliderlength=35) #creates a slider to adjust the sharpness
blurSlider.grid(row=3,column=2,padx=5,pady=1) #sets dimensions of the scale widget
blursubmit = Button(window,text="Submit",width=10,command=blursharpen_image,bg="gray25",fg="white").grid(row=3,column=5,padx=5)
#creates button that runs the Blur/Sharpen function, passing the value of the slider as the input

#-----------------------

filterLabel = Label(window,text="Filter",bg="gray24",fg="white") #creates a label widget to identify the Filter function
filterLabel.grid(row = 4, column = 0, padx = 10, pady=10) #sets dimensions of the label widget
filterMenu = OptionMenu(window,filterval,"BLACK","WHITE","YELLOW","RED","BLUE","GREEN","ORANGE","PINK","TURQUOISE","FUCHSIA") #creates an Option Menu to change the first colour
filterMenu.grid(row=4,column=3,padx=10,pady=10) #sets dimensions of the OptionMenu widget
filter1Menu = OptionMenu(window,filterval1,"BLACK","WHITE","YELLOW","RED","BLUE","GREEN","ORANGE","PINK","TURQUOISE","FUCHSIA") #creates an Option Menu to change the second colour
filter1Menu.grid(row=4,column=4,padx=10,pady=10) #sets dimensions of the OptionMenu widget
filter1submit = Button(window,text="Submit",width=10,command=filter_image,bg="gray25",fg="white").grid(row=4,column=5,padx=5,pady=5)
#creates button that runs the Blur/Sharpen function, passing the values of the two filter Option Menus as the inputs

#-----------------------

flipLabel = Label(window,text="Flip",bg="gray24",fg="white") #creates a label widget to identify the Flip function
flipLabel.grid(row = 5, column = 0, padx = 10, pady=15) #sets dimensions of the label widget
flipMenu = OptionMenu(window,flipval,"1","2").grid(row=5,column=3,padx=5) #creates an Option Menu to change the orientation of the flip, and sets dimensions
flipSubmit = Button(window,text="Submit",width=10,command=flip_input,bg="gray25",fg="white").grid(row=5,column=5,padx=5)
#creates button that runs the Flip function, passing the value of the Option Menu as the input

#-----------------------

resizeLabel = Label(window,text="Resize",bg="gray24",fg="white") #creates a label widget to identify the Resize function
resizeLabel.grid(row = 6, column = 0, padx = 10, pady=15) #sets dimensions of the label widget
xvalEntry = Entry(window,textvariable=resizexval,width=5).grid(row=6,column=3,padx=5) #creates an Entry box to set the x-value for resizing the image, and sets dimensions
yvalEntry = Entry(window,textvariable=resizeyval,width=5).grid(row=6,column=4,padx=5) #creates an Entry box to set the y-value for resizing the image, and sets dimensions
resizesubmit = Button(window,text="Submit",width=10,command=resize_image,bg="gray25",fg="white").grid(row=6,column=5,padx=5)
#creates button that runs the Resize function, passing the x- and y-values as the input

#-----------------------

rotateLabel = Label(window,text="Rotate",bg="gray24",fg="white") #creates a label widget to identify the Rotate function
rotateLabel.grid(row = 7, column = 0, padx = 10, pady=15) #sets dimensions of the label widget
rotateentry = Entry(window,textvariable=rotateval,width=5).grid(row=7,column=3,padx=5) #creates an Entry box to set the rotation degree for rotating the image, and sets dimensions
rotatesubmit = Button(window,text="Submit",width=10,command=rotate_image,bg="gray25",fg="white").grid(row=7,column=5,padx=5)
#creates button that runs the Rotate function, passing the rotation degree value as the input

#-----------------------

cropLabel = Label(window,text="Crop",bg="gray24",fg="white") #creates a label to identify the Crop function
cropLabel.grid(row = 8, column = 0, padx = 10, pady=15) #sets dimensions of the label widget
cropentry = Entry(window,textvariable=cropval,width=5).grid(row=8,column=3,padx=5) #creates an Entry box to set the crop value for cropping the image, and sets dimensions
cropsubmit = Button(window,text="Submit",width=10,command=crop_imageops,bg="gray25",fg="white").grid(row=8,column=5,padx=5)
#creates button that runs the Crop function, passing the crop value as the input

#-----------------------



#-----------------------

window.mainloop()

#------------------------
#------------------------
