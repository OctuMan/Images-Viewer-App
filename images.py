# Import Modules 
from tkinter import * 
from tkinter import ttk
from PIL import ImageTk, Image

# the root window
root = Tk()
root.title('Image Manupilation')
root.geometry("620x600")
root.minsize('620','600')
root.maxsize('620','600')

# defining functions 
def back():
    '''This function is for displaying the previeus image'''

    global img_counter
    # Update the existing label with the new image
    if img_counter > 0:
        img_counter -= 1
    else:
        img_counter = len(liste_images)-1
    lb.config(image=liste_images[img_counter])
       
def next():
    '''This function is for displaying the next image'''
    global img_counter

    # Update the existing label with the new image
    if img_counter < len(liste_images) - 1:
        img_counter += 1
    else:
        img_counter = 0

    lb.config(image=liste_images[img_counter])

# Frames for our app 
fr1=Frame(width='50', height='500' )
fr1.place(x=5, y=260)

fr2=Frame(width='300', height='500')
fr2.place(x=50, y=0)

fr3=Frame(width='50', height='500' )
fr3.place(x=575, y=260)

# Icons for next and back buttons 

back_image=ImageTk.PhotoImage(Image.open(r"C:\Users\said\Desktop\Python\TkinterGUI\ImagesGUI\back-icon.png"))
next_image=ImageTk.PhotoImage(Image.open(r"C:\Users\said\Desktop\Python\TkinterGUI\ImagesGUI\next-icon.png"))

# importing all images 

i1=ImageTk.PhotoImage(Image.open(r"C:\Users\said\Desktop\Python\TkinterGUI\ImagesGUI\python.png"))
i2=ImageTk.PhotoImage(Image.open(r"C:\Users\said\Desktop\Python\TkinterGUI\ImagesGUI\sql-server.png"))
i4=ImageTk.PhotoImage(Image.open(r"C:\Users\said\Desktop\Python\TkinterGUI\ImagesGUI\git.png"))
i5=ImageTk.PhotoImage(Image.open(r"C:\Users\said\Desktop\Python\TkinterGUI\ImagesGUI\html-5.png"))
i6=ImageTk.PhotoImage(Image.open(r"C:\Users\said\Desktop\Python\TkinterGUI\ImagesGUI\css-3.png"))
i7=ImageTk.PhotoImage(Image.open(r"C:\Users\said\Desktop\Python\TkinterGUI\ImagesGUI\js.png"))
i8=ImageTk.PhotoImage(Image.open(r"C:\Users\said\Desktop\Python\TkinterGUI\ImagesGUI\coding.png"))

# List of images
liste_images=[i1, i2, i4, i5, i6, i7, i8]

img_counter = len(liste_images)-1

# the label widget to display images 
lb=Label(fr2, image=i1)
lb.grid()

# Next and back images 
btn = Button(fr1, image=back_image,
                command=lambda: back()) 
btn.grid()

btn1 = Button(fr3,image=next_image,
             command=lambda: next())
btn1.grid()



root.mainloop()