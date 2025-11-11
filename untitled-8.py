# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title("Ultimate Scientific Calculator")
root.geometry("550x700")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 26), bd=5, relief=tk.RIDGE, justify='right', bg="#f0f0f0")
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=20, ipady=15)