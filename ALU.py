from IC import IC

'''Test variables'''
def test():
    val1 = int(in1, 2) #imported de CU
    return val1

def test2():
    val2 = int(in2, 2) #imported de CU
    return val2

def test3():
    com = int(in3, 2) #imported de CU
    return com

def test4():
    signed #imported de CU, tiene que ser True or False
    return signed

'''Calling Tests''' #no necesario pero me ayuda a entender la logica mejor.
y = test()
print("First value:", y)
z = test2()
print("Second value:", z)
command = test3()
sm = test4()

'''Class ALU'''
class ALU(IC):
    def sum1(self):
        result = y + z
        return result
    def sub(self):
        result = y - z
        return result
    def overf(self):
        of = False
        if y > 0 and z > 0 and (x.sum1() < 0 or x.sum1() > 7) or y < 0 and z < 0 and (x.sum1() > 0 or x.sum1() < -7):
            of = True
        elif y > 0 and z > 0 and (x.sub() < 0 or x.sub() > 7) or y < 0 and z < 0 and (x.sub() > 0 or x.sub() < -7):
            of = True
        return of
    def carryf(self):
        cf = False
        if x.sum1() > 15 or x.sum1() <= 0:
            cf = True
        elif x.sub() > 15 or x.sub() <= 0:
            cf = True
        return cf
    def errorf(self):
        ef = False
        if sm == False:
            if x.carryf() == True:
                ef = False
        else:
            if x.overf() == True:
                ef = True
        return ef
    def and1(self):
        if in4 == True and in5 == True: #imported de CU
            return True
        else:
            return False
    def or1(self):
        if in4 == True: #imported de CU
            return True
        elif in5 == True: #imported de CU
            return True
        else:
            return False
    def not1(self):
        if in4 == True: #imported de CU
            return False
        else:
            return True
    def int2bin(self):
        if sm == False:
            if x.sum1() <= 15 and x.sum1() >= -15 and command == 0:
                r = ('{0:b}'.format(x.sum1()))
            if x.sub() <= 15 and x.sub() >= -15 and command == 1:
                r = ('{0:b}'.format(x.sub()))
        else:
            if x.sum1() <= 7 and x.sum1() >= -7 and command == 0:
                r = ('{0:b}'.format(x.sum1()))
            if x.sub() <= 7 and x.sub() >= -7 and command == 1:
                r = ('{0:b}'.format(x.sub()))
        return r

x = ALU()