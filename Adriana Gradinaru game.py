from pygame import *
init()
 
import random
from random import *

 
 
size = width, height = 1000, 700
screen = display.set_mode(size)

#colours
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GRAY = (160,160,160)
DARK_GRAY = (60,60,60)
BLUE = (0,0,255)
RED = (216, 73, 101)
 
 
#main menu function, and the main function (all / most of the other functions conect back to this one)
def drawScreen(screen, button):
    global main_menu, sign_up, log_in, exist, hi, start_game, game, colour1, colour2, colour3, colour4, end, user, pwd, collect, paused, charColourB, charColourG, char, runner1, runner2, instr
    
    
       
    running = True
    # Main menu:
    if main_menu == True:
        
        runner1 = runnerG1
        runner2 = runnerG2          
        
        charColourB = GRAY
        charColourG = GREEN
        user = ""
        pwd = ""
    
        draw.rect(screen, WHITE, (0, 0, 1000, 700))
        
        # Tittle
        Ariel100 = font.SysFont("Ariel", 100)
        text = Ariel100.render(("Main Menu"), 1, BLACK)
        screen.blit(text, Rect(310, 50, 100, 100))
       
        Ariel = font.SysFont("Ariel", 70)
        
       # sign up button
        signUpRect = Rect(200, 150, 600, 100)
        draw.rect(screen, colour1, signUpRect)
        text = Ariel.render(("Make an account"), 1, WHITE)
        screen.blit(text, Rect(295, 175, 100, 100))
       
       # Log in to an old account button
        logInRect = Rect(200, 300, 600, 100)
        draw.rect(screen, colour2, logInRect)
        text = Ariel.render(("Log in"), 1, WHITE)
        screen.blit(text, Rect(405, 325, 100, 100))
        
       # Enter as a Guest button
        guestRect = Rect(200, 450, 600, 100)
        draw.rect(screen, colour3, guestRect)
        text = Ariel.render(("Guest"), 1, WHITE)
        screen.blit(text, Rect(405, 475, 100, 100))        
        
       # Leave the game button 
        exitGameRect = Rect(200, 600, 600, 100)
        draw.rect(screen, colour4, exitGameRect)
        text = Ariel.render(("Exit Game"), 1, WHITE)
        screen.blit(text, Rect(375, 625, 100, 100))
        
        screen.blit(screen2, Rect(-40,-50,0,100)) 
           
        
        screen.blit(screen1, Rect(-50,-50,0,100))
        

        
        #flashing colours
        if signUpRect.collidepoint(mx, my) == True:
            colour1 = DARK_GRAY
            colour2 = BLACK
            colour3 = BLACK
            colour4 = BLACK
           
        elif logInRect.collidepoint(mx, my) == True:
            colour2 = DARK_GRAY
            colour1 = BLACK
            colour3 = BLACK
            colour4 = BLACK
            
        elif guestRect.collidepoint(mx, my) == True: 
            colour3 = DARK_GRAY
            colour2 = BLACK
            colour1 = BLACK
            colour4 = BLACK            
            
        elif exitGameRect.collidepoint(mx, my) == True:        
            colour4 = DARK_GRAY
            colour2 = BLACK
            colour3 = BLACK
            colour1 = BLACK  
        
        else:
            colour1 = BLACK
            colour2 = BLACK
            colour3 = BLACK
            colour4 = BLACK            
        
        if button == 1 and evnt.type != MOUSEMOTION:
            #To make a new account
            if signUpRect.collidepoint(mx, my) == True:
                sign_up = True
                main_menu = False
                button = 0
                
            #To enter an account
            elif logInRect.collidepoint(mx, my) == True:
                log_in = True
                main_menu = False
                button = 0
                
            #To to enter as a guest
            elif guestRect.collidepoint(mx, my) == True: 
                start_game = True 
                
            # running is made false so that it brakes out of the game loop and leaves the program   
            elif exitGameRect.collidepoint(mx, my) == True:
                running = False
                main_menu = False

    #Linking other function in to this one
    if sign_up == True:
        exist = ""
        sign(button)
        
    elif log_in == True:
        exist = ""
        log(button)
    
    elif start_game == True :
        sign_up = False
        log_in = False        
        startGame(button)
        
    elif char == True :       
        character(button)
    
    elif instr == True :       
        Instructions(button)    
            
    elif game == True :
        Game(button)
        
    elif paused == True:
        pause(button)          
        
    
    if end == True:
        End(button)
        
    elif collect == True:
        collection(button)
        
    
    display.flip()
    return running

# Text box function
def textBox(screen, form):
    global user, pwd
    #to figure out if it's for the user or pwd
    if form == "user":
        W = 200
        L = 200
        w = 600
        l = 100
             
    elif form == "pwd":
        W = 200
        L = 410
        w = 600
        l = 100 
        
    #font / size
    font1 = font.Font(None, 50)
    #box location
    inputBoxRect = Rect(W, L, w, l)
    #colour of box (on line I found a nice colour)
    color= Color('dodgerblue2')
    active = True
    text = ''
    done = False

    while not done:
        if active == False:
            break
        
        for evnt in event.get():
            if evnt.type == QUIT:
                done = True
            if evnt.type == MOUSEBUTTONDOWN:
                # If the user clicked on the inputBoxRect rect.
                if inputBoxRect.collidepoint(evnt.pos):
                    # Toggle the active variable.
                    active = True
                else:
                    active = False
                    break
            if evnt.type == KEYDOWN:
                if active:
                    if evnt.key == K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += evnt.unicode
                         
            if form == "user":
                user = text
                
            elif form == "pwd":
                pwd = text                    
                      
                   

        draw.rect(screen, (0, 0, 0), inputBoxRect)
        
        # Render the current text
        txt_surface = font1.render(text, True, color)
        
        inputBoxRect.w = w
        
        # put the text together
        screen.blit(txt_surface, (inputBoxRect.x+5, inputBoxRect.y+25))
        
        # inputBox rect.
        draw.rect(screen, color, inputBoxRect, 2)
        
        display.flip()

#to add a user   
def addUser(user, pwd):
    userFile = open("GRADuser_info.dat", "a")
    userFile.write(user + "," + pwd + "\n")
    userFile.close()
    
