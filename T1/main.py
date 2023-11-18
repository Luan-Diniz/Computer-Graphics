import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from src.interface.janela_principal import JanelaPrincipal

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainDisplay = QMainWindow()
    ui = JanelaPrincipal()
    ui.setupUi(MainDisplay)
    MainDisplay.show()
    sys.exit(app.exec_())
