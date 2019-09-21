add_library('sound')  #import sound library
wy = 100
y=0 #height of word
sentence = ""
current_words = []
current_words1 = []
speed = 3

#--------------------------------------------------------------------------------------------------------------------------------------------
def setup():
  size(1100,800)
  
  global mode # set mode to main screen
  mode = 0
  
  global img
  img = loadImage("intro_screen.jpg") #load background image
  
  global font
  font = createFont("yoster.ttf",100)
  
  global wordlist 
  wordlist = open("wordlist1.txt") #load txt file
  wordlist = {}
  
  global word_list1
  word_list1 = loadStrings("wordlist1.txt")
  
  global word_count
  word_count = 0
  
  global colour1 #colour changes depending on if word is right or wrong
  colour1 = 0 #initialize as 0
  global colour2 #second colour parameter
  colour2 = 0
  global colour3 #third colour parametter
  colour3 = 0
  
  global health_level
  health_level = 5
  
  global level
  level = 1
  
  global on #switch for music
  on = True 
  
  global click,powerup,error, game_over
  click = SoundFile(this,"Click.mp3")
  powerup = SoundFile(this,"power_up.wav")
  error = SoundFile(this,"error.mp3")
  game_over = SoundFile(this,"game_over.wav")

#--------------------------------------------------------------------------------------------------------------------------------------------
def draw():
    global mode,font, wy, word_list1, colour1, colour2, colour3, speed,on,click,powerup,error, game_over
#Main screen
    if mode == 0:
        image(img,-500,0) # load background image
        # text
        fill(255, 76, 0) #red outline
        textFont(font,101.5)
        text("Word Saviour",227,250)
        fill(255, 245, 160) #yellow outline
        textFont(font,100)
        text("Word Saviour",230,250)
        
        # click here to play box
        fill(219, 209, 127,127)
        stroke(0)
        rect(420,360,300,100) 
        #instructions box
        rect(420,500,300,100) 
        #text
        fill(0)
        textFont(font,30)
        text("Click here to play",423,420)
        text("Instructions",460,557)
        fill(255)
        textFont(font,15)
        text("Designed by Jennifer Zhang",2,783)
#Game screen--------------------------------------------------------------------------------------------------------------------------------
    if mode == 1:
        global y,health_level,game_over # set global variables
        background(255) #white background
        fill(170, 144, 99)
        #word list, 2nd parameter is x position, 3rd is when it falls
        
        fill(colour1,colour2,colour3) #black word text colour
        textSize(30)
        if frameCount % 180 == 0:
            random_index = int(random(1,len(word_list1))) #chooses a random word of the word list dictionary
            current_words.append([word_list1[random_index],random(width-100),75]) #add the list of words that already fell down
            current_words1.append(word_list1[random_index]) #a mirror of current_words1
        for word in current_words:
            text(word[0],word[1],word[2]) #word[0] is the word, word[1] is the x position, y is the word[2]
            word[2] += speed #speed of the falling
            if word[2] > 725: #remove from the current words if it touches the ground
                health_level -=1
                current_words.remove(word)
                current_words1.remove(word[0])
                on = True
                if on == True: 
                    error.play() #plays music
                    on = False #stops music
                
                if health_level == 0: #go to game over screen
                    mode = 3
                    on = True
                    if on == True: 
                        game_over.play() #plays music
                        on = False #stops music
#-----------------------------------------------------------------------------------------
        # score bars
        fill(151, 239, 235)
        rect(0,0,1100,40)
        line(367,0,367,40) #first separating line
        line(734,0,734,40) # second separating line
            
        fill(0)    
        #Word count
        text("Words:",440,35)
        text(word_count,600,35)
            
        #Level bar
        text("Level",20,35)
        text(level,170,35) 

        #Health Level Bar
        text("Health:", 800,35)
        fill(0)
        text(health_level,950,35)
   
        #bottom floor
        fill(170, 144, 99)
        rect(0,700,1100,100)
        
        #typing rectangle
        fill(255)
        rect(280,720,500,50)
        
        # User input typing place
        textSize(32)
        fill(0,102,153)
        text(sentence,300,760)
        
        fill(255)
        rect(0,760,70,40) #back to main screen button
        textFont(font,15)
        fill(0)
        text("BACK",16,784)
                            
