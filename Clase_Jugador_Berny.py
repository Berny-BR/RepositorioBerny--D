from colorama import Fore, Style


class Jugador:
    """Héroe (@) que explora la mazmorra."""

    def __init__(self, r, c):
        # r = fila inicial, c = columna inicial
        self.r = r
        self.c = c
        self.salud = 100          # inicia con 100 de salud
        self.puntos = 0           # inicia con 0 puntos
        self.simbolo = "@"        # simbolo que representa al jugador
        # diccionario de inventario de items recogidos
        self.inventario = {"tesoros": 0, "pociones": 0, "trampas": 0}

    # ---------- Movimiento ----------
    def mover(self, r, c):
        # actualiza la posicion del jugador
        self.r = r
        self.c = c

    def calcular_destino(self, tecla):
        # devuelve (fila, columna) a la que quiere ir segun la tecla.
        # No mueve al jugador: el Mapa debe validar primero la pared.
        tecla = tecla.strip().upper()
        if tecla == "W":
            return self.r - 1, self.c
        elif tecla == "S":
            return self.r + 1, self.c
        elif tecla == "A":
            return self.r, self.c - 1
        elif tecla == "D":
            return self.r, self.c + 1
        else:
            return self.r, self.c

    # ---------- Salud ----------
    def recibir_dano(self, cantidad):
        # resta salud (trampas), sin bajar de 0
        self.salud -= cantidad
        if self.salud < 0:
            self.salud = 0
        self.inventario["trampas"] += 1

    def curar(self, cantidad):
        # suma salud (pociones), sin pasar de 100
        self.salud += cantidad
        if self.salud > 100:
            self.salud = 100
        self.inventario["pociones"] += 1

    def morir(self):
        # muerte instantanea (monstruos)
        self.salud = 0

    def esta_vivo(self):
        # True si el jugador todavia tiene vida
        return self.salud > 0

    # ---------- Puntos ----------
    def sumar_puntos(self, cantidad):
        # suma puntos (tesoros)
        self.puntos += cantidad
        self.inventario["tesoros"] += 1

    # ---------- Dibujo ----------
    def dibujar(self, print_at):
        # dibuja el @ en su posicion actual
        print_at(self.r, self.c,
                 Fore.CYAN + Style.BRIGHT + self.simbolo + Style.RESET_ALL)

    def borrar(self, print_at):
        # borra el @ de su posicion actual
        print_at(self.r, self.c, " ")

    def texto_estado(self):
        # texto para el panel informativo inferior
        return (f"Vida: {self.salud}  Puntos: {self.puntos}  "
                f"Tesoros: {self.inventario['tesoros']}  "
                f"Pociones: {self.inventario['pociones']}")


# Prueba rápida (solo corre si ejecutas este archivo directamente)
if __name__ == "__main__":
    j = Jugador(5, 10)
    print(j.calcular_destino("w"))   # (4, 10)
    j.mover(4, 10)
    j.recibir_dano(30)
    j.curar(50)
    j.sumar_puntos(10)
    print(j.texto_estado())          # Vida: 100  Puntos: 10 ...
    j.morir()
    print(j.esta_vivo())             # False