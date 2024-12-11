# coding:utf-8
import sys
import os
from time import sleep

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
import qfluentwidgets as qfw
from qfluentwidgets import FluentIcon

class ButtonView(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet('Demo{background: white} QLabel{font-size: 20px}')



class Demo(ButtonView):

    # noinspection PyTypeChecker
    def __init__(self):
        super().__init__()

        # Text
        self.label = QLabel('Chose something ', self)

        # Virus Button
        self.virusButton = qfw.PrimaryPushButton(FluentIcon.PROJECTOR, 'Start megaVirus', self)

        # Compile Button
        self.compileButton = qfw.PrimaryPushButton(FluentIcon.CONNECT, 'Compile Files', self)

        # AntiVirus Button
        self.antiVirusButton = qfw.PrimaryPushButton(FluentIcon.VPN, 'Start AntiVirus', self)

        self.gridLayout = QGridLayout(self)

        self.gridLayout.addWidget(self.label, 0, 0)
        self.gridLayout.addWidget(self.virusButton, 1, 0, Qt.AlignLeft)
        self.gridLayout.addWidget(self.compileButton, 1, 1, Qt.AlignHCenter)
        self.gridLayout.addWidget(self.antiVirusButton, 1, 2, Qt.AlignRight)

        # noinspection PyUnresolvedReferences
        self.virusButton.clicked.connect(self.virusButtonEvent)
        # noinspection PyUnresolvedReferences
        self.compileButton.clicked.connect(self.compileButtonEvent)
        # noinspection PyUnresolvedReferences
        self.antiVirusButton.clicked.connect(self.antiVirusButtonEvent)

        self.resize(500, 150)

    @staticmethod
    def virusButtonEvent():
        os.system(f"python {os.path.dirname(os.path.abspath(__file__))}/virus/main.py")


    @staticmethod
    def compileButtonEvent():
        # AntiVirus
        os.system(f"{os.path.dirname(os.path.abspath(__file__))}/antiVirus/compile.py")

        sleep(1)

        # Virus
        os.system(f"{os.path.dirname(os.path.abspath(__file__))}/virus/compile.py")


    @staticmethod
    def antiVirusButtonEvent():
        os.system(f"python {os.path.dirname(os.path.abspath(__file__))}/antiVirus/main.py")



if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)

    window = Demo()
    window.show()

    app.exec_()


