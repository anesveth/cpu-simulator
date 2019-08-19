from IC import IC
import pygame 
pygame.init() 
# define for white colour 
white = (255, 255, 255) 
#size of window
X = 1000
Y = 1000
# create the display surface (display window) 
display_surface = pygame.display.set_mode((X, Y ), pygame.RESIZABLE) 
# set the window name 
pygame.display.set_caption('IC simulation') 
# create a surface object, with the image 
image = pygame.image.load(r'brain.png') 

while True : 
    # completely fill the surface object 
    # with white colour 
    display_surface.fill(white) 
    # copying the image to display surface object at 0,0
    display_surface.blit(image) 
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get():
        print(str(event)) 
        if event.type == pygame.VIDEORESIZE:
            surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            image = pygame.transform.scale(image, (int(event.w * 0.2), int(event.h*0.2)))
        if event.type == pygame.QUIT : 
            pygame.quit()
            break
        # Makes the updates to the surface object 
        pygame.display.update()

# class Graphics(IC):
#     #display info
#     a = ""