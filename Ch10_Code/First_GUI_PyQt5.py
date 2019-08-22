'''
Created on Aug 18, 2019
@author: Burkhard A. Meier
'''


import sys 
from PyQt5.QtWidgets import QApplication, QWidget
 
app = QApplication(sys.argv)    # sys.argv accepts arguments when run from the command line
gui = QWidget()                 # creates top-level window
gui.show()                      # have to call show() to make it visible
sys.exit(app.exec_())           # run the application; PyQt5 exec_ ends with an underscore