#to check if the username is already taken   
def userExists(user):
    userFile = open("GRADuser_info.dat", "r")
    
    while True:
        text = userFile.readline()
        #rstrip removes the newline character read at the end of the line
        text = text.rstrip("\n")     
        if text == "": 
            break
        record = text.split(",")
        if record[0] == user:
            return True                 # if true, user is already taken and can not be used
    return False          #if False, username dose not exist and is avalible to be used


# to find to user when they log in
def userFind(user, pwd):
    userFile = open("GRADuser_info.dat", "r")
    
    while True:
        text = userFile.readline()
        #rstrip removes the newline character read at the end of the line
        text = text.rstrip("\n")     
        if text == "": 
            break
        record = text.split(",")
        if record[0] == user and record[1] == pwd:
            return True                          # if true, user is real and can be used
    return False                #if False, user dose not exist

# when a new user is made, a new stat for the user is also made
def addStat(user):
    userFile = open("GRADuser_stats.dat", "a")
    apple = 0
    banana = 0
    can = 0
    juce_box = 0
    cell = 0
    Ipad = 0
    comp = 0    
    
    userFile.write(user + "," + str(apple)+ "," + str(banana) + "," + str(can) + "," + str(juce_box) + "," + str(cell)+ "," + str(Ipad) + "," + str(comp) +"\n")
    userFile.close()
     

# after a solo game is played the resalts of the game would afect their stats   
def changeStat():
    global solo_score, saved, apple, banana, can, juce_box, cell, Ipad, comp, user, newApple, newBanana, newCan, newBox, newCell, newIpad, newComp, user
    statFile = open("GRADuser_stats.dat", "r")
    
    user_list = []
    apple_list= []
    banana_list = []
    can_list = []
    juce_box_list = []
    cell_list= []
    Ipad_list = []
    comp_list = []    
    count = -1
    elem = -1
    
    
    while True:
        count += 1
        text = statFile.readline()
        text = text.rstrip("\n")
        
        if text=="":
            break
        
        record = text.split(",")
        user_list.append(record[0])
        apple_list.append(record[1])
        banana_list.append(record[2])
        can_list.append(record[3])
        juce_box_list.append(record[4])
        cell_list.append(record[5])
        Ipad_list.append(record[6])
        comp_list.append(record[7])          
        
        if user == record[0]:
            elem = count
        
    statFile.close()
    statFile = open ("GRADuser_stats.dat", "w")
    
    #Change value of each Item
    apple_list[elem] = apple + int(apple_list[elem])
    newApple = apple_list[elem]
    
    banana_list[elem] = banana + int(banana_list[elem])
    newBanana = banana_list[elem] 
    
    can_list[elem] = can + int(can_list[elem])
    newCan = can_list[elem]
    
    juce_box_list[elem] = juce_box + int(juce_box_list[elem])
    newBox = juce_box_list[elem]  
    
    cell_list[elem] = cell + int(cell_list[elem])
    newCell = cell_list[elem]
    
    Ipad_list[elem] = Ipad + int(Ipad_list[elem])
    newIpad = Ipad_list[elem]
    
    comp_list[elem] = comp + int(comp_list[elem])
    newComp = comp_list[elem]
    
    
    #Re-writing
    for i in range(0, len(user_list)):
        statFile.write(str(user_list[i])+ "," + str(apple_list[i]) + "," + str(banana_list[i]) + "," + str(can_list[i]) + "," + str(juce_box_list[i]) + "," + str(cell_list[i])+ "," + str(Ipad_list[i]) + "," + str(comp_list[i]) + "\n")
        
    statFile.close()     
    
    solo_score = True
    saved = True

def openStat(): #to view the values of every Item
    global newApple, newBanana, newCan, newBox, newCell, newIpad, newComp, user
    statFile = open("GRADuser_stats.dat", "r")
    
    user_list = []
    apple_list= []
    banana_list = []
    can_list = []
    juce_box_list = []
    cell_list= []
    Ipad_list = []
    comp_list = []     
    count = -1
    elem = -1
    
    
    while True:
        count += 1
        text = statFile.readline()
        text = text.rstrip("\n")
        
        if text=="":
            break
        
        record = text.split(",")
        user_list.append(record[0])
        apple_list.append(record[1])
        banana_list.append(record[2])
        can_list.append(record[3])
        juce_box_list.append(record[4])
        cell_list.append(record[5])
        Ipad_list.append(record[6])
        comp_list.append(record[7])        
        
        if user == record[0]:
            elem = count
    
    newApple = apple_list[elem]
    newBanana = banana_list[elem] 
    newCan = can_list[elem]     
    newBox = juce_box_list[elem] 
    newCell = cell_list[elem]
    newIpad = Ipad_list[elem] 
    newComp = comp_list[elem]       
    
    
    statFile.close()     


