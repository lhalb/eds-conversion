from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon, QPixmap
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from lib.edsHelper import gleit_durch
import os.path as op

import plotting as PLT


class PlotDialog(QtWidgets.QDialog, PLT.Ui_PlotWindow):
    def __init__(self, plot_data, calc_type, all_elements, smooth, n):
        super(PlotDialog, self).__init__()

        self.setupUi(self)

        self.cb_element.addItems(all_elements)
        self.current_element = str(self.cb_element.currentText())

        if smooth:
            self.cb_toggle_smooth.setChecked(True)
        else:
            self.cb_toggle_smooth.setChecked(False)

        self.data = plot_data
        self.smooth = smooth
        self.slid_max = 1

        self.x_data = plot_data['Distance (um)']
        # aktuellen Wert fuer y bekommen
        self.y_data = self.get_y_data()

        self.current_type = calc_type

        self.c1 = pg.PlotCurveItem()
        self.c1.setData(self.x_data.values, self.y_data.values)
        self.graphWidget.addItem(self.c1)

        self.initialize_slider(n)

        self.c2 = pg.PlotCurveItem()
        # self.c2.setData(0)

        if smooth:
            self.activate_slider()
            self.activate_smooth()

        self.initialize_plot()
        self.update_labels_and_title()

        self.setup_triggers()

        file_root = QtCore.QFileInfo(__file__).absolutePath()
        self.root = op.dirname(file_root)

        self.set_icons()

    def set_icons(self):
        # Setze icon
        icon = QIcon()
        icon.addPixmap(QPixmap(self.root + "/icons/appicon.ico"), QIcon.Normal, QIcon.On)
        self.setWindowIcon(icon)

    def setup_triggers(self):
        # self.slider.sliderReleased.connect(self.action_on_slider_press)
        self.cb_element.currentTextChanged.connect(self.on_element_change)
        self.cb_toggle_smooth.stateChanged.connect(self.toggle_smooth)
        self.txt_max.editingFinished.connect(self.update_slider_max)
        self.slider.valueChanged.connect(self.action_on_slider_press)

    def toggle_smooth(self):
        if self.cb_toggle_smooth.isChecked():
            self.smooth = True
            self.activate_slider()
            self.activate_smooth()
        else:
            self.smooth = False
            self.deactivate_slider()
            self.deactivate_smooth()


    def initialize_plot(self):
        self.graphWidget.setBackground('w')
        self.graphWidget.setLabel('bottom', self.x_data.name)
        self.graphWidget.setTitle(self.current_type)
        pen1 = pg.mkPen(color=(255, 0, 0), width=1.5, style=QtCore.Qt.DashLine)
        self.c1.setPen(pen1)

        pen2 = pg.mkPen(color=(0, 0, 255), width=3)
        self.c2.setPen(pen2)

    def update_labels_and_title(self):
        y_lab = f'{self.current_element}'
        self.graphWidget.setLabel('left', y_lab)

    def update_current_element(self):
        self.current_element = str(self.cb_element.currentText())

    def get_y_data(self):
        return self.data[self.current_element]

    def on_element_change(self):
        self.update_current_element()
        self.y_data = self.get_y_data()
        self.update_labels_and_title()

        self.c1.setData(self.x_data.values, self.y_data.values)
        if self.smooth:
            self.update_smooth()

    def action_on_slider_press(self):
        current_value = str(self.slider.value())
        self.update_smooth()
        self.labelCurrentValueSlider.setText(current_value)

    def update_smooth(self):
        x = self.x_data
        y = self.y_data

        n = self.slider.value()

        y2 = gleit_durch(y, n)

        self.c2.setData(x.values, y2.values)

    def activate_slider(self):
        self.labelCurrentValueSlider.setEnabled(True)
        self.txt_max.setEnabled(True)
        self.labSlider.setEnabled(True)
        self.slider.setEnabled(True)

    def initialize_slider(self, n):
        # Die Slidergruppe aktivieren
        sli = self.slider
        sli.setMinimum(1)

        set_max = int(len(self.x_data)/12)

        sli.setMaximum(set_max)

        self.txt_max.setText(str(set_max))

        sli.setValue(n)

        self.labelCurrentValueSlider.setText(str(n))

        sli.setTickPosition(QtWidgets.QSlider.TicksBelow)

    def deactivate_slider(self):
        self.labelCurrentValueSlider.setEnabled(False)
        self.txt_max.setEnabled(False)
        self.labSlider.setEnabled(False)
        self.slider.setEnabled(False)

    def update_slider_max(self):
        new_max = int(self.txt_max.text())
        slider_current = self.slider.value()
        self.slider.setMaximum(new_max)
        # self.slider.setValue(slider_current)

    def deactivate_smooth(self):
        self.graphWidget.removeItem(self.c2)

    def activate_smooth(self):
        self.graphWidget.addItem(self.c2)
        self.update_smooth()
