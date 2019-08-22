'''
Created on May 29, 2019
Ch07
@author: Burkhard A. Meier
'''

import mysql.connector 
import Ch07_Code.GuiDBConfig as guiConf 

# unpack dictionary credentials  
conn = mysql.connector.connect(**guiConf.dbConfig) 
print(conn) 