#This functionis made for peaple to sign up 
def sign(button):
    global main_menu, sign_up, exist, user, pwd, hi, playing_acount, start_game

        
    draw.rect(screen, WHITE, (0, 0, 1000, 700)) 

    Ariel = font.SysFont("Ariel", 70)
   
    Ariel100 = font.SysFont("Ariel", 100)
    text = Ariel100.render(("Create an account"), 1, BLACK)
    screen.blit(text, Rect(230, 40, 100, 100))   
    
    #username box
    userNameRect = Rect(200, 200, 600, 100)
    draw.rect(screen, BLACK, userNameRect)
    text = Ariel.render((user), 1, WHITE)
    screen.blit(text, Rect(220, 220, 600, 100))        
    text = Ariel.render(("User name:"), 1, BLACK)
    screen.blit(text, Rect(370, 135, 100, 100))
    
    #password box
    pwdsRect = Rect(200, 410, 600, 100)
    draw.rect(screen, BLACK, pwdsRect) 
    text = Ariel.render((pwd), 1, WHITE)
    screen.blit(text, Rect(220, 430, 600, 100))           
    text = Ariel.render(("Password:"), 1, BLACK)
    screen.blit(text, Rect(380, 350, 100, 100))   
    
    #enter user button
    enterRect = Rect(340, 525, 300, 100)
    draw.rect(screen, GREEN, enterRect)
    text = Ariel.render(("Enter"), 1, BLACK)
    screen.blit(text, Rect(425, 550, 100, 100)) 
    
    #go bake to main menu
    backRect = Rect(50, 615, 200, 75)
    draw.rect(screen, WHITE, backRect)
    text = Ariel.render(("Back"), 1, BLACK)
    screen.blit(text, Rect(75, 625, 100, 200))         
       
    text = Ariel.render((exist), 1, BLACK)
    screen.blit(text, Rect(0, 0, 100, 100))
    
    screen.blit(screen1, Rect(-50,-50,0,100))
    
    display.flip()
    #to press all the buttons and textboxes
    if button == 1:
        if userNameRect.collidepoint(mx, my) == True:
            textBox(screen, "user")                         #makes the username text box        
            
        if pwdsRect.collidepoint(mx, my) == True:
            textBox(screen, "pwd")                          #makes the pwd text box     
            
        if backRect.collidepoint(mx, my) == True:
            sign_up = False
            main_menu = True
            #drawScreen(screen, button) 
            
        if enterRect.collidepoint(mx, my) == True:
                            
            if user[0] == " ":
                exist = "The user name can't start with a space"
                           
            elif userExists (user):
                exist = "The user name is already taken, please try again."
               
            elif not userExists (user):
                addUser(user, pwd)
                addStat(user)
                playing_acount = True                
                sign_up = False
                start_game = True
                
# this function is very simular to sign (so im not going to coment as much in this one)
def log(button):
    global main_menu, log_in, exist, user, pwd, hi, inval, playing_acount, start_game
   
    if log_in == True:
        
        draw.rect(screen, WHITE, (0, 0, 1000, 700))
        
        Ariel = font.SysFont("Ariel", 70)
       
        Ariel100 = font.SysFont("Ariel", 100)
        text = Ariel100.render(("Log in"), 1, BLACK)
        screen.blit(text, Rect(400, 40, 100, 110))   
        
        userNameRect = Rect(200, 200, 600, 100)
        draw.rect(screen, BLACK, userNameRect)
        text = Ariel.render((user), 1, WHITE)
        screen.blit(text, Rect(220, 220, 600, 100))        
        text = Ariel.render(("User name:"), 1, BLACK)
        screen.blit(text, Rect(370, 135, 100, 100))
        
        pwdsRect = Rect(200, 410, 600, 100)
        draw.rect(screen, BLACK, pwdsRect) 
        text = Ariel.render((pwd), 1, WHITE)
        screen.blit(text, Rect(220, 430, 600, 100))           
        text = Ariel.render(("Password:"), 1, BLACK)
        screen.blit(text, Rect(380, 350, 100, 100)) 
        
        enterRect = Rect(340, 525, 300, 100)
        draw.rect(screen, GREEN, enterRect)
        text = Ariel.render(("Enter"), 1, BLACK)
        screen.blit(text, Rect(425, 550, 100, 100))
        
        backRect = Rect(50, 615, 200, 75)
        draw.rect(screen, WHITE, backRect)
        text = Ariel.render(("Back"), 1, BLACK)
        screen.blit(text, Rect(75, 625, 100, 200))         
        
        text = Ariel.render((inval), 1, BLACK)
        screen.blit(text, Rect(0, 0, 100, 100))        
        
        screen.blit(screen1, Rect(-50,-50,0,100))
        
        if button == 1:
            if userNameRect.collidepoint(mx, my) == True:
                textBox(screen, "user")
                
            if pwdsRect.collidepoint(mx, my) == True:
                textBox(screen, "pwd")
                
            if backRect.collidepoint(mx, my) == True:
                log_in = False
                main_menu = True
                drawScreen(screen, button)     
               
            if enterRect.collidepoint(mx, my) == True:             
                if userFind (user, pwd):
                    button = 0
                    playing_acount = True 
                    log_in = False
                    start_game  = True   
                    
                elif not userFind (user, pwd):
                    inval = "Invalid user name or password"

#To change the characters 
#Defult is girl
def character(button):
    global charColourB, charColourG, char, start_game, runner1, runner2
    
    draw.rect(screen, WHITE, (0, 0, 1000, 700))
    
    Ariel = font.SysFont("Ariel", 70)
   
    Ariel100 = font.SysFont("Ariel", 100)
    text = Ariel100.render(("Choose a Character"), 1, BLACK)
    screen.blit(text, Rect(150, 40, 100, 110))   
    
    #Girl button
    girlRect = Rect(300, 200, 400, 100)
    draw.rect(screen, charColourG, girlRect)
    text = Ariel.render(("Girl"), 1, BLACK)
    screen.blit(text, Rect(320, 220, 400, 100))        

    #Boy button
    boyRect = Rect(300, 410, 400, 100)
    draw.rect(screen, charColourB, boyRect) 
    text = Ariel.render(("Boy"), 1, BLACK)
    screen.blit(text, Rect(320, 430, 400, 100))           

    # Back button
    backRect = Rect(50, 615, 200, 75)
    draw.rect(screen, WHITE, backRect)
    text = Ariel.render(("Back"), 1, BLACK)
    screen.blit(text, Rect(75, 625, 100, 200)) 
        
    
    #TExt if an invaled username is inputted
    text = Ariel.render((inval), 1, BLACK)
    screen.blit(text, Rect(0, 0, 100, 100))        
    
    screen.blit(screen1, Rect(-50,-50,0,100))
    
    if button == 1:
        if girlRect.collidepoint(mx, my) == True: 
            #Green means 'selected'
            #Gray means 'not selected'            
            charColourB = GRAY
            charColourG = GREEN
            runner1 = runnerG1
            runner2 = runnerG2            
            
        elif boyRect.collidepoint(mx, my) == True: 
            charColourG = GRAY
            charColourB = GREEN 
            runner1 = runnerB1
            runner2 = runnerB2
            
            
        elif backRect.collidepoint(mx, my) == True: 
            char = False
            start_game = True
                
    
