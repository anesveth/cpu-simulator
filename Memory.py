from IC import IC

class Memory(IC):
    '''Father class to Registers and RAM'''

class RAM(Memory):
    '''Random Access Memory'''
    def __init__(self, size = 16):
        self.data_memory=[] * size
        self.size = size
    def read_enable(self,adress):
        #translates bit to int
        adress = int(adress, 2)
        if adress<self.size and adress>=0:
            return self.data_memory[adress] 
        else:
            return "overflow"
    def write_enable(self,adress,data):
        #translates bit to int
        adress = int(adress, 2)
        if adress<self.size and adress>=0:
            self.data_memory[adress]=data 
        else:
            return "overflow"


class Registers(Memory):
    '''Temporary memory handlers'''
    def __init__(self, data, size = 4):
        '''reserves space'''
        self.size = size
        self.data=""
    def read_register(self):
        return (self.data)
    def write_register(self,new_data):
        if len(new_data)==self.size:  #checks that the opcode length is correct
            self.data=new_data
        else:
            return("overflow")


