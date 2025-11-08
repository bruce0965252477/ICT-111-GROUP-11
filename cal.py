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