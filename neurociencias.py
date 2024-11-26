# neurociencias.py
from medicina import Medicina

class Neurociencias(Medicina):
    def __init__(self, descripcion, especialidad_general, campo_estudio):
        super().__init__(descripcion, especialidad_general)
        self.campo_estudio = campo_estudio

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Neurociencias - Campo de estudio: {self.campo_estudio}")
