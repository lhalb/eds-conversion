# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DiaColsToPlot(object):
    def setupUi(self, DiaColsToPlot):
        DiaColsToPlot.setObjectName("DiaColsToPlot")
        DiaColsToPlot.resize(256, 388)
        DiaColsToPlot.setSizeGripEnabled(False)
        DiaColsToPlot.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(DiaColsToPlot)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_dialog = QtWidgets.QLineEdit(DiaColsToPlot)
        self.txt_dialog.setObjectName("txt_dialog")
        self.verticalLayout.addWidget(self.txt_dialog)
        self.list_dialog = QtWidgets.QListWidget(DiaColsToPlot)
        self.list_dialog.setObjectName("list_dialog")
        self.verticalLayout.addWidget(self.list_dialog)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(DiaColsToPlot)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DiaColsToPlot)
        self.buttonBox.accepted.connect(DiaColsToPlot.close)
        self.buttonBox.rejected.connect(DiaColsToPlot.close)
        self.buttonBox.accepted.connect(DiaColsToPlot.accept)
        QtCore.QMetaObject.connectSlotsByName(DiaColsToPlot)

    def retranslateUi(self, DiaColsToPlot):
        _translate = QtCore.QCoreApplication.translate
        DiaColsToPlot.setWindowTitle(_translate("DiaColsToPlot", "Zu plottende Elemente"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DiaColsToPlot = QtWidgets.QDialog()
    ui = Ui_DiaColsToPlot()
    ui.setupUi(DiaColsToPlot)
    DiaColsToPlot.show()
    sys.exit(app.exec_())