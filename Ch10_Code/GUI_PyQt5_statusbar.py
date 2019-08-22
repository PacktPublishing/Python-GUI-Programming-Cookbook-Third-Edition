'''
Created on Aug 18, 2019
@author: Burkhard A. Meier
'''


# class inheriting from QMainWindow  
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow 
 

class GUI(QMainWindow):                 # inherit from QMainWindow
    def __init__(self): 
        super().__init__()              # initialize super class, which creates the window  
        self.initUI()                   # refer to window as 'self'
          
    def initUI(self):   
        self.setWindowTitle('PyQt5 GUI')     # call method
        self.resize(400, 300)                # resize window (width, height)
        self.add_widgets()
        
    def add_widgets(self):
        self.statusBar().showMessage('Text in statusbar')
 
 
if __name__ == '__main__':     
    app = QApplication(sys.argv)        # create Application     
    gui = GUI()                         # create instance of class
    gui.show()                          # show the constructed PyQt window
    sys.exit(app.exec_())               # execute the application
    