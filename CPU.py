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

        self.output_register=Registers(data)

        data_bios=Reader.YamlReader().yaml_loader()
        ### variables to assign to CPU parts
        ramdata=data_bios.get('RAM_NUMBERS')
        ramdata=ramdata.split(' ')
        clockdata=data_bios.get('clock')
        self.clock_time = int(clockdata)
        visualizationdata=data_bios.get('visualization')
        ##asigns all ram data to each ram space
        for i in range(16):
            adress=bin(i)[2:]
            if len(adress)<4:
                if len(adress)==1:
                    adress="000"+adress
                if len(adress)==2:
                    adress="00"+adress
                if len(adress)==3:
                    adress="0"+adress
            self.ram.write_enable(adress,ramdata[i])
        self.visualization_code=visualizationdata['code']
        self.visualization_ram=visualizationdata['RAM']
        self.visualization_registers=visualizationdata['Registers']
        self.visualization_clock=visualizationdata['clock']
        self.visualization_alu=visualizationdata['ALU']
        

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
            self.registerB.write_register(self.ALU.and1(data[0:2], data[2:4]))
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
            self.registerB.write_register(self.ALU.or1(data[0:2], data[2:4]))
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
            self.pretty_print()
            done = self.decode_execute()
            time.sleep(self.clock_time)
            sys.stdout.flush() 
    def pretty_print(self):
        print("-"*40)
        if (self.visualization_ram):
            for x in range(0,16):
                print("RAM"+str(x)+": " + self.ram.easy_read(x))
        if (self.visualization_registers):
            print("instruction_adress_register: " + "{0:b}".format(self.Instructions_memory.c_line))
            print("registerA: " + self.registerA.read_register())
            print("registerB: " + self.registerB.read_register())
            print("registerC " + self.registerC.read_register())
            print("registerD " + self.registerD.read_register())
            print("instruction_register " + self.instruction_register.read_register())
            print("output_register " + self.output_register.read_register())
        print("overfl_flag: " + str(self.ALU.overfl_flag))
        print("carry_flag: " + str(self.ALU.carry_flag))
        print("error_flag " + str(self.ALU.error_flag))
        print("zero_flag " + str(self.ALU.zero_flag))
        print("neg_flag " + str(self.ALU.neg_flag))
        print("-"*40)
    def debug(self):
        done = 0
        while(not(done)):
            self.pretty_print()
            done = self.decode_execute()
            input("Presiona enter para continuar: ")

if __name__ == "__main__":
    intel99 = cu()
    if(input("que desea hacer(debug/other): ") == "debug"):
        intel99.debug()
    else:
        intel99.main_thread()