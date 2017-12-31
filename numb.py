#! /usr/bin/env python
# -*- coding: utf-8 -*-

#import
import time
import sys
import random
import pygame
from pygame.locals import *
from sys import exit
backgrounda_image_filename='b4.jpg'
backgroundb_image_filename='b3.jpg'
collectstaroff_image_filename='collect_star_off.png'
collectstaron_image_filename='collect_star_on.png'
global a
global b
global c
global d
global mode_now
WHITE =(242,252,252)
BLUE =(58,113,140)
NUMPIECEWIDTH = 50
titlenow=0
a=[]
c=[]
collect=[]
d=['新手','入门','初级','中级','成语','收藏']
for i in range( 0,6 ):
        d[i] = unicode(d[i],'utf-8')
mode_now = 0


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('中华诗文成语拼图')
backgrounda = pygame.image.load(backgrounda_image_filename).convert()       
backgroundb = pygame.image.load(backgroundb_image_filename).convert()
collect_star_off = pygame.image.load(collectstaroff_image_filename).convert_alpha()
collect_star_on = pygame.image.load(collectstaron_image_filename).convert_alpha()

#class
class NumPiece(pygame.Surface):
    font = pygame.font.Font("yt.ttf", 28)
    def __init__(self, num):
        pygame.surface.Surface.__init__(self, (NUMPIECEWIDTH, NUMPIECEWIDTH))
        self.fill(WHITE)
        self.set_alpha(120)
        text = NumPiece.font.render(c[num-1], 1, BLUE)
        textRect = text.get_rect()
        textRect.center = (NUMPIECEWIDTH / 2, NUMPIECEWIDTH / 2)
        self.blit(text, textRect.topleft)
        a.append(num)

class RightPiece(pygame.Surface):
    font = pygame.font.Font("yt.ttf", 28)
    def __init__(self, num):
        pygame.surface.Surface.__init__(self, (NUMPIECEWIDTH, NUMPIECEWIDTH))
        self.fill(WHITE)
        self.set_alpha(120)
        text = RightPiece.font.render(c[num], 1, BLUE)
        textRect = text.get_rect()
        textRect.center = (NUMPIECEWIDTH / 2, NUMPIECEWIDTH / 2)
        self.blit(text, textRect.topleft)

