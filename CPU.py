from IC import IC
from Memory import RAM, Registers
import ALU
import Reader
import time
import sys
class cu(IC):
    def __init__(self):
        '''controls and connects everything'''
        self.Instructions_memory = Reader.CardReader()
        print("Ingresa nombre del codigo (sin el .code)")
        file_name = input()
        data=[""]*8 #creating data
        self.Instructions_memory.change_file(file_name)

        self.ALU = ALU.ALU()
        self.ram = RAM()
        self.registerA=Registers(data)
        self.registerB=Registers(data)
        self.registerC=Registers(data)
        self.registerD=Registers(data)

        self.instruction_register=Registers(data, 8) #shows the selected data that was located in RAM
        self.instruction_adress_register=Registers("00000000",8) #keeps 

        self.output_register=Registers(data)
    def decode_execute(self):
        self.instruction_register.write_register(str(self.Instructions_memory.read_line()))
        opcode = self.instruction_register.read_register()[0:4]
        data = self.instruction_register.read_register()[4:8]
        print("full: "+self.instruction_register.read_register())
        print("opcode: "+opcode)
        print("data: "+data)
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
            self.ALU.and1(data[0:2], data[2:4])
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
            self.ALU.or1(data[0:2], data[2:4])
        elif(opcode == "1000"):
            #Immediate Read constant into register B
            self.registerB.write_register(data)
        elif(opcode == "1001"):
            #Add two registers, store result into second register
            self.registerB.write_register(self.ALU.sum1(self.registerA.read_register(), self.registerB.read_register()))
        elif(opcode == "1010"):
            #Subtract two registers, store result into second register
            self.registerB.write_register(self.ALU.sub(self.registerA.read_register(), self.registerB.read_register()))
        elif(opcode == "1011"):
            #update Inst. Addr. Reg to new address
            self.Instructions_memory.change_line(data)
        elif(opcode == "1100"):
            #IF ALU result was negative , update Inst. Addr. Reg to new address
            if (self.ALU.o):
                self.Instructions_memory.change_line(data)
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
            print("-"*40)
            for x in range(0,14):
                print("RAM"+str(x)+": " + self.ram.easy_read(x))
            print("instruction_adress_register: " + self.instruction_adress_register.read_register())
            print("registerA: " + self.registerA.read_register())
            print("registerB: " + self.registerB.read_register())
            print("registerC " + self.registerC.read_register())
            print("registerD " + self.registerD.read_register())
            print("instruction_register " + self.instruction_register.read_register())
            print("output_register " + self.output_register.read_register())
            print("-"*40)
            done = self.decode_execute()
            time.sleep(0.5)
            sys.stdout.flush()
            
        

intel99 = cu()
intel99.main_thread()