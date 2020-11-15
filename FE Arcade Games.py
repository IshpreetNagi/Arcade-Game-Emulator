import pygame, time, random, sys
import math
from random import randint
from time import sleep

pygame.init()

#seting up the size and creating the screen
size = (900,900)
surface = pygame.display.set_mode(size)

font = pygame.font.SysFont('Ariel', 40, True, False)

quizgamescore = 0

#global variables for the 'GUESS IT!' game
lowerL = 0  #sets lower limit to 0
upperL = 100 #sets upper limit to 100
tries = 1   # sets number of tries to 0

#Creating the gird for the 'GUESS IT!' game
buttonArea = []
tooHigh = pygame.Rect(50,250, 130,75) #button tooHigh between (50,250) and (180, 325)
buttonArea.append(tooHigh)
gotit = pygame.Rect(200,250, 130,75) #button gotit between (200,250) and (330, 325)
buttonArea.append(gotit)
tooLow = pygame.Rect(350,250, 130,75) #button tooLow between (350,250) and (480, 325)
buttonArea.append(tooLow)

#Loading in music for all the games
quizmusic = pygame.mixer.Sound("Quiz background music.wav")
booing = pygame.mixer.Sound("Booing sound.wav")
cheering = pygame.mixer.Sound("cheering sound.wav")
gopherlosesound = pygame.mixer.Sound("gopher missed.wav")
gopherwinsound = pygame.mixer.Sound("got gopher.wav")
gopherbackgroundsound = pygame.mixer.Sound("gopher background music.wav")
gophergamewin = pygame.mixer.Sound("gopher game win.wav")
Arcademusic = pygame.mixer.Sound("Arcade Music.wav")
Game2music = pygame.mixer.Sound("Game2 music.wav")

#Loading in all the screens while setting their size
menuscreen = pygame.image.load("Ishpreet's Arcade.png")
menuscreen = pygame.transform.scale(menuscreen, (size))

quizrulesmenu = pygame.image.load("Quiz rules.png")
quizrulesmenu = pygame.transform.scale(quizrulesmenu, (size))

quizbackground = pygame.image.load("Quiz show background.jpg")
quizbackground = pygame.transform.scale(quizbackground, (size))

quizendscreen = pygame.image.load("Quiz end background.png")
quizendscreen = pygame.transform.scale(quizendscreen, (size))

game3background = pygame.image.load("Game 3 background.jpg")
game3background = pygame.transform.scale(game3background, (size))

gopher = pygame.image.load("coolgopher.png")
gopher = pygame.transform.scale(gopher, (80,80))

gopherhole = pygame.image.load("groundhole.png")
gopherhole = pygame.transform.scale(gopherhole, (300,300))

gopherrules = pygame.image.load("gopher game rules.png")
gopherrules = pygame.transform.scale(gopherrules, (size))

gopherwin = pygame.image.load("Gopher Win Screen.png")
gopherwin = pygame.transform.scale(gopherwin, (size))

gopherlose = pygame.image.load("Gopher Game Over.png")
gopherlose = pygame.transform.scale(gopherlose, (size))

#Bliting the menu screen on the screen
surface.blit(menuscreen, (0,0))
pygame.display.update()

#Overall menu code
def ArcadeMenu():
    Game2music.stop()
    gophergamewin.stop()
    booing.stop()
    cheering.stop()
    gopherlosesound.stop()
    gopherwinsound.stop()
    gopherbackgroundsound.stop()
    quizmusic.stop()
    Arcademusic.play()
    surface.blit(menuscreen, (0,0))
    left = -280
    top = 320
    width = 250
    height = 250
    pygame.display.update()
    for column in range(3):
        left += 300
        areaEllipse = pygame.Rect(left,top,width,height)
        pygame.draw.ellipse(surface, (255,0,127), areaEllipse)
        buttonsArea.append(areaEllipse)
        text = buttons[column]
        surface.blit(font.render(text, 1, (255,255,255)), (left +40, top +110))
        pygame.display.update()

    while True:
        pygame.event.pump()
        if pygame.event.peek(pygame.QUIT):
            pygame.display.quit()
        
        pygame.display.update()
        mx,my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        if b1 == 1:
            for i in range(3):
                if buttonsArea[i].collidepoint(mx, my):
                         buttonsFunc[i]()

