import tkinter as tk
from tkinter import Label
from tkinter import filedialog
import tkinter.font as tkFont
from PIL import Image, ImageTk
#https://pillow.readthedocs.io/en/stable/reference/ImageTk.html

#image uploader function
def imageUploader():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes=fileTypes)

    # if file is selected
    if len(path):
        img = Image.open(path)
        img = img.resize((200, 200))
        pic = ImageTk.PhotoImage(img)

        # re-sizing the app window in order to fit picture
        # and button
        window.geometry("560x300")
        label.config(image=pic)
        label.image = pic

    # if no file is selected, then we are displaying below message
    else:
        print("No file is Choosen !! Please choose a file.")

# Main method
if __name__ == "__main__":

    # defining tkinter object
    window = tk.Tk()
    FONT = tkFont.Font(family="Times")

    # setting title and basic size to our App
    window.title("Image Watermarking by Alis")
    window.minsize(400, 300)

    #welcome text
    welcome_label = Label(text="Welcome!\nYou're going to add the following logo:")
    welcome_label.config(font=FONT)
    welcome_label.pack()

    # adding background image
    img = ImageTk.PhotoImage(file='images/logo.png')
    imgLabel = Label(window, image=img)
    imgLabel.pack()

    #action text
    action_label = Label(text="Please upload your image:")
    action_label.config(font=FONT)
    action_label.pack()

    # adding background color to our upload button
    window.option_add("*Label*Background", "white")
    window.option_add("*Button*Background", "lightgreen")

    label = tk.Label(window)
    label.pack(pady=10)

#TODO Fai funzionare il bottone
    # defining our upload button
    uploadButton = tk.Button(window, text="Locate Image", command=imageUploader)
    uploadButton.pack(side=tk.BOTTOM, pady=20)

    window.mainloop()