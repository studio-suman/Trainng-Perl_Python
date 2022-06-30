from tkinter import *

root = Tk() # Initialize the widget

def printName(x):
	str = "Your name is {}"
	print(str.format(x))

#Creating a Label Widget

uLabel = Label(root, text="Name", bg="yellow")
pLabel = Label(root, text="Password", bg="red")
entry1 = Entry(root)
entry2 = Entry(root)

# initializing Grid Layout
uLabel.grid(row=0, sticky=E)
pLabel.grid(row=1, sticky=E)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me signed in")
c.grid(columnspan=2)

button1 = Button(root, text="Press Enter", bg="red")
button1.bind("<Button-1>", printName(entry1))
button1.grid(columnspan=4) 
# Putting on the screen --> .pack()

# Creating Container Frames Top & Bottom
# topFrame = Frame(root)
# topFrame.pack()

# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)

# #--------------------------

# # Initiating Buttons

# button1 = Button(topFrame, text="Button1", bg="red")
# button2 = Button(topFrame, text="Button2", bg="blue")
# button3 = Button(topFrame, text="Button3", bg="green")
# button4 = Button(bottomFrame, text="Button4", bg="purple")

# #Aligning Buttons and packing
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=LEFT)
# myLabel.pack(side=BOTTOM, fill=X)

root.mainloop() # Return to Loop the Widget