#This blits the quiz show rules
def QuizShow():
    Arcademusic.stop()
    booing.stop()
    quizmusic.stop()
    quizmusic.play()
    surface.blit(quizrulesmenu, (0,0))
    pygame.display.update()
    time.sleep(10)
    questionone()

#This blits question 1 of the quiz show
def questionone():
    surface.blit(quizbackground, (0,0))
    pygame.display.update()
    global quizgamescore
    quiztime = 10
    quiztime2 = 500
    left = 120
    top = 200
    width = 650
    height = 50
    questionbox = pygame.Rect(left,top,width,height)
    pygame.draw.rect(surface, (255,255,255), questionbox)
    questioninbox = question1buttons[0]
    surface.blit(font.render(questioninbox, 1, (0,0,0)), (left +20, top +20))
    pygame.display.update()
    for column in range(1):
        top = 200
        left += 25
        for row in range(4):
            top += 100
            area2 = pygame.Rect([left, top, 250, 50])
            pygame.draw.rect(surface, (255,255,255), area2)
            question1Area.append(area2)
            text = answer1buttons[row]
            surface.blit(font.render(text, 1, (0,0,0)), (left , top ))
            pygame.display.update()
            time.sleep(1)

    while True:
        pygame.event.pump()
        if pygame.event.peek(pygame.QUIT):
            pygame.display.quit()
        
        pygame.display.update()
        mx,my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        quiztime -= 0.02
        quiztime2 -= 1
        font33 = pygame.font.SysFont('Ariel', 200, True, False)
        boxbehindtime = pygame.Rect(500,400,200,200)
        pygame.draw.rect(surface, (0,0,0), boxbehindtime)
        quiztimeblit = font33.render(str(round(quiztime)), True, (255,255,255))
        surface.blit(quiztimeblit, (500,420))
        pygame.display.update()
        if mx>150 and mx<150+245 and my>300 and my<300+50 and b1 == 1:
            booing.play()
            questiontwo()
        elif mx>150 and mx<150+245 and my>400 and my<400+50 and b1 == 1:
            booing.play()
            questiontwo()
        elif mx>150 and mx<150+245 and my>500 and my<500+50 and b1 == 1:
            booing.play()
            questiontwo()
        elif mx>150 and mx<150+245 and my>600 and my<600+50 and b1 == 1:
            cheering.play()
            quizgamescore += 1
            questiontwo()
        elif quiztime2 == 0:
            booing.play()
            questiontwo()
        time.sleep(0.01)
               
#This blits question 2 of the quiz show
def questiontwo():
    surface.blit(quizbackground, (0,0))
    pygame.display.update()
    global quizgamescore
    quiztime = 10
    quiztime2 = 500
    left = 120
    top = 200
    width = 650
    height = 50
    questionbox = pygame.Rect(left,top,width,height)
    pygame.draw.rect(surface, (255,255,255), questionbox)
    questioninbox = question2buttons[0]
    surface.blit(font.render(questioninbox, 1, (0,0,0)), (left +20, top +20))
    pygame.display.update()
    for column in range(1):
        top = 200
        left += 25
        for row in range(4):
            top += 100
            area2 = pygame.Rect([left, top, 250, 50])
            pygame.draw.rect(surface, (255,255,255), area2)
            question2Area.append(area2)
            text = answer2buttons[row]
            surface.blit(font.render(text, 1, (0,0,0)), (left , top ))
            pygame.display.update()
            time.sleep(1)

    while True:
        pygame.event.pump()
        if pygame.event.peek(pygame.QUIT):
            pygame.display.quit()
        
        pygame.display.update()
        mx,my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        quiztime -= 0.02
        quiztime2 -= 1
        font33 = pygame.font.SysFont('Ariel', 200, True, False)
        boxbehindtime = pygame.Rect(500,400,200,200)
        pygame.draw.rect(surface, (0,0,0), boxbehindtime)
        quiztimeblit = font33.render(str(round(quiztime)), True, (255,255,255))
        surface.blit(quiztimeblit, (500,420))
        pygame.display.update()
        if mx>150 and mx<150+245 and my>300 and my<300+50 and b1 == 1:
            booing.play()
            questionthree()
        elif mx>150 and mx<150+245 and my>400 and my<400+50 and b1 == 1:
            cheering.play()
            quizgamescore += 1
            questionthree()
        elif mx>150 and mx<150+245 and my>500 and my<500+50 and b1 == 1:
            booing.play()
            questionthree()
        elif mx>150 and mx<150+245 and my>600 and my<600+50 and b1 == 1:
            booing.play()
            questionthree()
        elif quiztime2 == 0:
            booing.play()
            questionthree()
        time.sleep(0.01)
               