#Alot of Global veriabals :( 
#I needed to Restat all of the these variabls every time we re enter the game.             
def startGame(button):
    global playing_acount, playing_guest, user, pwd, colourStart1, colourStart2, colourStart3, colourStart4, colourStart5, start_game, game, main_menu, apple, can, banana, juce_box, cell, Ipad, comp, end, lifes, itemType, iteList, ite, Obsti, newType, step2, lastTime2, TOD, yList, itemList, numItem, cloudsList2, cloudsList, fenceList, cityList, runner, xList, obsticalRectList, ObstiList, obsticalList, step, lastTime, numObsticals, x, MyClock, relTime, space, showUp, collect, char, runner1, runner2, instr, gameTime
    
    ##Variablas used in the game 
    main_menu = False
    sign_up = False
    log_in = False 
    
    # this finds the amount of time that the game runs for  
    gameTime = time.get_ticks()    
    
    #items gathered in the game 
    apple = 0
    banana = 0
    can = 0
    juce_box = 0
    cell = 0
    Ipad = 0
    comp = 0    
    
    #Number of lives
    lifes = 3
    
    #Item/ obstical list
    itemType = []
    iteList = []
    Obsti = "N/A"
    newType = "N/A"
    
    
    
    
    #Time Of Day
    TOD = "Day"
    
    yList = []
    itemList = []
    numItem = 0
    
    cloudsList2 = []
    cloudsList = []
    fenceList = []
    cityList = []
    runner = 300
    xList = []
    obsticalRectList = []
    
    ObstiList=[]
    obsticalList = []
    
    
    step = 3000 # how often we check to move
    lastTime = time.get_ticks()
    numObsticals = 0
    x = 500
    step2 = 3000
    lastTime2 = time.get_ticks()
    
    
    MyClock = time.Clock()
    
    #help For running action
    relTime = 0
    space = False
    showUp = False    
    
    ##The stuf for the start game screen
    draw.rect(screen, WHITE, (0, 0, 1000, 700))
    
    screen.blit(screen3, Rect(0,0,0,100))
    
    Ariel50 = font.SysFont("Ariel", 50) 
    
    
    if playing_acount:
        #username to be in the top right corner
        userSize = Ariel50.size(user)
        length = userSize[0]
        length = 960 - length
        
        #to log out the account
        logOutRect = Rect(837, 87, 140, 50)
        draw.rect(screen, colourStart5, logOutRect)        
        text = Ariel50.render(("Log Out"), 1, BLACK)
        screen.blit(text, Rect(844, 94, 100, 100)) 
        
        Ariel70 = font.SysFont("Ariel", 70)
        
        #if logrd in, the items are saved
        collectRect = Rect(350, 500, 300, 100)
        draw.rect(screen, colourStart2, collectRect)
        text = Ariel70.render(("Collection"), 1, BLACK)
        screen.blit(text, Rect(375, 525, 100, 100))          
        
        #button clolours
        if logOutRect.collidepoint(mx, my) == True:        
            colourStart5 = GRAY
            colourStart2 = GRAY
            
            
        elif collectRect.collidepoint(mx, my) == True: 
            colourStart2 = DARK_GRAY
            colourStart5 = WHITE
            
        else:
            colourStart5 = WHITE  
            colourStart2 = GRAY
            
        #pressing buttons
        if button == 1 and evnt.type != MOUSEMOTION:
            if logOutRect.collidepoint(mx, my) == True:
                main_menu = True
                start_game = False
                button = 0  
                
            elif collectRect.collidepoint(mx, my) == True:
                collect = True
                         
        
    else:
        # guest insted of username
        user = "Guest"
        userSize = Ariel50.size(user)
        length = userSize[0]
        length = 960 - length
        
        #back in sted of log out 
        backRect = Rect(837, 87, 140, 50)
        draw.rect(screen, colourStart5, backRect)        
        text = Ariel50.render(("Back"), 1, BLACK)
        screen.blit(text, Rect(844, 94, 100, 100)) 
        
        if backRect.collidepoint(mx, my) == True:        
            colourStart5 = GRAY
    
        else:
            colourStart5 = WHITE  
            
        if button == 1 and evnt.type != MOUSEMOTION:
            if backRect.collidepoint(mx, my) == True:
                main_menu = True
                start_game = False
                button = 0           

    text = Ariel50.render((user), 1, BLACK)
    screen.blit(text, Rect(length, 50, 100, 100))        
    
    Ariel100 = font.SysFont("Ariel", 100)        
    
    text = Ariel100.render(("Trash the Junk"), 1, BLACK)
    screen.blit(text, Rect(250, 75, 100, 100))    
    
    Ariel = font.SysFont("Ariel", 70)    
    
    startRect = Rect(150, 200, 300, 100)
    draw.rect(screen, colourStart1, startRect)
    text = Ariel.render(("Start Game"), 1, BLACK)
    screen.blit(text, Rect(175, 225, 100, 100))    
 
    helpRect = Rect(550, 200, 300, 100)
    draw.rect(screen, colourStart3, helpRect)
    text = Ariel.render(("Help"), 1, BLACK)
    screen.blit(text, Rect(575, 225, 100, 100)) 
    
    charRect = Rect(350, 350, 300, 100)
    draw.rect(screen, colourStart4, charRect)
    text = Ariel.render(("Characters"), 1, BLACK)
    screen.blit(text, Rect(375, 375, 100, 100))    
                     
        
    screen.blit(screen1, Rect(-50,-50,0,100))    
    
    #Colours
    if startRect.collidepoint(mx, my) == True:
        colourStart1 = DARK_GRAY
        colourStart3 = GRAY
        colourStart4 = GRAY
        
        
    elif helpRect.collidepoint(mx, my) == True: 
        colourStart3 = DARK_GRAY
        colourStart1 = GRAY
        colourStart4 = GRAY
    
    elif charRect.collidepoint(mx, my) == True: 
        colourStart4 = DARK_GRAY
        colourStart1 = GRAY   
        colourStart3 = GRAY 
    
    else:
        colourStart1 = GRAY
        colourStart3 = GRAY
        colourStart4 = GRAY
        
        
    #to press stuf
    if button == 1 and evnt.type != MOUSEMOTION:
        if startRect.collidepoint(mx, my) == True:
            game = True
            start_game = False
            end = False
            button = 0
         
        #character change    
        elif charRect.collidepoint(mx, my) == True:
            char = True
            start_game = False
            button = 0   
        
        #Instructions
        elif helpRect.collidepoint(mx, my) == True:
            instr = True
            start_game = False
            button = 0           
        
            
