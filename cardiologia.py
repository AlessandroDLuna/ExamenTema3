# cardiologia.py
from medicina import Medicina

class Cardiologia(Medicina):
    def __init__(self, descripcion, especialidad_general, procedimientos_comunes):
        super().__init__(descripcion, especialidad_general)
        self.procedimientos_comunes = procedimientos_comunes

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cardiología - Procedimientos comunes: {', '.join(self.procedimientos_comunes)}")
