from src.interface.janela_principal import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainDisplay = QtWidgets.QMainWindow()
    ui = Ui_MainDisplay()
    ui.setupUi(MainDisplay)
    MainDisplay.show()
    sys.exit(app.exec_())
