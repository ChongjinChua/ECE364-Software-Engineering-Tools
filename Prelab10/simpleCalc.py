# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from math import *
from calculator import *
import re

class CalculatorConsumer(QMainWindow, Ui_Calculator):

    def __init__(self, parent=None):
        super(CalculatorConsumer, self).__init__(parent)
        self.setupUi(self)

        self.txtDisplay.clear()

        self.formula = ""

        self.btn0.clicked.connect(lambda :self.updateNum(0))
        self.btn1.clicked.connect(lambda :self.updateNum(1))
        self.btn2.clicked.connect(lambda :self.updateNum(2))
        self.btn3.clicked.connect(lambda :self.updateNum(3))
        self.btn4.clicked.connect(lambda :self.updateNum(4))
        self.btn5.clicked.connect(lambda :self.updateNum(5))
        self.btn6.clicked.connect(lambda :self.updateNum(6))
        self.btn7.clicked.connect(lambda :self.updateNum(7))
        self.btn8.clicked.connect(lambda :self.updateNum(8))
        self.btn9.clicked.connect(lambda :self.updateNum(9))
        self.btnDot.clicked.connect(lambda :self.updateNum('.'))

        self.btnPlus.clicked.connect(lambda :self.updateOperand('+'))
        self.btnMinus.clicked.connect(lambda :self.updateOperand('-'))
        self.btnMultiply.clicked.connect(lambda :self.updateOperand('*'))
        self.btnDivide.clicked.connect(lambda :self.updateOperand('/'))

        self.decimalPoint = 2
        self.connect(self.cboDecimal, SIGNAL('activated(QString)'), self.cboActivated)

        self.tstate = 1
        self.connect(self.chkSeparator, SIGNAL('clicked()'), self.stateChanged)

        self.btnClear.clicked.connect(self.clear)
        self.btnEqual.clicked.connect(self.print)

    def stateChanged(self):
        if self.tstate:
            self.tstate = 0
        else:
            self.tstate = 1

        self.print()

    def cboActivated(self,index):
        self.decimalPoint = int(index)
        self.print()

    def updateNum(self,index):
        if self.formula != "" and self.operandExist(self.formula[-1]):
            self.txtDisplay.clear()

        if type(index) is str:
            if '.' not in self.txtDisplay.text():
                self.txtDisplay.insert(index)
                self.formula += index

        else:
            self.txtDisplay.insert(str(index))
            self.formula += str(index)

    def updateOperand(self,op):
        if self.formula != "":
            if self.operandExist():
                self.print()

            self.formula += op

    def print(self):
        if self.formula != "" and not self.operandExist(self.formula[-1]):
            self.formula = str("%.{0}f".format(self.decimalPoint) %eval(self.formula))
            self.display = self.formula

            if self.tstate:
                if self.decimalPoint == 0:
                    self.display = "{:,.0f}".format(floor(float(self.display)))
                elif self.decimalPoint == 1:
                    self.display = "{:,.1f}".format(float(self.display))
                elif self.decimalPoint == 2:
                    self.display = "{:,.2f}".format(float(self.display))
                elif self.decimalPoint == 3:
                    self.display = "{:,.3f}".format(float(self.display))
                elif self.decimalPoint == 4:
                    self.display = "{:,.4f}".format(float(self.display))
                elif self.decimalPoint == 5:
                    self.display = "{:,.5f}".format(float(self.display))

            else:
                self.display = self.formula

            self.strlen = self.countLen(self.formula) + self.decimalPoint
            if self.strlen > 12:
                self.display = "Value exceeded 12 digits"

            self.txtDisplay.setText(self.display)

    def countLen(self,string):
        count = 0
        for i in string:
            if i == '.':
                break
            else:
                count += 1
        return count


    def clear(self):
        self.formula = ""
        self.txtDisplay.setText(self.formula)

    def operandExist(self,arg=None):
        if arg is not None:
            if arg == '+' or arg == '-' or arg == '*' or arg == '/':
                return 1
            else:
                return 0
        else:
            statement = self.formula
            if self.formula != "" and self.formula[0] == '-':
                statement = statement[1:]

            if '+' not in statement and '-' not in statement and '*' not in statement and '/' not in statement:
                return 0
            else:
                return 1

currentApp = QApplication(sys.argv)
currentForm = CalculatorConsumer()

currentForm.show()
currentApp.exec_()