def help0():
        esc = True
        while esc:
            font = pygame.font.Font("yt.ttf",35)
            font3 = pygame.font.Font("yt.ttf",25)
            string3 =u'游戏说明'
            text3 = font.render((string3),True,[0,0,0])
            textRect3 = text3.get_rect()
            textRect3.center = (screen.get_width() / 2, 35)
            string4 =u'欢迎体验本拼图游戏，以下是游戏说明'
            text4 = font3.render((string4),True,[0,0,0])
            textRect4 = text4.get_rect()
            textRect4.center = (screen.get_width() / 2, 85)
            string5 =u'1.在初始界面可以通过上下键选择年龄段'
            text5 = font3.render((string5),True,[0,0,0])
            textRect5 = text5.get_rect()
            textRect5.center = (screen.get_width() / 2, 120)
            string6 =u'2.选好后按回车键进入游戏 '
            text6 = font3.render((string6),True,[0,0,0])
            textRect6 = text6.get_rect()
            textRect6.center = (screen.get_width() / 2, 155)
            string7 =u'3.诗词模式下游戏目标是将诗词的片段从左到右'
            text7 = font3.render((string7),True,[0,0,0])
            textRect7 = text7.get_rect()
            textRect7.center = (screen.get_width() / 2, 190)
            string8 =u'  以及从上到下通过方向键按原句的顺序还原'
            text8 = font3.render((string8),True,[0,0,0])
            textRect8 = text8.get_rect()
            textRect8.center = (screen.get_width() / 2, 220)
            string9 =u'4.而成语模式则需要用给出的字组成两个成语'
            text9 = font3.render((string9),True,[0,0,0])
            textRect9 = text9.get_rect()
            textRect9.center = (screen.get_width() / 2, 255)
            string10 =u'  其中有一个字是通用的 把它们排列在黑框中'
            text10 = font3.render((string10),True,[0,0,0])
            textRect10 = text10.get_rect()
            textRect10.center = (screen.get_width() / 2, 285)
            string11 =u'5.在游戏中按A键获得提示，C键收藏诗词'
            text11 = font3.render((string11),True,[0,0,0])
            textRect11 = text11.get_rect()
            textRect11.center = (screen.get_width() / 2, 320)
            string12 =u'6.按esc返回主菜单，按F1开关BGM'
            text12 = font3.render((string12),True,[0,0,0])
            textRect12 = text12.get_rect()
            textRect12.center = (screen.get_width() / 2, 355)
            string13 =u'由于时间原因，游戏有些简陋望海涵'   
            text13 = font3.render((string13),True,[0,0,0])
            textRect13 = text13.get_rect()
            textRect13.center = (screen.get_width() / 2, 400)
            string14 =u'现在按esc开始你们的游戏吧'   
            text14 = font3.render((string14),True,[0,0,0])
            textRect14 = text14.get_rect()
            textRect14.center = (screen.get_width() / 2, 450)
            string15 =u'——夏月 马德拉小男孩 复古37'   
            text15 = font3.render((string15),True,[0,0,0])
            textRect15 = text15.get_rect()
            textRect15.center = (580,550)         
            screen.fill([255,255,255])
            screen.blit(text3, (textRect3.topleft))
            screen.blit(text4, (textRect4.topleft))
            screen.blit(text5, (textRect5.topleft))
            screen.blit(text6, (textRect6.topleft))
            screen.blit(text7, (textRect7.topleft))
            screen.blit(text8, (textRect8.topleft))
            screen.blit(text9, (textRect9.topleft))
            screen.blit(text10, (textRect10.topleft))
            screen.blit(text11, (textRect11.topleft))
            screen.blit(text12, (textRect12.topleft))
            screen.blit(text13, (textRect13.topleft))
            screen.blit(text14, (textRect14.topleft))
            screen.blit(text15, (textRect15.topleft))
            event = pygame.event.wait()
        
            if event.type == QUIT:
                    write_collect()
                    pygame.quit()
                    exit()
            elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        break
            pygame.display.flip()

def add_collect(poemnow):
    collect.append(poemnow)

def del_collect(poemnow):
    for i in range (0,len(collect)):
        if poemnow==collect[i]:
            del collect[i]
            break

def write_collect():
    collectfile = file('collectlist.txt','w')
    for i in range (0,len(collect)):
        collectfile.write(str(collect[i]))
        collectfile.write(' ')
    collectfile.close

def gettitle(poemget):
    poetry = {}
    c=[]        
    with open("allpoem.txt") as allpoem:            
        poetry[allpoem] = allpoem.readlines()
    prepared_poem = poetry[allpoem][poemget-1]
    poem_prepared = prepared_poem.split('/')
    title = poem_prepared[0]
    title = unicode(title,'utf-8')
    return title


def answer():
    global c
    #Draw
    if num == 1:
        screen.blit(backgrounda,(0,0))
    if num == 2:
        screen.blit(backgrounda,(0,0))
    if num == 3:
        screen.blit(backgrounda,(0,0))
    if num == 4:
        screen.blit(backgroundb,(0,0))

    if nume == 4:
        startPoint = (285, 185)
    if nume == 5:
        startPoint = (255, 185)
    if nume == 7:
        startPoint = (195, 155)
        
    counte = 0
    for rp in rightPieces:
        if rp == 0:
            counte += 1
            continue
        else:
            zz = (startPoint[0] + (counte%nume) * (NUMPIECEWIDTH + 10), startPoint[1] + (counte/nume) * (NUMPIECEWIDTH + 10))
            screen.blit(rp, zz)
            counte += 1
        pygame.display.flip()
        
def scan_collect():
    global num
    global numa
    global nume
    global title_list
    global poemnow
    global titlenow
    collectget0=False
    title_list=[]
    prepared_collect = {}
    if len(collect) == 0:
        with open("collectlist.txt") as readcollect:
                prepared_collect = readcollect.readlines()
        if len(prepared_collect)!=0:                
            read_collect = prepared_collect[0]
            read_collect_ = read_collect.split()
            for i in range (0,len(read_collect_)):
                collecta=int (read_collect_[i]);
                collect.append(collecta);
        
    if len(collect) == 0:
        collectget0=True
    if collectget0!=True:
        for i in range (0,len(collect)):
            title_list.append(gettitle(collect[i]))
         
