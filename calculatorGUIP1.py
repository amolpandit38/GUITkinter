import tkinter as tk

root = tk.Tk()

valueEntry = tk.Entry(root, width=35, borderwidth=5)
valueEntry.grid(column=0, row=0, columnspan=3)

button1 = tk.Button(root, text = "1", padx=40, pady=20, command = lambda: insertNumber(1))
button2 = tk.Button(root, text = "2", padx=40, pady=20, command = lambda: insertNumber(2))
button3 = tk.Button(root, text = "3", padx=40, pady=20, command = lambda: insertNumber(3))
button4 = tk.Button(root, text = "4", padx=40, pady=20, command = lambda: insertNumber(4))
button5 = tk.Button(root, text = "5", padx=40, pady=20, command = lambda: insertNumber(5))
button6 = tk.Button(root, text = "6", padx=40, pady=20, command = lambda: insertNumber(6))
button7 = tk.Button(root, text = "7", padx=40, pady=20, command = lambda: insertNumber(7))
button8 = tk.Button(root, text = "8", padx=40, pady=20, command = lambda: insertNumber(8))
button9 = tk.Button(root, text = "9", padx=40, pady=20, command = lambda: insertNumber(9))
button0 = tk.Button(root, text = "0", padx=40, pady=20, command = lambda: insertNumber(0))

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

button0.grid(row=4, column=0)


def insertNumber(number):
    valueEntry.insert(0, number)

root.mainloop()