## All off the move functions are bacicaly the same           
# this function moves the obsticals
def moveObsticals(obsticals, xList):
    
    #to go through the whole list
    for index in range(len(obsticals) - 1, -1, -1):
        #how many pixals the move
        obsticals[index] -= 9            
        # to remove when it has left the screen
        if obsticals[index] < -50:
            del(obsticals[index])  
            del(xList[index]) 

# this function moves the Items
def moveItem(itemList, yList, iteList):
    for index in range(len(itemList) - 1, -1, -1):
        itemList[index] -= 9
        if itemList[index] < -50: 
            del(itemList[index])  
            del(yList[index])
            del(iteList[index])

# this function moves the fence in the background
def moveFence(TOD):
    global fenceList
    #Time of day helps the program chose the appropiate pictuer to use
    if TOD == "Day" or TOD == "Eve":
        for count in range (0, len(fenceList)):
            temp = Rect(fenceList[count], 0, 20, 50)
            screen.blit(fence, Rect(temp))
    if TOD == "Night":
        for count in range (0, len(fenceList)):
            temp = Rect(fenceList[count], 0, 20, 50)
            screen.blit(fence1, Rect(temp))        

    for index in range(len(fenceList) - 1, -1, -1):       
        fenceList[index] -= 8
        if fenceList[index] < 0 and len(fenceList) < 2:
            newfence = 1000
            fenceList.append(newfence)            
        elif fenceList[index] < -1000: 
            del(fenceList[index])
            
    if len(fenceList) < 1:
        newfence = 1000
        fenceList.append(newfence) 

# this function moves the city in the background    
def moveCity(TOD):
    global cityList
    if TOD == "Day": 
        for count in range (0, len(cityList)):
            temp = Rect(cityList[count], 0, 20, 50)
            screen.blit(City1, Rect(temp))
    elif TOD == "Eve":
        for count in range (0, len(cityList)):
            temp = Rect(cityList[count], 0, 20, 50)
            screen.blit(City2, Rect(temp)) 
            
    else:
        for count in range (0, len(cityList)):
            temp = Rect(cityList[count], 0, 20, 50)
            screen.blit(City3, Rect(temp))         
        

    for index in range(len(cityList) - 1, -1, -1):       
        cityList[index] -= 5 
        if cityList[index] < 0 and len(cityList) < 2:
            newCity = 1000
            cityList.append(newCity)            
        elif cityList[index] < -1000: 
            del(cityList[index])
            
    if len(cityList) < 1:
        newCity = 1000
        cityList.append(newCity) 
 
# this function moves the clouds in the background      
def moveclouds():
    global cloudsList
    
    for count in range (0, len(cloudsList)):
            temp = Rect(cloudsList[count], 0, 20, 50)
            screen.blit(clouds, Rect(temp))   
        

    for index in range(len(cloudsList) - 1, -1, -1):       
        cloudsList[index] -= 3 
        if cloudsList[index] < 0 and len(cloudsList) < 2:
            newClouds = 1000
            cloudsList.append(newClouds)            
        elif cloudsList[index] < -1000: 
            del(cloudsList[index])
            
    if len(cloudsList) < 1:
        newClouds = 1000
        cloudsList.append(newClouds) 

# this function moves a second layer of clouds in the background
def moveclouds2():
    global cloudsList2
    
    for count in range (0, len(cloudsList2)):
            temp = Rect(cloudsList2[count], 0, 20, 50)
            screen.blit(clouds, Rect(temp))   
        

    for index in range(len(cloudsList2) - 1, -1, -1):       
        cloudsList2[index] -= 4
        if cloudsList2[index] < 0 and len(cloudsList2) < 2:
            newClouds2 = 1000
            cloudsList2.append(newClouds2)            
        elif cloudsList2[index] < -1000: # if it has gone off the horizon, lets remove
            del(cloudsList2[index])
            
    if len(cloudsList2) < 1:
        newClouds2 = 1000
        cloudsList2.append(newClouds2) 
     
#This function creates and randomizes the position of the obsticals
def Obsticals():
    global ObstiList
    global obsticalList 
    global myClock 
    global step 
    global lastTime
    global numObsticals, count, Obsti, xList, obsticalRectList
    
        
    for count in range (0, len(obsticalList)):
        temp = Rect(obsticalList[count], xList[count], 20, 50)
        screen.blit(ObstiList[count], Rect(temp))   

    moveObsticals(obsticalList, xList) # calls the move function
    if time.get_ticks() - lastTime > step and len(obsticalList) < 10:    #get current time and subtract the last time
        lastTime = time.get_ticks() # reset the lastTime variable for comparisons
        numObsticals += 1 # made a new circle
        if numObsticals % 20 == 0: # every 20 obsticals the speed obsical creation gets faster
            step *= 0.8 # obsticals would now get faster
           
        #to randomize the time they come out        
        Rand = randint(1, 3) 
        if Rand != 3:
            Obsti = Ob1                  
            ObstiList.append(Obsti)
        
            #to randomize the location the come out ( i Know it says 'x' but it is acctually the y axis
            Randx = randint(1, 3) 
            if Randx == 1:
                x = 550
            elif Randx == 2:
                x = 500
            elif Randx == 3:
                x = 450
            xList.append(x) 
            
        
                 
            newObsticals = 1000
            obsticalList.append(newObsticals)   

