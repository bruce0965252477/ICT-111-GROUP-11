def memory_subtract():
    global memory
    try:
        val = float(entry.get())
        memory -= val
        messagebox.showinfo("Memory", f"Subtracted {val} from memory.\nMemory: {memory}")
    except:
        messagebox.showerror("Error", "Enter a valid number to subtract from memory.")