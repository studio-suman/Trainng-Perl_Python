import pandas as pd
import numpy as np
import openpyxl
import sys


infile =  "C:\\Users\\hsass\\Desktop\\ZCOP_REPORT_DAY.csv" 
outfile = "C:\\Users\\hsass\\Desktop\\Zcop today.xlsx"  
#pd.read_csv("C:\Users\hsass\Desktop\ZCOP_REPORT_DAY.csv",low_memory = False)
data1 = pd.read_csv(infile,usecols=["EMP_CODE","CAREER_BAND","BULGE","LOCATION","DATE_OF_JOINING","SAP_BU_DESC","EXPERIENCE","BILLABILITY_STATUS","SAP_VERTICAL_DESC","GROUP_CUSTOMER_NAME","FRESHER_ENGAGEMENT_FLAG","DERIVED_SUITE_ID","DERIVED_SUITE_NAME","CUST_NAME","MODEL_TYPE","LOAD_DATE","DERIVED_EMP_CITY","FRESHER_INDEX","TM_EMP_NO","EMPLOYEE_EMAIL_ID","PM_ID","COMPANY_IDENTIFICATION_FG","ONS_OFF_FLAG"], engine='python') [["EMP_CODE","CAREER_BAND","BULGE","LOCATION","DATE_OF_JOINING","SAP_BU_DESC","EXPERIENCE","BILLABILITY_STATUS","SAP_VERTICAL_DESC","GROUP_CUSTOMER_NAME","FRESHER_ENGAGEMENT_FLAG","DERIVED_SUITE_ID","DERIVED_SUITE_NAME","CUST_NAME","MODEL_TYPE","LOAD_DATE","DERIVED_EMP_CITY","FRESHER_INDEX","TM_EMP_NO","EMPLOYEE_EMAIL_ID","PM_ID","COMPANY_IDENTIFICATION_FG","ONS_OFF_FLAG"]]



data1['DATE_OF_JOINING'] = data1['DATE_OF_JOINING'].astype('datetime64[ns]') 


data2 = pd.read_csv(infile,usecols=["EMP_CODE","ONSITE_DAYS","OFFSHORE_DAYS","ONSITE_BILLABLE_DAYS","OFFSHORE_BILLABLE_DAYS","ONSITE_NONBILLABLE_DAYS","OFFSHORE_NONBILLABLE_DAYS","ONSITE_SERVICE_DAYS","OFFSHORE_SERVICE_DAYS","ONSITE_FREE_DAYS","OFFSHORE_FREE_DAYS","SAP_BU_DESC"], engine='python')
data2["Total Billed"]= data2["ONSITE_BILLABLE_DAYS"] + data2["OFFSHORE_BILLABLE_DAYS"]
data2["TotalSupport"]= data2["ONSITE_SERVICE_DAYS"] + data2["OFFSHORE_SERVICE_DAYS"]
data2["TotalVNB"]= data2["ONSITE_NONBILLABLE_DAYS"] + data2["OFFSHORE_NONBILLABLE_DAYS"]
data2["TotalXFree"]= data2["ONSITE_FREE_DAYS"] + data2["ONSITE_FREE_DAYS"]
data2["Virtual/existing"]= data2["Total Billed"] + data2["TotalSupport"]
data2['YStatus'] = np.where(data2['Virtual/existing']>0, 'Virtual', 'Existing')
df1 = data1 


                  
table2 = data2.query('SAP_BU_DESC == ["BFSI"]')


table2["Total Billed"]= table2["ONSITE_BILLABLE_DAYS"] + table2["OFFSHORE_BILLABLE_DAYS"]
table2["TotalSupport"]= table2["ONSITE_SERVICE_DAYS"] + table2["OFFSHORE_SERVICE_DAYS"]
table2["TotalVNB"]= table2["ONSITE_NONBILLABLE_DAYS"] + table2["OFFSHORE_NONBILLABLE_DAYS"]
table2["TotalXFree"]= table2["ONSITE_FREE_DAYS"] + table2["OFFSHORE_FREE_DAYS"]

    
df23 = pd.pivot_table(data2,index=["EMP_CODE"],values =['YStatus','Total Billed','TotalSupport','TotalVNB','TotalXFree'],aggfunc='first')
df23.loc['Total Billed']= df23.sum(numeric_only=True, axis=0)


df24 = pd.pivot_table(table2,index = ["EMP_CODE"],values =['Total Billed','TotalSupport','TotalVNB','TotalXFree'],aggfunc= np.sum,margins=True,margins_name=' Grand Total', fill_value=0)
 

 
    
writer = pd.ExcelWriter(outfile,engine ='xlsxwriter')  



data1.to_excel(writer, sheet_name ="ZCOP",startcol = 14,startrow = 0)



workbook = writer.book
worksheet = writer.sheets["ZCOP"]
worksheet.set_zoom(100)




df23.to_excel(writer, sheet_name ="ZCOP", startcol = 0,startrow = 3)


df24.to_excel(writer, sheet_name ="ZCOP", startcol = 8,startrow = 3)



worksheet.set_column('A:F', 10)
worksheet.set_column('I:M', 10)
worksheet.set_column('P:AD', 10)
    
writer.save() 
