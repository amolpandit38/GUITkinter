import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()


def forward(number):
    imageLabel.config(image=imageList[number-1])
    forwardButton.config(command=lambda:forward(number+1))
    backButton.config(state='normal', command=lambda:back(number-1))

    statusBar.config(text=f"Image {str(number)} of {str(len(imageList))}")
    if number == len(imageList):
        forwardButton.config(state="disabled")
    
    
def back(number):
    imageLabel.config(image=imageList[number-1])
    forwardButton.config(command=lambda:forward(number+1), state="normal")
    backButton.config(state='normal', command=lambda:back(number-1))

    statusBar.config(text=f"Image {str(number)} of {str(len(imageList))}")
    if number == 1:
        backButton.config(state="disabled")


image1 = ImageTk.PhotoImage(Image.open('myImage.png'))
image2 = ImageTk.PhotoImage(Image.open('myImage.png'))
image3 = ImageTk.PhotoImage(Image.open('myImage.png'))
image4 = ImageTk.PhotoImage(Image.open('myImage.png'))
image5 = ImageTk.PhotoImage(Image.open('myImage.png'))

imageList = [image1, image2, image3, image4, image5]

imageLabel = tk.Label(root, image=image1, width=600)
imageLabel.grid(column=0, row=0, columnspan=3)

statusBar = tk.Label(root, text="Image 1 of 5", bd=1, relief="sunken", anchor="w")

backButton = tk.Button(root, text="<<", command=back, state="disabled")
exitButton = tk.Button(root, text="Exit program", command=root.quit)
forwardButton = tk.Button(root, text=">>", command=lambda: forward(2))

backButton.grid(column=0, row=1)
exitButton.grid(column=1, row=1)
forwardButton.grid(column=2, row=1)
statusBar.grid(column=0, row=2, columnspan=3, sticky="we")

root.mainloop()