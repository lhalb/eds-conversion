
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox as QMB

import edsgui as GUI
from lib import edsHelper as eds
import dialog as dia
from lib.edsPlot import PlotDialog


class App(QtWidgets.QMainWindow, GUI.Ui_edxKonverter):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)  # Laden der UI-Datei
        self.root = QtCore.QFileInfo(__file__).absolutePath()
        self.setup_triggers()
        self.path = None
        self.elements = []
        self.set_icons()

    def set_icons(self):
        # Setze icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.root + "/icons/appicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

    def setup_triggers(self):
        self.but_open_file.clicked.connect(self.file_open)
        self.but_open_folder.clicked.connect(self.folder_open)
        self.status_folder.clicked.connect(self.display_path_info)
        self.status_file.clicked.connect(self.display_path_info)

        self.but_process.clicked.connect(self.process_data)

        self.but_plot.clicked.connect(self.show_plot_window)

    def show_plot_window(self):
        path = self.path
        try:
            data, calc_type, elements = eds.get_data(path)
        except IndexError:
            self.show_error_box('Datentyp falsch!')
            return
        smooth = self.gb_smooth.isChecked()
        window = int(self.txt_smooth.text())
        plt = PlotDialog(data, calc_type, elements, smooth, window)
        plt.exec_()

    def process_data(self):
        file = self.path
        bool_smooth = self.gb_smooth.isChecked()
        n = int(self.txt_smooth.text())
        try:
            eds.run_process(file, smooth_data=bool_smooth, smooth_window=n)
        except IndexError:
            self.show_error_box('Datentyp falsch!')
            return

        self.show_info_box(f'Alle Daten erfolgreich unter\n{self.path}\nbearbeitet.')

    def display_path_info(self):
        p = self.path
        file_or_path = eds.check_path(p)
        # print(file_or_path)
        if file_or_path == 'datei':
            txt = f'Geladene Datei: \n{p}'
        elif file_or_path == 'ordner':
            txt = f'Geladenes Verzeichnis: \n{p}'
        else:
            txt = 'Es wurde keine Datei oder Verzeichnis geladen'
            # print(txt)

        self.show_info_box(txt)

    def clear_path(self):
        self.path = None
        self.check_status_path()

    def check_status_path(self):
        off_icon = QtGui.QIcon(":/icons/icons/red_light-512px.png")
        on_icon = QtGui.QIcon(":/icons/icons/green_light-512px.png")
        p = self.path
        file_or_path = eds.check_path(p)
        if file_or_path == 'datei':
            self.status_file.setIcon(on_icon)
            self.status_folder.setIcon(off_icon)
            self.but_plot.setEnabled(True)
            # self.pb_plotsettings.setEnabled(True)
            self.but_process.setEnabled(True)
        elif file_or_path == 'ordner':
            self.status_file.setIcon(off_icon)
            self.status_folder.setIcon(on_icon)
            self.but_plot.setEnabled(False)
            # self.pb_plotsettings.setEnabled(False)
            self.but_process.setEnabled(True)
        else:
            self.status_file.setIcon(off_icon)
            self.status_folder.setIcon(off_icon)
            self.but_plot.setEnabled(False)
            # self.pb_plotsettings.setEnabled(False)
            self.but_process.setEnabled(False)



    def un_highlight(self, field):
        field.setStyleSheet('border: 1px solid black')
        self.statusBar().setStyleSheet('color:black; font-weight:normal')

    def highlight_field(self, field):
        field.setStyleSheet('border: 2px solid red;')
        self.statusBar().setStyleSheet('color:red; font-weight:bold')

    def file_open(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'W??hle eine Quelldatei', filter='*.csv')[0]
        # Wenn Nutzer Dateipfadauswahl abbricht
        if not fname:
            return

        self.path = fname
        self.check_status_path()


    def folder_open(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, 'W??hle einen Quellordner')
        if not path:
            return
        self.path = path
        self.check_status_path()

    def show_msg_box(self, text='Dies ist eine Warnung.'):
        msg = QMB()
        msg.setWindowTitle("Warnung")
        msg.setText(text)
        msg.setIcon(QMB.Warning)
        msg.setStandardButtons(QMB.Cancel | QMB.Ok)
        msg.setDefaultButton(QMB.Ok)

        returnvalue = msg.exec()
        if returnvalue == QMB.Ok:
            press = True
        else:
            press = False

        return press

    def show_error_box(self, text='Fehler'):
        msg = QMB()
        msg.setWindowTitle("Hinweis")
        msg.setText(text)
        msg.setIcon(QMB.Critical)
        msg.setStandardButtons(QMB.Ok)
        msg.setDefaultButton(QMB.Ok)

        msg.exec()

    def show_info_box(self, text='Info'):
        msg = QMB()
        msg.setWindowTitle("Information")
        msg.setText(text)
        msg.setIcon(QMB.Information)
        msg.setStandardButtons(QMB.Ok)
        msg.setDefaultButton(QMB.Ok)
        msg.exec()


class Dialog(QtWidgets.QDialog, dia.Ui_DiaColsToPlot):
    def __init__(self, elements):
        super(Dialog, self).__init__()
        self.setupUi(self)

        for el in elements:
            self.add_item_to_list(el)

        self.setup_triggers()

    def add_item_to_list(self, text):
        item = QtWidgets.QListWidgetItem()
        item.setText(text)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.list_dialog.addItem(item)

    def setup_triggers(self):
        self.buttonBox.accepted.connect(self.onAccept)
        self.buttonBox.rejected.connect(self.onReject)

    def onAccept(self):
        self.accept()

    def onReject(self):
        self.reject()
