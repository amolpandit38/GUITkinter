import tkinter as tk

root = tk.Tk()

def insertNumber(number):
    current = valueEntry.get()
    valueEntry.delete(0, tk.END)
    valueEntry.insert(0, str(current) + str(number))

def addValues():
    global firstNumber
    global math

    math = "addition"
    firstNumberString = valueEntry.get()
    firstNumber = int(firstNumberString)
    valueEntry.delete(0, tk.END)

def subValues():
    global firstNumber
    global math
    math = "substraction"
    firstNumberString = valueEntry.get()
    firstNumber = int(firstNumberString)
    valueEntry.delete(0, tk.END)

def mulValues():
    global firstNumber
    global math
    math = "multiplication"
    firstNumberString = valueEntry.get()
    firstNumber = int(firstNumberString)
    valueEntry.delete(0, tk.END)

def divValues():
    global firstNumber
    global math
    math = "division"
    firstNumberString = valueEntry.get()
    firstNumber = int(firstNumberString)
    valueEntry.delete(0, tk.END)

def clearButton():
    valueEntry.delete(0, tk.END)

def equalButton():
    secondNumberString = valueEntry.get()
    valueEntry.delete(0, tk.END)
    secondNumber = int(secondNumberString)

    if (math == "addition"):
        valueEntry.insert(0, firstNumber + secondNumber)

    if (math == "substraction"):
        valueEntry.insert(0, firstNumber - secondNumber)

    if (math == "multiplication"):
        valueEntry.insert(0, firstNumber * secondNumber)

    if (math == "division"):
        valueEntry.insert(0, firstNumber / secondNumber)

valueEntry = tk.Entry(root, width=35, borderwidth=5)
valueEntry.grid(column=0, row=0, columnspan=3)
valueEntry.insert(0, "0")

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
buttonAdd = tk.Button(root, text = "+", padx=34, pady=20, font=('Arial', 15), command=addValues)
buttonClear = tk.Button(root, text = "Clear", padx=79, pady=20, command=clearButton)
buttonEqual = tk.Button(root, text = "=", padx=83.5, pady=20, command=equalButton, font=('Arial', 15))
buttonSub = tk.Button(root, text = "-", padx=36, pady=20, font=('Arial', 15), command=subValues)
buttonMul = tk.Button(root, text = "*", padx=38, pady=20, font=('Arial', 15), command=mulValues)
buttonDiv = tk.Button(root, text = "/", padx=38, pady=20, font=('Arial', 15), command=divValues)

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

buttonAdd.grid(row=5, column=0)
buttonSub.grid(row=6, column=0)
buttonMul.grid(row=6, column=1)
buttonDiv.grid(row=6, column=2)
buttonClear.grid(row=4, column=1, columnspan=2)
buttonEqual.grid(row=5, column=1, columnspan=2)

root.mainloop()
