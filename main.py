from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
#https://pillow.readthedocs.io/en/stable/reference/ImageTk.html

#Images
size = (102.4, 84.5)
logo = Image.open("images/logo.png")
logo.thumbnail(size)
logo.save("images/logo.png", "PNG")
# im = Image.open("images/priscilla.jpg")

#Tk
window = Tk()
FONT = tkFont.Font(family="Times")
window.title("Image Watermarking by Alis")
window.minsize(400, 300)

canvas = Canvas(width=600, height=450, bg="white")
welcome_text = canvas.create_text(300, 75, text="Welcome!", font=(FONT, 20))
ask_text = canvas.create_text(300, 125, text="You're going to add the following logo:", font=(FONT, 16))
logo_img = ImageTk.PhotoImage(file="images/logo.png")
canvas.create_image(300, 200, image=logo_img)
action_text = canvas.create_text(200, 280, text="Please upload your image:", font=(FONT, 12))
canvas.pack()

#TODO uploader function: https://www.geeksforgeeks.org/python/browse-upload-display-image-in-tkinter/

window.mainloop()