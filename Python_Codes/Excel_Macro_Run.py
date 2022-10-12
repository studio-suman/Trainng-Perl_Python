#Import the following library to make use of the DispatchEx to run the macro
# import win32com.client as wincl

# def runMacro():

    # if os.path.exists("E:\\Suman\\ETR_FS_.xlsm"):

    #DispatchEx is required in the newest versions of Python.
    # excel_macro = wincl.DispatchEx("Excel.application")
    # excel_path = os.path.expanduser("E:\\Suman\\ETR_FS_.xlsm")
    # workbook = excel_macro.Workbooks.Open(Filename = excel_path, ReadOnly =1)
    # excel_macro.Application.Run\# ("ThisWorkbook.ETR")
    #Save the results in case you have generated data
    # workbook.Save()
    # excel_macro.Application.Quit()  
    # del excel_macro
    # wb.Close(True) #close the work sheet object rather than quiting excel True - value will update the excel to close the file
    
import os, os.path
import win32com.client
import time
import gzip
import shutil
import subprocess
import sys
import pandas as pd
import numpy as np




def ETR():
	if os.path.exists(r"C:\Users\HSASS\OneDrive - Wipro\Suman\ETR_FS_.xlsm"):
		xl = win32com.client.Dispatch("Excel.Application")
		wb = xl.Workbooks.Open(os.path.abspath(r"C:\Users\HSASS\OneDrive - Wipro\Suman\ETR_FS_.xlsm"), ReadOnly=1) #create a workbook object
		xl.Application.Run("ETR_FS_.xlsm!ETR.ETR_Run")
		wb.Close(True)
		xl.DisplayAlerts = False
		xl.ActiveWorkBook.Close()
		xl.Application.Quit()
		del wb
		del xl
# End of ETR function

def ZCOP():

	starttime=time.time()
	with gzip.open(r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP Daily.csv.gz", 'rb') as f_in:
		with open(r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP_REPORT_DAY.csv", 'wb') as f_out:
			shutil.copyfileobj(f_in, f_out)
		print("File Extracted!!")
	

	if os.path.exists(r"C:\Users\HSASS\OneDrive - Wipro\Suman\Data\Manju_Ranga_Reports\Ad Hoc\ZCOP_Head1.xlsm"):
		xl = win32com.client.Dispatch("Excel.Application")
		wb = xl.Workbooks.Open(os.path.abspath(r"C:\Users\HSASS\OneDrive - Wipro\Suman\Data\Manju_Ranga_Reports\Ad Hoc\ZCOP_Head1.xlsm"), ReadOnly=1) #create a workbook object
		xl.Application.Run("ZCOP_Head1.xlsm!ZCOPrep.ZCOP")
		xl.DisplayAlerts = False
		wb.Close(True)
		# xl.ActiveWorkBook.Close()
		xl.Application.Quit()
		del wb
		del xl
		name = "A2 "+ time.strftime("%d-%b-%y") + ".csv"	
		path = r"C:\Users\HSASS\OneDrive - Wipro\Suman\Data\Manju_Ranga_Reports\Ad Hoc"
		combi = path + name
		# if os.path.exists(combi):
			# subprocess.call(r'net use Y: https://wipro365.sharepoint.com/:f:/s/Misanalytics_BFSI/EmlK0smZ2mFIsNezklQaw7gBfvMX_O-Dbk6lFK1oBfDKBw?e=FYCJvr', shell=True)
			# shutil.copy(combi,'Y:\\')
		# else:
			# print("File Not Found: ", combi)

	
	input_file = r"C:\Users\HSASS\OneDrive - Wipro\Suman\Data\Manju_Ranga_Reports\Ad Hoc\A2 "+ time.strftime("%d-%b-%y") + ".csv"
	map_file = r"C:\Users\HSASS\OneDrive - Wipro\Suman\Data\Manju_Ranga_Reports\Ad Hoc\BFSI_Jan_2021.xlsx"
	fdata = pd.read_csv(input_file, engine='python')
	mdata = pd.read_excel(map_file, sheet_name="BFSI 29-Dec-20", usecols=["EMP_CODE","Status With Foundation"])[["EMP_CODE","Status With Foundation"]]
	#print(mdata.head(5))
	#df = fdata
	fdata = fdata.merge(mdata, on = "EMP_CODE", how='left') # adding data to same dataframe after merge
	# Excel output
	#writer = pd.ExcelWriter(input_file,engine ='xlsxwriter') 
	#print(fdata.head(5))
	fdata.to_csv(input_file, index=False) #assiging to excel col indices
	
	if os.path.exists(r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP_REPORT_DAY.csv"):
		os.remove(r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP_REPORT_DAY.csv")
	else:
		print("File Not Found")
	time_calc(starttime)
	# End of ZCOP function

def FSZCOP():

	starttime=time.time()
	with gzip.open(r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP Daily.csv.gz", 'rb') as f_in:
		with open(r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP_REPORT_DAY.csv", 'wb') as f_out:
			shutil.copyfileobj(f_in, f_out)
		print("File Extracted!!")
	

	if os.path.exists(r"C:\Users\HSASS\OneDrive - Wipro\Suman\Data\Manju_Ranga_Reports\Ad Hoc\Zcopworking_file.xlsm"):
		xl = win32com.client.Dispatch("Excel.Application")
		wb = xl.Workbooks.Open(os.path.abspath(r"C:\Users\HSASS\OneDrive - Wipro\Suman\Data\Manju_Ranga_Reports\Ad Hoc\Zcopworking_file.xlsm"), ReadOnly=1) #create a workbook object
		xl.Application.Run("Zcopworking_file.xlsm!FSZCOP.ZCOP")
		xl.DisplayAlerts = False
		wb.Close(True)
		# xl.ActiveWorkBook.Close()
		xl.Application.Quit()
		del wb
		del xl
		name = "Z-COP_"+ time.strftime("%d%b%y") + ".csv"	
		path = r"C:\Users\HSASS\OneDrive - Wipro\Suman\Data\Manju_Ranga_Reports\Ad Hoc"
		combi = path + name
		# if os.path.exists(combi):
			# subprocess.call(r'net use Y: https://wipro365.sharepoint.com/:f:/s/Misanalytics_BFSI/EmlK0smZ2mFIsNezklQaw7gBfvMX_O-Dbk6lFK1oBfDKBw?e=FYCJvr', shell=True)
			# shutil.copy(combi,'Y:\\')
		# else:
			# print("File Not Found: ", combi)

	
	if os.path.exists(r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP_REPORT_DAY.csv"):
		os.remove(r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP_REPORT_DAY.csv")
	else:
		print("File Not Found")
	time_calc(starttime)
	#Enf of Function

	
def time_calc(starttime):	
	
	time_taken=time.time() - starttime
	hours,rest = divmod(time_taken,3600)
	minutes,seconds=divmod(rest,60)
	str="---Execution Done in {} minutes and {} seconds ---"
	print(str.format(minutes,seconds))	