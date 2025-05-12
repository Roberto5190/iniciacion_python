from datetime import datetime

class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def presentarse(self):
        return f"Hola, soy {self.nombre} y mi correo es {self.email}"


class Mascota:
    def __init__(self, nombre, especie, edad, duenio: Persona):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.duenio = duenio

    def presentar(self):
        return f"Soy {self.nombre}, un(a) {self.especie} de {self.edad} años. Mi dueño es {self.duenio.nombre}"


class CitaVeterinaria:
    def __init__(self, mascota: Mascota, fecha: datetime, motivo):
        self.mascota = mascota
        self.fecha = fecha
        self.motivo = motivo

    def mostrar_cita(self):
        return f"Cita para {self.mascota.nombre} el {self.fecha.strftime('%d/%m/%Y %H:%M')} por {self.motivo}"


# --- Prueba del sistema ---

if __name__ == "__main__":
    duenio1 = Persona("Ana Pérez", "ana@example.com")
    mascota1 = Mascota("Luna", "perra", 3, duenio1)
    cita1 = CitaVeterinaria(mascota1, datetime(2025, 5, 15, 10, 30), "vacunación anual")

    print(duenio1.presentarse())
    print(mascota1.presentar())
    print(cita1.mostrar_cita())
