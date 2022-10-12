
# # coding: utf-8

# # In[15]:

# import pandas as pd
# import numpy as np
# import openpyxl

#sys.setdefaultencoding('windows-1252')


# # In[17]:

# data1 = pd.read_csv("C:\Users\hsass\AppData\Local\Temp\7zO0E215F81\ZCOP_REPORT_DAY.csv",usecols=["EMP_CODE","CAREER_BAND","BULGE","LOCATION","DATE_OF_JOINING","SAP_BU_DESC","EXPERIENCE","BILLABILITY_STATUS","SAP_VERTICAL_DESC","GROUP_CUSTOMER_NAME","FRESHER_ENGAGEMENT_FLAG","DERIVED_SUITE_ID","DERIVED_SUITE_NAME","CUST_NAME","MODEL_TYPE","LOAD_DATE","DERIVED_EMP_CITY"]) [["EMP_CODE","CAREER_BAND","BULGE","LOCATION","DATE_OF_JOINING","SAP_BU_DESC","EXPERIENCE","BILLABILITY_STATUS","SAP_VERTICAL_DESC","GROUP_CUSTOMER_NAME","FRESHER_ENGAGEMENT_FLAG","DERIVED_SUITE_ID","DERIVED_SUITE_NAME","CUST_NAME","MODEL_TYPE" ,"LOAD_DATE","DERIVED_EMP_CITY"]]



# data1['DATE_OF_JOINING'] = data1['DATE_OF_JOINING'].astype('datetime64[ns]') 

# data2 = pd.read_csv("C:\Users\hsass\AppData\Local\Temp\7zO0E215F81\ZCOP_REPORT_DAY.csv",usecols=["EMP_CODE","ONSITE_DAYS","OFFSHORE_DAYS","ONSITE_BILLABLE_DAYS","OFFSHORE_BILLABLE_DAYS","ONSITE_NONBILLABLE_DAYS","OFFSHORE_NONBILLABLE_DAYS","ONSITE_SERVICE_DAYS","OFFSHORE_SERVICE_DAYS","ONSITE_FREE_DAYS","OFFSHORE_FREE_DAYS","SAP_BU_DESC"])
# data2["Total Billed"]= data2["ONSITE_BILLABLE_DAYS"] + data2["OFFSHORE_BILLABLE_DAYS"]
# data2["TotalSupport"]= data2["ONSITE_SERVICE_DAYS"] + data2["OFFSHORE_SERVICE_DAYS"]
# data2["TotalVNB"]= data2["ONSITE_NONBILLABLE_DAYS"] + data2["OFFSHORE_NONBILLABLE_DAYS"]
# data2["TotalXFree"]= data2["ONSITE_FREE_DAYS"] + data2["ONSITE_FREE_DAYS"]
# data2["Virtual/existing"]= data2["Total Billed"] + data2["TotalSupport"]
# data2['YStatus'] = np.where(data2['Virtual/existing']>0, 'Virtual', 'Existing')
# df1 = data1 

                  
# table2 = data2.query('SAP_BU_DESC == ["BFSI"]')

# table2["Total Billed"]= table2["ONSITE_BILLABLE_DAYS"] + table2["OFFSHORE_BILLABLE_DAYS"]
# table2["TotalSupport"]= table2["ONSITE_SERVICE_DAYS"] + table2["OFFSHORE_SERVICE_DAYS"]
# table2["TotalVNB"]= table2["ONSITE_NONBILLABLE_DAYS"] + table2["OFFSHORE_NONBILLABLE_DAYS"]
# table2["TotalXFree"]= table2["ONSITE_FREE_DAYS"] + table2["OFFSHORE_FREE_DAYS"]


# # In[18]:




# df23 = pd.pivot_table(data2,index=["EMP_CODE"],values =['YStatus','Total Billed','TotalSupport','TotalVNB','TotalXFree'],aggfunc='first')
# df23.loc['Total Billed']= df23.sum(numeric_only=True, axis=0)

# df24 = pd.pivot_table(table2,index = ["EMP_CODE"],values =['Total Billed','TotalSupport','TotalVNB','TotalXFree'],aggfunc= np.sum,margins=True,margins_name=' Grand Total', fill_value=0)




# # df23

# # In[85]:

# pd.pivot_table(df26,index= None ,values = 'YStatus',aggfunc="first")


# # In[29]:

# value


# # In[24]:

# value


# # In[33]:

# import numpy as np


# # In[34]:

# np.__version__


# # In[9]:

# import pandas as pd
# import numpy as np
# import string
# import openpyxl               
 