#main
    while True:
        if collectget0!=True:            
            if titlenow==len(title_list):
                titlenow=len(title_list)-1
            for event in pygame.event.get():
                if event.type == QUIT:
                    write_collect()
                    pygame.quit()
                    exit()
                elif event.type == KEYDOWN:
                    if collectget0==False:                
                        if event.key == K_DOWN:
                            if titlenow!=len(title_list)-1:
                                titlenow+=1
                            elif titlenow==len(title_list)-1:
                                titlenow=0                                       
                        elif event.key == K_UP:
                            if titlenow!=0:
                                titlenow-=1
                            elif titlenow==0:
                                titlenow=len(title_list)-1                             
                        elif event.key == K_RETURN:
                            getdata(collect[titlenow])
                        elif event.type == KEYDOWN:                    
                            if event.key == K_ESCAPE:
                                main()
                            
        for event in pygame.event.get():
            if event.type == QUIT:
                write_collect()
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:                    
                if event.key == K_ESCAPE:
                    main()
#draw           
        screen.fill([255,255,255])
        font = pygame.font.Font("yt.ttf",25)
        font1 = pygame.font.Font("yt.ttf", 50)                   
        if collectget0==True:

            string3 =u'没有收藏内容，在做题时按C键添加收藏'
            text3 = font.render((string3),True,BLUE)
            textRect3 = text3.get_rect()
            textRect3.center = (screen.get_width() / 2, 35)
            screen.blit(text3, (textRect3.topleft))
        else:
 
            text1 = font1.render(title_list[titlenow], 1, BLUE)
            textRect1 = text1.get_rect()
            textRect1.center = (screen.get_width() / 2, screen.get_height() / 2)                
            screen.blit(text1, (textRect1.topleft))

            string3 =u'上下键选择，回车键开始哦！'
            text3 = font.render((string3),True,BLUE)
            textRect3 = text3.get_rect()
            textRect3.center = (screen.get_width() / 2, 550)
            screen.blit(text3, (textRect3.topleft))               
        pygame.display.flip()
        pygame.display.update() 
        
