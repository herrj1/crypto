import sys
from PyQt4.QtGui import *
 
# Create an PyQT4 application objects

a = QApplication(sys.argv)       
 
# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QWidget()
 
# Show a message boxes
result = QMessageBox.question(w, 'Message', "Do you like Python?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
 
if result == QMessageBox.Yes:
    print 'Yes!'
else:
    print 'No!'        
 
# Show windows
w.show() 
 
sys.exit(a.exec_())

Result:
