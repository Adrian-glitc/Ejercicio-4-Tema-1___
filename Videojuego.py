class Mision:
    def __init__(self, nombre, dificultad):
        self.nombre = nombre
        self.dificultad = dificultad

    def __str__(self):
        return f"Misión: {self.nombre}"


class ColaMisiones:
    def __init__(self):
        self.misiones = []

    def agregar_mision(self, mision):
        self.misiones.append(mision)
        self.misiones.sort(key=lambda x: x.dificultad)

    def obtener_siguiente_mision(self):
        if self.misiones:
            return self.misiones.pop(0)
        else:
            return None

    def mostrar_misiones(self):
        for mision in self.misiones:
            print(mision)