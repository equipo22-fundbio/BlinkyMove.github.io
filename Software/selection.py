import tkinter as tk


Keyboard_App = tk.Tk()

keys = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '=',
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '<-',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '"',
    'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '!', 'TAB',
    'Espacio',
]

curBut = [-1,-1]
buttonL = [[]]
#entrada de texto
entry = tk.Text(Keyboard_App, width=97, height=8)
entry.grid(row=0, columnspan=15)


varRow = 1
varColumn = 0

def leftKey(event):
    if curBut == [-1,-1]:
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground="Green")
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="#32E385")
        curBut[:] = [0,10]
        buttonL[0][10].configure(highlightbackground="Green")
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="#32E385")
        curBut[:] = [curBut[0], (curBut[1]-1)%11]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="#32E385")
    buttonL[curBut[0]][curBut[1]].focus_set()

def rightKey(event):
    if curBut == [-1,-1]:
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground="Green")
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="#32E385")
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground="Green")
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="#32E385")
        curBut[:] = [curBut[0], (curBut[1]+1)%11]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="#32E385")
    buttonL[curBut[0]][curBut[1]].focus_set()

def upKey(event):
    if curBut == [-1,-1]:
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground="Green")
    elif curBut[0] == 0:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#32E385' )
        curBut[:] = [(curBut[0]-1)%5, 0]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#32E385')
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#32E385')
        curBut[:] = [(curBut[0]-1)%5, 5]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#32E385')
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#32E385')
        curBut[:] = [(curBut[0]-1)%5, curBut[1]]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#32E385')
    buttonL[curBut[0]][curBut[1]].focus_set()

def downKey(event):
    if curBut == [-1,-1]:
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='Green')
    elif curBut[0] == 3:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#32E385')
        curBut[:] = [(curBut[0]+1)%5, 0]
        buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='#32E385')
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#32E385')
        curBut[:] = [(curBut[0]+1)%5, 5]
        buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='#32E385')
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#32E385')
        curBut[:] = [(curBut[0]+1)%5, curBut[1]]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#32E385')
    buttonL[curBut[0]][curBut[1]].focus_set()

def select(value, x, y):

    if curBut != [-1,-1]:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#32E385')
        buttonL[curBut[0]][curBut[1]].configure(highlightcolor='#32E385')
    curBut[:] = [x,y]
    buttonL[x][y].configure(highlightbackground='Green')
    buttonL[x][y].configure(highlightcolor='#32E385')

    #delete
    if value == "<-":
        input_val = entry.get("1.0", 'end-2c')
        entry.delete("1.0", "end")
        entry.insert("1.0", input_val, "end")

    elif value == "Espacio":
        entry.insert("insert", ' ')
    elif value == "TAB":
        entry.insert("insert", '   ')
    else:
        entry.insert("end", value)

for button in keys:
    if button != "Espacio":
        but = tk.Button(Keyboard_App, text=button, width=5, bg="#8DE493", fg="#000000", highlightthickness=4,
                       activebackground="gray65", highlightcolor='#32E385', activeforeground="#000000", relief="raised", padx=12,
                       pady=4, bd=4, command=lambda x=button, i=varRow-1, j=varColumn: select(x, i, j))
        but.bind('<Return>', lambda event, x=button, i=varRow-1, j=varColumn: select(x, i, j))
        buttonL[varRow-1].append(but)
        but.grid(row=varRow, column=varColumn)

    if button == "Espacio":
        but = tk.Button(Keyboard_App, text=button, width=60, bg="#8DE493", fg="#000000", highlightthickness=6,
                       activebackground="gray65", highlightcolor="#32E385", activeforeground="#000000", relief="raised", padx=4,
                       pady=4, bd=4, command=lambda x=button, i=varRow-1, j=varColumn: select(x, i, j))
        but.bind('<Return>', lambda event, x=button, i=varRow-1, j=varColumn: select(x, i, j))
        buttonL[varRow-1].append(but)
        but.grid(row=6, columnspan=16)

    varColumn += 1
    if varColumn > 10:
        varColumn = 0
        varRow += 1
        buttonL.append([])

Keyboard_App.bind('<Left>', leftKey)
Keyboard_App.bind('<Right>', rightKey)
Keyboard_App.bind('<Up>', upKey)
Keyboard_App.bind('<Down>', downKey)

Keyboard_App.mainloop()