# writer = pd.ExcelWriter("C:\Users\hsass\Desktop\30-Jun\Zcop today.xlsx",engine ='xlsxwriter') 
# import pandas as pd
# import numpy as np
# import string
# import openpyxl               
 

# df23 .to_excel(writer, sheet_name ="ZCOP", startcol = 17,startrow = 0)
# writer.save() 


# # In[67]:

# df23


# # In[88]:

# df24 = pd.pivot_table(data2,index = ["EMP_CODE"],values =['Total Billed','TotalSupport','TotalVNB','TotalXFree','YStatus'],aggfunc="first",margins=True,margins_name=' Grand Total', numeric_only=True, fill_value=0) 


# # In[69]:

# df24


# # In[ ]:

# import pandas as pd
# import numpy as np
# import openpyxl
 
    
# writer = pd.ExcelWriter("‪‪C:\Users\hsass\Desktop\30-Jun\Zcop today.xlsx",engine ='xlsxwriter') 


# data1.to_excel(writer, sheet_name ="ZCOP",startcol = 14,startrow = 0)


# workbook = writer.book
# worksheet = writer.sheets['ZCOP']
# worksheet.set_zoom(100)



# df23.to_excel(writer, sheet_name ='ZCOP', startcol = 0,startrow = 3)

# df24.to_excel(writer, sheet_name ='ZCOP', startcol = 8,startrow = 3)


# worksheet.set_column('A:F', 10)
# worksheet.set_column('I:M', 10)
# worksheet.set_column('P:AD', 10)


    
# writer.save() 


# # In[101]:

# df14pd.DataFrame({'Data': ["SAP_ BU"]})
# df15pd.DataFrame({'Data': ["ALL"]})
# df16pd.DataFrame({'Data': ["SAP_ BU"]})
# df17pd.DataFrame({'Data': ["BFSI"]})


# # In[122]:




# # In[132]:

# data11 = pd.read_csv("C:\Users\hsass\AppData\Local\Temp\7zO0E215F81\ZCOP_REPORT_DAY.csv",usecols=["EMP_CODE","SAP_BU_DESC","SAP_VERTICAL_DESC","BILLABILITY_STATUS","CUST_NAME"])


# # In[5]:

# import pandas as pd
# import numpy as np
# import string as str
# import openpyxl

# writer = pd.ExcelWriter("C:\Users\hsass\Desktop\30-Jun\Zcop today.xlsx",engine ='xlsxwriter') 


# data11.to_excel(writer, sheet_name ="ZCOP",startcol = 15,startrow = 0)

# writer.save() 


# In[142]:

import pandas as pd
import time
import math
import numpy as np
import string as str
import openpyxl
#from importlib import reload
import sys

starttime=time.time()

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
input_file="C:\\Users\\hsass\\desktop\\ZCOP_REPORT_DAY.csv"
zdata = pd.read_csv(input_file,usecols=["EMP_CODE","SAP_BU_DESC","SAP_VERTICAL_DESC","BILLABILITY_STATUS","CUST_NAME"], engine='python')[["EMP_CODE","SAP_BU_DESC","SAP_VERTICAL_DESC","BILLABILITY_STATUS","CUST_NAME"]]


zdata.sort_values(by=['SAP_BU_DESC'],inplace=True) #sorting data based on BU col
# data1['DATE_OF_JOINING'].type

zdata.query('SAP_BU_DESC >= "BFSI"', inplace=True) #filtering on BU - BFSI
# extr=zdata.loc[zdata['SAP_BU_DESC'] == "BFSI"] #selecting cols which are BU
# zdata[extr]
zdata.reset_index(drop=True, inplace=True) #resetting the index
# print(zdata.head(4))
# print(zdata.tail(4))
# print(zdata.index)
# print(zdata.head)

# print(zdata['EMP_CODE'])
# print(type(zdata['EMP_CODE']))

emp=zdata['EMP_CODE']
print(emp[0])
print(zdata.at[0,"EMP_CODE"])

df=pd.read_csv(input_file,engine='python',index_col="EMP_CODE")
#print(df.index)
print(df.head(3))
#print(df.loc["EMP_CODE","FRESHER_ENGAGEMENT_FLAG"])
# writer = pd.ExcelWriter("C:\\Users\\hsass\\Desktop\\30-Jun\\Zcop today.xlsx",engine ='xlsxwriter') 

# zdata.to_excel(writer, sheet_name ="ZCOP",startcol = 0,startrow = 0,index=False) #assiging to excel col indices

# writer.save() #saving to excel

time_taken=time.time() - starttime
hours,rest = divmod(time_taken,3600)
minutes,seconds=divmod(rest,60)
str="---Execution Done in {} minutes and {} seconds ---"
print(str.format(minutes,seconds))

# In[33]:



