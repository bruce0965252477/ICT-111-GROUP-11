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