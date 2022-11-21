import math
import string as str
import sys
import time
from datetime import datetime

import numpy as np
import openpyxl
import pandas as pd

infile =   r"C:\Users\HSASS\OneDrive - Wipro\Suman\ETR\Mapping\completeFile_part_0.csv"
infile2 =   r"C:\Users\HSASS\OneDrive - Wipro\Suman\ETR\Mapping\completeFile_part_1.csv"
outfile =  r"C:\Users\HSASS\OneDrive - Wipro\Suman\ETR\Mapping\completeFile_A2.csv"
map_file = r"C:\Users\HSASS\OneDrive - Wipro\Desktop\AIR\Ops_Template_v1.xlsx"
table = pd.read_csv(infile, engine='python',sep=',', quotechar='"', error_bad_lines=False)
table2 = pd.read_csv(infile2, engine='python',sep=',', quotechar='"', error_bad_lines=False)

vertical_stack = pd.concat([table, table2], axis=0)

vertical_stack.to_csv(outfile,index=False)