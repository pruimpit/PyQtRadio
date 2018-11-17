import sys
from PyQt5.QtWidgets import QDialog, QApplication
import dialog
import radio
import atexit

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = dialog.Ui_Dialog()
        self.ui.setupUi(self)
        self.radio = radio.radio(self.ui, self)
        self.show()
    
    def stop(self):
        self.radio.stop()
        
        
            


app = QApplication(sys.argv)
w = AppWindow()
atexit.register(w.stop)
w.show()

sys.exit(app.exec_())