#This function creates and randomizes the position of the Items
#it is bacicaly the same as Obsticals so im not going to coment a lot of this
def pickUP():
    global iteList
    global itemList 
    global myClock 
    global step2
    global lastTime2
    global numItem, ite, yList, newType
    
   
    for count in range (0, len(itemList)):
        temp = Rect(itemList[count], yList[count], 20, 50)
        screen.blit(iteList[count], Rect(temp))   

    
    
    if time.get_ticks() - lastTime2 > step2 and len(itemList) < 10:   
        lastTime2 = time.get_ticks() 
        numItem += 1 
        if numItem % 20 == 0:
            step2 *= 0.8 
         
        #to randoize the Item type (and timing too)                     
        Rand2 = randint(1, 10) 
        if Rand2 != 8 or Rand2 != 9 or Rand2 != 10:
            if Rand2 == 1:
                ite = item1
                newType = "banana"
            elif Rand2 == 2:
                ite = item2  
                newType = "apple"
            elif Rand2 == 3:
                ite = item3  
                newType = "can"
            elif Rand2 == 4:
                ite = item4  
                newType = "juce box" 
            elif Rand2 == 5:
                ite = item5  
                newType = "cell" 
            elif Rand2 == 6:
                ite = item6  
                newType = "ipad" 
            else:
                ite = item7 
                newType = "comp"             
            iteList.append(ite)
            itemType.append(newType) 
            
            Randy = randint(1, 3) 
            if Randy == 1:
                y = 550
            elif Randy == 2:
                y = 500
            elif Randy == 3:
                y = 450
            yList.append(y) 
            
        
                 
            newItem = 1000
            itemList.append(newItem) 
    moveItem(itemList, yList, iteList)        


#the acctual game  
def Game(button):
    global relTime, space, showUp, run, count, end, game, lifes, TOD, runner, lifes, Randx, paused, sec1, sec2, minn1, minn2, mil1, mil2, itemType, apple, can, banana, juce_box, cell, Ipad, comp, pausing, runner1, runner2, gameTime
    
    #the transparent backgroung in paused gets drawn only onece
    pausing = 1
    
    draw.rect(screen, RED, (0, 0, 1000, 700))
    
    ##To set the time of day
    if time.get_ticks() - gameTime > 50000 and time.get_ticks() - gameTime < 100000:
        TOD = "Eve"
        screen.blit(Sky2, Rect(0,0,0,100))
        
    elif time.get_ticks() - gameTime > 100000:
        TOD = "Night" 
        screen.blit(Sky3, Rect(0,0,0,100))
    else:
        screen.blit(Sky1, Rect(0,0,0,100))
    
    ## Background Functions    
    moveclouds() 
    moveclouds2() 
    moveCity(TOD)    
    screen.blit(ground, Rect(0,0,0,100))
    moveFence(TOD)
    
    ##Obsticals/ pickup
    Obsticals()
    pickUP()
    
    #pauseIcon
    screen.blit(pauseIcon, Rect(25,25,0,100))
    pausRect =Rect(25,25,50,50)
    
    if button == 1 and evnt.type != MOUSEMOTION:
        if pausRect.collidepoint(mx, my) == True:
            paused = True
            game = False
            
            button = 0                   
  
    ##Character controlls
    if evnt.type == KEYDOWN:
        
        if evnt.key == K_UP and runner > 300:      
                runner -= 50
                
        elif evnt.key == K_DOWN and runner < 400:      
                runner += 50       

    if run % 2 == 0:

        screen.blit(runner1, Rect(50,runner,0,100))
            
        if time.get_ticks() - relTime > 300:
                run += 1
                relTime = time.get_ticks()
            
    else:

        screen.blit(runner2, Rect(50,runner,0,100))         
        
        if time.get_ticks() - relTime > 200:
            run += 1
            relTime = time.get_ticks() 
              
    
    ##To check for interactions with obsticals
    #compar to all in the list    
    for index in range(len(itemList) - 1, -1, -1):
        #Check the x axis    
        if itemList[index] + 20 > 149 and itemList[index] + 20 < 246:
            #Check the y axis            
            if yList[index] + 20 > runner + 150 and  yList[index] + 20 < runner + 210:
                # if intersected, remove the obsical                
                del(itemList[index])
                del(yList[index])
                del(iteList[index])
                
                #Add one to the item it intersepted
                if itemType[-1] == "apple":
                    apple += 1
                elif itemType[-1] == "banana":
                    banana += 1  
                elif itemType[-1] == "can":
                    can += 1  
                elif itemType[-1] == "juce box":
                    juce_box += 1 
                elif itemType[-1] == "cell":
                    cell += 1  
                elif itemType[-1] == "Ipad":
                    Ipad += 1  
                elif itemType[-1] == "comp":
                    comp += 1                    
                    
                
    
    
    ##To check for interactions with obsticals
    #compar to all in the list
    for index in range(len(obsticalList) - 1, -1, -1):
        #Check the x axis
        if obsticalList[index] + 20 > 149 and obsticalList[index] + 20 < 246:
            #Check the y axis
            if xList[index] + 20 > runner + 150 and  xList[index] + 20 < runner + 210:
                # if intersected, remove the obsical
                del(obsticalList[index])
                del(xList[index])
                # remove a life
                lifes -= 1
    #The drawings for the life
    if lifes == 1:
        screen.blit(lifes1, Rect(0,0,0,100))
    elif lifes == 2:
        screen.blit(lifes2, Rect(0,0,0,100))        
    elif lifes == 3:
        screen.blit(lifes3, Rect(0,0,0,100))
    #game ends if no more lifes
    elif lifes == 0:
    
        game = False
        end = True   
                
            
#If one pauses during a game     
def pause(button):
    global paused, game, apple, banana, can, juce_box, cell, Ipad, comp, end, pausing
    
    #Calcuate the curent score
    score = apple + banana + can + juce_box + cell + Ipad + comp
    #draw transperent screen only once
    if pausing == 1:
        screen.blit(pauseScreen, Rect(0,0,0,100))
        
    pausing = 2
    
    Ariel100 = font.SysFont("Ariel", 100)        
    
    text = Ariel100.render(("Paussed"), 1, BLACK)
    screen.blit(text, Rect(350, 75, 100, 100))    
    
    Ariel = font.SysFont("Ariel", 75)    
    
    text = Ariel.render(("Current Score:" + str(score) ), 1, BLACK)
    screen.blit(text, Rect(275, 225, 100, 100)) 
    
    #to continue the game
    ResumeRect = Rect(225, 325, 250, 75)    
    text = Ariel.render(("Resume"), 1, BLACK)
    screen.blit(text, Rect(240, 340, 100, 100))
    
    #To leave to the start game screen
    exitRect = Rect(525, 325, 275, 75)       
    text = Ariel.render(("End game"), 1, BLACK)
    screen.blit(text, Rect(540, 340, 100, 100))

    #Pressing the buttons
    if button == 1 and evnt.type != MOUSEMOTION:
        if ResumeRect.collidepoint(mx, my) == True:
            paused = False
            game = True
            button = 0 
        elif exitRect.collidepoint(mx, my) == True:
            paused = False
            end = True
            button = 0         
    
        
        