#This blits question 3 of the quiz show
def questionthree():
    surface.blit(quizbackground, (0,0))
    pygame.display.update()
    global quizgamescore
    quiztime = 10
    quiztime2 = 500
    left = 120
    top = 200
    width = 650
    height = 50
    questionbox = pygame.Rect(left,top,width,height)
    pygame.draw.rect(surface, (255,255,255), questionbox)
    questioninbox = question3buttons[0]
    surface.blit(font.render(questioninbox, 1, (0,0,0)), (left +20, top +20))
    pygame.display.update()
    for column in range(1):
        top = 200
        left += 25
        for row in range(4):
            top += 100
            area2 = pygame.Rect([left, top, 250, 50])
            pygame.draw.rect(surface, (255,255,255), area2)
            question3Area.append(area2)
            text = answer3buttons[row]
            surface.blit(font.render(text, 1, (0,0,0)), (left , top ))
            pygame.display.update()
            time.sleep(1)

    while True:
        pygame.event.pump()
        if pygame.event.peek(pygame.QUIT):
            pygame.display.quit()
        
        pygame.display.update()
        mx,my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        quiztime -= 0.02
        quiztime2 -= 1
        font33 = pygame.font.SysFont('Ariel', 200, True, False)
        boxbehindtime = pygame.Rect(500,400,200,200)
        pygame.draw.rect(surface, (0,0,0), boxbehindtime)
        quiztimeblit = font33.render(str(round(quiztime)), True, (255,255,255))
        surface.blit(quiztimeblit, (500,420))
        pygame.display.update()
        if mx>150 and mx<150+245 and my>300 and my<300+50 and b1 == 1:
            booing.play()
            questionfour()
        elif mx>150 and mx<150+245 and my>400 and my<400+50 and b1 == 1:
            booing.play()
            questionfour()
        elif mx>150 and mx<150+245 and my>500 and my<500+50 and b1 == 1:
            cheering.play()
            quizgamescore += 1
            questionfour()
        elif mx>150 and mx<150+245 and my>600 and my<600+50 and b1 == 1:
            booing.play()
            questionfour()
        elif quiztime2 == 0:
            booing.play()
            questionfour()
        time.sleep(0.01)
                
#This blits question 4 of the quiz show
def questionfour():
    surface.blit(quizbackground, (0,0))
    pygame.display.update()
    global quizgamescore
    quiztime = 10
    quiztime2 = 500
    left = 120
    top = 200
    width = 650
    height = 50
    questionbox = pygame.Rect(left,top,width,height)
    pygame.draw.rect(surface, (255,255,255), questionbox)
    questioninbox = question4buttons[0]
    surface.blit(font.render(questioninbox, 1, (0,0,0)), (left +20, top +20))
    pygame.display.update()
    for column in range(1):
        top = 200
        left += 25
        for row in range(4):
            top += 100
            area2 = pygame.Rect([left, top, 250, 50])
            pygame.draw.rect(surface, (255,255,255), area2)
            question4Area.append(area2)
            text = answer4buttons[row]
            surface.blit(font.render(text, 1, (0,0,0)), (left , top ))
            pygame.display.update()
            time.sleep(1)

    while True:
        pygame.event.pump()
        if pygame.event.peek(pygame.QUIT):
            pygame.display.quit()
        
        pygame.display.update()
        mx,my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        quiztime -= 0.02
        quiztime2 -= 1
        font33 = pygame.font.SysFont('Ariel', 200, True, False)
        boxbehindtime = pygame.Rect(500,400,200,200)
        pygame.draw.rect(surface, (0,0,0), boxbehindtime)
        quiztimeblit = font33.render(str(round(quiztime)), True, (255,255,255))
        surface.blit(quiztimeblit, (500,420))
        pygame.display.update()
        if mx>150 and mx<150+245 and my>300 and my<300+50 and b1 == 1:
            booing.play()
            questionfive()
        elif mx>150 and mx<150+245 and my>400 and my<400+50 and b1 == 1:
            booing.play()
            questionfive()
        elif mx>150 and mx<150+245 and my>500 and my<500+50 and b1 == 1:
            booing.play()
            questionfive()
        elif mx>150 and mx<150+245 and my>600 and my<600+50 and b1 == 1:
            cheering.play()
            quizgamescore += 1
            questionfive()
        elif quiztime2 == 0:
            booing.play()
            questionfive()
        time.sleep(0.01)
                
