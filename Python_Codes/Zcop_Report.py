import gzip
import os.path
import shutil
import sys
import time

import numpy as np
import openpyxl
import pandas as pd
import pandas.io.formats.excel

#infile =  r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP_REPORT_DAY.csv"
infile = r"C:\Users\HSASS\Downloads\ZCOP Daily "+ time.strftime("%d%b%y") + ".csv"
outfilew = r"C:\Users\HSASS\OneDrive - Wipro\Suman\Data\Manju_Ranga_Reports\Ad Hoc\Zcop_weekly.xlsx"
outfilec = r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ChurnZCOP_today.csv"
outfiler = r"C:\Users\HSASS\OneDrive - Wipro\Desktop\RFPZCOP_today.csv"
outfiled = r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP_today.csv"   
skillFile = r"C:\Users\HSASS\Downloads\Employee Skill Details.csv"
def weekly_zcop():

	with gzip.open(r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP Daily.csv.gz", 'rb') as f_in:
		with open(r"C:\Users\HSASS\OneDrive - Wipro\Desktop\ZCOP_REPORT_DAY.csv", 'wb') as f_out:
			shutil.copyfileobj(f_in, f_out)
		print("File Extracted!!")
		
	starttime=time.time()
	#pd.read_csv("C:\Users\hsass\Desktop\ZCOP_REPORT_DAY.csv",low_memory = False)
	data1 = pd.read_csv(infile,usecols=["EMP_CODE","CAREER_BAND","BULGE","LOCATION","DATE_OF_JOINING","SMU","EXPERIENCE","BILLABILITY_STATUS","SECTOR","GROUP_CUSTOMER_NAME","FRESHER_ENGAGEMENT_FLAG","DERIVED_SUITE_ID","DERIVED_SUITE_NAME","CUST_NAME","LOAD_DATE","DERIVED_EMP_CITY","FRESHER_INDEX","TM_EMP_NO","EMPLOYEE_EMAIL_ID","PM_ID","COMPANY_IDENTIFICATION_FG","ONS_OFF_FLAG"], engine='python',sep=',', quotechar='"') [["EMP_CODE","CAREER_BAND","BULGE","LOCATION","DATE_OF_JOINING","SMU","EXPERIENCE","BILLABILITY_STATUS","SECTOR","GROUP_CUSTOMER_NAME","FRESHER_ENGAGEMENT_FLAG","DERIVED_SUITE_ID","DERIVED_SUITE_NAME","CUST_NAME","LOAD_DATE","DERIVED_EMP_CITY","FRESHER_INDEX","TM_EMP_NO","EMPLOYEE_EMAIL_ID","PM_ID","COMPANY_IDENTIFICATION_FG","ONS_OFF_FLAG"]]



	data1['DATE_OF_JOINING'] = data1['DATE_OF_JOINING'].astype('datetime64[ns]') 


	data2 = pd.read_csv(infile,usecols=["EMP_CODE","ONSITE_DAYS","OFFSHORE_DAYS","ONSITE_BILLABLE_DAYS","OFFSHORE_BILLABLE_DAYS","ONSITE_NONBILLABLE_DAYS","OFFSHORE_NONBILLABLE_DAYS","ONSITE_SERVICE_DAYS","OFFSHORE_SERVICE_DAYS","ONSITE_FREE_DAYS","OFFSHORE_FREE_DAYS","SMU"], engine='python',sep=',', quotechar='"')
	data2["Total Billed"]= data2["ONSITE_BILLABLE_DAYS"] + data2["OFFSHORE_BILLABLE_DAYS"]
	data2["TotalSupport"]= data2["ONSITE_SERVICE_DAYS"] + data2["OFFSHORE_SERVICE_DAYS"]
	data2["TotalVNB"]= data2["ONSITE_NONBILLABLE_DAYS"] + data2["OFFSHORE_NONBILLABLE_DAYS"]
	data2["TotalXFree"]= data2["ONSITE_FREE_DAYS"] + data2["ONSITE_FREE_DAYS"]
	data2["Virtual/existing"]= data2["Total Billed"] + data2["TotalSupport"]
	data2['YStatus'] = np.where(data2['Virtual/existing']>0, 'Virtual', 'Existing')
	df1 = data1 


	table2 = data2.query('SMU == ["AMR2","IDA2"]')


	table2["Total Billed"]= table2["ONSITE_BILLABLE_DAYS"] + table2["OFFSHORE_BILLABLE_DAYS"]
	table2["TotalSupport"]= table2["ONSITE_SERVICE_DAYS"] + table2["OFFSHORE_SERVICE_DAYS"]
	table2["TotalVNB"]= table2["ONSITE_NONBILLABLE_DAYS"] + table2["OFFSHORE_NONBILLABLE_DAYS"]
	table2["TotalXFree"]= table2["ONSITE_FREE_DAYS"] + table2["OFFSHORE_FREE_DAYS"]

		
	df23 = pd.pivot_table(data2,index=["EMP_CODE"],values =['YStatus','Total Billed','TotalSupport','TotalVNB','TotalXFree'],aggfunc='first')  # type: ignore
	df23.loc['Total Billed']= df23.sum(numeric_only=True, axis=0)


	df24 = pd.pivot_table(table2,index = ["EMP_CODE"],values =['Total Billed','TotalSupport','TotalVNB','TotalXFree'],aggfunc= np.sum,margins=True,margins_name=' Grand Total', fill_value=0)
	 

		
	with pd.ExcelWriter(
		outfilew,engine ='xlsxwriter'  # type: ignore
		) as writer:
		data1.to_excel(writer, sheet_name ="ZCOP",startcol = 14,startrow = 0)

	workbook = writer.book
	worksheet = writer.sheets["ZCOP"]
	worksheet.set_zoom(100)

	df23.to_excel(writer, sheet_name ="ZCOP", startcol = 0,startrow = 3)

	df24.to_excel(writer, sheet_name ="ZCOP", startcol = 8,startrow = 3)

	worksheet.set_column('A:F', 10)
	worksheet.set_column('I:M', 10)
	worksheet.set_column('P:AD', 10)
		
	writer.save()  # type: ignore
	time_calc(starttime)
	
	
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
	
	data = data[['EMP_CODE','SMU','SECTOR','CUST_NAME','BILLABILITY_STATUS','APPROVED_INVESTMENT','EMP_NAME','LOCATION','CAREER_BAND','DERIVED_EMP_CITY','DERIVED_EMP_COUNTRY','ONS_OFF_FLAG','SERVICE_LINE','PRACTICE','TALENT_IDENTIFICATION',
	'GROUP_CUSTOMER_ID','GROUP_CUSTOMER_NAME','ROLE_DESCRIPTION','COMPANY_IDENTIFICATION_FG','BILLABILITY_STATUS_NEW','EXECUTION_HUB']]

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
	
	data = data[['EMP_CODE','SMU','SECTOR','CUST_NUM','CUST_NAME','PROJECT_CODE','BILLABILITY_STATUS_NEW','EMP_NAME','TM_NAME','CAREER_BAND','LOCATION','GROUP_CUSTOMER_ID','GROUP_CUSTOMER_NAME','FRESHER_INDEX','DERIVED_EMP_COUNTRY','DERIVED_EMP_GEOGRAPHY','ONS_OFF_FLAG','PROJ_COUNTRY','EXECUTION_HUB','COMPANY_IDENTIFICATION_FG']]

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
	
	data = data[['EMP_CODE','EMP_NAME','SMU','SECTOR','CUST_NAME','BILLABILITY_STATUS_NEW','TOTAL_DAYS','TM_NAME','CAREER_BAND','LOCATION','DATE_OF_JOINING','EXPERIENCE','ROLE_DESCRIPTION','GROUP_CUSTOMER_ID','GROUP_CUSTOMER_NAME','FRESHER_INDEX','DERIVED_EMP_COUNTRY','DERIVED_EMP_GEOGRAPHY','ONS_OFF_FLAG','EXECUTION_HUB','INVOICE_TYPE','SOW_NO','GBL','GBL_EH','DERIVED_SERVICE_LINE','PRACTICE','TALENT_IDENTIFICATION','PROJECT_PC_TYPE','PRACTICE_PC_TYPE']]

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