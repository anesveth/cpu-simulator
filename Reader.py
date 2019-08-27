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




class CardReader(IC):
    '''Manages exterior files'''
    #other bouilder is already passed down by the father
    def __init__(self):
        self.file = ""
        self.c_line = 0
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
            
            self.file.seek(int(line_number,2))
            self.c_line = int(line_number,2)
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
            current_line = current_line.replace("OUTPUT ", "0000")
            current_line = current_line.replace("ILD_A ", "0100")
            current_line = current_line.replace("ILD_B ", "1000")
            current_line = current_line.replace("LD_A ", "0001")
            current_line = current_line.replace("LD_B ", "0010")
            current_line = current_line.replace("AND ", "0011")
            current_line = current_line.replace("STR_A ", "0101")
            current_line = current_line.replace("STR_B ", "0110")
            current_line = current_line.replace("OR ", "0111")
            current_line = current_line.replace("ADD ", "1001")
            current_line = current_line.replace("SUB ", "1010")
            current_line = current_line.replace("JMP_N ", "1100")
            current_line = current_line.replace("JMP ", "1011")
            current_line = current_line.replace("NOT ", "1101")
            current_line = current_line.replace("CLEAR ", "1110")
            current_line = current_line.replace("HALT ", "1111")
            current_line = current_line.replace(" A", "00")
            current_line = current_line.replace(" B", "01")
            current_line = current_line.replace(" ", "")
            print("CurrentLine: "+current_line)
            self.c_line = self.c_line + 1
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




