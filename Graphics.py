from IC import IC
# import CPU
import pygame 
class graphics(IC):
    def __init__(self):
        pygame.init() 
        self.white = (255, 255, 255)# white background
        # assigning values to X and Y variable 
        self.width = 1000
        self.height = 718
        # create the display surface (display window) 
        self.display_surface = pygame.display.set_mode((self.width, self.height)) 
        pygame.display.set_caption('IC simulation')# window name 
        # create a surface object, with the image 
        self.image = pygame.image.load(r'display.png') 
    def put_text(self, text, x=0, y=0, color=(0,0,0),font_type = 'Arial.ttf', size = 25):
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
            clocktxt = self.put_text("1.2 Hz",x=865,y=35)
            print (clocktxt) 
            ############################################## RAM (69 downward separation)
            ################### NUMBER OF RAM LOCATION
            yvalue=148
            for i in range(16):
                adress=bin(i)[2:]
                if len(adress)<4:
                    if len(adress)==1:
                        adress="000"+adress
                    if len(adress)==2:
                        adress="00"+adress
                    if len(adress)==3:
                        adress="0"+adress
                    opcodeitxt=self.put_text(str(adress),x=760,y=yvalue)
                    print(opcodeitxt)
                    yvalue+=35
                else:
                    opcodeitxt=self.put_text(str(adress),x=760,y=yvalue)
                    print(opcodeitxt)
                    yvalue+=35
            #
            ################### NUMBER SECTION
            #
            number0txt=self.put_text("0000",x=880,y=148)
            print (number0txt) 
            number1txt=self.put_text("0001",x=880,y=180)
            print (number1txt) 
            number2txt=self.put_text("0010",x=880,y=212)
            print (number2txt) 
            number3txt=self.put_text("0011",x=880,y=248)
            print (number3txt) 
            number4txt=self.put_text("0100",x=880,y=286)
            print (number4txt) 
            number5txt=self.put_text("0101",x=880,y=320)
            print (number5txt) 
            number6txt=self.put_text("0110",x=880,y=352)
            print (number6txt) 
            number7txt=self.put_text("0111",x=880,y=386)
            print (number7txt) 
            number8txt=self.put_text("1000",x=880,y=420)
            print (number8txt) 
            number9txt=self.put_text("1001",x=880,y=459)
            print (number9txt) 
            number10txt=self.put_text("1010",x=880,y=490)
            print (number10txt) 
            number11txt=self.put_text("1011",x=880,y=524)
            print (number11txt) 
            number12txt=self.put_text("1100",x=880,y=560)
            print (number12txt) 
            number13txt=self.put_text("1101",x=880,y=600)
            print (number13txt) 
            number14txt=self.put_text("1110",x=880,y=632)
            print (number14txt) 
            number15txt=self.put_text("1111",x=880,y=664)
            print (number15txt)
            ############################################## ALU 
            alutxt=self.put_text("0001-0001",x=535,y=267)
            print (alutxt)
            flagtxt=self.put_text("Z",x=565,y=325)
            print (flagtxt)
            ############################################## REGISTERS 
            outputtxt=self.put_text("0000",x=499,y=435) #OUTPUT R
            print (outputtxt)
            instruction_registertxt=self.put_text("0001 0001",x=470,y=545) #INSTRUCTION R
            print (instruction_registertxt)
            instruction_adress_registertxt=self.put_text("0010 0001",x=470,y=645) #INSTRUCTION ADRESS R
            print (instruction_adress_registertxt)
            registerAtxt=self.put_text("0000 0000",x=100,y=350) #REGISTER A
            print (registerAtxt)
            registerBtxt=self.put_text("0000 0000",x=100,y=450) #REGISTER B
            print (registerBtxt)
            registerCtxt=self.put_text("0000 0000",x=100,y=550) #REGISTER C
            print (registerCtxt)
            registerDtxt=self.put_text("0000 0000",x=100,y=660) #REGISTER D
            print (registerDtxt)
            ############################################## .CODE FILE DISPLAY 
            self.codetxt="123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960"
            lenght_code=len(self.codetxt)
            line_start=0#position in string
            if lenght_code>55:
                line_space=60#position in display
                finish_length=55
                lenght_code_left=lenght_code
                while lenght_code_left>55: #stops the string displayed from going over the 'Instructios.code' window
                    displayedtxt=self.codetxt[line_start:finish_length]
                    codetxt_displayed=self.put_text("{}".format(displayedtxt),x=32,y=line_space,size=12)
                    print(codetxt_displayed)
                    line_space+=20
                    line_start+=55
                    finish_length=line_start+55
                    lenght_code_left=lenght_code_left-55
                displayedtxt=str(self.codetxt[line_start:])
                codetxt_displayed=self.put_text("{}".format(displayedtxt),x=32,y=line_space,size=12)
                print(codetxt_displayed)
            #if it's not necessary (because the string lenght won't go over the window)
            else:
                codetxt_displayed=self.put_text("{}".format(self.codetxt[0:55]),x=32,y=60,size=12)
                print(codetxt_displayed)


            for event in pygame.event.get():
                print(str(event)) 
                if event.type == pygame.VIDEORESIZE:
                    self.display_surface = pygame.display.set_mode(event.w, event.h)
                    self.image=self.adjust_to_resize(self.image, event, 1, 1)

                if event.type == pygame.QUIT : 
                    pygame.quit()
                    break
                # Makes the updates to the surface object 
                pygame.display.update()

graphs = graphics()
graphs.core()




