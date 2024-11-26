# neurocirugia.py
from neurologia import Neurologia

class Neurocirugia(Neurologia):
    def __init__(self, descripcion, especialidad_general, campo_estudio, enfermedades_comunes, procedimientos_quirurgicos):
        super().__init__(descripcion, especialidad_general, campo_estudio, enfermedades_comunes)
        self.procedimientos_quirurgicos = procedimientos_quirurgicos

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Neurocirugía - Procedimientos quirúrgicos: {', '.join(self.procedimientos_quirurgicos)}")
