# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\edsgui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_edxKonverter(object):
    def setupUi(self, edxKonverter):
        edxKonverter.setObjectName("edxKonverter")
        edxKonverter.resize(326, 515)
        self.centralwidget = QtWidgets.QWidget(edxKonverter)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.but_plot = QtWidgets.QPushButton(self.centralwidget)
        self.but_plot.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_plot.sizePolicy().hasHeightForWidth())
        self.but_plot.setSizePolicy(sizePolicy)
        self.but_plot.setMinimumSize(QtCore.QSize(75, 75))
        self.but_plot.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/chart-512px.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.but_plot.setIcon(icon)
        self.but_plot.setIconSize(QtCore.QSize(65, 65))
        self.but_plot.setObjectName("but_plot")
        self.horizontalLayout_4.addWidget(self.but_plot)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gb_smooth = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(16)
        self.gb_smooth.setFont(font)
        self.gb_smooth.setAlignment(QtCore.Qt.AlignCenter)
        self.gb_smooth.setCheckable(True)
        self.gb_smooth.setObjectName("gb_smooth")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gb_smooth)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_smooth = QtWidgets.QLineEdit(self.gb_smooth)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_smooth.sizePolicy().hasHeightForWidth())
        self.txt_smooth.setSizePolicy(sizePolicy)
        self.txt_smooth.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(10)
        self.txt_smooth.setFont(font)
        self.txt_smooth.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txt_smooth.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_smooth.setClearButtonEnabled(False)
        self.txt_smooth.setObjectName("txt_smooth")
        self.horizontalLayout.addWidget(self.txt_smooth)
        self.verticalLayout_2.addWidget(self.gb_smooth)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.but_open_folder = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_open_folder.sizePolicy().hasHeightForWidth())
        self.but_open_folder.setSizePolicy(sizePolicy)
        self.but_open_folder.setMinimumSize(QtCore.QSize(150, 150))
        self.but_open_folder.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/folder-512px.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.but_open_folder.setIcon(icon1)
        self.but_open_folder.setIconSize(QtCore.QSize(130, 130))
        self.but_open_folder.setFlat(False)
        self.but_open_folder.setObjectName("but_open_folder")
        self.gridLayout.addWidget(self.but_open_folder, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.status_folder = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_folder.sizePolicy().hasHeightForWidth())
        self.status_folder.setSizePolicy(sizePolicy)
        self.status_folder.setMinimumSize(QtCore.QSize(40, 40))
        self.status_folder.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/red_light-512px.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.status_folder.setIcon(icon2)
        self.status_folder.setIconSize(QtCore.QSize(40, 40))
        self.status_folder.setCheckable(False)
        self.status_folder.setFlat(True)
        self.status_folder.setObjectName("status_folder")
        self.horizontalLayout_3.addWidget(self.status_folder)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.but_process = QtWidgets.QPushButton(self.centralwidget)
        self.but_process.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_process.sizePolicy().hasHeightForWidth())
        self.but_process.setSizePolicy(sizePolicy)
        self.but_process.setMinimumSize(QtCore.QSize(160, 160))
        self.but_process.setMaximumSize(QtCore.QSize(170, 170))
        self.but_process.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/start-512px.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.but_process.setIcon(icon3)
        self.but_process.setIconSize(QtCore.QSize(150, 150))
        self.but_process.setAutoDefault(False)
        self.but_process.setDefault(False)
        self.but_process.setFlat(False)
        self.but_process.setObjectName("but_process")
        self.horizontalLayout_5.addWidget(self.but_process)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.status_file = QtWidgets.QPushButton(self.centralwidget)
        self.status_file.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_file.sizePolicy().hasHeightForWidth())
        self.status_file.setSizePolicy(sizePolicy)
        self.status_file.setMinimumSize(QtCore.QSize(40, 40))
        self.status_file.setText("")
        self.status_file.setIcon(icon2)
        self.status_file.setIconSize(QtCore.QSize(40, 40))
        self.status_file.setCheckable(False)
        self.status_file.setFlat(True)
        self.status_file.setObjectName("status_file")
        self.horizontalLayout_2.addWidget(self.status_file)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.but_open_file = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_open_file.sizePolicy().hasHeightForWidth())
        self.but_open_file.setSizePolicy(sizePolicy)
        self.but_open_file.setMinimumSize(QtCore.QSize(150, 150))
        self.but_open_file.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/file-512px.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.but_open_file.setIcon(icon4)
        self.but_open_file.setIconSize(QtCore.QSize(130, 130))
        self.but_open_file.setDefault(False)
        self.but_open_file.setFlat(False)
        self.but_open_file.setObjectName("but_open_file")
        self.gridLayout.addWidget(self.but_open_file, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        edxKonverter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(edxKonverter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 326, 21))
        self.menubar.setObjectName("menubar")
        edxKonverter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(edxKonverter)
        self.statusbar.setObjectName("statusbar")
        edxKonverter.setStatusBar(self.statusbar)

        self.retranslateUi(edxKonverter)
        QtCore.QMetaObject.connectSlotsByName(edxKonverter)

    def retranslateUi(self, edxKonverter):
        _translate = QtCore.QCoreApplication.translate
        edxKonverter.setWindowTitle(_translate("edxKonverter", "edx-Konverter"))
        self.but_plot.setToolTip(_translate("edxKonverter", "<html><head/><body><p>Plottet die Elementdaten<br/><span style=\" font-weight:600;\">(nur aktiv, wenn einzelne Datei angewählt ist)</span></p><p>Über Einstellungsbutton können einzlene Elemente an- und abgewählt werden.</p></body></html>"))
        self.gb_smooth.setToolTip(_translate("edxKonverter", "Stellt ein, ob die Werte mit gleitendem Durchschnitt geglättet werden"))
        self.gb_smooth.setTitle(_translate("edxKonverter", "Glätten"))
        self.txt_smooth.setToolTip(_translate("edxKonverter", "Anzahl der Werte, über die geglättet wird"))
        self.txt_smooth.setText(_translate("edxKonverter", "20"))
        self.txt_smooth.setPlaceholderText(_translate("edxKonverter", "Anzahl Glättungspunkte"))
        self.but_open_folder.setToolTip(_translate("edxKonverter", "<html><head/><body><p>Ordner öffnen.</p><p>Dateien sollten vorher in folgende Struktur gebracht werden: </p><p>Ebene 0<br/>  ˪ Ordner 1<br/>    ˪ CSV-1<br/>    ˪ ...<br/>    ˪ CSV-n</p><p>  ˪ Ordner 2<br/>    ˪ CSV-1<br/>    ˪ ...<br/>    ˪ CSV-n</p><p>...</p><p>  ˪ Ordner n<br/>    ˪ CSV-1<br/>    ˪ ...<br/>    ˪ CSV-n</p></body></html>"))
        self.status_folder.setToolTip(_translate("edxKonverter", "<html><head/><body><p>Statusinformationen zu Dateien/Ordnern</p></body></html>"))
        self.but_process.setToolTip(_translate("edxKonverter", "Konvertiert die ausgewählte Datei/die ausgewählten Dateien in .xlsx-Dateien"))
        self.status_file.setToolTip(_translate("edxKonverter", "<html><head/><body><p>Statusinformationen zu Dateien/Ordnern</p></body></html>"))
        self.but_open_file.setToolTip(_translate("edxKonverter", "<html><head/><body><p>Datei öffnen.</p><p>Auswählbare Dateien: <br/>- *.csv</p></body></html>"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    edxKonverter = QtWidgets.QMainWindow()
    ui = Ui_edxKonverter()
    ui.setupUi(edxKonverter)
    edxKonverter.show()
    sys.exit(app.exec_())
