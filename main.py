import tkinter as tk
from tkinter import Label
from tkinter import filedialog, messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk

#image uploader function
def imageUploader():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes=fileTypes)

    # if file is selected
    if len(path):
        logo = Image.open('images/logo.png')
        image = Image.open(path)

        # RIDIMENSIONAMENTO AUTOMATICO
        # Scegli la percentuale di spazio che il logo deve occupare (es. 20% della larghezza della foto)
        percentage = 0.20
        new_width = int(image.size[0] * percentage)

        # Calcola l'altezza proporzionale per non distorcere il logo
        proportion = new_width / logo.size[0]
        new_height = int(logo.size[1] * proportion)

        # Ridimensiona il logo usando il filtro Resampling.LANCZOS per la massima qualità
        logo = logo.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # 2. Calcola le coordinate per l'angolo in basso a destra
        # Sottraiamo le dimensioni del logo da quelle dell'immagine principale
        img_w, img_h = image.size
        logo_w, logo_h = logo.size

        x = img_w - logo_w
        y = img_h - logo_h

        # 3. Incolla il logo usando se stesso come maschera (gestisce la trasparenza)
        image.paste(logo, (x, y), mask=logo)

        # 4. Salva il risultato
        image.save("../../../pic_with_logo.jpg")
        # image.save("images/pic_with_logo.jpg")
        tk.messagebox.showinfo("Done!", message="Your new image has been saved!")
    # if no file is selected, then we are displaying below message
    else:
        tk.messagebox.showerror("No file chosen!!", message="Please choose a file.")

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