#This blits question 5 of the quiz show
def questionfive():
    surface.blit(quizbackground, (0,0))
    pygame.display.update()
    global quizgamescore
    quiztime = 10
    quiztime2 = 500
    left = 120
    top = 200
    width = 650
    height = 50
    questionbox = pygame.Rect(left,top,width,height)
    pygame.draw.rect(surface, (255,255,255), questionbox)
    questioninbox = question5buttons[0]
    surface.blit(font.render(questioninbox, 1, (0,0,0)), (left +20, top +20))
    pygame.display.update()
    for column in range(1):
        top = 200
        left += 25
        for row in range(4):
            top += 100
            area2 = pygame.Rect([left, top, 250, 50])
            pygame.draw.rect(surface, (255,255,255), area2)
            question5Area.append(area2)
            text = answer5buttons[row]
            surface.blit(font.render(text, 1, (0,0,0)), (left , top ))
            pygame.display.update()
            time.sleep(1)

    while True:
        pygame.event.pump()
        if pygame.event.peek(pygame.QUIT):
            pygame.display.quit()
        
        pygame.display.update()
        mx,my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        quiztime -= 0.02
        quiztime2 -= 1
        font33 = pygame.font.SysFont('Ariel', 200, True, False)
        boxbehindtime = pygame.Rect(500,400,200,200)
        pygame.draw.rect(surface, (0,0,0), boxbehindtime)
        quiztimeblit = font33.render(str(round(quiztime)), True, (255,255,255))
        surface.blit(quiztimeblit, (500,420))
        pygame.display.update()
        if mx>150 and mx<150+245 and my>300 and my<300+50 and b1 == 1:
            cheering.play()
            quizgamescore += 1
            questionsix()
        elif mx>150 and mx<150+245 and my>400 and my<400+50 and b1 == 1:
            booing.play()
            questionsix()
        elif mx>150 and mx<150+245 and my>500 and my<500+50 and b1 == 1:
            booing.play()
            questionsix()
        elif mx>150 and mx<150+245 and my>600 and my<600+50 and b1 == 1:
            booing.play()
            questionsix()
        elif quiztime2 == 0:
            booing.play()
            questionsix()
        time.sleep(0.01)
               
#This blits question 6 of the quiz show
def questionsix():
    surface.blit(quizbackground, (0,0))
    pygame.display.update()
    global quizgamescore
    quiztime = 10
    quiztime2 = 500
    left = 120
    top = 200
    width = 650
    height = 50
    questionbox = pygame.Rect(left,top,width,height)
    pygame.draw.rect(surface, (255,255,255), questionbox)
    questioninbox = question6buttons[0]
    surface.blit(font.render(questioninbox, 1, (0,0,0)), (left +20, top +20))
    pygame.display.update()
    for column in range(1):
        top = 200
        left += 25
        for row in range(4):
            top += 100
            area2 = pygame.Rect([left, top, 250, 50])
            pygame.draw.rect(surface, (255,255,255), area2)
            question6Area.append(area2)
            text = answer6buttons[row]
            surface.blit(font.render(text, 1, (0,0,0)), (left , top ))
            pygame.display.update()
            time.sleep(1)

    while True:
        pygame.event.pump()
        if pygame.event.peek(pygame.QUIT):
            pygame.display.quit()
        
        pygame.display.update()
        mx,my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        quiztime -= 0.02
        quiztime2 -= 1
        font33 = pygame.font.SysFont('Ariel', 200, True, False)
        boxbehindtime = pygame.Rect(500,400,200,200)
        pygame.draw.rect(surface, (0,0,0), boxbehindtime)
        quiztimeblit = font33.render(str(round(quiztime)), True, (255,255,255))
        surface.blit(quiztimeblit, (500,420))
        pygame.display.update()
        if mx>150 and mx<150+245 and my>300 and my<300+50 and b1 == 1:
            cheering.play()
            quizgamescore += 1
            QuizEndMenu()
        elif mx>150 and mx<150+245 and my>400 and my<400+50 and b1 == 1:
            booing.play()
            QuizEndMenu()
        elif mx>150 and mx<150+245 and my>500 and my<500+50 and b1 == 1:
            cheering.play()
            quizgamescore += 1
            QuizEndMenu()
        elif mx>150 and mx<150+245 and my>600 and my<600+50 and b1 == 1:
            cheering.play()
            quizgamescore += 1
            QuizEndMenu()
        elif quiztime2 == 0:
            booing.play()
            QuizEndMenu()
        time.sleep(0.01)

