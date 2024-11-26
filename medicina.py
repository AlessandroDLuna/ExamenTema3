# medicina.py
from biologia import Biologia

class Medicina(Biologia):
    def __init__(self, descripcion, especialidad_general):
        super().__init__(descripcion)
        self.especialidad_general = especialidad_general

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Medicina: {self.especialidad_general}")
