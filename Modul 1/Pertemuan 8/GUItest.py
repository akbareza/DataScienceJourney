import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.configure(bg='white')

label = tk.Label(root, text="Hello, World!", fg='red')
label.pack()

button = tk.Button(root, text="Click me!")
button.pack()

root.mainloop()