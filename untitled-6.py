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