#the game() function
def game():
    global a
    global b
    global c
    global d
    global r
    global num
    global rightPieces
    global backtocollect
    b = []
    rightPieces = []
          
    if num == 4:
        rightPieces = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        rightPieces[1] = RightPiece(1)
        rightPieces[5] = RightPiece(5)
        rightPieces[8] = RightPiece(8)
        rightPieces[9] = RightPiece(9)
        rightPieces[10] = RightPiece(10)
        rightPieces[11] = RightPiece(11)
        rightPieces[13] = RightPiece(13)
        b=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]    
    if num != 4:
            r = []
            j=1
            while j<right+1:
                b.append(j)
                r.append(0)
                j=j+1
            for i in range(0,right):
                rightPieces.append(RightPiece(i))
                    
    pressing=0
    numPieces = []
    tmpPieces = range(1,numa)
    while len(tmpPieces) > 1:
        numPieces.append(NumPiece(tmpPieces.pop(random.randint(0, len(tmpPieces) - 1))))
    numPieces.append(NumPiece(tmpPieces.pop()))
    numPieces.append(0)
    now = numa - 1

    a.append(0)

    #some bool
    gameover = False
    running = True
    collect_star = False

    #music
    g = random.randint(0,2)
    if g==0:
        pygame.mixer.music.load('1.ogg')
    elif g==1:
        pygame.mixer.music.load('2.ogg')
    elif g==2:
        pygame.mixer.music.load('3.ogg')
    pygame.mixer.music.play()
    m = True
    start = time.time()
    
    while running:
        blit_answer = False
        if not gameover:
            if num !=4:
                for i in range (0,right):
                    r[i]=a[i]
                if r==b:                    
                    gameover = True

                for i in range (0,len(collect)):
                    if poemnow == collect[i]:
                            collect_star=True
                            break
           
            elif num == 4:
                if a[1]==b[1]:
                    if a[5]==b[5]:
                        if a[8]==b[8]:
                            if a[9]==b[9]:
                                if a[10]==b[10]:
                                    if a[11]==b[11]:
                                        if a[13]==b[13]:
                                                gameover = True
                                                                                       
            
                    
            #Handle event
            for event in pygame.event.get():
                if event.type == QUIT:
                    write_collect()
                    pygame.quit()
                    exit()
                elif event.type == KEYDOWN:
                
                    if event.key == K_DOWN:
                        if now / nume > 0:
                            numPieces[now] = numPieces[now - nume]
                            numPieces[now - nume] = 0                    
                            a[now] = a[now - nume]
                            a[now - nume] = 0
                            now = now - nume
                       
                        
                    elif event.key == K_UP:
                        if num == 1:
                            if now / nume < nume - 1:
                                    numPieces[now] = numPieces[now + nume]
                                    numPieces[now + nume] = 0                    
                                    a[now]= a[now + nume]
                                    a[now + nume] = 0
                                    now = now + nume
                        if num == 2:
                            if now<= 14:
                                    if now / nume < nume - 1:
                                        numPieces[now] = numPieces[now + nume]
                                        numPieces[now + nume] = 0                    
                                        a[now]= a[now + nume]
                                        a[now + nume] = 0
                                        now = now + nume                                    
                               
                        if num == 3:
                            if now <= 27:
                                if now / nume < nume - 1:
                                    numPieces[now] = numPieces[now + nume]
                                    numPieces[now + nume] = 0                    
                                    a[now]= a[now + nume]
                                    a[now + nume] = 0
                                    now = now + nume
                                


                        if num == 4:
                            if now / nume < nume - 1:
                                numPieces[now] = numPieces[now + nume]
                                numPieces[now + nume] = 0                    
                                a[now]= a[now + nume]
                                a[now + nume] = 0
                                now = now + nume
                                
                           
                
                    elif event.key == K_RIGHT:
                        if now % nume > 0:
                            numPieces[now] = numPieces[now - 1]
                            numPieces[now - 1] = 0                   
                            a[now] = a[now - 1]
                            a[now - 1] = 0
                            now = now - 1
                       
                    elif event.key == K_LEFT:
                        if now % nume < nume - 1:
                            numPieces[now] = numPieces[now + 1]
                            numPieces[now + 1] = 0                    
                            a[now] = a[now + 1]
                            a[now + 1] = 0
                            now = now + 1
                    elif event.key == K_ESCAPE:
                            
                            pygame.mixer.music.stop()
                            poetry = {}
                            nowa = 0
                            bland_surface = pygame.Surface((800,600))
                            running = True
                            gameover = False
                            a=[]
                            num=0
                            write_collect()
                            if  backtocollect==True:
                                scan_collect()
                            else:
                                main()
                    elif event.key == K_F1:
                            if m == True:
                                pygame.mixer.music.stop()
                                m = False
                            elif m == False:
                                pygame.mixer.music.play()
                                m = True
                    elif event.key == K_a:
                        pressing = 1
                    elif event.key == K_c:
                            if num!=4:
                                if collect_star == False:
                                        add_collect(poemnow)
                                        collect_star = True

                                elif collect_star == True:
                                        del_collect(poemnow)
                                        collect_star = False            
                if event.type == KEYUP and pressing:
                    pressing = 0
                if pressing:
                    answer() 
            #Draw
            if num == 1:
                screen.blit(backgrounda,(0,0))
            if num == 2:
                screen.blit(backgrounda,(0,0))
            if num == 3:
                screen.blit(backgrounda,(0,0))
            if num == 4:
                screen.blit(backgroundb,(0,0))
                    
            fonttitle = pygame.font.Font('msyhbd.ttc', 28)
            fonttime = pygame.font.Font('yt.ttf', 35)
            fontauthor = pygame.font.Font('msyhbd.ttc', 22)

            
            now_time = time.time()
            passed_time = now_time - start
            passed_time_int = int(passed_time)
                      
            timebar = fonttime.render((str(passed_time_int)),True,BLUE)
            timeRect = timebar.get_rect()
            timeRect.center = (100,75) 
            screen.blit(timebar,(timeRect.topleft))

            if num == 1:
                headline = fonttitle.render((title),True, [84,107,131])
                headRect = headline.get_rect()
                headRect.center = (400,155)
                screen.blit(headline,(headRect.topleft))

            elif num == 2:
                headline = fonttitle.render((title),True, [84,107,131])
                headRect = headline.get_rect()
                headRect.center = (400,150)
                screen.blit(headline,(headRect.topleft))
            
            elif num == 3:
                headline = fonttitle.render((title),True, [84,107,131])
                headRect = headline.get_rect()
                headRect.center = (400,120)
                screen.blit(headline,(headRect.topleft))

                authorline = fontauthor.render((author),True, [84,107,131])
                authorRect = authorline.get_rect()
                authorRect.center = (535,158)
                #screen.blit(authorline,(authorRect.topleft))
            
            #Draw NumPieces
            if nume == 4:
                startPoint = (285, 185)
            if nume == 5:
                startPoint = (255, 185)
            if nume == 7:
                startPoint = (195, 155)
            counter = 0

            #star
            if num!=4:
                if collect_star == False:
                    screen.blit(collect_star_off,(690,40))
                elif collect_star == True:
                    screen.blit(collect_star_on,(690,40) )

                
            for np in numPieces:
                if np == 0:
                    counter += 1
                    continue
                else:
                    xy = (startPoint[0] + (counter%nume) * (NUMPIECEWIDTH + 10), startPoint[1] + (counter/nume) * (NUMPIECEWIDTH + 10))
                    screen.blit(np, xy)
                    counter += 1
            if not pressing:        
                    pygame.display.flip()
                    pygame.display.update() 

        else:            
            gameoover()

            event = pygame.event.wait()
            if event.type == QUIT:
                write_collect()
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.mixer.music.stop()
                        m==False
                        poetry = {}
                        nowa = 0
                        mode_now  = d[0]
                        bland_surface = pygame.Surface((800,600))
                        running = True
                        gameover = False
                        a=[]
                        num=0
                        if  backtocollect==True:
                            scan_collect()
                        else:
                            main()
                    elif event.key == K_c:
                            if num!=4:
                                if collect_star == False:
                                        add_collect(poemnow)
                                        collect_star = True

                                elif collect_star == True:
                                        del_collect(poemnow)
                                        collect_star = False
                    elif event.key == K_RETURN:
                        pygame.mixer.music.stop()
                        m==False
                        poetry = {}
                        nowa = 0
                        mode_now  = d[0]
                        bland_surface = pygame.Surface((800,600))
                        running = True
                        gameover = False
                        a=[]
                        num=0
                        main()

            if num!=4:
                if collect_star == False:
                    screen.blit(collect_star_off,(690,40))
                elif collect_star == True:
                    screen.blit(collect_star_on,(690,40) )
            pygame.display.flip()
            pygame.display.update() 
                
