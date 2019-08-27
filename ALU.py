from IC import IC

'''Class ALU'''
class ALU(IC): #Maximo de datos es 15, minimo es 0. Maximo de output es 15, minimo -7
    o = 0
#-------------------------------------------------------------------------------Arithmetic-------------------------------------------------------------------------
    def sum1(self, data1, data2):
        '''Adds the two values'''
        data1_int = int(data1, 2)
        data2_int = int(data2, 2)
        #sumamos
        result = data1_int + data2_int
        #comprobamos overflow, carry, error, zero y negative
        overfl_flag = self.overfl(result, data1_int, data2_int)
        carry_flag = self.carry(result)
        error_flag = self.error(result, data1_int, data2_int)
        zero_flag = self.zero(result)
        neg_flag = self.negative(result)
        #convertimos el resultado en binario
        if 15 >= result >= 0: #Cuando es positivo y no tiene overflow
            result = '{0:04b}'.format(result)
        elif -7 <= result < 0: #Cuando es negativo y no tiene overflow
            result = '{0:04b}'.format(result * -1)
            result = ''.join('1' if x == '0' else '0' for x in result) #Si es negativo cambia 1 por 0 y 0 por 1
            result_list = list(result)
            result = ''.join(result_list) #Regresa el sign bit a 1 si es negativo
        else: #Cuando hay overflow (Mayor a 4 bits)
            result = "----"
        #llamamos la funcion output como resultado
        return result, overfl_flag, carry_flag, error_flag, zero_flag, neg_flag 
    def sub(self, data1, data2):
        '''Subtracts the two values'''
        data1_int = int(data1, 2)
        data2_int = int(data2, 2)
        #restamos
        result = data1_int - data2_int
        #comprobamos overflow, carry, error, zero y negative
        overfl_flag = self.overfl(result, data1_int, data2_int)
        carry_flag = self.carry(result)
        error_flag = self.error(result, data1_int, data2_int)
        zero_flag = self.zero(result)
        neg_flag = self.negative(result)
        #convertimos el resultado en binario
        if 15 >= result >= 0: #Cuando es positivo y no tiene overflow
            result = '{0:04b}'.format(result)
        elif -7 <= result < 0: #Cuando es negativo y no tiene overflow
            result = '{0:04b}'.format(result * -1)
            result = ''.join('1' if x == '0' else '0' for x in result) #Si es negativo cambia 1 por 0 y 0 por 1
            result_list = list(result)
            result = ''.join(result_list) #Regresa el sign bit a 1 si es negativo
        else: #Cuando hay overflow (Mayor a 4 bits)
            result = '----'
        #llamamos la funcion output como resultado
        return result, overfl_flag, carry_flag, error_flag, zero_flag, neg_flag

#----------------------------------------------------------------------Flags---------------------------------------------------------------------------------------
    def overfl(self, resultado, data1_int, data2_int): 
        '''Checks for overflow, overflow only happens when two positive values become negative or greater than 15 or if they are negative and become positive or less than -7.'''
        if data1_int > 0 and data2_int > 0 and (resultado < 0 or resultado > 15): #En unsigned math, el valor mas grande es 15 y el menor es 0.
            return True
        elif data1_int < 0 and data2_int < 0 and (resultado > 0 or resultado < -7): #Si el resultado es negativo, el valor mas pequeno es -7 y el mas grande es 0.
            return True
        else:
            return False
    def carry(self, resultado): 
        '''Checks for carry, carry happens when the result is greater than 15 or if the result is negative.'''
        if resultado > 15 or resultado <= 0:
            return True
        else:
            return False
    def error(self, result, data1_int, data2_int):
        '''Checks for error, error occurs when an overflow occurs.'''
        overfl_flag = self.overfl(result, data1_int, data2_int)
        if overfl_flag == True:
            return True
        else:
            return False
    def zero(self, resultado): 
        '''Checks if the result is 0.'''
        if resultado == 0:
            return True
        else:
            return False
    def negative(self, resultado): 
        '''Checks if the result is negative.'''
        if resultado < 0:
            return True
        else:
            return False

#------------------------------------------------------------------------Logical Gates----------------------------------------------------------------------------
    def and1(self, data3, data4): 
        '''Checks if both are True.'''
        andlist1 = list(data3)
        andlist2 = list(data4)
        if andlist1[0] == "1" and andlist2[0] == "1" and andlist1[1] == "1" and andlist2[1] == "1":
            self.o=1
            return "1" #And is true when the values are both 1.
        else:
            self.o=0
            return "0"
    def or1(self, data3, data4): 
        '''Checks if either one is True.'''
        andlist1 = list(data3)
        andlist2 = list(data4)
        if (andlist1[0] == "0" and andlist2[0] == "0" and andlist1[1] == "0" and andlist2[1] == "0"):
            self.o=0
            return "0" #Or is true when both values are not 0.
        else:
            self.o=1
            return "1"
    def not1(self, data3): 
        '''Negates each bit.'''
        return ''.join('1' if x == '0' else '0' for x in data3)
            

'''Tests'''
# mi_alu = ALU()
# print("Sum test:", mi_alu.sum1("0011", "0110"))
# print("Sum test 2:", mi_alu.sum1("0101", "1110"))

# print("Sub test:", mi_alu.sub("0110", "0111"))

# print(mi_alu.and1("11", "11"))

# print(mi_alu.or1("01", "00"))

# print(mi_alu.not1("1001")) #Lo hize con 4 bits.
