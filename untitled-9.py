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
    elif text == "⌫":
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=backspace).grid(row=row,column=col,padx=5,pady=5)
    elif text == "ANS":
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=lambda: click("ANS")).grid(row=row,column=col,padx=5,pady=5)
    elif text == "H":
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=show_history).grid(row=row,column=col,padx=5,pady=5)
    elif text == "M+":
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=memory_add).grid(row=row,column=col,padx=5,pady=5)
    elif text == "M-":
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),bg=color,command=memory_subtract).grid(row=row,column=col,padx=5,pady=5)
    elif text == "MR":