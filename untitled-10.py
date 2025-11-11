tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=memory_recall).grid(row=row,column=col,padx=5,pady=5)
    elif text == "MC":
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=memory_clear).grid(row=row,column=col,padx=5,pady=5)
    else:
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=lambda t=text: click(t)).grid(row=row,column=col,padx=5,pady=5)