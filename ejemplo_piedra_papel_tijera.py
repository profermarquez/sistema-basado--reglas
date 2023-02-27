# fuente: https://www.youtube.com/watch?v=dzQTxnfyC6E

from experta import *

class Jugador(Fact):pass

class Computadora(Fact):pass

class Juego(KnowledgeEngine): 
    @Rule(OR(
    AND(Jugador(tirada='piedra'),Computadora(tirada='piedra')),
    AND(Jugador(tirada='papel'),Computadora(tirada='papel')),
    AND(Jugador(tirada='tijera'),Computadora(tirada='tijera'))
    ))
    def empate(self):
        print("empate")
    
    @Rule(OR(
        AND(Jugador(tirada='piedra'),Computadora(tirada='tijera')),
        AND(Jugador(tirada='papel'),Computadora(tirada='piedra')),
        AND(Jugador(tirada='tijera'),Computadora(tirada='papel'))
        ))
    def ganaJugador(self):
        print("Gano el jugador")
    
    @Rule(OR(
        AND(Jugador(tirada='papel'),Computadora(tirada='tijera')),
        AND(Jugador(tirada='tijera'),Computadora(tirada='piedra')),
        AND(Jugador(tirada='piedra'),Computadora(tirada='papel'))
        ))
    def ganaComputador(self):
        print("Gano la computadora")

motor=Juego()
motor.reset()
motor.declare(Jugador(tirada='tijera'))
motor.declare(Computadora(tirada='piedra'))
motor.run()