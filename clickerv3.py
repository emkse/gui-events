import tkinter as tk

root = tk.Tk()
root.title("Clicker")
root.geometry("200x200")
root.config(bg = "grey")
count = 0 
countLabel = tk.Label(root,text = count)
countCheck = ""

def XorDivide(event):    
    global count, countCheck
    if countCheck == "Multiply":
        count *= 3
    elif countCheck == "Divide":
        count /= 3
    countLabel.configure(text = count)
    

def backgroundcolorchange(event):
    root.configure(bg = "yellow")
    

def colourChanges(event):
    global count
    if count > 0:
        root.configure(bg = "green")
    elif count < 0:
        root.configure(bg = "red")
    else:
        root.configure(bg = "grey")
 
        
        
def Up():
    global count, countCheck
    count += 1
    countLabel.configure(text = count)
    colourChanges("")
    countCheck = "Multiply"

def Down():
    global count, countCheck
    count -= 1
    countLabel.configure(text = count)
    colourChanges("")
    countCheck = "Divide"

buttonUp = tk.Button(
    root,
    command = Up,
    text = "Up"    
)

buttonDown = tk.Button(
    root,
    command = Down,
    text = "Down"    
)

buttonUp.pack(
ipadx = 55, 
side = "top",
expand = True
)

countLabel.pack(
    ipadx = 60,
    expand = True
)       

buttonDown.pack(
    ipadx = 45,
    side = "bottom",
    expand = True
)

countLabel.bind("<Enter>", backgroundcolorchange)
countLabel.bind("<Leave>", colourChanges)
countLabel.bind("<Double-Button>", XorDivide)

root.mainloop()