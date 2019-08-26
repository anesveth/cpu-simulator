from IC import IC
import CPU
import pygame 
class graphics(IC):
    def __init__(self):
        pygame.init() 
        self.white = (255, 255, 255)# white background
        # assigning values to X and Y variable 
        width = 2000
        height = 1435
        # create the display surface (display window) 
        self.display_surface = pygame.display.set_mode((width, height ), pygame.RESIZABLE) 
        pygame.display.set_caption('IC simulation')# window name 
        # create a surface object, with the image 
        self.image = pygame.image.load(r'display.png') 
    def put_text(self, text, x=0, y=0, color=(0,0,0),font_type = 'Arial.ttf', size = 40):
        '''displays a text on surface
        returns surface, 0 if failed'''
        try:
            font = pygame.font.Font(font_type, size)
            text = font.render(str(text), True, color)
            self.display_surface.blit(text, (x, y))
            return text
        except Exception as e:
            print (str(e))
            return 0
    def put_image(self, object1, x, y):
        # copying the object to display surface object at x.y
        self.display_surface.blit(object1, (x,y)) 
    def adjust_to_resize(self, surface, event, width_percentage, height_percentage):
        return pygame.transform.scale(surface, (int(event.w * width_percentage), int(event.h*height_percentage)))
    def core(self):
        # infinite loop 
        while True : 
            # completely fill the surface object 
            # with white colour 
            self.display_surface.fill(self.white)   
            self.put_image(self.image, 0, 0)
            #DISPLAYING TEXT
            clocktxt = self.put_text("1.2 Hz",x=1740,y=67,size=60)
            print (clocktxt) 
            ############################################## RAM (69 downward separation)
            ################### OPCODE SECTION
            opcode0txt=self.put_text("0000",x=1505,y=296,size=48)
            print (opcode0txt) 
            opcode1txt=self.put_text("0001",x=1505,y=365,size=48)
            print (opcode1txt) 
            opcode2txt=self.put_text("0010",x=1505,y=434,size=48)
            print (opcode2txt) 
            opcode3txt=self.put_text("0011",x=1505,y=503,size=48)
            print (opcode3txt) 
            opcode4txt=self.put_text("0100",x=1505,y=572,size=48)
            print (opcode4txt) 
            opcode5txt=self.put_text("0101",x=1505,y=641,size=48)
            print (opcode5txt) 
            opcode6txt=self.put_text("0110",x=1505,y=710,size=48)
            print (opcode6txt) 
            opcode7txt=self.put_text("0111",x=1505,y=779,size=48)
            print (opcode7txt) 
            opcode8txt=self.put_text("1000",x=1505,y=848,size=48)
            print (opcode8txt) 
            opcode9txt=self.put_text("1001",x=1505,y=917,size=48)
            print (opcode9txt) 
            opcode10txt=self.put_text("1010",x=1505,y=986,size=48)
            print (opcode10txt) 
            opcode11txt=self.put_text("1011",x=1505,y=1055,size=48)
            print (opcode11txt) 
            opcode12txt=self.put_text("1100",x=1505,y=1124,size=48)
            print (opcode12txt) 
            opcode13txt=self.put_text("1101",x=1505,y=1193,size=48)
            print (opcode13txt) 
            opcode14txt=self.put_text("1110",x=1505,y=1262,size=48)
            print (opcode14txt) 
            opcode15txt=self.put_text("1111",x=1505,y=1331,size=48)
            print (opcode15txt) 
            #
            ################### NUMBER SECTION
            #
            number0txt=self.put_text("0000",x=1765,y=296,size=48)
            print (number0txt) 
            number1txt=self.put_text("0001",x=1765,y=365,size=48)
            print (number1txt) 
            number2txt=self.put_text("0010",x=1765,y=434,size=48)
            print (number2txt) 
            number3txt=self.put_text("0011",x=1765,y=503,size=48)
            print (number3txt) 
            number4txt=self.put_text("0100",x=1765,y=572,size=48)
            print (number4txt) 
            number5txt=self.put_text("0101",x=1765,y=641,size=48)
            print (number5txt) 
            number6txt=self.put_text("0110",x=1765,y=710,size=48)
            print (number6txt) 
            number7txt=self.put_text("0111",x=1765,y=779,size=48)
            print (number7txt) 
            number8txt=self.put_text("1000",x=1765,y=848,size=48)
            print (number8txt) 
            number9txt=self.put_text("1001",x=1765,y=917,size=48)
            print (number9txt) 
            number10txt=self.put_text("1010",x=1765,y=986,size=48)
            print (number10txt) 
            number11txt=self.put_text("1011",x=1765,y=1055,size=48)
            print (number11txt) 
            number12txt=self.put_text("1100",x=1765,y=1124,size=48)
            print (number12txt) 
            number13txt=self.put_text("1101",x=1765,y=1193,size=48)
            print (number13txt) 
            number14txt=self.put_text("1110",x=1765,y=1262,size=48)
            print (number14txt) 
            number15txt=self.put_text("1111",x=1765,y=1331,size=48)
            print (number15txt)
            ############################################## ALU 
            alutxt=self.put_text("0001-0001",x=1065,y=525,size=48)
            print (alutxt)
            flagtxt=self.put_text("Z",x=1145,y=642,size=55)
            print (flagtxt)
            ############################################## REGISTERS 
            outputtxt=self.put_text("0000",x=1000,y=860,size=50) #OUTPUT R
            print (outputtxt)
            instruction_registertxt=self.put_text("0001 0001",x=950,y=1099,size=50) #INSTRUCTION R
            print (instruction_registertxt)
            instruction_adress_registertxt=self.put_text("0010 0001",x=950,y=1299,size=50) #INSTRUCTION ADRESS R
            print (instruction_adress_registertxt)
            registerAtxt=self.put_text("0000 0000",x=198,y=697,size=49) #REGISTER A
            print (registerAtxt)
            registerBtxt=self.put_text("0000 0000",x=198,y=888,size=49) #REGISTER B
            print (registerBtxt)
            registerCtxt=self.put_text("0000 0000",x=198,y=1100,size=49) #REGISTER C
            print (registerCtxt)
            registerDtxt=self.put_text("0000 0000",x=198,y=1309,size=49) #REGISTER D
            print (registerDtxt)
            ############################################## .CODE FILE DISPLAY 
            codetxt="123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960"
            lenght_code=len(codetxt)
            line_start=0#position in string
            if lenght_code>34:
                line_space=120#position in display
                finish_length=34
                lenght_code_left=lenght_code
                while lenght_code_left>34: #stops the string displayed from going over the 'Instructios.code' window
                    displayedtxt=codetxt[line_start:finish_length]
                    codetxt_displayed=self.put_text("{}".format(displayedtxt),x=69,y=line_space,size=45)
                    print(codetxt_displayed)
                    line_space+=40
                    line_start+=34
                    finish_length=line_start+34
                    lenght_code_left=lenght_code_left-34
                displayedtxt=str(codetxt[line_start:])
                codetxt_displayed=self.put_text("{}".format(displayedtxt),x=69,y=line_space,size=45)
                print(codetxt_displayed)
            #if it's not necessary (because the string lenght won't go over the window)
            codetxt_displayed=self.put_text("{}".format(codetxt[0:34]),x=69,y=120,size=45)
            print(codetxt_displayed)


            for event in pygame.event.get():
                print(str(event)) 
                if event.type == pygame.VIDEORESIZE:
                    self.display_surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.image=self.adjust_to_resize(self.image, event, 0.5, 0.5)
                    #self.image = pygame.transform.scale(self.image, (int(event.w * 0.2), int(event.h*0.2)))
                if event.type == pygame.QUIT : 
                    pygame.quit()
                    break
                # Makes the updates to the surface object 
                pygame.display.update()

graphs = graphics()
graphs.core()




