from experta import *

class MyFact(Fact):
    pass

class EsGatoONo(KnowledgeEngine):

    @Rule( NOT(MyFact(animal='Gato')))  
    def match_with_every_myfact(self):
        print("NoEsGato")

    @Rule(MyFact(animal='Gato'))
    def match_with_cats(self):
        print("Meow!")


print("Primer caso errado")
motor=EsGatoONo()
motor.reset()
motor.declare(MyFact(animal='Perro'))
motor.run()

print("Segundo caso como vacio")
motor=EsGatoONo()
motor.reset()
motor.declare(MyFact())
motor.run()

print("Tercer caso como gato")
motor=EsGatoONo()
motor.reset()
motor.declare(MyFact(animal='Gato'))
motor.run()