from IC import IC

'''Test variables'''
def test(in1):
    val1 = int(in1, 2) #First data variable (translates form binary to integer)
    return val1
def test2(in2):
    val2 = int(in2, 2) #Second data variable (translates form binary to integer)
    return val2
def test3(in3):
    com = in3 #Command variable (Puse Sum como 0, Sub como 1, And como 2, Or como 3 y Not como 4) 
    return com
def test4(signed):
    signed #imported de CU, tiene que ser True or False (almenos que quieran usar 0 y 1, lo puedo cambiar)
    return signed
def test5(in4):
    in4
    return in4
def test6(in5):
    in5
    return in5

'''Objects''' #no necesario pero me ayuda a entender la logica mejor.
y = test() #First data object
z = test2() #Second data object
command = test3() #Command object
sm = test4() #Signed Math data object (tells the ALU if the most significant bit is a value or a sign +/-)
h = test5()
i = test6()

'''Class ALU'''
class ALU(IC):
    def sum1(self):
        result = y + z
        return result, x.overf(), x.carryf(), x.errorf(), x.zerof(), x.negf(), x.and1(), x.or1(), x.not1(), x.int2bin()
    def sub(self):
        result = y - z
        return result, x.overf(), x.carryf(), x.errorf(), x.zerof(), x.negf(), x.and1(), x.or1(), x.not1(), x.int2bin()
    def overf(self): #overflow flag (segun reglas de overflow)
        of = False
        if y > 0 and z > 0 and (x.sum1() < 0 or x.sum1() > 7) or y < 0 and z < 0 and (x.sum1() > 0 or x.sum1() < -7):
            of = True
        elif y > 0 and z > 0 and (x.sub() < 0 or x.sub() > 7) or y < 0 and z < 0 and (x.sub() > 0 or x.sub() < -7):
            of = True
        return of
    def carryf(self): #carry flag (segun reglas de carry)
        cf = False
        if x.sum1() > 15 or x.sum1() <= 0:
            cf = True
        elif x.sub() > 15 or x.sub() <= 0:
            cf = True
        return cf
    def errorf(self): #error flag (If signed math, error only when carry flag. If not sm, error only when overflow flag)
        ef = False
        if sm == False:
            if x.carryf() == True:
                ef = False
        else:
            if x.overf() == True:
                ef = True
        return ef
    def zerof(self): #Checks if the result is 0.
        zf = False
        if (x.sum1() == 0 or x.sub() == 0):
            zf = True
        return zf
    def negf(self): #Checks if the result is negative. (Can only happen if it is signed math)
        nf = False
        if sm == True and (x.sum1() < 0 or x.sub() < 0):
            nf = True
        return nf
    def and1(self): #Checks if both are True.
        and2 = False
        if command == 2:
            if h == True and i == True: #Receives two values (Has to be True or False)
                and2 == True
            else:
                and2 == False
        return and2
    def or1(self): #Checks if either one is True.
        or2 = False
        if command == 3:
            if h == True: #Receives a value (Has to be True or False)
                or2 == True
            elif i == True: #Receives another value (Has to be True or False)
                or2 == True
            else:
                or2 == False
        return or2
    def not1(self): #Negates the value (Has to be True or False)
        not2 = False
        if command == 4:
            if h == True: #Receives a value (Has to be True or False)
                not2 == False
            else:
                not2 == True
        return not2
    def int2bin(self): #changes the integer back into a binary code
        r = 0
        if sm == False:
            if x.sum1() <= 15 and x.sum1() >= -15 and command == 0:
                r = ('{0:b}'.format(x.sum1()))
            if x.sub() <= 15 and x.sub() >= -15 and command == 1:
                r = ('{0:b}'.format(x.sub()))
        else:
            if x.sum1() <= 7 and x.sum1() >= -7 and command == 0: #7 es el valor mas alto en signed math de 4 bits.
                r = ('{0:b}'.format(x.sum1()))
            if x.sub() <= 7 and x.sub() >= -7 and command == 1:
                r = ('{0:b}'.format(x.sub()))
        return r

x = ALU() #ALU object

#print(x.int2bin()) #Solo uso esto para revisar si funciona.