#This blits the rules menu for game 2 and gives the player the intsruction to think of a number
def Game2():
    Game2music.stop()
    Arcademusic.stop()
    Game2music.play()
    global number
    global lowerL
    global upperL
    global tries
    surface.fill((255,255,255)) #starts with white screen

    surface.blit(font.render("Think of a number from 1 to 100",True, (0,0,0)),(10,200))#user instruction

    pygame.display.update() #updates the first screen on the window
    time.sleep(3)
    
    surface.fill((66,244,223)) # colours screen turquoise
    number = randint (lowerL,upperL) #generates a random number from low to high
    text = "Is "+ str(number) +" your number?" #creates the string with the number guess
    numberBlit = font.render(text,True,(0,0,0)) #creates the font object with the string above
    surface.blit(numberBlit, (50,100))  #blits the number on screen
    showButtons() #calls on showButtons function to blit all 3 buttons

    while True:  #infinite loop
        pygame.event.pump() #listens to all user events
        mx,my = pygame.mouse.get_pos() #gets mouse position
        b,b1,b2 = pygame.mouse.get_pressed() #gets mouse poressed activity
        if b==1 and buttonArea[0].collidepoint(mx,my):
            upperL = number - 1
            tries += 1
            try_again(lowerL, upperL)
            sleep(0.5)
        elif b == 1 and buttonArea[1].collidepoint(mx,my):
            guessed(tries)
            break
        elif b == 1 and buttonArea[2].collidepoint(mx,my):
            lowerL = number + 1
            tries += 1
            try_again(lowerL, upperL)
            sleep(0.5)

#This is the code for the lower and upper buttons that create the new number that the game tries to guess
def try_again(lower,upper):
    global number
    global lowerL
    global upperL
    global tries
    
    print(lower,upper)
    number = randint(lower,upper)
    surface.fill((255,51,255))
    yatext = "YO! This... " + str(number) + " your number?"
    numberBlit = font.render(yatext,True,(255,255,255))
    surface.blit(numberBlit, (125,125))
    showButtons()
    pygame.display.update()

#This is the screen that appers when you tell the game that the number it has guessed is in fact the player's number, and this code blits the number of tries it took the game to gues the number
def guessed(count):
    winning = "DAMN! IT TOOK ME " + str(tries) + " attempt[s] to get your number!"
    winningblit = font.render(winning,True,(0,0,0))
    surface.fill((0,204,0))
    surface.blit(winningblit, (5,160))
    pygame.display.update()
    left = -170
    top = 660
    width = 200
    height = 200
    for column in range(2):
        left += 350
        areaEllipse2 = pygame.Rect(left, top, width, height)
        pygame.draw.ellipse(surface, (255,0,127), areaEllipse2)
        endArea.append(areaEllipse2)
        text = endbuttons[column]
        surface.blit(font.render(text, 1, (255,255,255)), (left +20, top +80))
        pygame.display.update()

    while True:
        pygame.event.pump()
        if pygame.event.peek(pygame.QUIT):
            pygame.display.quit()
        
        pygame.display.update()
        mx,my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        if b1 == 1:
            for i in range(2):
                if endArea[i].collidepoint(mx, my):
                         end2Func[i]()

#This code actually creates the buttons the player clicks in game 2
def showButtons():
    #takes no parameters
    #returns nothing
    #simply draws the same 3 buttons and their text labels on the same locations on screen
    pygame.draw.ellipse(surface,(50,50,50),tooHigh) #draws an ellipse over the button Rect area
    surface.blit(font.render("too high!", True,(255,255,255)),(63,270)) # puts too high text on it
    pygame.draw.ellipse(surface,(50,50,50),gotit)
    surface.blit(font.render("   yes!", True,(255,255,255)),(213,270))
    pygame.draw.ellipse(surface,(50,50,50),tooLow)
    surface.blit(font.render("too low!", True,(255,255,255)),(363,270))
    pygame.display.update()

