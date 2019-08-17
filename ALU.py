from IC import IC

command = 0
sum1 = 0
carry = 0
class ALU(IC):
    def __init__(self):
#---------------------------------flags-------------------------
        def zero(a, b):
            if a == 0 and b == 0:
                self.zero = TRUE
        def ovfl(a, b):
            if a + b > 15:
                self.ovfl = TRUE
        def neg(a, b):
            if a - b < 0:
                self.neg = TRUE
#---------------------------------arithmetic--------------------
    if command == 1:
        def add(a, b):
            sum1 = a + b
            if sum1 >= 2:
                carry = 1
    elif command == 2:
        def addC(a, b, carry):
            sum1 = a + b + carry
            if sum1 >= 2:
                carry = 1
    elif command == 3:
        def sub(a, b):
            sub1 = a - b
            if sub1 >= 2:
                carry = 1
    elif command == 4:
        def subC(a, b, carry):
            sub1 = a - b - carry
            if sub1 >= 2:
                carry = 1
    elif command == 5:
        def onecomp(): #No entendi q significa esto o para q se usa / es algo asi pero saber
            0 == "1111"
            1 == "1110"
            2 == "1101"
            3 == "1100"
            4 == "1011"
            5 == "1010"
            6 == "1001"
            7 == "1000"
            8 == "0111"
            9 == "0110"
            10 == "0101"
            11 == "0100"
            12 == "0011"
            13 == "0010"
            14 == "0001"
            15 == "0000"
    elif command == 6:
        def twocomp(): #No entendi q significa esto o para q se usa / es algo asi pero saber
            0 == "0000"
            1 == "0001"
            2 == "0010"
            3 == "0011"
            4 == "0100"
            5 == "0101"
            6 == "0110"
            7 == "0111"
            8 == "1000"
            9 == "1001"
            10 == "1010"
            11 == "1011"
            12 == "1100"
            13 == "1101"
            14 == "1110"
            15 == "1111"
#faltan los twocomp negativos

    elif command == 7:
        if a == 1 and b == 1:
            and1 = TRUE
    elif command == 8:
        if a == 1 and b == 1 or a == 1 or b == 1:
            or1 = TRUE
    elif command == 9: #Todavia tengo que investigar esto pero es algo asi
        a << b
        a >> b
        a & b
        a | b
        ~ a
        a ^ b
