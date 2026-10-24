import sys
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QPushButton, QGraphicsScene, QGraphicsView, QMainWindow , QWidget , QLabel
from QLed import QLed
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        
        self.setWindowTitle("Softech Control Solution")
        self.setGeometry(0, 0, 480, 640)
        
        self.label_B = QLabel('', self)
        self.label_B.setStyleSheet("border :1px solid Black; color:blue;")
        self.label_B.setAlignment(Qt.AlignCenter)
        self.label_B.move(5, 5)
        self.label_B.resize(470,630)
        
        self.label_head = QLabel('HELP CHAIN ANDON', self)
        self.label_head.setFont(QFont('Times', 32, QFont.Bold))
        self.label_head.setStyleSheet("border :0px solid Black; color:blue;")
        self.label_head.setAlignment(Qt.AlignCenter)
        self.label_head.move(0, 0)
        self.label_head.resize(480,70)
    

    #1
        self.Prod_led=QLed(self, shape=QLed.Round)
        self.Prod_led.onColour=QLed.Green
        self.Prod_led.move(115, 70)
        self.Prod_led.resize(250,150)
        self.Prod_led.value=True
        #self.Prod_led.clicked.connect(self.Call_Prod_click)
        
        self.Maint_led=QLed(self, shape=QLed.Round)
        self.Maint_led.onColour=QLed.Green
        self.Maint_led.move(115, 210)
        self.Maint_led.resize(250,150)
        self.Maint_led.value=True
        #self.Maint_led.clicked.connect(self.Call_Maint_click)
        
        self.Qty_led=QLed(self, shape=QLed.Round)
        self.Qty_led.onColour=QLed.Green
        self.Qty_led.move(115, 350)
        self.Qty_led.resize(250,150)
        self.Qty_led.value=True
        #self.Qty_led.clicked.connect(self.Call_Qty_click)

        self.Tools_led=QLed(self, shape=QLed.Round)
        self.Tools_led.onColour=QLed.Green
        self.Tools_led.move(115, 490)
        self.Tools_led.resize(250,150)
        self.Tools_led.value=True
        #self.Tools_led.clicked.connect(self.Call_Tool_click)
        
        #2
        self.btn_Prod = QPushButton('PRODUCTION',self)
        self.btn_Prod.setFont(QFont('Times', 20, QFont.Bold))
        self.btn_Prod.move(130, 100)
        self.btn_Prod.resize(220,95)
        self.btn_Prod.clicked.connect(self.Call_Prod_click)
        self.btn_Prod.setStyleSheet("border-radius : 40; border : 1px solid black; outline: none; background: Transparent")
        
        self.btn_Maint = QPushButton('MAINTANCE',self)
        self.btn_Maint.setFont(QFont('Times', 20, QFont.Bold))
        self.btn_Maint.move(130, 240)
        self.btn_Maint.resize(220,95)
        self.btn_Maint.clicked.connect(self.Call_Maint_click)
        self.btn_Maint.setStyleSheet("border-radius : 40; border : 1px solid black; outline: none; background: Transparent")
        
        self.btn_Qty = QPushButton('QUALITY',self)
        self.btn_Qty.setFont(QFont('Times', 20, QFont.Bold))
        self.btn_Qty.move(130, 380)
        self.btn_Qty.resize(220,95)
        self.btn_Qty.clicked.connect(self.Call_Qty_click)
        self.btn_Qty.setStyleSheet("border-radius : 40; border : 1px solid black; outline: none; background: Transparent")
        
        self.btn_Tool = QPushButton('TOOL',self)
        self.btn_Tool.setFont(QFont('Times', 20, QFont.Bold))
        self.btn_Tool.move(130, 520)
        self.btn_Tool.resize(220,95)
        self.btn_Tool.clicked.connect(self.Call_Tool_click)
        self.btn_Tool.setStyleSheet("border-radius : 40; border : 1px solid black; outline: none; background: Transparent")
        
        
        
    def Call_Prod_click(self) -> None:
        if self.Prod_led.onColour==QLed.Green:
            self.Prod_led.onColour=QLed.Red
        elif self.Prod_led.onColour==QLed.Red:
            self.Prod_led.onColour=QLed.Yellow
        else:
            self.Prod_led.onColour=QLed.Green
    
    def Call_Maint_click(self) -> None:
        if self.Maint_led.onColour==QLed.Green:
            self.Maint_led.onColour=QLed.Red
        elif self.Maint_led.onColour==QLed.Red:
            self.Maint_led.onColour=QLed.Yellow
        else:
            self.Maint_led.onColour=QLed.Green
        
    def Call_Qty_click(self) -> None:
        if self.Qty_led.onColour==QLed.Green:
            self.Qty_led.onColour=QLed.Red
        elif self.Qty_led.onColour==QLed.Red:
            self.Qty_led.onColour=QLed.Yellow
        else:
            self.Qty_led.onColour=QLed.Green
        
    def Call_Tool_click(self) -> None:
        if self.Tools_led.onColour==QLed.Green:
            self.Tools_led.onColour=QLed.Red
        elif self.Tools_led.onColour==QLed.Red:
            self.Tools_led.onColour=QLed.Yellow
        else:
            self.Tools_led.onColour=QLed.Green
            

if __name__ == '__main__':
    app = QApplication([])
    app.setOrganizationName('Softech')
    app.setApplicationName('Nurse Station')
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )