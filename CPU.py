from IC import IC
from Memory import RAM, Registers
import Reader
class cu(IC):
    def __init__(self):
        '''controls and connects everything'''
        self.Instructions_memory = Reader.CardReader()
        print("Ingresa nombre del codigo (sin el .code)")
        file_name = input()
        data=[""]*8 #creating data
        self.Instructions_memory.change_file(file_name)

        self.ram = RAM()
        self.registerA=Registers(data)
        self.registerB=Registers(data)
        self.registerC=Registers(data)
        self.registerD=Registers(data)

        self.instruction_register=Registers(data) #shows the selected data that was located in RAM
        self.instruction_adress_register=Registers("00000000",8) #keeps 

        self.output_register=Registers(data)
    def decode_execute(self):
        
        opcode, data = self.Instructions_memory.read_line()
        #decides what to do with instructions
        if(opcode == "0000"):
            #Wires OUTPUT register directly to RAM address location (writes to console)
            self.output_register.write_register(data)
            print(self.output_register.read_register())
        elif(opcode == "0001"):
            #Reads RAM location into register A
            self.registerA.write_register(self.ram.read_enable(data))
        elif(opcode == "0010"):
            #Reads RAM location into register B
            self.registerB.write_register(self.ram.read_enable(data))
        elif(opcode == "0011"):
            #Performs AND between 2-bit registers ID
            pass
        elif(opcode == "0100"):
            #Immediate Read constant into register A
            self.registerA.write_register(data)
        elif(opcode == "0101"):
            #Write from Register A into RAM location
            self.ram.write_enable(self.registerA.read_register(),data)
        elif(opcode == "0110"):
            #Write from Register B into RAM location
            self.ram.write_enable(self.registerB.read_register(),data)
        elif(opcode == "0111"):
            #Performs OR between 2-bit registers ID
            pass
        elif(opcode == "1000"):
            #Immediate Read constant into register B
            self.registerB.write_register(data)
        elif(opcode == "1001"):
            #Add two registers, store result into second register
            pass
        elif(opcode == "1010"):
            #Subtract two registers, store result into second register
            pass
        elif(opcode == "1011"):
            #update Inst. Addr. Reg to new address
            self.Instructions_memory.change_line(data)
        elif(opcode == "1100"):
            #IF ALU result was negative , update Inst. Addr. Reg to new address
            pass
        elif(opcode == "1101"):
            #custom, it's not defined yet
            pass
        elif(opcode == "1110"):
            #custom, it's not defined yet
            pass
        elif(opcode == "1111"):
            #Program done. Halt computer
            return 1
        return 0

    def main_thread(self):
        done = 0
        while(not(done)):
            done = self.decode_execute()
            
        

