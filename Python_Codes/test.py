#import pandas
#import numpy
#import openpyxl
#import sys
#import random
#import math
import gzip
import shutil
import time
import sys
from Excel_Macro_Run import ETR,ZCOP,FSZCOP
from Zcop_Report import weekly_zcop,daily_zcop
from array import *


def run_macro(option):
	
	if option == "ETR":
	# Calling ETR function
		ETR()
	elif option == "ZCOP":
		#Calling ZCOP
		ZCOP()
	elif option == "FSZCOP":
		#Calling ZCOP
		FSZCOP()
	elif option == "weekly_zcop":
		weekly_zcop()
	elif option == "daily_zcop":
		daily_zcop()
	else:
		print("Yet to run")


# Calling Self function to run individual macros through argument
if __name__ == "__main__":
 globals()[sys.argv[1]](sys.argv[2])
 

# def printIterates(OneDMap, initialConditions, nIterates):
    # x=initialConditions
    # for i in range(nIterates):
        # x=OneDMap(x)
        # print (i, x)

# def LogisticMap(x):
    # return 4.0 * x * (1.0 - x)

# printIterates(LogisticMap, 0.3, 10)

# #Hello World
# print("Hello World\n")
# #Ask user for name
# name = input("Whats your name?:")

# #Ask user for age
# age = input("How old are you?:")

# #Ask user for city
# #AI  = array('b',["How are doing today","What are you upto?"])
# #AI(1)

# #Create output
# str = "Your name is {} and you are {} yrs old"
# #output = str.format(name,age)
# print(str.format(name,age))