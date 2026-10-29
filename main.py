import tkinter as tk
from tkinter import Label
from tkinter import filedialog
import tkinter.font as tkFont
from PIL import Image, ImageTk
#https://pillow.readthedocs.io/en/stable/reference/ImageTk.html

#TODO RISOLVI IL PROBLEMA COL PASTE PER IL WATERMARK; dopo togli i resize e fai salvare in automatico nuova img, non mostrarla
#image uploader function
def imageUploader():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes=fileTypes)

    # if file is selected
    if len(path):
        image = Image.open(path)
        image = image.resize((200, 200))
        image_width, image_height = image.size
        image_sheet = Image.new("RGB", (image_width, image_height))
        image_sheet.paste(image)
        box = (100, 100, 0, 0)
        # image_sheet.paste(logo, box, 255)
        pic = ImageTk.PhotoImage(image)

        # re-sizing the app window in order to fit picture
        # and button
        window.geometry("560x300")
        label.config(image=pic)
        label.image = pic

    # if no file is selected, then we are displaying below message
    else:
        print("No file is chosen !! Please choose a file.")

# Main method
if __name__ == "__main__":

    # defining tkinter object
    window = tk.Tk()
    FONT = tkFont.Font(family="Times")

    # setting title and basic size to our App
    window.title("Image Watermarking by Alis")
    window.geometry("560x270")

    #welcome text
    welcome_label = Label(text="Welcome!\nYou're going to add the following logo:")
    welcome_label.config(font=FONT)
    welcome_label.pack()

    # adding background image
    logo = ImageTk.PhotoImage(file='images/logo.png')
    logoLabel = Label(window, image=logo)
    logoLabel.pack()

    #action text
    action_label = Label(text="Please upload your image:")
    action_label.config(font=FONT)
    action_label.pack()

    # adding background color to our upload button
    window.option_add("*Label*Background", "white")
    window.option_add("*Button*Background", "lightgreen")

    label = tk.Label(window)
    label.pack(pady=10)

    # defining our upload button
    uploadButton = tk.Button(window, text="Locate Image", command=imageUploader)
    uploadButton.pack(side=tk.BOTTOM, pady=20)

    window.mainloop()