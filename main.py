# main.py
from biologia import Biologia
from medicina import Medicina
from cardiologia import Cardiologia
from neurociencias import Neurociencias
from neurologia import Neurologia
from neurocirugia import Neurocirugia
from pediatria import Pediatria


def imprimir_separador():
    print("\n" + "-" * 40 + "\n")


if __name__ == "__main__":
    # Instancias de cada clase
    bio = Biologia("Ciencia que estudia los seres vivos.")
    med = Medicina("Ciencia aplicada al cuidado de la salud.", "General")
    cardio = Cardiologia(
        "Ciencia que estudia los seres vivos.",
        "Tratamiento del corazón",
        ["ECG", "Cateterismo", "Eco Doppler"]
    )
    neurociencia = Neurociencias(
        "Ciencia que estudia el sistema nervioso",
        "Sistema nervioso",
        "Estudio del cerebro y sus funciones"
    )
    neuro = Neurologia(
        "Ciencia que estudia los seres vivos.",
        "Tratamiento del sistema nervioso",
        "Sistema nervioso central y periférico",
        ["Epilepsia", "Migraña", "Parkinson"]
    )
    neurocirugia = Neurocirugia(
        "Ciencia que estudia los seres vivos.",
        "Tratamiento quirúrgico del sistema nervioso",
        "Sistema nervioso central",
        ["Tumores cerebrales", "Herniación de disco", "Aneurismas"],
        ["Craneotomía", "Microcirugía", "Endoscopia cerebral"]
    )
    ped = Pediatria(
        "Ciencia que estudia los seres vivos.",
        "Cuidado infantil",
        "0-18 años"
    )

    # Impresión organizada
    print("Características de las diferentes ciencias:")
    imprimir_separador()

    print("Biología:")
    print(f"Descripción: {bio.descripcion}")
    imprimir_separador()

    print("Medicina:")
    print(f"Descripción: {med.descripcion}")
    print(f"Especialidad General: {med.especialidad_general}")
    imprimir_separador()

    print("Cardiología:")
    print(f"Descripción: {cardio.descripcion}")
    print(f"Especialidad General: {cardio.especialidad_general}")
    print(f"Procedimientos Comunes: {', '.join(cardio.procedimientos_comunes)}")
    imprimir_separador()

    print("Neurociencias:")
    print(f"Descripción: {neurociencia.descripcion}")
    print(f"Especialidad General: {neurociencia.especialidad_general}")
    print(f"Campo de Estudio: {neurociencia.campo_estudio}")
    imprimir_separador()

    print("Neurología:")
    print(f"Descripción: {neuro.descripcion}")
    print(f"Especialidad General: {neuro.especialidad_general}")
    print(f"Campo de Estudio: {neuro.campo_estudio}")
    print(f"Enfermedades Comunes: {', '.join(neuro.enfermedades_comunes)}")
    imprimir_separador()

    print("Neurocirugía:")
    print(f"Descripción: {neurocirugia.descripcion}")
    print(f"Especialidad General: {neurocirugia.especialidad_general}")
    print(f"Campo de Estudio: {neurocirugia.campo_estudio}")
    print(f"Enfermedades Comunes: {', '.join(neurocirugia.enfermedades_comunes)}")
    print(f"Procedimientos Quirúrgicos: {', '.join(neurocirugia.procedimientos_quirurgicos)}")
    imprimir_separador()

    print("Pediatría:")
    print(f"Descripción: {ped.descripcion}")
    print(f"Especialidad General: {ped.especialidad_general}")
    print(f"Edades Atendidas: {ped.edades_atendidas}")
    imprimir_separador()
