'''
Created on May 29, 2019
Ch07
@author: Burkhard A. Meier
'''

import mysql.connector 
# conn = mysql.connect(user=<adminUser>, password=<adminPwd>, host='127.0.0.1') 
conn = mysql.connector.connect(user='Admin', password='admin', host='127.0.0.1') 
print(conn)  
conn.close() 
