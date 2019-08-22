'''
Created on May 29, 2019
Ch07
@author: Burkhard A. Meier
'''

import mysql.connector 
import Ch07_Code.GuiDBConfig as guiConf 

GUIDB = 'GuiDB' 
 
# unpack dictionary credentials  
conn = mysql.connector.connect(**guiConf.dbConfig) 
 
cursor = conn.cursor() 
 
try: 
    cursor.execute("CREATE DATABASE {} \
                    DEFAULT CHARACTER SET 'utf8'".format(GUIDB))     
except mysql.connector.Error as err:                                          
    print("Failed to create DB: {}".format(err)) 
 
conn.close() 