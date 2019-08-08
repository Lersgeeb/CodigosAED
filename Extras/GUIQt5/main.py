from ventana_ui import *

class MainWindowUser(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #No entiendo nada de lo que esta arriba
    
        #Esto ya si 
        self.label.setText("Haz click en el boton")
        self.pushButton.setText("Presionameeeeee!")

        # Conectamos los eventos con sus acciones
        self.pushButton.clicked.connect(self.actualizar)

    def actualizar(self):
        self.label.setText("¡Acabas de hacer clic en el botón!")

    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindowUser()
    window.show()
    app.exec_()
    #creo que es para que salga la ventana xd0.
    