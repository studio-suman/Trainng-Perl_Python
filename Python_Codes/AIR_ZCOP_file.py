#import modin.pandas as pd
import pandas as pd
import time
import math
import numpy as np
import string as str
import openpyxl
#import sqlite3
#from sqlalchemy import create_engine
#from importlib import reload
from datetime import datetime
import sys

def time_calc(time): 

	hours,rest = divmod(time,3600)
	minutes,seconds=divmod(rest,60)
	str="---Execution Done in {} minutes and {} seconds ---"
	print(str.format(minutes,seconds))


starttime=time.time()

#time_calc(starttime)

# PYTHONIOENCODING="UTF-8"

# if sys.version[0] == '3':
    # reload(sys)
    # PYTHONIOENCODING="UTF-8"


# df = pd.read_excel("F:\STATS\EBD ERD LOCKED IN Report_11-09-2019.xlsx")

# d = pd.pivot_table(df,index=["Grand Total"])
# print(d)

#ZCOP_Load=pd.read_csv("C:\\Users\\hsass\\desktop\\ZCOP_REPORT_DAY.csv", engine='python') 
#print(ZCOP_Load.head(5))
#zdata=pd.read_csv('ZCOP_REPORT_DAY.csv',usecols=["EMP_CODE","SAP_BU_DESC","SAP_VERTICAL_DESC","BILLABILITY_STATUS","CUST_NAME"], encoding="utf-8")
#importing data to dataframe 'zdata'

def zcop():

	# input_file="C:\\Users\\hsass\\desktop\\ZCOP_REPORT_DAY.csv"
	# output_file="C:\\Users\\hsass\\Desktop\\30-Jun\\Zcop today.xlsx"
	# zdata = pd.read_csv(input_file,usecols=["EMP_CODE","SAP_BU_DESC","SAP_VERTICAL_DESC","BILLABILITY_STATUS","CUST_NAME"], engine='python')[["EMP_CODE","SAP_BU_DESC","SAP_VERTICAL_DESC","BILLABILITY_STATUS","CUST_NAME"]]


	# zdata.sort_values(by=['SAP_BU_DESC'],inplace=True) #sorting data based on BU col
	# # data1['DATE_OF_JOINING'].type

	# #zdata.query('SAP_BU_DESC >= "BFSI"', inplace=True) #filtering on BU - BFSI
	# # extr=zdata.loc[zdata['SAP_BU_DESC'] == "BFSI"] #selecting cols which are BU
	# # zdata[extr]
	# zdata.reset_index(drop=True, inplace=True) #resetting the index
	# # print(zdata.head(4))
	# # print(zdata.tail(4))
	# # print(zdata.index)
	# # print(zdata.head)

	# # print(zdata['EMP_CODE'])
	# # print(type(zdata['EMP_CODE']))

	# # emp=zdata['EMP_CODE']
	# # print(emp[0])
	# # print(zdata.at[0,"EMP_CODE"])

	# # df=pd.read_csv(input_file,engine='python',index_col="EMP_CODE")
	# # #print(df.index)
	# # print(df.head(3))
	# #print(df.loc["EMP_CODE","FRESHER_ENGAGEMENT_FLAG"])

	# engine=create_engine('sqlite://', echo=False)
	# zdata.to_sql('zcop',engine, if_exists='replace', index=False)
	# results = engine.execute("Select * from zcop where SAP_BU_DESC = 'BFSI'")
	# final=pd.DataFrame(results, columns=zdata.columns)
	# final.to_excel(output_file,index=False)
	# print(final.head(5))
	
	
	input_file="E:\\Suman\\Data\Manju_Ranga_Reports\\Ad Hoc\\BFSI "+ time.strftime("%d-%b-%y") + ".csv"
	map_file="E:\\Suman\\Data\Manju_Ranga_Reports\\Ad Hoc\\BFSI_Jan_2020_Aggregate.xlsx"
	fdata = pd.read_csv(input_file, engine='python')
	mdata = pd.read_excel(map_file, sheet_name="BFSI-20-Dec", usecols=["EMP_CODE","Status With Foundation"])[["EMP_CODE","Status With Foundation"]]
	print(mdata.head(5))
	#df = fdata
	fdata = fdata.merge(mdata, on = "EMP_CODE", how='left') # adding data to same dataframe after merge
	# Excel output
	#writer = pd.ExcelWriter(input_file,engine ='xlsxwriter') 
	print(fdata.head(5))
	fdata.to_csv(input_file, index=False)



