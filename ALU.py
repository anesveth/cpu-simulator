from IC import IC

'''Class ALU'''
class ALU(IC): #Al ALU no le importa si es signed math o no, sin importar el signo es la misma mate pero los flags van a etsar raros.
#-------------------------------------------------------------------------------Arithmetic-------------------------------------------------------------------------
    def sum1(self, data1, data2, signed):
        signed
        #sumamos
        result = int(data1, 2) + int(data2, 2)
        #comprobamos overflow, carry y zero
        overfl_flag = self.overfl(result, signed, data1, data2)
        carry_flag = self.carry(result)
        error_flag = self.error(result, signed, data1, data2)
        zero_flag = self.zero(result)
        neg_flag = self.negative(result)
        #convertimos el resultado en binario
        if result >= 0:
            result = '{0:b}'.format(result)
        else:
            result = '{0:b}'.format(8 - result)
            result = ''.join('1' if x == '0' else '0' for x in result) #Si es negativo cambia 1 por 0 y 0 por 1
            result_list = list(result)
            if result_list[0] == "0":
                result_list[0] = "1"
            else:
                result_list[0] = "0"
            result = ''.join(result_list) #Regresa el sign bit a 1 si es negativo
        #llamamos la funcion output como resultado
        return result, overfl_flag, carry_flag, error_flag, zero_flag, neg_flag 
    def sub(self, data1, data2, signed):
        signed
        #restamos
        result = int(data1, 2) - int(data2, 2)
        #comprobamos overflow, carry y zero
        overfl_flag = self.overfl(result, signed, data1, data2)
        carry_flag = self.carry(result)
        error_flag = self.error(result, signed, data1, data2)
        zero_flag = self.zero(result)
        neg_flag = self.negative(result)
        #convertimos el resultado en binario
        if result >= 0:
            result = '{0:b}'.format(result)
        else:
            result = '{0:b}'.format(8 - result)
            result = ''.join('1' if x == '0' else '0' for x in result) #Si es negativo cambia 1 por 0 y 0 por 1
            result_list = list(result)
            if result_list[0] == "0":
                result_list[0] = "1"
            else:
                result_list[0] = "0"
            result = ''.join(result_list) #Regresa el sign bit a 1 si es negativo
        #llamamos la funcion output como resultado
        return result, overfl_flag, carry_flag, error_flag, zero_flag, neg_flag

#----------------------------------------------------------------------Flags---------------------------------------------------------------------------------------
    def overfl(self, resultado, signed, data1, data2):
        #revisa si es signed math
        if signed == 1: #En signed math, el valor mas grande es 7 y el menor es -7, si es mayor a 15 regresa a 0, igual con -15.
            if int(data1, 2) > 7 and int(data2, 2) > 7 and (resultado < 7 or resultado > 15) or int(data1, 2) < 7 and int(data1, 2) < 7 and (resultado > 7 or resultado < 15):
                return True
            elif int(data1, 2) > 0 and int(data2, 2) > 0 and (resultado < 0 or resultado > 7) or int(data1, 2) < 0 and int(data1, 2) < 0 and (resultado > 0 or resultado < -7):
                return True
            else: 
                return False
        #Cuando no es signed math
        else:
            if resultado > 15 or resultado < 0:
                return True
            else:
                return False
    def carry(self, resultado): #carry flag
        #el carry flag solo se prende si el primer bit cambia de valor, no le importa si es signed o no.
        if resultado > 15 or resultado <= 0:
            return True
        else:
            return False
    def error(self, result, signed, data1, data2): #error flag (If signed math, error only when carry flag. If not sm, error only when overflow flag)
        #Si es signed math, hay error si se prende el carry flag.
        overfl_flag = self.overfl(result, signed, data1, data2)
        carry_flag = self.carry(result)
        if signed == 1:
            if carry_flag == True:
                return True
            else:
                return False
        #Si no es signed math, hay error si se prende el overflow flag.
        else:
            if overfl_flag == True:
                return True
            else: 
                return False
    def zero(self, resultado): #Checks if the result is 0.
        if resultado == 0:
            return True
        else:
            return False
    def negative(self, result): #Checks if the result is negative. (Can only happen if it is signed math)
        if result < 0:
            return True
        else:
            return False

#------------------------------------------------------------------------Logical Gates----------------------------------------------------------------------------
    def and1(self, data3, data4): #Checks if both are True.
        andlist1 = list(data3)
        andlist2 = list(data4)
        if andlist1[0] == "1" and andlist2[0] == "1" and andlist1[1] == "1" and andlist2[1] == "1":
            return "1" #And is true when the values are both 1.
        else:
            return "0"
    def or1(self, data3, data4): #Checks if either one is True.
        andlist1 = list(data3) #Makes string into a list.
        andlist2 = list(data4)
        if (andlist1[0] == "0" and andlist2[0] == "0" and andlist1[1] == "0" and andlist2[1] == "0"):
            return "0" #Or is true when both values are not 0.
        else:
            return "1"
    def not1(self, data3): #Negates each bit.
        return ''.join('1' if x == '0' else '0' for x in data3)
            

'''Tests'''
mi_alu = ALU()
print("Sum test:", mi_alu.sum1("0011", "0110", 0))
print("Sum test 2:", mi_alu.sum1("1101", "1110", 1))

print("Sub test:", mi_alu.sub("0011", "1100", 0))

print(mi_alu.and1("11", "11"))

print(mi_alu.or1("01", "00"))

print(mi_alu.not1("1001")) #Lo hize con 4 bits.
