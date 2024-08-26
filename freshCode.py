import tkinter as tk
from tkinter import messagebox
# print("hello world")

# list = [2,45,6,4,32,45,6,7,755,1]

# list.sort()

# for i in list:
#     print(i)

# Create the main application window
# root = tk.Tk()
# root.title("Simple Tkinter App")
# root.geometry("300x200")

# # Create a label widget
# label = tk.Label(root, text="Hello, Tkinter!")
# label.pack(pady=20)

# # Create a button widget
# button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
# button.pack(pady=10)

# # Run the Tkinter event loop
# root.mainloop()


def show_message():
    messagebox.showinfo("Message", "You clicked the button!")

# Create the main application window
root = tk.Tk()
root.title("Advanced Tkinter App")
root.geometry("400x300")

# Create a frame to hold widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Create a label widget
label = tk.Label(frame, text="Enter your name:")
label.grid(row=0, column=0, padx=5, pady=5)

# Create an entry widget
entry = tk.Entry(frame)
entry.grid(row=0, column=1, padx=5, pady=5)

# Create a button widget
button = tk.Button(frame, text="Submit", command=show_message)
button.grid(row=1, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
