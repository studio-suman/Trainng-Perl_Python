    
import os, os.path
import win32com.client
import time
import gzip
import shutil
import subprocess
import sys



if os.path.exists("C:\\Users\\hsass\Desktop\\ZCOP_REPORT_DAY.csv"):
	os.remove("C:\\Users\\hsass\Desktop\\ZCOP_REPORT_DAY.csv")
else:
	print("File Not Found")