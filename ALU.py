from IC import IC

'''Class ALU'''
class ALU(IC): #Al ALU no le importa si es signed math o no, maximo es 7.
#-------------------------------------------------------------------------------Arithmetic-------------------------------------------------------------------------
    def sum1(self, data1, data2, signed):
        data1_int = int(data1, 2)
        data2_int = int(data2, 2)
        if signed == 1:
            data1_list = list(data1)
            data1 = ''.join('1' if x == '0' else '0' for x in data1)
            data1_list = list(data1)
            if data1_list[0] == "0":
                data1_list[0] = "1"
            else:
                data1_list[0] = "0"
            data1 = ''.join(data1_list)
            data1_int = -int(data1, 2)
        if signed == 1:
            data2_list = list(data2)
            data2 = ''.join('1' if x == '0' else '0' for x in data2)
            data2_list = list(data2)
            if data2_list[0] == "0":
                data2_list[0] = "1"
            else:
                data2_list[0] = "0"
            data2 = ''.join(data2_list)
            data2_int = -int(data2, 2)
        #sumamos
        result = data1_int + data2_int
        #comprobamos overflow, carry y zero
        overfl_flag = self.overfl(result, data1, data2, data1_int, data2_int)
        carry_flag = self.carry(result)
        error_flag = self.error(result)
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
        data1_int = int(data1, 2)
        data2_int = int(data2, 2)
        if signed == 1:
            data1_list = list(data1)
            data1 = ''.join('1' if x == '0' else '0' for x in data1)
            data1_list = list(data1)
            if data1_list[0] == "0":
                data1_list[0] = "1"
            else:
                data1_list[0] = "0"
            data1 = ''.join(data1_list)
            data1_int = -int(data1, 2)
        if signed == 1:
            data2_list = list(data2)
            data2 = ''.join('1' if x == '0' else '0' for x in data2)
            data2_list = list(data2)
            if data2_list[0] == "0":
                data2_list[0] = "1"
            else:
                data2_list[0] = "0"
            data2 = ''.join(data2_list)
            data2_int = -int(data2, 2)
        #restamos
        result = data1_int - data2_int
        #comprobamos overflow, carry y zero
        overfl_flag = self.overfl(result, data1, data2, data1_int, data2_int)
        carry_flag = self.carry(result)
        error_flag = self.error(result)
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
    def overfl(self, resultado, data1, data2, data1_int, data2_int): #En signed math, el valor mas grande es 7 y el menor es -7.
        if data1_int > 7 and data2_int > 7 and (resultado < 7 or resultado > 15) or data1_int < 7 and data2_int < 7 and (resultado > 7 or resultado < 15):
            return True
        elif data1_int > 0 and data2_int > 0 and (resultado < 0 or resultado > 7) or data1_int < 0 and data2_int < 0 and (resultado > 0 or resultado < -7):
            return True
        else: 
            return False
    def carry(self, resultado): #carry flag
        #el carry flag solo se prende si el primer bit cambia de valor, no le importa si es signed o no.
        if resultado > 7 or resultado <= 0:
            return True
        else:
            return False
    def error(self, result): #error flag, si es signed math, hay error si se prende el carry flag.
        carry_flag = self.carry(result)
        if carry_flag == True:
            return True
        else:
            return False
    def zero(self, resultado): #Checks if the result is 0.
        if resultado == 0:
            return True
        else:
            return False
    def negative(self, result): #Checks if the result is negative.
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

print("Sub test:", mi_alu.sub("0011", "1100", 1))

print(mi_alu.and1("11", "11"))

print(mi_alu.or1("01", "00"))

print(mi_alu.not1("1001")) #Lo hize con 4 bits.
