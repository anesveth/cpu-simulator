from IC import IC

class Memory(IC):
    '''Father class to Registers and RAM'''
    def __init__(self,data):
        self.data=data

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
        
ram_memory=RAM(data)

class Registers(Memory):
    '''Temporary memory handlers
    '''
    list_of_registers=[]
    def read_enable(self,adress):
        #gets ram space adress
        return self.list_of_registers[adress]
    def write_enable(self,adress,data):
        self.list_of_registers[adress]=[data]   


registerA=Registers(data)
registerB=Registers(data)
registerC=Registers(data)
registerD=Registers(data)

instruction_register=Registers(data) #shows the selected data that was located in RAM
instruction_adress_register=Registers(data) #keeps a tab on the number of instructions successfully executed

output_register=Registers(data)

