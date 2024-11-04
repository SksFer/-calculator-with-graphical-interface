import tkinter as tk 

window = tk.Tk()
value_a = 0
value_b = 0
operation = "addition"
result = 0

#functions (add, substract,multiply, divide, delete)

def add ():
    global value_a, value_b
    return value_a + value_b

def subtract():
    global value_a, value_b
    return value_a - value_b

def multiply():
    global value_a, value_b
    return value_a * value_b

def divide():
    global value_a, value_b
    try:
        return value_a / value_b
    except ZeroDivisionError:
        return "Error: Division by zero"
    
def Delete ():
    global window
    screen.delete(0, tk.END)
def add_on_screen(value):
    global screen
    screen.insert(tk.END, value)
def operate (symbol):
    global screen, value_a, operation
    value_a = float(screen.get())
    print(value_a)
    screen.delete(0, tk.END)
    if symbol == "/":   
        operation = "division"
    elif symbol == "*": 
        operation = "multiplication"
    elif symbol == "-":
        operation = "subtraction"
    else:
        operation = "addition"
    print(operation)
def result_equal():
    global screen
    global value_a
    global value_b
    global result
    global operation 

    value_b = float(screen.get())
    screen.delete(0, tk.END)

    if operation == "addition":
        result = add()
    elif operation == "subtraction":
        result = subtract()
    elif operation == "multiplication":
        result = multiply()
    elif operation == "division":
        result = divide()

    screen.insert(tk.END, result)
    print(result)


#grafic interface



#window
screen = tk.Entry(window, width=31, bd=6, justify="right")
screen.grid(row=0, column=0, columnspan=4)



#buttons
seven = tk.Button(window, text="7", width=5,command=lambda: add_on_screen(7))
seven.grid(row=1, column=0)

eight = tk.Button(window, text ="8",  width=5,command=lambda: add_on_screen(8))
eight.grid(row=1, column=1)

nine = tk.Button(window,text = "9", width=5,command=lambda: add_on_screen(9))
nine.grid(row=1, column=2)

division= tk.Button(window, text="÷",  width=7,command=lambda: operate("/"))
division.grid(row=1, column=3)

four = tk.Button(window, text="4", width=5,command=lambda: add_on_screen(4))
four.grid(row=2, column=0)

five = tk.Button(window, text="5", width=5,command=lambda: add_on_screen(5))
five.grid(row=2, column=1)

six = tk.Button(window, text="6", width=5,command=lambda: add_on_screen(6))
six.grid(row=2, column=2)

multiplication = tk.Button(window, text="x", width=7,command=lambda:operate("*"))
multiplication.grid(row=2, column=3)

one = tk.Button(window, text="1", width=5,command=lambda: add_on_screen(1))
one.grid(row=3, column=0)


two = tk.Button(window, text="2", width=5,command=lambda: add_on_screen(2))
two.grid(row=3, column=1)

three = tk.Button(window, text="3", width=5,command=lambda: add_on_screen(3))
three.grid(row=3, column=2)

subtraction = tk.Button(window, text="-", width=7,command=lambda: operate("-"))
subtraction.grid(row=3, column=3)

zero= tk.Button(window, text="0", width=5,command=lambda: add_on_screen(0))
zero.grid(row=4, column=0)

dot = tk.Button(window, text=".", width=5,command=lambda: add_on_screen("."))
dot.grid(row=4, column=1)

equal = tk.Button(window, text="=", width=5,command=result_equal)
equal.grid(row=4, column=2)

plus = tk.Button(window, text="+", width=7,command=lambda: operate("+"))
plus.grid(row=4, column=3)

delete = tk.Button(window, text="Delete", width=27,command=Delete)
delete.grid(row=5, column=0, columnspan=4)
window.mainloop()

