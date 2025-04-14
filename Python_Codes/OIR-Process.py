import gzip
#import os.path
import shutil
#import sys
import time

import numpy as np
#import openpyxl
import pandas as pd
#import pandas.io.formats.excel

infile =  r"C:\Users\HSASS\OneDrive - Wipro\Suman\Data\Manju_Ranga_Reports\Power Apps\PowerApp\OIR-Daily-Input.csv"
outfiled = r"C:\Users\HSASS\OneDrive - Wipro\Suman\Data\Manju_Ranga_Reports\Power Apps\PowerApp\OIR-Daily-Output.csv"   
skillFile = r"C:\Users\HSASS\Downloads\Employee Skill Details.csv"

def time_calc(starttime):	
	
	time_taken=time.time() - starttime
	hours,rest = divmod(time_taken,3600)
	minutes,seconds=divmod(rest,60)
	str="---Execution Done in {} minutes and {} seconds ---"
	print(str.format(minutes,seconds))	

## Start Time for Calculation
starttime=time.time()

data = pd.read_csv(infile, engine='python',sep=',', quotechar='"') 
data = [['SR_ID','RESERVED','OPEN_POS','PROJECT_NAME','PROJECT_DESCRIPTION','SERVICE_LINE','PRACTICE','INVOICE_TYPE','JOBCODE','CONTRACTOR_JC','CUSTOMER_NAME','INDENT_STATUS','DEM_ST_DATE','DEM_END_DATE','TM_NAME','PM_NAME','ESSENTIAL_SKILL','DERIVED_INDENT_CITY','AREA','ACCOUNT_ID','ACCOUNT_TEXT','IFP_EMP_NO','IFP_EMP_NAME','ROLE_DESCRIPTION','SMU','Sector','SR_BAND','CUSTOMER_DISCUSSION_REQUIRED','EXECUTION_HUB','DEMAND_BU_SL','MIS_DUE_IN_CATEGORY','RLS_ID','DERIVED_INDENT_GEOGRAPHY','T&M/FPP','Derived Sector','Derived Practice V1','Derived Practice V2','Final SL_V10']]
data.to_csv(outfiled, index=False) # type: ignore

#End Time for Calculations
time_calc(starttime)


