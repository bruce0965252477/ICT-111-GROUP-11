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
    expr = expr.replace("^", "").replace("√", "math.sqrt").replace("ln", "math.log").replace("log", "math.log10")
    
    # Handle factorial
    while '!' in expr:
        index = expr.index('!')
        num = ''
        i = index-1
        while i >=0 and (expr[i].isdigit() or expr[i]=='.'):
            num = expr[i] + num
            i -=1
        expr = expr[:i+1] + f"math.factorial({num})" + expr[index+1:]
        #Replace trig functions for degrees/radians
    trig_funcs = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sinh', 'cosh', 'tanh']
    for func in trig_funcs:
        if func in expr and use_degrees:
            expr = expr.replace(f"{func}(", f"math.{func}(math.radians(")
        try:
result = eval(expr, {"_builtins_": None, "math": math})
        last_result = result
        history.append(f"{expr} = {result}")
        return result
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero!")
        return None
    except Exception:
        messagebox.showerror("Error", "Invalid expression!")
        return None
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
        messagebox.showerror("Error", "Enter a valid number to add to memory.")
        def memory_subtract():
    global memory
    try:
        val = float(entry.get())
        memory -= val
        messagebox.showinfo("Memory", f"Subtracted {val} from memory.\nMemory: {memory}")
    except:
        messagebox.showerror("Error", "Enter a valid number to subtract from memory.")
        