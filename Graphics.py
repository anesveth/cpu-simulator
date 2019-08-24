from IC import IC
import pygame 
class graphics(IC):
    def __init__(self):
        pygame.init() 
        # define for white colour 
        self.white = (255, 255, 255) 
        # assigning values to X and Y variable 
        X = 1920
        Y = 1080
        # create the display surface (display window) 
        self.display_surface = pygame.display.set_mode((X, Y ), pygame.RESIZABLE) 
        # set the window name 
        pygame.display.set_caption('IC simulation') 
        # create a surface object, with the image 
        self.image = pygame.image.load(r'brain.png') 
        #creates font to use
        self.font = pygame.font.SysFont("comicsansms", 72)
    def put_text(self, text, x=0, y=0, color=(0,0,0), 
        font_type = 'OpenSans-Regular.ttf', size = 30):
        '''displays a text on surface
        returns surface, 0 if failed'''
        try:
            font = pygame.font.Font(font_type, size)
            text = font.render(str(text), True, color)
            self.display_surface.blit(text, (x, y))
            return text
        except Exception:
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
            self.put_image(self.image, 100, 100)
            #displaying text
            teext = self.put_text("alv")
            self.display_surface.blit(teext, (0,0)) 
            # iterate over the list of Event objects 
            # that was returned by pygame.event.get() method. 
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




