import gzip
import os.path
import shutil
import sys
import time

import numpy as np
import openpyxl
import pandas as pd


#infile =  r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP_REPORT_DAY.csv"
infile = r"C:\Users\HSASS\Downloads\ZCOP Daily "+ time.strftime("%d%b%y") + ".csv"
outfilew = r"C:\Users\HSASS\OneDrive - Wipro\Suman\Data\Manju_Ranga_Reports\Ad Hoc\Zcop_weekly.xlsx"
outfilec = r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ChurnZCOP_today.csv"
outfiler = r"C:\Users\HSASS\OneDrive - Wipro\Desktop\RFPZCOP_today.csv"
outfiled = r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP_today.csv"   
skillFile = r"C:\Users\HSASS\Downloads\Employee Skill Details.csv"

def daily_zcop():

	starttime=time.time()
	
	#with gzip.open(r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP Daily.csv.gz", 'rb') as f_in:
	#	with open(r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP_REPORT_DAY.csv", 'wb') as f_out:
	#		shutil.copyfileobj(f_in, f_out)
	#	print("File Extracted!!")
	
	#data = pd.read_csv(infile,usecols=["EMP_CODE","SMU","SECTOR","CUST_NAME","BILLABILITY_STATUS","APPROVED_INVESTMENT","EMP_NAME","LOCATION","CAREER_BAND","DERIVED_EMP_CITY","DERIVED_EMP_COUNTRY","ONS_OFF_FLAG","SERVICE_LINE","PRACTICE","TALENT_IDENTIFICATION",
	#"GROUP_CUSTOMER_ID","GROUP_CUSTOMER_NAME","ROLE_DESCRIPTION","COMPANY_IDENTIFICATION_FG"], engine='python',sep=',', quotechar='"', error_bad_lines=False) 
	#[["EMP_CODE","SMU","SECTOR","CUST_NAME","BILLABILITY_STATUS","INVESTMENT_FLAG","EMP_NAME","LOCATION","CAREER_BAND","DERIVED_EMP_CITY","DERIVED_EMP_COUNTRY","ONS_OFF_FLAG","SERVICE_LINE","PRACTICE","TALENT_IDENTIFICATION","GROUP_CUSTOMER_ID","GROUP_CUSTOMER_NAME","ROLE_DESCRIPTION","COMPANY_IDENTIFICATION_FG"]]

	data = pd.read_csv(infile, engine='python',sep=',', quotechar='"') 
	
	data = data[['EMP_CODE','SMU','SECTOR','CUST_NAME','BILLABILITY_STATUS','APPROVED_INVESTMENT','EMP_NAME','LOCATION','CAREER_BAND','DERIVED_EMP_CITY','DERIVED_EMP_COUNTRY','ONS_OFF_FLAG','SERVICE_LINE','PRACTICE',
	'GROUP_CUSTOMER_ID','GROUP_CUSTOMER_NAME','ROLE_DESCRIPTION','COMPANY_IDENTIFICATION_FG','BILLABILITY_STATUS_NEW','SLDU']]

	mapping = pd.read_csv(skillFile,usecols=["EMP_CODE","PROJECT_ACQUIRED_SKILLS","PRIMARY_SKILL","ROLE_ID","ROLE_DESCRIPTION"],engine='python',sep=',', quotechar='"')[["EMP_CODE","PROJECT_ACQUIRED_SKILLS","PRIMARY_SKILL","ROLE_ID","ROLE_DESCRIPTION"]]
	
	#pd.io.formats.excel.header_style = None
	
	#mapping = {
	#'BFSI': 0, 'ACQ':1
	#}
	
	data = data.sort_values(by ='SMU',ascending=True)

	final = data.merge(mapping, on='EMP_CODE', how='left')
	
	#writer = pd.ExcelWriter(outfiled,engine ='xlsxwriter')  

	#data.to_excel(writer, sheet_name ="ZCOP",startcol = 0,startrow = 0, index = False)
	
	#workbook = writer.book
	#worksheet = writer.sheets["ZCOP"]
	
	# header_format = workbook.add_format({
    # 'bold': False,
    # 'text_wrap': True,
    # 'valign': 'top',
    # 'fg_color': '#D7E4BC',
    # 'border': 0})
	
	
	# worksheet.set_row(0, None, header_format)
	# worksheet.set_zoom(100)

	# writer.save()
	#data.to_csv(outfiled,index=False)
	final.to_csv(outfiled, index=False)
	time_calc(starttime)