# end of game function
# This function just displays the score and number of items collected, nothing specal or diferent, so im not going to coment
def End(button):
    global  saved, apple, banana, can, juce_box, cell, Ipad, comp, playing_acount, playing_guest, start_game, end
    
    draw.rect(screen, WHITE, (0, 0, 1000, 700))
    
    if playing_acount == True:
        while saved == False:
            changeStat()
            
    score = apple + banana + can + juce_box + cell + Ipad + comp
    
    Ariel100 = font.SysFont("Ariel", 100)  
    
    text = Ariel100.render(("Score: " + str(score)), 1, BLACK)    
    screen.blit(text, Rect(350, 25, 100, 100))
          
    Ariel70 = font.SysFont("Ariel", 70)  
    
    text = Ariel70.render(("Apple(s): " + str(apple)+ "      Banana(s): " + str(banana)), 1, BLACK)
    screen.blit(text, Rect(175, 125, 100, 100)) 
    
    text = Ariel70.render(("Can(s): " +str(can)+"      Juice Box(s): " + str(juce_box) ), 1, BLACK)
    screen.blit(text, Rect(175, 200, 100, 100))     
    
    text = Ariel70.render(("Cell Phone(s): " + str(cell)+ "      Tablet(s): " + str(Ipad)), 1, BLACK)
    screen.blit(text, Rect(175, 300, 100, 100)) 
    
    text = Ariel70.render(("Computer(s): " +str(comp)), 1, BLACK)
    screen.blit(text, Rect(175, 375, 100, 100))
    
    exitRect = Rect(300, 475, 400, 100)
    draw.rect(screen, BLACK, exitRect)
    text = Ariel70.render(("Exit to Menu"), 1, WHITE)
    screen.blit(text, Rect(325, 500, 100, 100))
    
    screen.blit(screen1, Rect(-50,-50,0,100))
    
    if button == 1 and evnt.type != MOUSEMOTION:
        if exitRect.collidepoint(mx, my) == True:
            start_game = True
            end = False
            
            button = 0            

#To lern how to play  
#It's made out of one image and one button, even less specal then the ens function, nothing to coment.
def Instructions(button):
    global instr, start_game
    
    screen.blit(inst, Rect(0,0,0,100))
    
    Ariel70 = font.SysFont("Ariel", 70)
    
    backRect = Rect(25, 25, 150, 75)
    draw.rect(screen, BLACK, backRect)
    text = Ariel70.render(("Back"), 1, WHITE)
    screen.blit(text, Rect(40, 40, 100, 100))    
        
    if button == 1 and evnt.type != MOUSEMOTION:
        if backRect.collidepoint(mx, my) == True:
            start_game = True
            instr = False
            
            button = 0        
    
    
    
#if one is logged in, this function canbe used to show all of the Items that have been collected
def collection(button):
    global newApple, newBanana, newCan, newBox, newCell, newIpad, newComp, user, collect, start_game
    
    #Opens their stats to get their progress
    openStat()
     #to Caluate the score
    score = int(newApple) + int(newBanana) + int(newCan) + int(newBox) + int(newCell) + int(newIpad) + int(newComp)
    
    ##The rest is just  putting the tittles and images together
    draw.rect(screen, WHITE, (0, 0, 1000, 700))
    
    Ariel100 = font.SysFont("Ariel", 100)    
            
    text = Ariel100.render(("Collection" ), 1, BLACK)
    screen.blit(text, Rect(300, 25, 100, 100))
    
    Ariel75 = font.SysFont("Ariel", 75)    
    Ariel50 = font.SysFont("Ariel", 50)    
            
    text = Ariel75.render(("Garbage:" ), 1, BLACK)
    screen.blit(text, Rect(100, 100, 100, 100))
    
    text = Ariel50.render((str(newBanana) ), 1, BLACK)
    screen.blit(text, Rect(200, 250, 100, 100))  
    
    text = Ariel50.render((str(newApple) ), 1, BLACK)
    screen.blit(text, Rect(350, 250, 100, 100))  
    
    text = Ariel50.render((str(newCan) ), 1, BLACK)
    screen.blit(text, Rect(500, 250, 100, 100))   
    
    text = Ariel50.render((str(newBox) ), 1, BLACK)
    screen.blit(text, Rect(650, 250, 100, 100))     
    
    screen.blit(item11, Rect(150,150,0,100))
    screen.blit(item22, Rect(300,150,0,100))
    screen.blit(item33, Rect(450,150,0,100))
    screen.blit(item44, Rect(600,150,0,100))
    
    text = Ariel75.render(("E-waste:" ), 1, BLACK)
    screen.blit(text, Rect(100, 325, 100, 100))
    
    text = Ariel50.render((str(newCell) ), 1, BLACK)
    screen.blit(text, Rect(250, 500, 100, 100))  
    
    text = Ariel50.render((str(newIpad) ), 1, BLACK)
    screen.blit(text, Rect(450, 500, 100, 100))  
    
    text = Ariel50.render((str(newComp) ), 1, BLACK)
    screen.blit(text, Rect(650, 500, 100, 100))       
    
    screen.blit(item55, Rect(200,375,0,100))
    screen.blit(item66, Rect(400,375,0,100))
    screen.blit(item77, Rect(600,375,0,100))
    
    text = Ariel75.render(("Score: " + str(score)), 1, BLACK)
    screen.blit(text, Rect(450, 600, 100, 100))        
    
    backRect = Rect(75, 575, 300, 100)
    draw.rect(screen, BLACK, backRect)
    text = Ariel75.render(("Back"), 1, WHITE)
    screen.blit(text, Rect(100, 600, 100, 100))
    
    screen.blit(screen1, Rect(-50,-50,0,100))
    
    if button == 1 and evnt.type != MOUSEMOTION:
        if backRect.collidepoint(mx, my) == True:
            start_game = True
            collect = False    
    

 
