import random 
import string 
import tkinter as tk 
from tkinter import messagebox 
  
def generate_password(): 
    length = int(length_entry.get())   
     
    if length <= 0: 
        messagebox.showerror("Error", "Password length must be greater than 0") 
        return 
     
    characters = "" 
     
    if alphabet_var.get(): 
        characters += string.ascii_letters   
     
    if numbers_var.get(): 
        characters += string.digits  
     
    if symbols_var.get(): 
        characters += string.punctuation   
     
    if not characters:  
        messagebox.showerror("Error", "Select at least one option!") 
        return 
     
    password = ''.join(random.choice(characters) for _ in range(length))  
    result_label.config(text="Generated Password: " + password)  

root = tk.Tk() 
root.title("Password Generator") 
root.geometry("400x300") 

tk.Label(root, text="Enter Password Length:").pack(pady=5) 
length_entry = tk.Entry(root) 
length_entry.pack() 

alphabet_var = tk.BooleanVar(value=True) 
numbers_var = tk.BooleanVar(value=False) 
symbols_var = tk.BooleanVar(value=False) 
tk.Checkbutton(root, text="Include Alphabets", variable=alphabet_var).pack() 
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack() 
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack() 

generate_button = tk.Button(root, text="Generate Password", 
command=generate_password) 
generate_button.pack(pady=10) 

result_label = tk.Label(root, text="", font=("Arial", 12)) 
result_label.pack() 

root.mainloop() 
