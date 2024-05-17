import tkinter as tk
from tkinter import messagebox

def perform_calculation():
    try:
        numbers = list(map(float, entry.get().split()))
        operation = var.get()

        if not numbers:
            messagebox.showerror("Error", "Please enter at least one number!")
            return

        if operation == 1:
            result = sum(numbers)
        elif operation == 2:
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
        elif operation == 3:
            result = 1
            for num in numbers:
                result *= num
        elif operation == 4:
            result = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    messagebox.showerror("Error", "Division by zero!")
                    return
                result /= num
        else:
            messagebox.showerror("Error", "Invalid operation selected!")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Create the main window
root = tk.Tk()
root.title("Ushaswini's  Calculator")

# Create and place the widgets
tk.Label(root, text="Enter numbers (separated by spaces):").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Select operation:").grid(row=1, column=0, padx=10, pady=10)
var = tk.IntVar()
tk.Radiobutton(root, text="Add", variable=var, value=1).grid(row=1, column=1, sticky='W')
tk.Radiobutton(root, text="Subtract", variable=var, value=2).grid(row=2, column=1, sticky='W')
tk.Radiobutton(root, text="Multiply", variable=var, value=3).grid(row=3, column=1, sticky='W')
tk.Radiobutton(root, text="Divide", variable=var, value=4).grid(row=4, column=1, sticky='W')

tk.Button(root, text="Calculate", command=perform_calculation).grid(row=5, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()
