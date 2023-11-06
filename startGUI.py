import tkinter as tk

root = tk.Tk()

# this is how you write a label
label1 = tk.Label(root, text="This is a label")
label2 = tk.Label(root, text="This is a label")

label1.grid(column=0, row=0)
label2.grid(column=0, row=1)

root.mainloop()