def gameoover():
        font = pygame.font.Font("qckt.ttf",45)
        string =u'恭喜你挑战成功！按回车再来一局'
        text = font.render((string),True,([0,0,0]))
        textRect = text.get_rect()
        textRect.center = (screen.get_width() / 2, 565)
        screen.blit(text, (textRect.topleft))

def getdata(poemget):
        global backtocollect
        global title
        global author
        global right
        global c
        global num
        global numa
        global nume
        global poemnow
        poetry={}
        c=[]
        backtocollect=True
        with open("allpoem.txt") as allpoem:            
            poetry[allpoem] = allpoem.readlines()
        prepared_poem = poetry[allpoem][poemget-1]
        poem_prepared = prepared_poem.split('/')
        poemnow = poemget

        title = poem_prepared[0]
        title = unicode(title,'utf-8')
        author = poem_prepared[1]
        author = unicode(author,'utf-8')                
        right = int (poem_prepared[3])
        poem = poem_prepared[2].split()

        for i in range( 0,len(poem) ):
            c.append(poem[i]);
        for i in range( 0,len(poem) ):
            c[i] = unicode(c[i],'utf-8');
        numa = len(c)+1
        if numa == 16:
                num = 1
                nume = 4
        elif numa == 20:
                num = 2
                nume = 5
        elif numa == 35:
                num = 3
                nume = 7
        game()

