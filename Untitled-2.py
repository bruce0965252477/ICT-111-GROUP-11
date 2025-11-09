def memory_recall():
    global last_result
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(memory))
    last_result = memory

def memory_clear():
    global memory
    memory = 0.0
    messagebox.showinfo("Memory", "Memory cleared.")