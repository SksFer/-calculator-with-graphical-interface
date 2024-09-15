##Overview
This project is a basic calculator GUI application built using Python's tkinter library. It supports basic arithmetic operations such as addition, subtraction, multiplication, and division. The user interacts with a graphical interface containing buttons for numbers, operations, and a result display.

Features
Addition, Subtraction, Multiplication, Division: Perform basic arithmetic operations.
Error Handling: Division by zero is managed by returning an error message.
Graphical User Interface: Interactive buttons to input numbers and operations.
Result Display: Shows results of the calculations directly on the screen.
Clear Button: Clear the screen with a delete button.
Files
There is only one file needed for this project, which contains both the calculator's logic and the GUI setup using tkinter.

##Functions
add(): Returns the sum of value_a and value_b.
subtract(): Returns the difference between value_a and value_b.
multiply(): Returns the product of value_a and value_b.
divide(): Returns the quotient of value_a and value_b (handles division by zero).
Delete(): Clears the display screen.
add_on_screen(value): Adds the given value to the screen display.
operate(symbol): Handles the operator selection (addition, subtraction, multiplication, or division) and stores the first operand.
result_equal(): Computes the result based on the selected operation and the second operand, then displays the result.
Graphical User Interface (GUI)
Screen: Displays the entered numbers and results (tk.Entry widget).
Buttons:
Number buttons (0-9): Used to input numbers.
Operation buttons (+, -, x, ÷): Specify the arithmetic operation to be performed.
Equals button (=): Calculates the result of the operation.
Delete button: Clears the screen for a new calculation.
