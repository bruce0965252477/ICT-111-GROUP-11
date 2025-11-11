import tkinter as tk
from tkinter import messagebox
import math

# -----------------------------
# Global variables
# ----------------------------
last_result = None
memory = 0.0
history = []
use_degrees = True  # Toggle between degrees and radians for trig

# -----------------------------
# Core Functions
# -----------------------------
def safe_eval(expr):
    global last_result, use_degrees

    if last_result is not None:
        expr = expr.replace("ANS", str(last_result))
    
    # Replace common symbols
    expr = expr.replace("^", "**").replace("√", "math.sqrt").replace("ln", "math.log").replace("log", "math.log10")
    
    # Handle factorial
    while '!' in expr:
        index = expr.index('!')
        num = ''
        i = index-1
        while i >=0 and (expr[i].isdigit() or expr[i]=='.'):
            num = expr[i] + num
            i -=1
        expr = expr[:i+1] + f"math.factorial({num})" + expr[index+1:]
    
    # Replace trig functions for degrees/radians
    trig_funcs = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sinh', 'cosh', 'tanh']
    for func in trig_funcs:
        if func in expr and use_degrees:
            expr = expr.replace(f"{func}(", f"math.{func}(math.radians(")
    
    try:
        result = eval(expr, {"__builtins__": None, "math": math})
        last_result = result
        history.append(f"{expr} = {result}")
        return result
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero!")
        return None
    except Exception:
        messagebox.showerror("Error", "Invalid expression!")
        return None

# -----------------------------
# Memory Functions
# -----------------------------
def memory_add():
    global memory
    try:
        val = float(entry.get())
        memory += val
        messagebox.showinfo("Memory", f"Added {val} to memory.\nMemory: {memory}")
    except:
        messagebox.showerror("Error", "Enter a valid number to add to memory.")

def memory_subtract():
    global memory
    try:
        val = float(entry.get())
        memory -= val
        messagebox.showinfo("Memory", f"Subtracted {val} from memory.\nMemory: {memory}")
    except:
        messagebox.showerror("Error", "Enter a valid number to subtract from memory.")

def memory_recall():
    global last_result
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(memory))
    last_result = memory

def memory_clear():
    global memory
    memory = 0.0
    messagebox.showinfo("Memory", "Memory cleared.")

# -----------------------------
# Button Functions
# -----------------------------
def click(char):
    entry.insert(tk.END, str(char))

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    expr = entry.get()
    result = safe_eval(expr)
    if result is not None:
        entry.delete(0, tk.END)
        entry.insert(0, str(result))

def show_history():
    if not history:
        messagebox.showinfo("History", "No history available.")
    else:
        hist = "\n".join(history[-10:])
        messagebox.showinfo("History", hist)

def toggle_degrees():
    global use_degrees
    use_degrees = not use_degrees
    mode = "Degrees" if use_degrees else "Radians"
    degree_button.config(text=mode)

# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title("Ultimate Scientific Calculator")
root.geometry("550x700")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 26), bd=5, relief=tk.RIDGE, justify='right', bg="#f0f0f0")
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=20, ipady=15)

# Buttons: text, row, col, color
buttons = [
    ('7',1,0,'#ffffff'), ('8',1,1,'#ffffff'), ('9',1,2,'#ffffff'), ('/',1,3,'#ffb74d'), ('C',1,4,'#f06292'), ('⌫',1,5,'#f06292'),
    ('4',2,0,'#ffffff'), ('5',2,1,'#ffffff'), ('6',2,2,'#ffffff'), ('*',2,3,'#ffb74d'), ('(',2,4,'#64b5f6'), (')',2,5,'#64b5f6'),
    ('1',3,0,'#ffffff'), ('2',3,1,'#ffffff'), ('3',3,2,'#ffffff'), ('-',3,3,'#ffb74d'), ('√',3,4,'#ffb74d'), ('^',3,5,'#ffb74d'),
    ('0',4,0,'#ffffff'), ('.',4,1,'#ffffff'), ('+',4,2,'#ffb74d'), ('=',4,3,'#81c784'), ('ANS',4,4,'#64b5f6'), ('H',4,5,'#64b5f6'),
    ('sin(',5,0,'#ffb74d'), ('cos(',5,1,'#ffb74d'), ('tan(',5,2,'#ffb74d'), ('log(',5,3,'#ffb74d'), ('ln(',5,4,'#ffb74d'), ('!',5,5,'#ffb74d'),
    ('asin(',6,0,'#ffb74d'), ('acos(',6,1,'#ffb74d'), ('atan(',6,2,'#ffb74d'), ('sinh(',6,3,'#ffb74d'), ('cosh(',6,4,'#ffb74d'), ('tanh(',6,5,'#ffb74d'),
    ('M+',7,0,'#aed581'), ('M-',7,1,'#aed581'), ('MR',7,2,'#aed581'), ('MC',7,3,'#aed581')
]

for (text,row,col,color) in buttons:
    if text == "=":
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=calculate).grid(row=row,column=col,padx=5,pady=5)
    elif text == "C":
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=clear).grid(row=row,column=col,padx=5,pady=5)
    elif text == "⌫":
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=backspace).grid(row=row,column=col,padx=5,pady=5)
    elif text == "ANS":
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=lambda: click("ANS")).grid(row=row,column=col,padx=5,pady=5)
    elif text == "H":
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=show_history).grid(row=row,column=col,padx=5,pady=5)
    elif text == "M+":
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=memory_add).grid(row=row,column=col,padx=5,pady=5)
    elif text == "M-":
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=memory_subtract).grid(row=row,column=col,padx=5,pady=5)
    elif text == "MR":
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=memory_recall).grid(row=row,column=col,padx=5,pady=5)
    elif text == "MC":
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=memory_clear).grid(row=row,column=col,padx=5,pady=5)
    else:
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=lambda t=text: click(t)).grid(row=row,column=col,padx=5,pady=5)

# Degrees/Radians toggle
degree_button = tk.Button(root,text="Degrees",width=10,height=2,font=("Arial",16),bg="#64b5f6",command=toggle_degrees)
degree_button.grid(row=7,column=4,columnspan=2,padx=5,pady=5)

root.mainloop()
