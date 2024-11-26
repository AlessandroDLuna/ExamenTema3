# neurologia.py
from neurociencias import Neurociencias

class Neurologia(Neurociencias):
    def __init__(self, descripcion, especialidad_general, campo_estudio, enfermedades_comunes):
        super().__init__(descripcion, especialidad_general, campo_estudio)
        self.enfermedades_comunes = enfermedades_comunes

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Neurología - Enfermedades comunes: {', '.join(self.enfermedades_comunes)}")
