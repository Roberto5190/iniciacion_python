class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Sonido genérico"


class Perro(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Guau!"


class Gato(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Miau!"


class Vaca(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Muu!"


# --- Demostración de polimorfismo ---
def hacer_cantar_animales(animales):
    for animal in animales:
        print(animal.hacer_sonido())


if __name__ == "__main__":
    perro = Perro("Toby")
    gato = Gato("Michi")
    vaca = Vaca("Lola")

    lista_animales = [perro, gato, vaca]
    hacer_cantar_animales(lista_animales)
