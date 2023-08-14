import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)  # terminates window
    win = QMainWindow() # desktop window
   
   
    win.setGeometry(1200,300,500,500) # (top right x,y size x , y)
    win.setWindowTitle("BALLS")
    win.setWindowIcon(QIcon("projects\\amongus.jpg")) # need QtGui for icon 
    win.setToolTip("Balls In yo jaw")
    
    
    lbl_name = QtWidgets.QLabel(win) # sends lable to the window
    lbl_name.setText('Enter your name :') # sets text to lable 
    lbl_name.move(50,50) # sets position x,y
    
    lbl_surname = QtWidgets.QLabel(win) 
    lbl_surname.setText('Enter your surname :')
    lbl_surname.move(50,90)
    
    txt_name = QtWidgets.QLineEdit(win) # text editor
    txt_name.move(200,50)
    
    txt_surname = QtWidgets.QLineEdit(win) # text editor
    txt_surname.move(200,90)

    def clicked(self):
        print("button Clicked")
        print('name: ' + txt_name.text()) # prints the text within the textbox
        print('surname: ' + txt_surname.text())
       

    btn_save = QtWidgets.QPushButton(win) # pushable button
    btn_save.setText("Save")
    btn_save.clicked.connect(clicked) # calls function
    btn_save.move(200,130)    

    win. show() # show window 
    sys.exit(app.exec_()) # exit on command 





window()