#--------------------------------------------------------------------------------------------------------------------------------------------
# Instructions screen
    if mode == 2:
        image(img,-500,0) #import background image
        fill(219, 209, 127,127)
        stroke(0)
        rect(150,170,800,500) #yellow box
        
        textFont(font,30)
        fill(0)
        text("Storyline and Instructions",350,200)
        
        textFont(font,15)
        text("Dalemark World is under attack and their language's words are being in danger of getting ", 180,300)
        text("obliterated eternally. It's your duty as the Word Saviour to save these words from ",180,330)
        text("disappearing forever by typing in the falling words before they reach the ground box at the ", 180,360)
        text("bottom.",180,390)
        text("You have 5 lives, best of luck!",180,450)
        
        fill(255) #back button 
        stroke(0)
        rect(290,500,150,70)
        rect(600,500,150,70) #play button
        textFont(font,20) #text for buttons
        fill(0)
        text("Back",330,540)
        text("Start!",637,540)
#--------------------------------------------------------------------------------------------------------------------------------------------
#Game over screen
    if mode == 3:
        image(img,-600,-100)
        fill(255,0,0)
        textFont(font,120)
        text("GAME OVER!",200,400)
        textFont(font,50)
        fill(255)
        text("You saved:",350,500)
        text(word_count, 670,500)
        text("words",750,500)
        #back to home screen button
        textSize(30)
        fill(219, 209, 127,127)
        stroke(0)
        rect(600,600,300,100)
        fill(0)
        text("Back to HOME",650,660)
#--------------------------------------------------------------------------------------------------------------------------------------------
def mousePressed():
       global mode,click, on
       if mode == 0: #main screen
           
           # for the start box
           if 720 > mouseX > 420 and 460 > mouseY > 360:
               mode = 1
               on = True
               if on == True:
                   click.play() #click sound
                   on = False #turn off sound
        
           # instructions box
           if 720 > mouseX > 420 and 600 > mouseY > 500:
               mode = 2
               on = True
               if on == True:
                   click.play() #click sound
                   on = False #turn off sound
        #go back from game screen
       if mode == 1:
            if 70 > mouseX > 0 and 800 > mouseY > 760:
               mode = 0
               on = True
               if on == True:
                   click.play() #click sound
                   on = False #turn off sound
        #go back or start from instructions screen
       if mode == 2:
            if 440 > mouseX > 290 and 570 > mouseY > 500: #back to main
                mode = 0
                on = True
                if on == True:
                   click.play() #click sound
                   on = False #turn off sound
            if 750 > mouseX > 600 and 570 > mouseY > 500:
                mode = 1 #game screen
                on = True
                if on == True:
                   click.play() #click sound
                   on = False #turn off sound
        
        #go to home screen from game over
       if mode == 3:
            if 900 > mouseX > 600 and 700 > mouseY > 600: #back to main
                mode = 0 
                on = True
                if on == True:
                   click.play() #click sound
                   on = False #turn off sound
    
#--------------------------------------------------------------------------------------------------------------------------------------------
def keyPressed():
    global sentence,word_count, colour1, colour2, colour3, health_level, level, speed,error,powerup, on
    if key!= CODED and key != ENTER:
        if len(sentence) < 22: #can't type words more than 22 characters
            sentence = sentence + key
        
#key recognition
    if key == ENTER: #if word is right, then can press enter
        println("key entered is correct")
        if sentence in current_words1: #if word is right
            del current_words[current_words1.index(sentence)] #clean the typing space after each word given the index 
            current_words1.remove(sentence)
            sentence = "" #starts a new sentence
            word_count += 1 #adds one to word count score bar
            colour1 = 0 #remains black
            colour2 = 0
            colour3 = 0
            
            if word_count == 7:
                level +=1 #level 2
                speed += 0.5 #increase speed by 5 pixels for y
                on = True
                if on == True:
                   powerup.play() #powerup sound
                   on = False #turn off sound
            if word_count == 17:
                speed +=1 #level 3
                level +=1
                on = True
                if on == True:
                   powerup.play() #powerup sound
                   on = False #turn off sound
            if word_count == 27:
                speed +=1.5 #level 4
                level +=1
                on = True
                if on == True:
                   powerup.play() #powerup sound
                   on = False #turn off sound
            if word_count == 37:
                speed +=2 #level 5
                level +=1
                on = True
                if on == True:
                   powerup.play() #powerup sound
                   on = False #turn off sound
            if word_count == 47:
                speed +=3 #level 6
                level +=1
                on = True
                if on == True:
                   powerup.play() #powerup sound
                   on = False #turn off sound

        else: #when word is wrong
            println("incorrect")
            sentence = "" #new line when enter is pressed
            colour1 = 255 #turn all other words red to indicate a wrong word
            colour2 = 0
            colour3 = 0
            on = True
            if on == True:
                   error.play() #error sound
                   on = False #turn off sound

    if key == BACKSPACE or key == DELETE: #backspace code
        sentence = sentence[:-2] #delete the last 2 characters, DELETE and inputted character
        println(sentence)
            
