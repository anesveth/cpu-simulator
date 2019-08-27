from os.path import isfile as file_exist
from IC import IC #Importing SuperClass
import yaml 
import CPU

class YamlReader(IC):
    '''Reads Bios.yaml initial configuration'''
    def __init__(self):
        self.filepath="bios.yml"
    def yaml_loader(self):
        with open(self.filepath,"r") as config:
            data=yaml.load(config)
        return data
data=YamlReader().yaml_loader()
### variables to assign to CPU parts
ramdata=data.get('RAM_NUMBERS')
ramdata=ramdata.split(' ')
clockdata=data.get('clock')
visualizationdata=data.get('visualization')
visualizationdata=visualizationdata.split(' ')
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
    CPU.intel99.ram.write_enable(adress,ramdata[i])
CPU.intel99.visualization_code=bool(visualizationdata[0])
CPU.intel99.visualization_ram=bool(visualizationdata[1])
CPU.intel99.visualization_registers=bool(visualizationdata[2])
CPU.intel99.visualization_clock=bool(visualizationdata[3])
CPU.intel99.visualization_alu=bool(visualizationdata[4])


class CardReader(IC):
    '''Manages exterior files'''
    #other bouilder is already passed down by the father
    def __init__(self):
        self.file = ""

    def check_code(self):
        def check_binary(bistring):
            '''checks if a string is binary'''
            for char in bistring:
                if (char == 1 or char == 0):
                    return False
            return True
        '''Checks code in file, returns 0 if file doesnt exist'''
        #chequeamos existencia del archivo  
        if (self.file != ""):
            self.file.seek(0)
            #revisamos
            line = 1
            current_line = self.file.readline()
            errors = ""
            while (current_line != ""):
                size = len(current_line) == 10
                space = current_line.count(" ") == 1
                tem = current_line.replace(" ", "").replace("\n", "")
                digit = check_binary(tem)
                print(size)
                print(space)
                print(tem)
                print (digit)
                #print(current_line.count(" ") == 1 and len(current_line) == 10 and current_line.replace(" ", "").isdigit())
                if (not(size and space and digit)):
                    #has an error
                    errors = errors +"Mistake in line: "+str(line)+ ";          "+current_line+"\n"
                current_line = self.file.readline()
                line = line + 1
            return(errors)
        else:
            return 0
    def read_especific_line(self, line_number):
        self.change_line(line_number)
        return self.read_line()
    def change_line(self, line_number):
        '''Changes the current line to the one passed, if file not found returns 0'''
        if (self.file != ""):
            self.file.seek(line_number)
        else:
            return 0
    def read_line(self):
        '''returns the first line of the file, if it had already started,\
            it returns the next one. If the file is not open itll return 0 '''
        #chequeamos existencia del archivo
        if (self.file != ""):
            current_line = self.file.readline().strip("\n")
            while current_line.startswith("#"):
                current_line = self.file.readline().strip("\n")
            print("CurrentLine: "+current_line)
            return(current_line)
        else:
            return 0
    def free_reader(self):
        '''Cierra la referencia del archivo'''
        self.file.close()
        self.file = ""
    def change_file(self, file_name):
        '''changes the reader's file, leaves the previous file and \
            returns 0 if file not found, 1 for operation succesful'''
        file_name = file_name+".code"
        if (file_exist(file_name)):
            self.file = open(file_name)
            return 1
        else:
            self.file = ""
            return 0