def poemprepared(mode_now):
        global num
        global numa
        global nume
        global c
        global poemnow
        global right
        global title
        global author
        poetry = {}
        c=[]
        randoma = random.randint(0,14)
        randomb = random.randint(0,17)
        randomc = random.randint(0,29)
        randomd = random.randint(0,34)

        if mode_now == 0:
                with open("1.txt") as one_poem:
                    poetry[1] = one_poem.readlines()
                prepared_poem = poetry[1][randoma]
                poem_prepared = prepared_poem.split('/')
                poemnow = randoma+1
        elif mode_now == 1:
                with open("2.txt") as two_poem:
                    poetry[2] = two_poem.readlines()        
                prepared_poem = poetry[2][randomb]
                poem_prepared = prepared_poem.split('/')
                poemnow = randomb +16                
        elif mode_now == 2:
                with open("3.txt") as three_poem:            
                    poetry[3] = three_poem.readlines()
                prepared_poem = poetry[3][randomc]
                poem_prepared = prepared_poem.split('/')
                poemnow = randomc +34
        elif mode_now == 3:
                with open("4.txt") as four_poem:            
                    poetry[4] = four_poem.readlines()
                prepared_poem = poetry[4][randomd]
                poem_prepared = prepared_poem.split('/')
                poemnow = randomd +64
        title = poem_prepared[0]
        title = unicode(title,'utf-8')
        author = poem_prepared[1]
        author = unicode(author,'utf-8')                
        right = int (poem_prepared[3])
        poem = poem_prepared[2].split()
        for i in range( 0,len(poem) ):
            c.append(poem[i]);
        for i in range( 0,len(poem) ):
            c[i] = unicode(c[i],'utf-8');
        numa = len(c)+1

        if numa == 16:
                num = 1
                nume = 4
        elif numa == 20:
                num = 2
                nume = 5
        elif numa == 35:
                num = 3
                nume = 7
        game()
def idiomprepared():
        global num
        global numa
        global nume
        global c
        poetry = {}
        c=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        randob = random.randint(0,9)
        right=14
        num = 4
        nume=4
        numa=16

        with open("5.txt") as five_poem:            
            poetry[5] = five_poem.readlines()
        prepared_poem = poetry[5][randob]
        poem = prepared_poem.split()
        for i in range( 0,15 ):
            c[i] = poem[i];
            c[i] = unicode(c[i],'utf-8');
        game()     

#main
def main():
    global nowa
    global poem
    global a
    global b
    global c
    global d
    global collect
    global mode_now
    global backtocollect
    backtocollect = False
    prepared_collect = {}
    if len(collect) == 0:
        with open("collectlist.txt") as readcollect:
                prepared_collect = readcollect.readlines()
        if len(prepared_collect)!=0:                
            read_collect = prepared_collect[0]
            read_collect_ = read_collect.split()
            for i in range (0,len(read_collect_)):
                collecta=int (read_collect_[i]);
                collect.append(collecta);

    num = 0
    bland_surface = pygame.Surface((800,600))
    clock = pygame.time.Clock()
    runnings = True
    while runnings:
        clock.tick(30)

        #Handle input
        event = pygame.event.wait()
        if event.type == QUIT:
            write_collect()
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                write_collect()
                pygame.quit()
                exit()
            elif event.key == K_DOWN:
                if mode_now != 5:
                    mode_now = mode_now+1
                else:
                    mode_now = 0
            elif event.key == K_UP:
                if mode_now != 0:
                    mode_now = mode_now-1
                else:
                    mode_now = 5
            elif event.key == K_F1:
                    help0()


            elif event.key == K_RETURN:
                    if mode_now < 4:
                        poemprepared(mode_now)
                    elif mode_now == 4: 
                        idiomprepared()
                    elif mode_now==5:
                        scan_collect()
                                    
        #Update
        font1 = pygame.font.Font("qckt.ttf", 55)            
        text1 = font1.render(d[mode_now], 1, BLUE)
        textRect1 = text1.get_rect()
        textRect1.center = (screen.get_width() / 2, screen.get_height() / 2)

        font2 = pygame.font.Font("yt.ttf",25)
        string2 =u'使用F1查看游戏说明哦'
        text2 = font2.render((string2),True,BLUE)
        textRect2 = text2.get_rect()
        textRect2.center = (screen.get_width() / 2, 550)

        #Draw
        screen.fill([255,255,255])
        screen.blit(text2, (textRect2.topleft))
        screen.blit(text1, (textRect1.topleft))
        pygame.display.flip()


        #start here
if __name__ == "__main__":
    main()
