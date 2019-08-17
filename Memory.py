from IC import IC

class Memory(IC):
    '''Father class to Registers and RAM'''

class RAM(Memory):
    '''Random Access Memory'''
    size="4 bits"
    data_memory=[] * 15
    def read_enable(self,adress):
        if adress<16 and adress>=0:
            return self.data_memory[adress] 
        else:
            return "Adress out of bounds"
    def write_enable(self,adress,data):
        if adress<16 and adress>=0:
            self.data_memory[adress]=data 
        else:
            return "Adress out of bounds"

ram_memory=RAM()

class Registers(Memory):
    '''Temporary memory handlers
    '''
    list_of_registers=[]
    def read_register(self,registername,selection):
        if selection=="op":#you can ask for the opcode specifically
            return (registername[0:4])
        if selection=="number":#you can ask for the number specifically
            return (registername[4:8])
        if selection=="all":#get everything
            return (registername)
    def write_register(self,new_data,registername,selection):
        temporary_list=[]
        for i in new_data:#turns data into a list so we can overwrite what we want
            temporary_list.append(i)

        if selection=="1":
            if len(new_data)==4:  #checks that the opcode length is correct
                for i in range(4):
                    temporary_list[i]=new_data[i] 
                registername="".join(temporary_list)#inserts it as string
            else:
                return("OPCODE length not acceptable")

        if selection=="2":#you can write the number specifically
            if len(new_data)==4:  #checks that the number size is correct
                for i in range(4):
                    temporary_list[4+i]=new_data[i]
                registername="".join(temporary_list)
            else:
                return ("Number size not acceptable")

        if selection=="3":#input everything
            if len(new_data)==8:
                for i in range(len(new_data)):
                    temporary_list[i]=(new_data[i])
                registername="".join(temporary_list)
            else:
                return("overflow")
        
data=[""]*8



registerA=Registers(data)
registerB=Registers(data)
registerC=Registers(data)
registerD=Registers(data)

instruction_register=Registers(data) #shows the selected data that was located in RAM
instruction_adress_register=Registers(data) #keeps a tab on the number of instructions successfully executed

output_register=Registers(data)

