import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QGroupBox, QRadioButton, QSlider, QVBoxLayout, QComboBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Standard settings
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # Radio button for soda
        self.radioButton_soda = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_soda.setGeometry(QtCore.QRect(50, 30, 90, 20))

        # adding signal and slot
        self.radioButton_soda.toggled.connect(self.selsoda)

        # Radio button for isotonic
        self.radioButton_isotonic = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_isotonic.setGeometry(QtCore.QRect(150, 30, 90, 20))

        # adding signal and slot
        self.radioButton_isotonic.toggled.connect(self.selisotonic)

        # Radio button for energy
        self.radioButton_energy = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_energy.setGeometry(QtCore.QRect(250, 30, 90, 20))

        # adding signal and slot
        self.radioButton_energy.toggled.connect(self.selenergy)

        #First size slider
        self.sliderSize = QtWidgets.QSlider(self.centralwidget)
        self.sliderSize.setGeometry(QtCore.QRect(45, 100, 50, 50))
        self.sliderSize.setFocusPolicy(Qt.StrongFocus)
        self.sliderSize.setTickPosition(QSlider.TicksBothSides)
        self.sliderSize.setTickInterval(50)
        self.sliderSize.setSingleStep(1)
        self.sliderSize.valueChanged[int].connect(self.changeValue)

        #Second sugar slider
        self.sliderSugar = QtWidgets.QSlider(self.centralwidget)
        self.sliderSugar.setGeometry(QtCore.QRect(145, 100, 50, 50))
        self.sliderSugar.setFocusPolicy(Qt.StrongFocus)
        self.sliderSugar.setTickPosition(QSlider.TicksBothSides)
        self.sliderSugar.setTickInterval(50)
        self.sliderSugar.setSingleStep(1)
        self.sliderSugar.valueChanged[int].connect(self.changeValue)

        #DROP LISTS
        self.firstTastedroplist = QtWidgets.QComboBox(self.centralwidget)
        self.firstTastedroplist.addItems(['None', 'Lemon', 'Orange', 'Lime', 'Mint', 'Mango', 'Fruity', 'Caramel', 'Melon', 'Grassy', 'Other'])
        self.firstTastedroplist.setGeometry(QtCore.QRect(50, 200, 100, 30))
        self.firstTastedroplist.currentIndexChanged.connect(self.changeValue)

        self.secondTastedroplist = QtWidgets.QComboBox(self.centralwidget)
        self.secondTastedroplist.addItems(
            ['None', 'Lemon', 'Orange', 'Lime', 'Mint', 'Mango', 'Fruity', 'Caramel', 'Melon', 'Grassy', 'Other'])
        self.secondTastedroplist.setGeometry(QtCore.QRect(150, 200, 100, 30))
        self.secondTastedroplist.currentIndexChanged.connect(self.changeValue)

        self.thirdTastedroplist = QtWidgets.QComboBox(self.centralwidget)
        self.thirdTastedroplist.addItems(
            ['None', 'Lemon', 'Orange', 'Lime', 'Mint', 'Mango', 'Fruity', 'Caramel', 'Melon', 'Grassy', 'Other'])
        self.thirdTastedroplist.setGeometry(QtCore.QRect(250, 200, 100, 30))
        self.thirdTastedroplist.currentIndexChanged.connect(self.changeValue)

        self.fourthTastedroplist = QtWidgets.QComboBox(self.centralwidget)
        self.fourthTastedroplist.addItems(
            ['None', 'Lemon', 'Orange', 'Lime', 'Mint', 'Mango', 'Fruity', 'Caramel', 'Melon', 'Grassy', 'Other'])
        self.fourthTastedroplist.setGeometry(QtCore.QRect(100, 250, 100, 30))
        self.fourthTastedroplist.currentIndexChanged.connect(self.changeValue)

        self.fivethTastedroplist = QtWidgets.QComboBox(self.centralwidget)
        self.fivethTastedroplist.addItems(
            ['None', 'Lemon', 'Orange', 'Lime', 'Mint', 'Mango', 'Fruity', 'Caramel', 'Melon', 'Grassy', 'Other'])
        self.fivethTastedroplist.setGeometry(QtCore.QRect(200, 250, 100, 30))
        self.fivethTastedroplist.currentIndexChanged.connect(self.changeValue)
        #DROP LISTS

        # LABELES
        self.ChooseDrinkLabel = QtWidgets.QLabel(self.centralwidget)
        self.ChooseDrinkLabel.setGeometry(QtCore.QRect(150, 0, 210, 20))

        self.SizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.SizeLabel.setGeometry(QtCore.QRect(50, 60, 210, 20))

        self.SugarLabel = QtWidgets.QLabel(self.centralwidget)
        self.SugarLabel.setGeometry(QtCore.QRect(150, 60, 210, 20))

        self.HealthyLabel = QtWidgets.QLabel(self.centralwidget)
        self.HealthyLabel.setGeometry(QtCore.QRect(265, 80, 200, 20))

        self.SelectTastes = QtWidgets.QLabel(self.centralwidget)
        self.SelectTastes.setGeometry(QtCore.QRect(150, 175, 90, 20))
        # LABELES

        #CheckBox
        self.HealthyCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.HealthyCheckBox.setGeometry(QtCore.QRect(275, 100, 20, 20))

        #Final Button
        self.FinalButton = QtWidgets.QPushButton(self.centralwidget)
        self.FinalButton.setGeometry(QtCore.QRect(150, 300, 100, 50))

        #Output line

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def changeValue(self, value):
        #стандартизировать данные
        print(value)

    def selsoda(self, selected):
        if selected:
            return 0

    def selisotonic(self, selected):
        if selected:
            return 0

    def selenergy(self, selected):
        if selected:
            return 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton_soda.setText(_translate("MainWindow", "Soda"))
        self.ChooseDrinkLabel.setText(_translate("MainWindow", "Select drink:"))
        self.SizeLabel.setText(_translate("MainWindow", "Size"))
        self.SugarLabel.setText(_translate("MainWindow", "Sugar"))
        self.radioButton_isotonic.setText(_translate("MainWindow", "Isotonic"))
        self.radioButton_energy.setText(_translate("MainWindow", "Energy"))
        self.HealthyLabel.setText(_translate("MainWindow", "Healthy"))
        self.SelectTastes.setText(_translate("MainWindow", "Select Tastes: "))
        self.FinalButton.setText(_translate("MainWindow", "Start"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())