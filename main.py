import sys
from PyQt5 import QtWidgets
import appGUI

'''
Autor: Halbauer
Date: 19.08.2021
'''


def main():
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    form = appGUI.App()  # We set the form to be our ExampleApp (bsp1)
    form.show()  # Show the form
    sys.exit(app.exec_())  # and execute the app


if __name__ == '__main__':
    main()
