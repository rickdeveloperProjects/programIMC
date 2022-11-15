import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 550
        self.altura = 250
        self.titulo = "Cálculo do IMC - Indice de Massa Corporal"

        label1 = QLabel(self)
        label1.setText('Nome do paciente: ')
        label1.move(20,15)

        label2 = QLabel(self)
        label2.setText('Endereço completo: ')
        label2.move(20, 55)

        label3 = QLabel(self)
        label3.setText('Altura (cm): ')
        label3.move(20, 95)

        label4 = QLabel(self)
        label4.setText('Peso (Kg): ')
        label4.move(20, 135)

        self.label_resultado = QLabel(self)
        self.label_resultado.setText('RESULTADO IMC= ')
        self.label_resultado.move(290, 95)
        self.label_resultado.resize(240,90)
        self.label_resultado.setStyleSheet("QLabel"
                             "{"
                             "border : 2px solid black;"
                             "font-size: 20px;"
                             "background-color:#ccdde8;font:bold"
                              "}")

        self.nome = QLineEdit(self)
        self.nome.setText(' ')
        self.nome.move(130,15)
        self.nome.resize(400,25)

        self.endereco = QLineEdit(self)
        self.endereco.setText(' ')
        self.endereco.move(130, 55)
        self.endereco.resize(400, 25)

        self.alturap = QLineEdit(self)
        self.alturap.setText('')
        self.alturap.move(130, 95)
        self.alturap.resize(150, 25)


        self.peso = QLineEdit(self)   #Peso
        self.peso.setText(' ')
        self.peso.move(130, 135)
        self.peso.resize(150, 25)

        botao_calcular = QPushButton('Calcular',self)
        botao_calcular.move(100,205)
        botao_calcular.resize(120,30)
        botao_calcular.setStyleSheet('QPushButton {background-color:#ccdde8;font:bold}')
        botao_calcular.clicked.connect(self.mostra_resultado)


        botao_reiniciar = QPushButton('Reiniciar',self)
        botao_reiniciar.move(225,205)
        botao_reiniciar.resize(120,30)
        botao_reiniciar.setStyleSheet('QPushButton {background-color:#ccdde8;font:bold}')
        botao_reiniciar.clicked.connect(self.botao_reinicar)

        botao_sair = QPushButton ('Sair',self)
        botao_sair.move(410,205)
        botao_sair.resize(120,30)
        botao_sair.setStyleSheet('QPushButton {background-color:#ccdde8;font:bold}')
        botao_sair.clicked.connect(self.botao_sair)

        self.CarregarJanela()

    def CarregarJanela (self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_calcular(self):
       print ('Teste')

    def mostra_resultado(self):
        altura = float(self.alturap.text())
        peso = float(self.peso.text())
        IMC = (peso/(altura**2))

        self.label_resultado.setNum(IMC)

    def botao_reinicar(self):
        self.label_resultado.setText('RESULTADO IMC= ')
        self.nome.setText(' ')
        self.endereco.setText(' ')
        self.alturap.setText(' ')
        self.peso.setText(' ')

    def botao_sair(self):
        sys.exit()

aplicacao = QApplication(sys.argv)
j= Janela()
sys.exit(aplicacao.exec())


