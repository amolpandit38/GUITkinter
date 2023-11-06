import tkinter as tk

root = tk.Tk()

def ButtonClicked():
    label = tk.Label(root, text="Clicked a button!")
    label.pack()

# this is how you write a label
button = tk.Button(root, text= "A button", state="normal", command=ButtonClicked)
button.pack()

root.mainloop()