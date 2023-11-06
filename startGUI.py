import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("GUI Starter")
root.iconbitmap('myImage.png')

quitButton = tk.Button(root, text="X", command=root.quit)
quitButton.pack()

myImage = ImageTk.PhotoImage(Image.open("myImage.png"))
label = tk.Label(root, image=myImage, width=300)
label.pack()

root.mainloop()