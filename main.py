
from Videojuego import Mision
from Videojuego import ColaMisiones

# Ejemplo de uso
if __name__ == "__main__":
    cola = ColaMisiones()

    cola.agregar_mision(Mision("Rescatar al aldeano", 3))
    cola.agregar_mision(Mision("Recolectar hierbas", 1))
    cola.agregar_mision(Mision("Derrotar al dragón", 5))

    print("Misiones en cola:")
    cola.mostrar_misiones()

    print("\nSiguiente misión:")
    print(cola.obtener_siguiente_mision())

    print("\nMisiones restantes:")
    cola.mostrar_misiones()