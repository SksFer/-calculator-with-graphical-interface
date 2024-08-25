import tkinter as tk 

window = tk.Tk()


#functions 




#grafic interface



#window interface
screen = tk.Entry(window)
screen.grid(row=0, column=0, columnspan=4)



#buttons
seven = tk.Button(window, text="7")
seven.grid(row=1, column=0)

eight = tk.Button(window, text ="8")
eight.grid(row=1, column=1)

nine = tk.Button(window,text = "9")
nine.grid(row=1, column=2)

division= tk.Button(window, text="÷")
division.grid(row=1, column=3)

four = tk.Button(window, text="4")
four.grid(row=2, column=0)

five = tk.Button(window, text="5")
five.grid(row=2, column=1)

six = tk.Button(window, text="6")
six.grid(row=2, column=2)

multiplication = tk.Button(window, text="×")
multiplication.grid(row=2, column=3)

one = tk.Button(window, text="1")
one.grid(row=3, column=0)


two = tk.Button(window, text="2")
two.grid(row=3, column=1)

three = tk.Button(window, text="3")
three.grid(row=3, column=2)

subtraction = tk.Button(window, text="-")
subtraction.grid(row=3, column=3)

zero= tk.Button(window, text="0")
zero.grid(row=4, column=0)

dot = tk.Button(window, text=".")
dot.grid(row=4, column=1)

equal = tk.Button(window, text="=")
equal.grid(row=4, column=2)

plus = tk.Button(window, text="+")
plus.grid(row=4, column=3)
window.mainloop()