#fk control unit
from IC import IC
import Reader
class cu(IC):
    def recibe_code(self):
        #pass
        print("")
    def interpretacion(self):
        #pass
        print("ARRREEE")
    def main_thread(self):
        '''controls and connects everything'''
        hard_drive = Reader.CardReader()
        print("Ingresa nombre del codigo (sin el .code)")
        file_name = input()
        hard_drive.change_file(file_name)
        intruction = hard_drive.read_line()
        #decides what to do with instructions
        

