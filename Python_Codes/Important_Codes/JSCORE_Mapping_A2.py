import pandas as pd
"""import time
import math
import numpy as np
import string as str
import openpyxl
from datetime import datetime
import sys"""

infile =   r"C:\Users\HSASS\OneDrive - Wipro\Suman\ETR\Mapping\completeFile_part_0.csv"
infile2 =   r"C:\Users\HSASS\OneDrive - Wipro\Suman\ETR\Mapping\completeFile_part_1.csv"
outfile =  r"C:\Users\HSASS\OneDrive - Wipro\Suman\ETR\Mapping\completeFile_A2.csv"
map_file = r"C:\Users\HSASS\OneDrive - Wipro\Desktop\AIR\Ops_Template_v1.xlsx"
table = pd.read_csv(infile, engine='python',sep=',', quotechar='"')
table2 = pd.read_csv(infile2, engine='python',sep=',', quotechar='"')
print("Read the File....")
vertical_stack = pd.concat([table, table2], axis=0)
print("Merged the Files....")
""" mdata = pd.read_excel(map_file, sheet_name='Sheet1', parse_dates=['INDENT_CREATED_ON'])
final = table.merge(mdata, on="CUSTOMER_NO", how='left')
odata = final.query('Sector != [""]')
odata = final[final['Sector'].notnull()]
mask = final['INDENT_CREATED_ON'].dt.month >= 10 """
vertical_stack.to_csv(outfile,index=False)
print("Executed Succesfully")