def OIR():

	infile="C:\\Users\\hsass\\desktop\\New_Open_Indent_Report.csv"
	outfile="C:\\Users\\hsass\\Desktop\\30-Jun\\OIR.xlsx"
	# odata = pd.read_csv(infile,usecols=["DEMAND_ID","PROJECT_NAME","PRACTICE_GRP_TXT","RM_EMP_NAME","MODEL_TYPE"], engine='python')[["DEMAND_ID","PROJECT_NAME","PRACTICE_GRP_TXT","RM_EMP_NAME","MODEL_TYPE"]]
	odata = pd.read_csv(infile, engine='python')


	engine=create_engine('sqlite://', echo=False)
	odata.to_sql('oir',engine, if_exists='replace', index=False)
	results = engine.execute("Select * from oir where RM_EMP_NAME = 'Suman Saha'")
	final=pd.DataFrame(results, columns=odata.columns)
	final.to_excel(outfile,index=False)

	
def AIR():
	starttime=time.time()
	infile =   r"C:\Users\HSASS\OneDrive - Wipro\Desktop\AIR\AIR_CREATIONS_20_21.CSV"
	outfile =  r"C:\Users\HSASS\OneDrive - Wipro\Desktop\AIR\AIR_BFSI_today.csv"
	map_file = r"C:\Users\HSASS\OneDrive - Wipro\Desktop\AIR\Ops_Template.xlsx"
	odata = pd.read_csv(infile, engine='python',sep=',', quotechar='"', error_bad_lines=False)
	
	#odata = pd.read_csv(infile,usecols=["DEMAND_ID","PROJECT_NAME","ESSENTIAL_SKILL","PRACTICE_GRP_TXT","RM_EMP_NAME","MODEL_TYPE"], engine='python' ,sep=',', quotechar='"', error_bad_lines=False)[["DEMAND_ID","PROJECT_NAME","ESSENTIAL_SKILL","PRACTICE_GRP_TXT","RM_EMP_NAME","MODEL_TYPE"]]
	
	
	table = odata.query('SMU == ["AMR2]')
	#table = odata.query('PROJ_SAP_BU == ["BFSI"]' and 'PROJ_SAP_VERTICAL == ["CAPITAL MARKETS"]')
	# ---- Using Sql Query -- to build the db
	# engine=create_engine('sqlite://', echo=False)
	# odata.to_sql('oir',engine, if_exists='replace', index=False)
	# results = engine.execute("Select * from oir where PROJ_SAP_BU = 'BFSI'")
	# final=pd.DataFrame(results, columns=odata.columns)
	# ---- pd table is ready and merged into final table
	
	mdata = pd.read_excel(map_file, sheet_name='Sheet1')
	final = table.merge(mdata, on = "INDENT_CLASSIFICATIONS", how='left') # adding data to same dataframe after merge
	final['INDENT_CREATED_ON'] = pd.to_datetime(final['INDENT_CREATED_ON'])
	mask = final['INDENT_CREATED_ON'].dt.month >= 10 # Month Filter Flag
	final.loc[mask].to_csv(outfile,index=False)
	#odata.to_csv(outfile,index=False)
	time_calc(starttime)

if __name__ == "__main__":
 globals()[sys.argv[1]]()


# time_taken=time.time() - starttime
# time_calc(time_taken) 

