import time
import tkinter as tk
from tkinter import Button, IntVar, Label, Radiobutton, W, mainloop, messagebox


from AIR_ZCOP_file import AIR
from Excel_Macro_Run import ETR, FSZCOP, ZCOP
from Zcop_Report import churn_zcop, daily_zcop, weekly_zcop, rfp_zcop


def printName(x):
	str = "Your name is {}"
	print(str.format(x))


def function():
	selection = var.get()
	if selection == 1:
		printName(1)
	elif selection == 2:
		printName(2)
	else :	
		print("Function Closed")
	master.quit()

	
def run_macro():

	# Label(master, text = "Macro is Running --->").grid(row=10, sticky=W)
	option = var.get()
	if option == 1:
	# Calling ETR function
		Label(master, text = "Macro is Running --->").grid(row=10, sticky=W)
		time.sleep(10)
		ETR()
		messagebox.showinfo('Information', 'Macro Ran Successfully')
	elif option == 2:
		#Calling ZCOP
		Label(master, text = "Macro is Running --->").grid(row=10, sticky=W)
		ZCOP()
		messagebox.showinfo('Information', 'Macro Ran Successfully')
	elif option == 3:
		#Calling ZCOP
		Label(master, text = "Macro is Running --->").grid(row=10, sticky=W)
		FSZCOP()
		messagebox.showinfo('Information', 'Macro Ran Successfully')
	elif option == 4:
		#Calling Weekly ZCOP
		Label(master, text = "Macro is Running --->").grid(row=10, sticky=W)
		weekly_zcop()
		messagebox.showinfo('Information', 'Macro Ran Successfully')
	elif option == 5:
		#Calling Daily ZCOP
		Label(master, text = "Macro is Running --->").grid(row=10, sticky=W)
		time.sleep(50)
		daily_zcop()
		messagebox.showinfo('Information', 'Macro Ran Successfully')
	elif option == 6:		
		#Calling AIR
		Label(master, text = "Macro is Running --->").grid(row=10, sticky=W)
		time.sleep(50)
		AIR()
		messagebox.showinfo('Information', 'Macro Ran Successfully')
	elif option == 7:		
		#Calling Churn ZCOP
		Label(master, text = "Macro is Running --->").grid(row=10, sticky=W)
		time.sleep(50)
		churn_zcop()
		messagebox.showinfo('Information', 'Macro Ran Successfully')
	elif option == 8:		
		#Calling Churn ZCOP
		Label(master, text = "Macro is Running --->").grid(row=10, sticky=W)
		time.sleep(50)
		rfp_zcop()
		messagebox.showinfo('Information', 'Macro Ran Successfully')		
	else:
		messagebox.showinfo('Information', 'Nothing is Selected. Closing the Application...')
	master.quit()
	
master = tk.Tk(className='Tkinter - Run Macros')
master.geometry('400x200')
var = IntVar()

Label(master, text = "Select the Macro You Want to Run").grid(row=0, sticky=W)
Radiobutton(master, text = "ETR", variable = var, value = 1).grid(row=1, sticky=W)
Radiobutton(master, text = "ZCOP", variable = var, value = 2).grid(row=2, sticky=W)
Radiobutton(master, text = "FS-ZCOP", variable = var, value = 3).grid(row=3, sticky=W)
Radiobutton(master, text = "WEEKLY ZCOP", variable = var, value = 4).grid(row=4, sticky=W)
Radiobutton(master, text = "DAILY ZCOP", variable = var, value = 5).grid(row=5, sticky=W)
Radiobutton(master, text = "AIR", variable = var, value = 6).grid(row=6, sticky=W)
Radiobutton(master, text = "CHURN ZCOP", variable = var, value = 7).grid(row=1, column=4, sticky=W)
Radiobutton(master, text = "RFP ZCOP", variable = var, value = 8).grid(row=2, column=4, sticky=W)

Button(master, text = "OK", height=1, width=15, command = run_macro).grid(row=9, sticky=W)

mainloop()