#This is the end menu of the quiz, where it tells the player their score and gives them the option to play again or play another game
def QuizEndMenu():
    surface.blit(quizendscreen, (0,0))
    font23 = pygame.font.SysFont('Ariel', 200, True, False)
    gamescore = font23.render(str(quizgamescore), True, (0,0,0))
    surface.blit(gamescore, (300,490))
    pygame.display.update()
    left = -170
    top = 660
    width = 200
    height = 200
    for column in range(2):
        left += 350
        areaEllipse2 = pygame.Rect(left, top, width, height)
        pygame.draw.ellipse(surface, (255,0,127), areaEllipse2)
        endArea.append(areaEllipse2)
        text = endbuttons[column]
        surface.blit(font.render(text, 1, (255,255,255)), (left +20, top +80))
        pygame.display.update()

    while True:
        pygame.event.pump()
        if pygame.event.peek(pygame.QUIT):
            pygame.display.quit()
        
        pygame.display.update()
        mx,my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        if b1 == 1:
            for i in range(2):
                if endArea[i].collidepoint(mx, my):
                         endFunc[i]()

#This display's the rules of the gopher game on the screen
def GopherRules():
    Arcademusic.stop()
    surface.blit(gopherrules, (0,0))
    area2 = pygame.Rect(380, 720, 170, 170)
    pygame.draw.ellipse(surface, (0,204,0), area2)
    surface.blit(font.render('START', 1, (0,0,0)), (410, 790))
    pygame.display.update()

    while True:
        pygame.event.pump()
        if pygame.event.peek(pygame.QUIT):
            pygame.display.quit()
        
        pygame.display.update()
        mx,my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        if mx>380 and mx<380+170 and my>720 and my<720+160 and b1 == 1:
            GopherHunt1()

#This creates the holes that apper on the screen and blits the gopher in a random spot on the holes
def GopherHunt1():
    gophergamewin.stop()
    gopherlosesound.stop()
    gopherbackgroundsound.stop()
    gopherbackgroundsound.play()
    surface.blit(game3background, (0,0))
    pygame.display.update()
    gophertime = 1
    gophertime2 = 50
    n = 5
    m = 5
    for n in range(1):
        top = -240
        left = 310
        for m in range(4):
            top += 220
            cell = pygame.Rect([left,top,100,100])
            surface.blit(gopherhole, (left,top))
            grid.append(cell)
            pygame.display.update()
            time.sleep(0.4)

    x = random.randint(400, 460)
    y = random.randint(50,800)
    surface.blit(gopher, (x,y))

    while True:
        pygame.event.pump()
        if pygame.event.peek(pygame.QUIT):
            pygame.display.quit()
        
        pygame.display.update()
        mx,my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        gophertime -= 0.02
        gophertime2 -= 1
        pygame.display.update()
        if mx>x and mx<x+70 and my>y and my<y+75 and b1 == 1:
            gopherwinsound.play()
            GopherHunt2()
        elif gophertime2 == 0:
            gopherlosesound.play()
            gopherLoseScreen()
        time.sleep(0.01)

#This blits the gopher in another spot on the holes when the gopher is clicked
def GopherHunt2():
    surface.blit(game3background, (0,0))
    pygame.display.update()
    gophtime = 1
    gophtime2 = 50
    n = 5
    m = 5
    for n in range(1):
        top = -240
        left = 310
        for m in range(4):
            top += 220
            cell = pygame.Rect([left,top,100,100])
            surface.blit(gopherhole, (left,top))
            grid2.append(cell)
            pygame.display.update()

    x = random.randint(400, 460)
    y = random.randint(50,800)
    surface.blit(gopher, (x,y))

    while True:
        pygame.event.pump()
        if pygame.event.peek(pygame.QUIT):
            pygame.display.quit()
        
        pygame.display.update()
        mx,my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        gophtime -= 0.02
        gophtime2 -= 1
        pygame.display.update()
        if mx>x and mx<x+70 and my>y and my<y+75 and b1 == 1:
            gopherwinsound.play()
            GopherHunt3()
        elif gophtime2 == 0:
            gopherlosesound.play()
            gopherLoseScreen()
        time.sleep(0.01)