#to get the events of the mouse
def getVal(tup):                 
    for i in range(3):
        if tup[i] == 1:
            return i+1
    return 0

mx, my = 0, 0

runnerG1 = image.load("GRADrun_girl_1.png")          	 	# position one of running Girl
runnerG1 = transform.scale(runnerG1, (400, 250))

runnerG2 = image.load("GRADrun_girl_2.png")          	 	# position two of running Girl
runnerG2 = transform.scale(runnerG2, (400, 250))

runnerB1 = image.load("GRADrun_boy_1.png")          	 	# position one of running Boy 
runnerB1 = transform.scale(runnerB1, (400, 250))

runnerB2 = image.load("GRADrun_boy_2.png")          	 	# position two of running boy
runnerB2 = transform.scale(runnerB2, (400, 250))

Sky1 = image.load("GRADsky_day.png")          	 	# day sky 
Sky1 = transform.scale(Sky1, (1000, 700))

Sky2 = image.load("GRADsky_eve.png")          	 	# evening sky 
Sky2 = transform.scale(Sky2, (1000, 700))

Sky3 = image.load("GRADsky_night.png")          	 	# night sky 
Sky3 = transform.scale(Sky3, (1000, 700))

City1 = image.load("GRADcity.png")          	 	# city at day 
City1 = transform.scale(City1, (1000, 700))

City2 = image.load("GRADcity_with_some_lights.png")          	 	#  city at eve 
City2 = transform.scale(City2, (1000, 700))

City3 = image.load("GRADcity_lights.png")          	 	#  city at night 
City3 = transform.scale(City3, (1000, 700))

ground = image.load("GRADgrownd.png")          	 	# ground 
ground = transform.scale(ground, (1000, 700))

fence = image.load("GRADfence.png")          	 	# fence at day / eve 
fence = transform.scale(fence, (1000, 700))

fence1 = image.load("GRADfence_light.png")          	 	# fence at night 
fence1 = transform.scale(fence1, (1000, 700))

clouds = image.load("GRADclouds.png")          	 	# clouds 
clouds = transform.scale(clouds, (1200, 900))

Ob1 = image.load("GRADob.png")          	 	# obstical (barrel)
Ob1 = transform.scale(Ob1, (250, 200))

screen1 = image.load("GRADscreen_out.png")          	 	# Brocken computerborder 
screen1 = transform.scale(screen1, (1100, 800))

screen2 = image.load("GRADscreen_in_one.png")          	 	# main menu picture
screen2 = transform.scale(screen2, (1100, 800))

screen3 = image.load("GRADstart_menu.png")          	 	# game menu picture 
screen3 = transform.scale(screen3, (1000, 700))

####Items

item1 = image.load("GRADBana.png")          	 	# banana 
item1 = transform.scale(item1, (400, 250))
item11 = transform.scale(item1, (500, 350))


item2 = image.load("GRADapp.png")          	 	# apple 
item2 = transform.scale(item2, (400, 250))
item22 = transform.scale(item2, (500, 350))


item3 = image.load("GRADcan.png")          	 	# can
item3 = transform.scale(item3, (400, 250))
item33 = transform.scale(item3, (500, 350))


item4 = image.load("GRADjui.png")          	 	# juice box 
item4 = transform.scale(item4, (400, 250))
item44 = transform.scale(item4, (500, 350))


item5 = image.load("GRADcell.png")          	 	# cell phone 
item5 = transform.scale(item5, (400, 250))
item55 = transform.scale(item5, (500, 350))


item6 = image.load("GRADIpad.png")          	 	# tablet 
item6 = transform.scale(item6, (400, 250))
item66 = transform.scale(item6, (500, 350))


item7 = image.load("GRADcomputer.png")          	 	# computer 
item7 = transform.scale(item7, (400, 250))
item77 = transform.scale(item7, (500, 350))



pauseIcon = image.load("GRADPaus button.png")          	 	# pause Icon
pauseIcon = transform.scale(pauseIcon, (400, 250))


##Lifes
lifes1 = image.load("GRADlifes1.png")          	 	#  1 life left
lifes1 = transform.scale(lifes1, (1000, 700))

lifes2 = image.load("GRADlifes2.png")          	 	# 2 lifes left 
lifes2 = transform.scale(lifes2, (1000, 700))

lifes3 = image.load("GRADlifes3.png")          	 	# 3 lifes 
lifes3 = transform.scale(lifes3, (1000, 700))

#Transperant background
pauseScreen = image.load("GRADplaying_menu.png")          	 	 
pauseScreen = transform.scale(pauseScreen, (1800, 1500))

#help page
inst = image.load("GRADInstructions.png")          	 	
inst = transform.scale(inst, (1000, 700))




saved = False

instr = False

#To enter/leave character page
char = False

inval = ""
user = ""
pwd = ""
exist = ""

#To enter/leave main menu page
main_menu = True

#To enter/leave sign up page
sign_up = False

#To enter/leave log in page
log_in = False

#To enter/leave game menu page
start_game = False

#To remember if the person is using an account 
playing_acount = False
playing_guest = False

#To enter/leave the collection page
collect = False

#To enter/leave game
game = False
run = 2

#To enter/leave results page
end = False

#lifes = 3
backIn = True



#main menu button colours
colour1 = BLACK
colour2 = BLACK
colour3 = BLACK
colour4 = BLACK

#start menu button colours
colourStart1 = GRAY
colourStart2 = GRAY
colourStart3 = GRAY
colourStart4 = GRAY
colourStart5 = GRAY

#To enter/leave the in game pause page
paused = False

running = True
 
# Game Loop
while running:
    button = 0  #added this in so we don't have it accidentally click a rectangle again in a different screen
    for evnt in event.get():       
        if evnt.type == MOUSEBUTTONDOWN:
            mx, my = evnt.pos         
            button = evnt.button       
        if evnt.type == MOUSEMOTION:
            mx, my = evnt.pos
            button = getVal(evnt.buttons)
       
           # print(mx, my)
    running = drawScreen(screen, button)

quit()