def churn_zcop():

	starttime=time.time()
	
	#with gzip.open(r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP Daily.csv.gz", 'rb') as f_in:
	#	with open(r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP_REPORT_DAY.csv", 'wb') as f_out:
	#		shutil.copyfileobj(f_in, f_out)
	#	print("File Extracted!!")
	
	data = pd.read_csv(infile, engine='python',sep=',', quotechar='"') 
	
	data = data[['EMP_CODE','SMU','SECTOR','CUST_NUM','CUST_NAME','PROJECT_CODE','BILLABILITY_STATUS_NEW','EMP_NAME','TM_NAME','CAREER_BAND','LOCATION','GROUP_CUSTOMER_ID','GROUP_CUSTOMER_NAME','FRESHER_INDEX','DERIVED_EMP_COUNTRY','DERIVED_EMP_GEOGRAPHY','ONS_OFF_FLAG','PROJ_COUNTRY','SLDU','COMPANY_IDENTIFICATION_FG']]

	# Below is dataframe is to prepare for qtr begining Churn
	#data = data[['EMP_CODE','LOAD_DATE','SMU','SECTOR','CUST_NUM','CUST_NAME','PROJECT_CODE','BILLABILITY_STATUS','TM_NAME','CAREER_BAND','LOCATION','GROUP_CUSTOMER_ID','GROUP_CUSTOMER_NAME','DERIVED_EMP_CITY','DERIVED_EMP_STATE','DERIVED_EMP_COUNTRY','DERIVED_EMP_GEOGRAPHY','ONS_OFF_FLAG','EXECUTION_HUB','MIS_PROP_DATE','MIS_PROP_LVL','MIS_VIS_DATE','MIS_VIS_LVL','HOME_COUNTRY','PROJ_COUNTRY','COMPANY_IDENTIFICATION_FG']]

	
	
	data = data.sort_values(by ='SMU',ascending=True)
	
	data.to_csv(outfilec, index=False)
	time_calc(starttime)

def rfp_zcop():

	starttime=time.time()
	
	#with gzip.open(r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP Daily.csv.gz", 'rb') as f_in:
	#	with open(r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP_REPORT_DAY.csv", 'wb') as f_out:
	#		shutil.copyfileobj(f_in, f_out)
	#	print("File Extracted!!")
	
	data = pd.read_csv(infile, engine='python',sep=',', quotechar='"') 
	
	data = data[['EMP_CODE','EMP_NAME','SMU','SECTOR','CUST_NAME','BILLABILITY_STATUS_NEW','TOTAL_DAYS','TM_NAME','CAREER_BAND','LOCATION','DATE_OF_JOINING','EXPERIENCE','ROLE_DESCRIPTION','GROUP_CUSTOMER_ID','GROUP_CUSTOMER_NAME','FRESHER_INDEX','DERIVED_EMP_COUNTRY','DERIVED_EMP_GEOGRAPHY','ONS_OFF_FLAG','SLDU','INVOICE_TYPE','SOW_NO','GBL','GBL_EH','DERIVED_SERVICE_LINE','PRACTICE','PROJECT_PC_TYPE','PRACTICE_PC_TYPE']]

	# Below is dataframe is to prepare for qtr begining Churn
	#data = data[['EMP_CODE','LOAD_DATE','SMU','SECTOR','CUST_NUM','CUST_NAME','PROJECT_CODE','BILLABILITY_STATUS','TM_NAME','CAREER_BAND','LOCATION','GROUP_CUSTOMER_ID','GROUP_CUSTOMER_NAME','DERIVED_EMP_CITY','DERIVED_EMP_STATE','DERIVED_EMP_COUNTRY','DERIVED_EMP_GEOGRAPHY','ONS_OFF_FLAG','EXECUTION_HUB','MIS_PROP_DATE','MIS_PROP_LVL','MIS_VIS_DATE','MIS_VIS_LVL','HOME_COUNTRY','PROJ_COUNTRY','COMPANY_IDENTIFICATION_FG']]

	
	data = data.sort_values(by ='SMU',ascending=True)
	
	data.to_csv(outfiler, index=False)
	time_calc(starttime)


def time_calc(starttime):	
	
	time_taken=time.time() - starttime
	hours,rest = divmod(time_taken,3600)
	minutes,seconds=divmod(rest,60)
	str="---Execution Done in {} minutes and {} seconds ---"
	print(str.format(minutes,seconds))	