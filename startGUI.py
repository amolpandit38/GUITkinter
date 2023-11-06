import tkinter as tk

root = tk.Tk()

def ButtonClicked():
    label = tk.Label(root, text=entry.get())
    label.pack()

entry = tk.Entry(root, width=50, bg="white", borderwidth=5)
entry.pack()
entry.insert(0, "Default Value")

# this is how you write a label
button = tk.Button(root, text= "A button", state="normal", command=ButtonClicked)
button.pack()

root.mainloop()