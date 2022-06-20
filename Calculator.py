from multiprocessing.connection import answer_challenge
from unicodedata import numeric
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 566)
        MainWindow.setStyleSheet("background-color: rgb(227, 235, 205);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 431, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.outputLabel.setFont(font)
        self.outputLabel.setStyleSheet("background-color: rgb(174, 219, 206);")
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.outputLabel.setLineWidth(3)
        self.outputLabel.setMidLineWidth(0)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("CE"))
        self.clearButton.setGeometry(QtCore.QRect(10, 120, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.clearButton.setFont(font)
        self.clearButton.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"background-color: rgb(157, 214, 83);\n"
"color: rgb(99, 86, 102);")
        self.clearButton.setObjectName("clearButton")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(120, 120, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentButton.setFont(font)
        self.percentButton.setStyleSheet("background-color: rgb(131, 154, 168);\n"
"color: rgb(99, 86, 102);")
        self.percentButton.setObjectName("percentButton")
        self.devideButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("/"))
        self.devideButton.setGeometry(QtCore.QRect(230, 120, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.devideButton.setFont(font)
        self.devideButton.setStyleSheet("background-color: rgb(131, 154, 168);color: rgb(99, 86, 102);")
        self.devideButton.setObjectName("devideButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(340, 120, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setStyleSheet("background-color: rgb(131, 154, 168);color: rgb(99, 86, 102);")
        self.multiplyButton.setObjectName("multiplyButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 200, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setStyleSheet("color: rgb(99, 86, 102);background-color: rgb(131, 154, 168);")
        self.sevenButton.setObjectName("sevenButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(120, 200, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setStyleSheet("background-color: rgb(131, 154, 168);color: rgb(99, 86, 102);")
        self.eightButton.setObjectName("eightButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(230, 200, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setStyleSheet("background-color: rgb(131, 154, 168);color: rgb(99, 86, 102);")
        self.nineButton.setObjectName("nineButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(340, 200, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setStyleSheet("background-color: rgb(131, 154, 168);color: rgb(99, 86, 102);")
        self.minusButton.setObjectName("minusButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 280, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setStyleSheet("color: rgb(99, 86, 102);background-color: rgb(131, 154, 168);")
        self.fourButton.setObjectName("fourButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(120, 280, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setStyleSheet("color: rgb(99, 86, 102);background-color: rgb(131, 154, 168);")
        self.fiveButton.setObjectName("fiveButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(230, 280, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setStyleSheet("color: rgb(99, 86, 102);background-color: rgb(131, 154, 168);")
        self.sixButton.setObjectName("sixButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("+"))
        self.addButton.setGeometry(QtCore.QRect(340, 280, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("background-color: rgb(131, 154, 168);color: rgb(99, 86, 102);")
        self.addButton.setObjectName("addButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 360, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setStyleSheet("color: rgb(99, 86, 102);background-color: rgb(131, 154, 168);")
        self.oneButton.setObjectName("oneButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(120, 360, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setStyleSheet("color: rgb(99, 86, 102);background-color: rgb(131, 154, 168);")
        self.twoButton.setObjectName("twoButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(230, 360, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setStyleSheet("color: rgb(99, 86, 102);background-color: rgb(131, 154, 168);")
        self.threeButton.setObjectName("threeButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(340, 360, 101, 151))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setAutoFillBackground(False)
        self.equalButton.setStyleSheet("background-color: rgb(174, 219, 206);\n"
"color: rgb(99, 86, 102);")
        self.equalButton.setObjectName("equalButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(10, 440, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setStyleSheet("color: rgb(99, 86, 102);background-color: rgb(131, 154, 168);")
        self.zeroButton.setObjectName("zeroButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(230, 440, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButton.setFont(font)
        self.decimalButton.setStyleSheet("color: rgb(99, 86, 102);background-color: rgb(131, 154, 168);")
        self.decimalButton.setObjectName("decimalButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def dot_it(self):
        screen = self.outputLabel.text()
        operator_tuple=("/","*","+","-")
        for i in operator_tuple:
            if i not in screen:
                if "." in screen:
                    pass
                else:
                    self.outputLabel.setText(f'{screen}.')
            else:
                if screen[-1].isnumeric() and "." not in screen[screen.rfind(i):]:
                    self.outputLabel.setText(f'{screen}.')
                else:
                    pass

    def math_it(self):
        screen = self.outputLabel.text()
        try:
            answer = eval(screen)
            screen = str(answer)
            if screen[-1] =='0' and screen[-2] == '.':
                screen = screen[:-2]
            self.outputLabel.setText(screen)
        except:
            self.outputLabel.setText("ERROR")
    def press_it(self, pressed):
        if pressed =="CE":
            self.outputLabel.setText("0")
        else:
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.clearButton.setText(_translate("MainWindow", "CE"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.devideButton.setText(_translate("MainWindow", "/"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.decimalButton.setText(_translate("MainWindow", "."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())