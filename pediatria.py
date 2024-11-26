# pediatria.py
from medicina import Medicina

class Pediatria(Medicina):
    def __init__(self, descripcion, especialidad_general, edades_atendidas):
        super().__init__(descripcion, especialidad_general)
        self.edades_atendidas = edades_atendidas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Pediatría - Edades atendidas: {self.edades_atendidas}")
