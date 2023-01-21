#modules
from tkinter import *
import customtkinter
import subprocess
from PIL import Image, ImageTk


#function sto call
print("bye")
def adi():
	subprocess.call("C:/Users/Aditya/AppData/Local/Programs/Microsoft VS Code/Code.exe")

def adi1():
	subprocess.call('C:/Windows/System32/SlideToShutDown.exe')

def adi2():
	subprocess.call("C:/Program Files/Adobe/Adobe Photoshop 2022/Photoshop.exe")

def adi3():
	subprocess.call("C:/Program Files/Blackmagic Design/DaVinci Resolve/Resolve.exe")

def adi4():
	subprocess.call("C:/Users/Aditya/AppData/Local/MongoDBCompass/MongoDBCompass.exe")

def adi5():
	subprocess.call("C:/Program Files/MySQL/MySQL Workbench 8.0/MySQLWorkbench.exe")

def adi6():
	subprocess.call("C:/Program Files/JetBrains/PyCharm Community Edition 2021.3.3/bin/pycharm64.exe")

def adi7():
	subprocess.call("C:/Program Files/Blender Foundation/Blender 3.3/blender-launcher.exe")




#tkinter
root = customtkinter.CTk()
customtkinter.set_appearance_mode("black")
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
bg = PhotoImage(file='C:/Users/Aditya/Downloads/612520.png')

# Create Canvas
canvas1 = Canvas()
canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0,0,image=bg,anchor="nw")
root.title('Levi')

#screen size
root.geometry("1080x720")

#buttons
add_folder_image = ImageTk.PhotoImage(Image.open('C:/Users/Aditya/Downloads/vs.jpg').resize((300,200)))
button = customtkinter.CTkButton(master=root, image=add_folder_image, text="",command=adi)
button.place(x=150,y=70)

add_folder_image1 = ImageTk.PhotoImage(Image.open('C:/Users/Aditya/Downloads/ss.jpg').resize((300,200)))
button_1 = customtkinter.CTkButton(master=root, image=add_folder_image1, text="",command=adi1)
button_1.place(x=650,y=70)

add_folder_image2 = ImageTk.PhotoImage(Image.open('C:/Users/Aditya/Downloads/ps.jpg').resize((300,200)))
button_2 = customtkinter.CTkButton(master=root, image=add_folder_image2, text="",command=adi2)
button_2.place(x=1150,y=70)

add_folder_image3 = ImageTk.PhotoImage(Image.open('C:/Users/Aditya/Downloads/dr.jpg').resize((300,200)))
button_3 = customtkinter.CTkButton(master=root, image=add_folder_image3, text="",command=adi3)
button_3.place(x=150,y=600)

add_folder_image4 = ImageTk.PhotoImage(Image.open('C:/Users/Aditya/Downloads/mdb.png').resize((300,200)))
button_4 = customtkinter.CTkButton(master=root, image=add_folder_image4, text="",command=adi4)
button_4.place(x=650,y=600)

add_folder_image5 = ImageTk.PhotoImage(Image.open('C:/Users/Aditya/Downloads/ms.png').resize((300,200)))
button_5 = customtkinter.CTkButton(master=root, image=add_folder_image5, text="",command=adi5)
button_5.place(x=1150,y=600)

add_folder_image6 = ImageTk.PhotoImage(Image.open('C:/Users/Aditya/Downloads/pc.png').resize((300,200)))
button_6 = customtkinter.CTkButton(master=root, image=add_folder_image6, text="",command=adi6)
button_6.place(x=150,y=335)

add_folder_image7 = ImageTk.PhotoImage(Image.open('C:/Users/Aditya/Downloads/b.jpg').resize((300,200)))
button_7 = customtkinter.CTkButton(master=root, image=add_folder_image7, text="",command=adi7)
button_7.place(x=1150,y=335)



root.mainloop()

