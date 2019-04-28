import pygame
import math
import time
import pickle
pygame.init()
#####<< variable >>####
i=0
j=0
sheet_w=700
sheet_h=700
sheet=pygame.display.set_mode((sheet_w,sheet_h))
clock=pygame.time.Clock()
######################
######(colors)#####
light_blue=(102, 204, 255)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
##################
pygame.display.set_caption("Majic Circle")
def text_objects(text,font,color):
    textSurface = font.render(text, True , color)
    return textSurface, textSurface.get_rect()
def message_display(text,x,y,color,size):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(str(text),largeText,color)
    TextRect.center = ((x),(y))
    sheet.blit(TextSurf,TextRect)
    pygame.display.update()
def poolar_to_dekart(r,teta):
    X=r*math.cos(-teta*math.pi/180)
    Y=r*math.sin(-teta*math.pi/180)
    x=X+sheet_w/2
    y=Y+sheet_h/2
    return [int(x),int(y)]
def draw(x_c,y_c,r,R,T,d):
    x=d*math.cos(T*R/r)+x_c
    y=d*math.sin(T*R/r)+y_c
    return [int(x),int(y)]
def main_circle(rad):
    pygame.draw.circle(sheet,red,(int(sheet_w/2),int(sheet_h/2)),rad,3)
def small_circle(x_pos,y_pos,rad):
    pygame.draw.circle(sheet,blue,(x_pos,y_pos),rad,3)
def point(x,y):
    pygame.draw.circle(sheet,green,(x,y),1)
def main():    
    intro=True
    poin_location=[]
    c_color=white
    c_color_2=white
    c_color_3=white
    c_color_4=black
    c_color_5=white
    c_x=60
    c_x_2=390
    c_y_3=50
    teta_change=0
    teta_2=0
    while intro: 
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    teta_change=0.5      
        if c_x-10<mouse[0]<c_x+10 and 20<mouse[1]<40:
            c_color=red
            message_display(c_x,c_x,60,white,20)
        else:
            c_color=white
        if c_x-10<mouse[0]<c_x+10 and 20<mouse[1]<40:   
            if click[0]==1 and 50<mouse[0]<290:
                c_x=mouse[0]
        if c_x_2-10<mouse[0]<c_x_2+10 and 20<mouse[1]<40:
            c_color_2=blue
            message_display(c_x_2-330,c_x_2,60,white,20)
        else:
            c_color_2=white
        if c_x_2-20<mouse[0]<c_x_2+20 and 10<mouse[1]<50:   
            if click[0]==1 and 380<mouse[0]<590:
                c_x_2=mouse[0]
        if c_y_3-10<mouse[1]<c_y_3+10 and 650<mouse[0]<680:
            c_color_3=green
            message_display(c_y_3,620,c_y_3,white,20)
        else:
            c_color_3=white
        
        if c_y_3-20<mouse[1]<c_y_3+20 and 640<mouse[0]<690:    
            if click[0]==1 and 40<mouse[1]<270:
                c_y_3=mouse[1]
        teta_2+=teta_change
        sheet.fill(black)
        pygame.draw.rect(sheet,green,(50,sheet_h-100,70,50)) 
        pygame.draw.rect(sheet,c_color_4,(70,sheet_h-95,10,40))
        pygame.draw.rect(sheet,c_color_4,(90,sheet_h-95,10,40))
        pygame.draw.rect(sheet,blue,(20,20,20,20))
        pygame.draw.rect(sheet,blue,(300,20,20,20))
        pygame.draw.line(sheet,white,(40,30),(300,30),2)
        pygame.draw.rect(sheet,blue,(350,20,20,20))
        pygame.draw.rect(sheet,blue,(600,20,20,20))
        pygame.draw.line(sheet,white,(370,30),(600,30),2)
        pygame.draw.rect(sheet,blue,(650,20,20,20))
        pygame.draw.rect(sheet,blue,(650,270,20,20))
        pygame.draw.line(sheet,white,(660,40),(660,270),2)
        pygame.draw.circle(sheet,c_color,(c_x,30),10)
        pygame.draw.circle(sheet,c_color_2,(c_x_2,30),10)
        pygame.draw.circle(sheet,c_color_3,(660,c_y_3),10)
        point(draw(poolar_to_dekart(int(c_x-(c_x_2-330)),teta_2)[0],poolar_to_dekart(int(c_x-(c_x_2-330)),teta_2)[1],int(c_x_2-330),c_x,teta_2*math.pi/180,c_y_3-50)[0],draw(poolar_to_dekart(int(c_x-(c_x_2-330)),teta_2)[0],poolar_to_dekart(int(c_x-(c_x_2-330)),teta_2)[1],int(c_x_2-330),c_x,teta_2*math.pi/180,c_y_3-50)[1])
        poin_location.append([draw(poolar_to_dekart(int(c_x-(c_x_2-330)),teta_2)[0],poolar_to_dekart(int(c_x-(c_x_2-330)),teta_2)[1],int(c_x_2-330),c_x,teta_2*math.pi/180,c_y_3-50)[0],draw(poolar_to_dekart(int(c_x-(c_x_2-330)),teta_2)[0],poolar_to_dekart(int(c_x-(c_x_2-330)),teta_2)[1],int(c_x_2-330),c_x,teta_2*math.pi/180,c_y_3-50)[1]])
        for i in range(0,len(poin_location)):
            pygame.draw.circle(sheet,c_color_5,[poin_location[i][0],poin_location[i][1]],1)
        main_circle(c_x)
        small_circle(poolar_to_dekart(int(c_x-(c_x_2-330)),teta_2)[0],poolar_to_dekart(int(c_x-(c_x_2-330)),teta_2)[1],int(c_x_2-330))
        pygame.display.update()
        clock.tick(320)
        i+=1 
        if sheet_h-100<mouse[1]<sheet_h-50 and 50<mouse[0]<120:
            c_color_4=red
            if click[0]==1:
                poin_location=[]
        else:
            c_color_4=black       
main()
