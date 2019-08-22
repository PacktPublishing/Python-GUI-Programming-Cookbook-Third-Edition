'''
Created on Aug 18, 2019
@author: Burkhard A. Meier
'''



import sys
from PyQt5.QtWidgets import QApplication, QWidget 
 

class GUI(QWidget):                 # inherit from QWidget
    def __init__(self): 
        super().__init__()          # initialize super class, which creates the Window  
        self.initUI()               # refer to Window as 'self'
          
    def initUI(self):   
        self.setWindowTitle('PyQt5 GUI')    # call method
 
 
if __name__ == '__main__':     
    app = QApplication(sys.argv)        # create Application     
    gui = GUI()                         # create instance of class
    gui.show()                          # show the constructed PyQt window
    sys.exit(app.exec_())               # execute the application




