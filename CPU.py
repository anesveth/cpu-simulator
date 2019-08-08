#Grupo 7

#Cosas Importantes en texto --------------------------------------------
# Recuerdense de poner todas las funciones que puedan en FCO. 
# Este solo es un medio layout, no quiere decir que esos sean los attributos que vamos a 
# usar, tampoco son los correctos (solo lo hize rapido sin leer exactamente lo que queria el prof en las instrucciones)
# Tambien recuerdense de usar CI asi sacamos puntos extras. Todos los demas puntos extras deberiamos integrar
# mas tarde ya que son mas dificiles.



class IC:
    def __init__(self, manufacterer, build_date, purpose):
        self.manufacterer  = manufacterer
        self.build_date = build_date
        self.purpose = purpose

class Memory:
    def __init__(self, algo, algo2):
        self.algo = algo
        self.algo2 = algo2

class ALU(IC):
    def __init__(self, zero, overflow, negative, input2, output): #Hay que cambiarlos a flags. Ejemplo de if commands para los flags abajo.
        self.zero = zero
        self.overflow = overflow
        self.negative = negative
        self.input = input2
        self.output = output

class CU(IC):
    def __init__(self, saber):
        self.saber = saber
    
class Registers:
    def __init__(self, a, b, c, d, pc, ir, or2):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.pc = pc
        self.ir = ir
        self.or2 = or2

class RAM:
    def __init__(self, x):
        self.x = x

class Clock:
    frequency = 1.2 #Hay que poner el range de 0 a 2

# when ENTER: #Ni idea como escribir esto en code. Talvez algo como input("Press Enter to skip to next step: ") y aparte el metodo.
#    step == TRUE

# if step == TRUE:
#    frequency = 0
    
# if op == -x:
#    negmethod()

# if op > 15:
#    ovmethod()

# if op == 0:
#     0method()



