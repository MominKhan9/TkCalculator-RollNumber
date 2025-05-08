import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import math

def add():
    try:
        result.set(f"{float(entry1.get()) + float(entry2.get()):.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def subtract():
    try:
        result.set(f"{float(entry1.get()) - float(entry2.get()):.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def multiply():
    try:
        result.set(f"{float(entry1.get()) * float(entry2.get()):.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def divide():
    try:
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Math error", "Cannot divide by zero.")
            return
        result.set(f"{float(entry1.get()) / num2:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def square():
    try:
        result.set(f"{float(entry1.get())**2:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number in the first input.")

def square_root():
    try:
        num = float(entry1.get())
        if num < 0:
            messagebox.showerror("Math error", "Cannot take square root of a negative number.")
            return
        result.set(f"{math.sqrt(num):.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number in the first input.")

# GUI setup
root = tk.Tk()
root.title("Professional Calculator")
root.geometry("350x350")
root.resizable(False, False)
root.configure(bg="#f5f5f5")

# Styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#f5f5f5")
style.configure("TButton", font=("Segoe UI", 10), padding=6, background="#4CAF50", foreground="white")
style.map("TButton", background=[('active', '#45A049')])
style.configure("TLabel", font=("Segoe UI", 10), background="#f5f5f5")
style.configure("TEntry", font=("Segoe UI", 10))

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(expand=True)

# Entry widgets
entry1 = ttk.Entry(main_frame, width=20)
entry1.grid(row=0, column=0, columnspan=2, pady=5)

entry2 = ttk.Entry(main_frame, width=20)
entry2.grid(row=1, column=0, columnspan=2, pady=5)

# Result variable and label
result = tk.StringVar()
ttklbl = ttk.Label(main_frame, text="Result:")
ttklbl.grid(row=2, column=0, sticky="e", pady=5)

result_entry = ttk.Entry(main_frame, textvariable=result, width=20, state='readonly')
result_entry.grid(row=2, column=1, sticky="w", pady=5)

# Buttons for operations
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=3, column=0, columnspan=2, pady=10)

btn_opts = {"width": 14, "padding": 4}
ttk.Button(button_frame, text="➕ Add", command=add).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(button_frame, text="➖ Subtract", command=subtract).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(button_frame, text="✖ Multiply", command=multiply).grid(row=1, column=0, padx=5, pady=5)
ttk.Button(button_frame, text="➗ Divide", command=divide).grid(row=1, column=1, padx=5, pady=5)
ttk.Button(button_frame, text="² Square", command=square).grid(row=2, column=0, padx=5, pady=5)
ttk.Button(button_frame, text="√ Square Root", command=square_root).grid(row=2, column=1, padx=5, pady=5)

# Start the main loop
root.mainloop()
