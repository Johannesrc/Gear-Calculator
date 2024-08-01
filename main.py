# Python module
import sys

# Third-party modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTextEdit

# Own modules
from calculations.calculations import calculate_module
from calculations.calculations import calculate_diametral_pitch


class GearCalculator(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Cálculo de Engranajes')

        layout = QVBoxLayout()

        # Sección para Módulo
        module_layout = QVBoxLayout()
        module_layout.addWidget(QLabel('Cálculo de Engranajes (Módulo)'))

        module_input_layout = QHBoxLayout()
        module_input_layout.addWidget(QLabel('Módulo:'))
        self.module_entry = QLineEdit()
        module_input_layout.addWidget(self.module_entry)
        module_layout.addLayout(module_input_layout)

        teeth_module_input_layout = QHBoxLayout()
        teeth_module_input_layout.addWidget(QLabel('Número de Dientes:'))
        self.teeth_module_entry = QLineEdit()
        teeth_module_input_layout.addWidget(self.teeth_module_entry)
        module_layout.addLayout(teeth_module_input_layout)

        self.module_result = QTextEdit()
        self.module_result.setReadOnly(True)
        module_layout.addWidget(self.module_result)

        module_button = QPushButton('Calcular')
        module_button.clicked.connect(self.calculate_module)
        module_layout.addWidget(module_button)

        layout.addLayout(module_layout)

        # Sección para Paso Diametral
        diametral_pitch_layout = QVBoxLayout()
        diametral_pitch_layout.addWidget(
            QLabel('Cálculo de Engranajes (Paso Diametral)'))

        diametral_pitch_input_layout = QHBoxLayout()
        diametral_pitch_input_layout.addWidget(QLabel('Paso Diametral:'))
        self.diametral_pitch_entry = QLineEdit()
        diametral_pitch_input_layout.addWidget(self.diametral_pitch_entry)
        diametral_pitch_layout.addLayout(diametral_pitch_input_layout)

        teeth_diametral_pitch_input_layout = QHBoxLayout()
        teeth_diametral_pitch_input_layout.addWidget(
            QLabel('Número de Dientes:'))
        self.teeth_diametral_pitch_entry = QLineEdit()
        teeth_diametral_pitch_input_layout.addWidget(
            self.teeth_diametral_pitch_entry)
        diametral_pitch_layout.addLayout(teeth_diametral_pitch_input_layout)

        self.diametral_pitch_result = QTextEdit()
        self.diametral_pitch_result.setReadOnly(True)
        diametral_pitch_layout.addWidget(self.diametral_pitch_result)

        diametral_pitch_button = QPushButton('Calcular')
        diametral_pitch_button.clicked.connect(self.calculate_diametral_pitch)
        diametral_pitch_layout.addWidget(diametral_pitch_button)

        layout.addLayout(diametral_pitch_layout)

        self.setLayout(layout)

    def calculate_module(self):
        try:
            module = float(self.module_entry.text())
            num_teeth = int(self.teeth_module_entry.text())
            results = calculate_module(module, num_teeth)
            result_text = "\n".join(
                [f"{k}: {v:.2f}" for k, v in results.items()])
            self.module_result.setText(result_text)
        except ValueError:
            self.module_result.setText("Por favor, ingrese valores válidos.")

    def calculate_diametral_pitch(self):
        try:
            diametral_pitch = float(self.diametral_pitch_entry.text())
            num_teeth = int(self.teeth_diametral_pitch_entry.text())
            results = calculate_diametral_pitch(diametral_pitch, num_teeth)
            result_text = "\n".join(
                [f"{k}: {v:.2f}" for k, v in results.items()])
            self.diametral_pitch_result.setText(result_text)
        except ValueError:
            self.diametral_pitch_result.setText(
                "Por favor, ingrese valores válidos.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GearCalculator()
    ex.show()
    sys.exit(app.exec_())