#This code blits the code in the third spot after the gopher has been clicked from the last piece of code
def GopherHunt3():
    surface.blit(game3background, (0,0))
    pygame.display.update()
    gotime = 1
    gotime2 = 50
    n = 5
    m = 5
    for n in range(1):
        top = -240
        left = 310
        for m in range(4):
            top += 220
            cell = pygame.Rect([left,top,100,100])
            surface.blit(gopherhole, (left,top))
            grid3.append(cell)
            pygame.display.update()

    x = random.randint(400, 460)
    y = random.randint(50,800)
    surface.blit(gopher, (x,y))

    while True:
        pygame.event.pump()
        if pygame.event.peek(pygame.QUIT):
            pygame.display.quit()
        
        pygame.display.update()
        mx,my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        gotime -= 0.02
        gotime2 -= 1
        pygame.display.update()
        if mx>x and mx<x+70 and my>y and my<y+75 and b1 == 1:
            gophergamewin.play()
            gopherWinScreen()
        elif gotime2 == 0:
            gopherlosesound.play()
            gopherLoseScreen()
        time.sleep(0.01)

#This blits the 'winner' end screen of the gopher game once the player has caught the gopher three times, this screen also gives the player an option to play again or play another game
def gopherWinScreen():
    surface.blit(gopherwin, (0,0))
    pygame.display.update()
    left = -200
    top = 600
    width = 250
    height = 250
    for column in range(2):
        left += 350
        areaEllipse3 = pygame.Rect(left, top, width, height)
        pygame.draw.ellipse(surface, (255,0,127), areaEllipse3)
        gopherArea.append(areaEllipse3)
        text = gopherbuttons[column]
        surface.blit(font.render(text, 1, (255,255,255)), (left +30, top +110))
        pygame.display.update()

    while True:
        pygame.event.pump()
        if pygame.event.peek(pygame.QUIT):
            pygame.display.quit()
        
        pygame.display.update()
        mx,my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        if b1 == 1:
            for i in range(2):
                if gopherArea[i].collidepoint(mx, my):
                         gopherFunc[i]()

#This blits the 'loser' screen when the player is unable in their efforts to catch the gopher, this screen also gives the player an option to play again or play another game
def gopherLoseScreen():
    surface.blit(gopherlose, (0,0))
    pygame.display.update()
    left = -200
    top = 600
    width = 250
    height = 250
    for column in range(2):
        left += 350
        areaEllipse3 = pygame.Rect(left, top, width, height)
        pygame.draw.ellipse(surface, (255,0,127), areaEllipse3)
        gopherArea.append(areaEllipse3)
        text = gopherbuttons[column]
        surface.blit(font.render(text, 1, (255,255,255)), (left +30, top +110))
        pygame.display.update()

    while True:
        pygame.event.pump()
        if pygame.event.peek(pygame.QUIT):
            pygame.display.quit()
        
        pygame.display.update()
        mx,my = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        if b1 == 1:
            for i in range(2):
                if gopherArea[i].collidepoint(mx, my):
                         gopherFunc[i]()
    
#These are all my lists that I use for my gopher game, game 2, and quiz game
buttons = ["QUIZ-SHOW", "GUESS IT!", "GOPHERS"]
buttonsFunc = [QuizShow, Game2, GopherRules]
buttonsArea = []

endbuttons = ['Main Menu', 'Play Again']
endFunc = [ArcadeMenu, questionone]
end2Func = [ArcadeMenu, Game2]
endArea = []

grid = []
grid2 = []
grid3 = []

gopherbuttons = ["Main Menu", "Play Again"]
gopherFunc = [ArcadeMenu, GopherHunt1]
gopherArea = []

question1buttons = ["What is the name of Batman's sidekick?"]
answer1buttons = ['Superman', 'Wonder Women', 'Flash', 'Robin']
question1Area = []

question2buttons = ["What city does Batman protect?"]
answer2buttons = ['New York', 'Gotham City', 'Washington', 'Toronto']
question2Area = []

question3buttons = ["What is Batman's real name?"]
answer3buttons = ['Clark Kent', 'Tom Hardy', 'Bruce Wayne', 'Bruce Willis']
question3Area = []

question4buttons = ["What is the name of Batman's car?"]
answer4buttons = ['Ratmobile', 'Catcar', 'Batcar', 'Batmobile']
question4Area = []

question5buttons = ["Who is Batman's Butler?"]
answer5buttons = ['Alfred', 'Nightwing', 'Jim Gordon', 'Iron Man']
question5Area = []

question6buttons = ["Can Batman fly?"]
answer6buttons = ['IDK', 'DUH, HE A BAT', 'END ALREADY!', 'No']
question6Area = []

#This calls on the ArcadeMenu def menu and activites the game itself
ArcadeMenu()
