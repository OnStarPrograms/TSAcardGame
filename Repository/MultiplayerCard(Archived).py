from tkinter import *
from tkinter import filedialog
import base64
import random
from pathlib import Path

AlreadyStolen = False
CardinHand = NONE
TheOriginalFilename = ""
# Working on:
"""
- Steal an equal Value card from a player
- Discard a Chosen Card
- Create a Discard Pile.
"""

#What IS Needed (In Order)
"""
- Playing Card Artwork
- Single page game mode runner
- Actual GameModes
- File Transfer Creation
"""

#What is WANTED
"""
- File Encryption
- Text Channel
- Internet File Tranference
"""

#Available Variables:
"""
- (NewUsed)-Player1 Deck
- (NewUsed1)-Player2 Deck
- (NewUsed2)-Player3 Deck
- (NewUsed3)-Player4 Deck
- (UsedPile)-DiscardPile
- (Deck)-DrawPile
- (PlayerTurn)-Whos Turn Is It
    IMAGE PATH VARIABLES:
    - (Heart)
    - (Club)
    - (Diamond)
    - (Spade)
"""

def PickCardPhoto():
    print("Where you can choose where the card photos are.")
def Card():
    print ("Where the card artwork goes")

def Register():
    root = Tk()
    Label(root, text="Button Input Registered").pack()
    root.after(1500, lambda: root.destroy())
    root.mainloop()

def errorHandling():
    root = Tk()
    Label(root, text="Error: please input all required buttons").pack()
    root.after(1500, lambda: root.destroy())
    root.mainloop()

def FinishedWriting():
    root = Tk()
    Label(root, text="Finished Writing game info,\n Search for 'MultiplayerFile.txt'\n or the file you orignally inserted").pack()
    root.after(1500, lambda: root.destroy())
    root.mainloop()
    
def NoneInHand():
    root = Tk()
    Label(root, text="Error: Your opponent didn't have any cards equal to you").pack()
    root.after(1500, lambda: root.destroy())
    root.mainloop()
Deck = []
suite = " "
card = " "
for i in range (4):
  for j in range (12):
    card = j+1
    if (i==0):
      suite="H"
    elif (i==1):
      suite="C"
    elif (i==2):
      suite="D"
    elif (i==3):
      suite="S"
    if (j==0):
      card = "A"
    elif (j==9):
      card = "J"
    elif (j == 10):
      card = "Q"
    elif (j == 11):
      card = "K"
    cards = str(card)
      
      
    Deck.append(suite+cards)

def FileCheck():
    global AllPlayerContent
    global GameMode
    global UsedCards
    global PlayerTurn
    a=0
    b=0

    AllPlayerContent=[]
    f = open("FileName.txt","r")
    content = f.readlines()
    for i in range(10000):                              
        if (content[i]== "END"):
            break                                       
        else:                                           
            a+=1
    for i in range(a):
        if (a==5):
            if (i==0):
                Player1=content[i]
            if (i==1):
                GameMode=content[i]
            if (i==3):
                UsedCards=content[i]
            if (i==4):
                PlayerTurn=content[i]
        if (a==6):
            if (i==0):
                Player1=content[i]
            if (i==1):
                Player2=content[i]
            if (i==2):
                GameMode=content[i]
            if (i==4):
                UsedCards=content[i]
            if (i==5):
                PlayerTurn=content[i]
        if (a==7):
            if (i==0):
                Player1=content[i]
            if (i==1):
                Player2=content[i]
            if (i==2):
                Player3=content[i]
            if (i==3):
                GameMode=content[i]
            if (i==5):
                UsedCards=content[i]
            if (i==6):
                PlayerTurn=content[i]
        if (a==8):
            if (i==0):
                Player1=content[i]
            if (i==1):
                Player2=content[i]
            if (i==2):
                Player3=content[i]
            if (i==3):
                Player4=content[i]
            if (i==4):
                GameMode=content[i]
            if (i==6):
                UsedCards=content[i]
            if (i==7):
                PlayerTurn=content[i]
    if (a==5):
        AllPlayerContent.append(Player1)
    if (a==6):
        AllPlayerContent.append(Player1)
        AllPlayerContent.append(Player2)
    if (a==7):
        AllPlayerContent.append(Player1)
        AllPlayerContent.append(Player2)
        AllPlayerContent.append(Player3)
    if (a==8):
        AllPlayerContent.append(Player1)
        AllPlayerContent.append(Player2)
        AllPlayerContent.append(Player3)
        AllPlayerContent.append(Player4)
    ReadOtherFile()

def ReadOtherFile():
    global Heart
    global Club
    global Diamond
    global Spade
    f = open ("CardBacking.txt","r")
    content = f.readlines()
    a = 0
    BreakLine = content[0]
    Spade = ""
    Diamond = ""
    Club = ""
    Heart = ""
    for i in range(len(BreakLine)):
        if (a == 0):
            if (BreakLine[i]!=">"):
                if (BreakLine[i] == "!"):
                    print ("Skip")
                else:
                    Heart += BreakLine[i]
            else:
                a+=1
        elif (a == 1):
            if (BreakLine[i]!=">"):
                if (BreakLine[i] == "!"):
                    print ("Skip")
                else:
                    Club += BreakLine[i]
            else:
                a+=1
        elif (a == 2):
            if (BreakLine[i]!=">"):
                if (BreakLine[i] == "!"):
                    print ("Skip")
                else:
                    Diamond += BreakLine[i]
            else:
                a+=1
        elif (a == 3):
            if (BreakLine[i]!=">"):
                if (BreakLine[i] == "!"):
                    print ("Skip")
                else:
                    Spade += BreakLine[i]
            else:
                a+=1
    Heart = Path(Heart)
    Club = Path(Club)
    Diamond = Path(Diamond)
    Spade = Path(Spade)
    #content[i] 
    #add some file reading for card backing
    #OR MOVE THIS TO THE ACTUAL GAME RUNNER
    DeckOnUsedCards()

def FileChecking():
    global TheOriginalFilename
    TheOriginalFilename = filedialog.askopenfilename() 
    file = open(TheOriginalFilename,"r")
    f = open ("FileName.txt","w")
    f.write(file.read())
    f.close()
    file.close()

def DeckOnUsedCards():
    a=0
    global GameMode
    global Deck
    global NewUsed
    global NewUsed1
    global NewUsed2
    global NewUsed3
    global UsedPile
    global PlayerTurn
    Used = []
    NewUsed = []
    NewUsed1 = []
    NewUsed2 = []
    NewUsed3 = []
    UsePile = []
    UsedPile = []
    for i in range (len(AllPlayerContent)):
        for j in AllPlayerContent[i]:
            Used.append(j)
    for i in (UsedCards):
        UsePile.append(i)

    for i in range (len(Used)-1):
        if (Used[i]==">"):
            if (a==0):
                NewUsed.append(Used[i-2]+Used[i-1])
            if (a==1):
                NewUsed1.append(Used[i-2]+Used[i-1])
            if (a==2):
                NewUsed2.append(Used[i-2]+Used[i-1])
            if (a==3):
                NewUsed3.append(Used[i-2]+Used[i-1])
        elif ((Used[i])=="!"):
            a+=1
    for i in range (len(UsePile)-1):
        if (UsePile[i]==">"):
            UsedPile.append(UsePile[i-2]+UsePile[i-1])
    print(NewUsed)
    print(NewUsed1)
    print(NewUsed2)
    print(NewUsed3)
    print(UsedPile)
    print(Deck)
    print(PlayerTurn)
    for i in range (len(NewUsed)):
        for j in range (len(Deck)):
            if (NewUsed[i]==Deck[j]):
                Deck.pop(j)
                break
    for i in range (len(NewUsed1)):
        for j in range (len(Deck)):
            if (NewUsed1[i]==Deck[j]):
                Deck.pop(j)
                break
    for i in range (len(NewUsed2)):
        for j in range (len(Deck)):
            if (NewUsed2[i]==Deck[j]):
                Deck.pop(j)
                break
    for i in range (len(NewUsed3)):
        for j in range (len(Deck)):
            if (NewUsed3[i]==Deck[j]):
                Deck.pop(j)
                break
    for i in range (len(UsedPile)):
        for j in range (len(Deck)):
            if (UsedPile[i]==Deck[j]):
                Deck.pop(j)
                break
    for a in range (len(UsedPile)):
        Luser = UsedPile[i]
        for b in range (len(NewUsed)):
            FPlayer = NewUsed[b]
            for c in range (len(NewUsed1)):
                SPlayer = NewUsed1[c]
                for d in range (len(NewUsed2)):
                    TPlayer = NewUsed2[d]
                    for e in range (len(NewUsed3)):
                        FRPlayer = NewUsed3[e]

    try:
        if (Luser[0]=="J" and FPlayer[0] != "J" and SPlayer[0] != "J" and TPlayer[0] != "J" and FRPlayer[0] != "J"):
            Deck.append("JJ")
    except:
        try:
            if (Luser[0]=="J" and FPlayer[0] != "J" and SPlayer[0] != "J" and TPlayer[0] != "J"):
                Deck.append("JJ")
        except:
            try:
                if (Luser[0]=="J" and FPlayer[0] != "J" and SPlayer[0] != "J"):
                    Deck.append("JJ")
            except:
                if (Luser[0]=="J" and FPlayer[0] != "J"):
                    Deck.append("JJ")
    try:
        for abb in range(len(Deck)):
            for abc in range(len(Deck)):
                if (abb != abc):
                    if (Deck[abb] == Deck[abc]):
                        Deck.pop(j)
                        break
    except:
        print("Hit A Wall")
    print(Deck)
    print(GameMode)
    Gamestartup()



################# /\ PULLS DATA /\ ############################################################################################


def encode(UncodedMessage):
    key = 3
    enc = []
     
    for i in range(len(UncodedMessage)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(UncodedMessage[i]) +
                     ord(key_c)) % 256)
                      
        enc.append(enc_c)
         
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
 
# Function to decode
def decode(CodedMessage):
    key = 3
    dec = []
     
    CodedMessage = base64.urlsafe_b64decode(CodedMessage).decode()
    for i in range(len(CodedMessage)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(CodedMessage[i]) -
                           ord(key_c)) % 256)
                            
        dec.append(dec_c)
    return "".join(dec)


################################## /\ ENCODER AND DECODER (When Done With Everything And Provide Game Safety) /\ #######################################################################






################## The GUI: FEEL FREE TO MESS WITH ONCE YOUR FINISHED WITH EVERYTHING ##############################################

def Gamestartup():
    print("this is where the game start up is")
    GameCap =Tk()
    window_width = 307
    window_height = 100
    # get the screen dimension
    GameCap.geometry(f'{window_width}x{window_height}+{0}+{0}')
    def Finish():
        GameCap.destroy()
        WriteFile()    
    Button (GameCap, text = "Check Cards In Your Hand", command = CardArt).grid(row = 0, column = 0)
    Button (GameCap, text = "Draw A Card From The Deck", command= OverFillDeck).grid(row=0 , column = 1)
    Button (GameCap, text = "Input All Your Actions", command = Finish).grid(row=2 , column = 0)
    Button (GameCap, text = "Steal Card", command = StealCard).grid(row = 1, column = 1)
    Button (GameCap, text = "Check the Discard Pile", command = CheckDiscard).grid(row = 1, column = 0)
    GameCap.mainloop()


def CheckDiscard():
                SmallNewUsed = UsedPile[(len(UsedPile))-1]
                print(SmallNewUsed)
                if (SmallNewUsed[0]=="S"):
                        Spades = Toplevel()
                        Spades.wm_attributes("-topmost", 1)
                        def exit_btn():
                            Spades.quit()
                            Spades.destroy()
                            Spades.update()

                            # Adjust size 
                        Spades.geometry("250x323")

                                    # Add image file
                        filename = str(Spade)
                        print (filename)
                        bg = PhotoImage(file = filename)
                        print(Spade)

                            # Show image using label
                        label1 = Label( Spades, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Spades, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                            # Create Frame
                        frame1 = Frame(Spades)
                        frame1.grid(row=2,column=3)

                            # Add buttons
                        button1 = Button(frame1,text="Close", command = exit_btn)
                        button1.grid(row=2,column=4)


                            # Execute tkinter
                        Spades.mainloop()
                elif (SmallNewUsed[0] == "D"):
                        Diamonds = Toplevel()
                        Diamonds.wm_attributes("-topmost", 2)
                        def exit_btn():
                            Diamonds.quit()
                            Diamonds.destroy()
                            Diamonds.update()
                        # Adjust size 
                        Diamonds.geometry("250x323")

                                # Add image file
                        filename = str(Diamond)
                        bg = PhotoImage(file = filename)
                        print(Diamond)

                        # Show image using label
                        label1 = Label( Diamonds, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Diamonds, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                        # Create Frame
                        frame1 = Frame(Diamonds)
                        frame1.grid(row=2,column=3)

                        # Add buttons
                        button1 = Button(frame1,text="Close",command = exit_btn)
                        button1.grid(row=2,column=4)

                        # Execute tkinter
                        Diamonds.mainloop()
                elif (SmallNewUsed[0] == "C"):
                        Clubs = Toplevel()
                        Clubs.wm_attributes("-topmost", 2)
                        def exit_btn():
                            Clubs.quit()
                            Clubs.destroy()
                            Clubs.update()
                        

                        # Adjust size 
                        Clubs.geometry("250x323")

                                # Add image file
                        filename = str(Club)
                        bg = PhotoImage(file = filename)
                        print(Clubs)

                        # Show image using label
                        label1 = Label( Clubs, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Clubs, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                        # Create Frame
                        frame1 = Frame(Clubs)
                        frame1.grid(row=2,column=3)

                        # Add buttons
                        button1 = Button(frame1,text="Close", command=exit_btn)
                        button1.grid(row=2,column=4)

                        # Execute tkinter
                        Clubs.mainloop()

                elif (SmallNewUsed[0] == "H"):
                        Hearts = Toplevel()
                        Hearts.wm_attributes("-topmost", 2)
                        def exit_btn():
                            Hearts.quit()
                            Hearts.destroy()
                            Hearts.update()

                        # Adjust size 
                        Hearts.geometry("250x323")

                                # Add image file
                        filename = str(Heart)
                        bg = PhotoImage(file = filename)
                        print(Heart)

                        # Show image using label
                        label1 = Label( Hearts, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Hearts, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                        # Create Frame
                        frame1 = Frame(Hearts)
                        frame1.grid(row=2,column=3)

                        # Add buttons
                        button1 = Button(frame1,text="Close", command= exit_btn)
                        button1.grid(row=2,column=4)

                        Hearts.wm_attributes("-topmost", 2)
                        # Execute tkinter
                        Hearts.mainloop()


def WriteFile():
    print("This is where we write the file")
    print (TheOriginalFilename)
    if (TheOriginalFilename != ""):
        f = open(TheOriginalFilename, "w")
        f.write("")
        f.close()
        f = open(TheOriginalFilename, "a")
    else:
        try:
            f = open("MultiplayerFile.txt", "x")
            f.close()
            f = open("MultiplayerFile.txt", "w")
            f.write("")
            f.close()
            f = open("MultiplayerFile.txt", "a")
        except:
            f = open("MultiplayerFile.txt", "w")
            f.write("")
            f.close()
            f = open("MultiplayerFile.txt","a")
    try:
        for i in range(len(NewUsed)):
            if (i == (len(NewUsed)-1)):
                f.write(NewUsed[i]+">!\n")
            else:
                f.write(NewUsed[i]+">")
        try:
            for i in range(len(NewUsed1)):
                if (i == (len(NewUsed1)-1)):
                    f.write(NewUsed1[i]+">!\n")
                else:
                    f.write(NewUsed1[i]+">")
            try:
                for i in range(len(NewUsed2)):
                    if (i == (len(NewUsed2)-1)):
                        f.write(NewUsed2[i]+">!\n")
                    else:
                        f.write(NewUsed2[i]+">")
                try:
                    for i in range(len(NewUsed3)):
                        if (i == (len(NewUsed3)-1)):
                            f.write(NewUsed3[i]+">!\n")
                        else:
                            f.write(NewUsed3[i]+">")
                except:
                    print("No Player")
            except:
                print("No Player")
        except:
            print("No Player")
    except:
        print("WahWah")
    f.write(GameMode+">!\n")
    for i in range(len(UsedPile)):
        if (i == len(UsedPile)-1):
            f.write(UsedPile[i]+">!\n")
        else:
            f.write(UsedPile[i]+">")
    for i in PlayerTurn:
        if (i=="1"):
            try:
                abba = NewUsed1[0]
                print(abba)
                f.write("P2>!\n")
            except:
                f.write("P1>!\n")
        elif (i=="2"):
            try:
                abba = NewUsed2[0]
                print(abba)
                f.write("P3>!\n")
            except:
                f.write("P1>!\n")
        elif (i=="3"):
            try:
                abba = NewUsed3[0]
                print(abba)
                f.write("P4>!\n")
            except:
                f.write("P1>!\n")
        elif (i=="4"):
            f.write("P1>!\n")
    f.write("END")
    f.close()
    FinishedWriting()

def OverFillDeck():
    for i in PlayerTurn:
        if (i=='1'):
            a = random.randint(0,len(Deck)-1)
            NewUsed.append(Deck[a])
            Deck.pop(a)
        if (i=='2'):
            a = random.randint(0,len(Deck)-1)
            NewUsed1.append(Deck[a])
            Deck.pop(a)
        if (i=='3'):
            a = random.randint(0,len(Deck)-1)
            NewUsed2.append(Deck[a])
            Deck.pop(a)
        if (i=='4'):
            a = random.randint(0,len(Deck)-1)
            NewUsed3.append(Deck[a])
            Deck.pop(a)
    Register()

def StealCard():
    global AlreadyStolen
    StealerPage = Tk()
    if (AlreadyStolen==False):
        def RandomSteal():
            global AlreadyStolen
            AlreadyStolen = False
            def RandomCardOne():
                NewerSteal.destroy()
                for i in PlayerTurn:
                    if (i == "2"):
                        a = random.randint(0, len(NewUsed)-1)
                        NewUsed1.append(NewUsed[a])
                        NewUsed.pop(a)
                    if (i == "3"):
                        a = random.randint(0, len(NewUsed)-1)
                        NewUsed2.append(NewUsed[a])
                        NewUsed.pop(a)
                    if (i == "4"):
                        a = random.randint(0, len(NewUsed)-1)
                        NewUsed3.append(NewUsed[a])
                        NewUsed.pop(a)

            def RandomCardTwo():
                NewerSteal.destroy()
                for i in PlayerTurn:
                    if (i == "1"):
                        a = random.randint(0, len(NewUsed1)-1)
                        NewUsed.append(NewUsed1[a])
                        NewUsed1.pop(a)
                    if (i == "3"):
                        a = random.randint(0, len(NewUsed1)-1)
                        NewUsed2.append(NewUsed1[a])
                        NewUsed1.pop(a)
                    if (i == "4"):
                        a = random.randint(0, len(NewUsed1)-1)
                        NewUsed3.append(NewUsed1[a])
                        NewUsed1.pop(a)

            def RandomCardThree():
                NewerSteal.destroy()
                for i in PlayerTurn:
                    if (i == "1"):
                        a = random.randint(0, len(NewUsed2)-1)
                        NewUsed.append(NewUsed2[a])
                        NewUsed2.pop(a)
                    if (i == "2"):
                        a = random.randint(0, len(NewUsed2)-1)
                        NewUsed1.append(NewUsed2[a])
                        NewUsed2.pop(a)
                    if (i == "4"):
                        a = random.randint(0, len(NewUsed2)-1)
                        NewUsed3.append(NewUsed2[a])
                        NewUsed2.pop(a)

            def RandomCardFour():
                NewerSteal.destroy()
                for i in PlayerTurn:
                    if (i == "1"):
                        a = random.randint(0, len(NewUsed3)-1)
                        NewUsed.append(NewUsed3[a])
                        NewUsed3.pop(a)
                    if (i == "2"):
                        a = random.randint(0, len(NewUsed3)-1)
                        NewUsed1.append(NewUsed3[a])
                        NewUsed3.pop(a)
                    if (i == "3"):
                        a = random.randint(0, len(NewUsed3)-1)
                        NewUsed2.append(NewUsed3[a])
                        NewUsed3.pop(a)
            StealerPage.destroy()
            for i in PlayerTurn:
                if (i == "1"):
                    NewerSteal = Toplevel()
                    NewerSteal.attributes("-topmost", 1)
                    Label(NewerSteal, text = "Choose a player to steal from \n (You Are Player 1)").grid(column = 0, row = 0)
                    try:
                        print(NewUsed1[1])
                        Button(NewerSteal, text = "Player 2",command = RandomCardTwo).grid(column = 1, row = 0)
                        try:
                            print(NewUsed2[1])
                            Button(NewerSteal, text = "Player 3", command = RandomCardThree).grid(column = 2, row = 0)
                            try:
                                print(NewUsed3[1])
                                Button(NewerSteal, text = "Player 4", command = RandomCardFour).grid(column = 3, row = 0)
                            except:
                                print ("No Fourth Player")
                        except:
                            print ("No third Player")
                    except:
                        print ("No Second Player")
                    
                if (i == "2"):
                    NewerSteal = Toplevel()
                    NewerSteal.attributes("-topmost", 1)
                    Label(NewerSteal, text = "Choose a player to steal from \n (You Are Player 2)").grid(column = 0, row = 0)
                    try:
                        print(NewUsed1[1])
                        Button(NewerSteal, text = "Player 1",command = RandomCardOne).grid(column = 1, row = 0)
                        try:
                            print(NewUsed2[1])
                            Button(NewerSteal, text = "Player 3", command = RandomCardThree).grid(column = 2, row = 0)
                            try:
                                print(NewUsed3[1])
                                Button(NewerSteal, text = "Player 4", command = RandomCardFour).grid(column = 3, row = 0)
                            except:
                                print ("No Fourth Player")
                        except:
                            print ("No third Player")
                    except:
                        print ("No Second Player")

                if (i == "3"):
                    NewerSteal = Toplevel()
                    NewerSteal.attributes("-topmost", 1)
                    Label(NewerSteal, text = "Choose a player to steal from \n (You Are Player 3)").grid(column = 0, row = 0)
                    try:
                        print(NewUsed1[1])
                        Button(NewerSteal, text = "Player 1",command = RandomCardOne).grid(column = 1, row = 0)
                        try:
                            print(NewUsed2[1])
                            Button(NewerSteal, text = "Player 2", command = RandomCardTwo).grid(column = 2, row = 0)
                            try:
                                print(NewUsed3[1])
                                Button(NewerSteal, text = "Player 4", command = RandomCardFour).grid(column = 3, row = 0)
                            except:
                                print ("No Fourth Player")
                        except:
                            print ("No third Player")
                    except:
                        print ("No Second Player")
                    

                if (i == "4"):
                    NewerSteal = Toplevel()
                    NewerSteal.attributes("-topmost", 1)
                    Label(NewerSteal, text = "Choose a player to steal from \n (You Are Player 4)").grid(column = 0, row = 0)
                    try:
                        print(NewUsed1[1])
                        Button(NewerSteal, text = "Player 1",command = RandomCardOne).grid(column = 1, row = 0)
                        try:
                            print(NewUsed2[1])
                            Button(NewerSteal, text = "Player 2", command = RandomCardTwo).grid(column = 2, row = 0)
                            try:
                                print(NewUsed3[1])
                                Button(NewerSteal, text = "Player 3", command = RandomCardThree).grid(column = 3, row = 0)
                            except:
                                print ("No Fourth Player")
                        except:
                            print ("No third Player")
                    except:
                        print ("No Second Player")
        StealerPage.attributes("-topmost", 1)
        def StealChosenCard():
            def RandomCardOne():
                NewerSteal.destroy()
                for i in PlayerTurn:
                    if (i == "2"):
                        a = CardinHand
                        NewerUsed1 = NewUsed1[a]
                        for Check in range(len(NewUsed)):
                            NewerUsed=NewUsed[Check]
                            if (NewerUsed[1]==NewerUsed1[1]):
                                NewUsed1.append(NewUsed[Check])
                                NewUsed.pop(Check)
                            else:
                                NoneInHand
                    if (i == "3"):
                        a = CardinHand
                        NewerUsed1 = NewUsed2[a]
                        for Check in range(len(NewUsed)):
                            NewerUsed=NewUsed[Check]
                            if (NewerUsed[1]==NewerUsed1[1]):
                                NewUsed2.append(NewUsed[Check])
                                NewUsed.pop(Check)
                            else:
                                NoneInHand
                    if (i == "4"):
                        a = CardinHand
                        NewerUsed1 = NewUsed3[a]
                        for Check in range(len(NewUsed)):
                            NewerUsed=NewUsed[Check]
                            if (NewerUsed[1]==NewerUsed1[1]):
                                NewUsed3.append(NewUsed[Check])
                                NewUsed.pop(Check)
                            else:
                                NoneInHand

            def RandomCardTwo():
                NewerSteal.destroy()
                for i in PlayerTurn:
                    if (i == "1"):
                        a = CardinHand
                        NewerUsed1 = NewUsed[a]
                        for Check in range(len(NewUsed1)):
                            NewerUsed=NewUsed1[Check]
                            if (NewerUsed[1]==NewerUsed1[1]):
                                NewUsed.append(NewUsed1[Check])
                                NewUsed1.pop(Check)
                            else:
                                NoneInHand
                    if (i == "3"):
                        a = CardinHand
                        NewerUsed1 = NewUsed2[a]
                        for Check in range(len(NewUsed1)):
                            NewerUsed=NewUsed1[Check]
                            if (NewerUsed[1]==NewerUsed1[1]):
                                NewUsed2.append(NewUsed1[Check])
                                NewUsed1.pop(Check)
                            else:
                                NoneInHand
                    if (i == "4"):
                        a = CardinHand
                        NewerUsed1 = NewUsed3[a]
                        for Check in range(len(NewUsed1)):
                            NewerUsed=NewUsed1[Check]
                            if (NewerUsed[1]==NewerUsed1[1]):
                                NewUsed3.append(NewUsed1[Check])
                                NewUsed1.pop(Check)
                            else:
                                NoneInHand

            def RandomCardThree():
                NewerSteal.destroy()
                for i in PlayerTurn:
                    if (i == "1"):
                        a = CardinHand
                        NewerUsed1 = NewUsed[a]
                        for Check in range(len(NewUsed2)):
                            NewerUsed=NewUsed2[Check]
                            if (NewerUsed[1]==NewerUsed1[1]):
                                NewUsed.append(NewUsed2[Check])
                                NewUsed2.pop(Check)
                            else:
                                NoneInHand
                    if (i == "2"):
                        a = CardinHand
                        NewerUsed1 = NewUsed1[a]
                        for Check in range(len(NewUsed2)):
                            NewerUsed=NewUsed2[Check]
                            if (NewerUsed[1]==NewerUsed1[1]):
                                NewUsed1.append(NewUsed2[Check])
                                NewUsed2.pop(Check)
                            else:
                                NoneInHand
                    if (i == "4"):
                        a = CardinHand
                        NewerUsed1 = NewUsed3[a]
                        for Check in range(len(NewUsed2)):
                            NewerUsed=NewUsed2[Check]
                            if (NewerUsed[1]==NewerUsed1[1]):
                                NewUsed3.append(NewUsed2[Check])
                                NewUsed2.pop(Check)
                            else:
                                NoneInHand

            def RandomCardFour():
                NewerSteal.destroy()
                for i in PlayerTurn:
                    if (i == "1"):
                        a = CardinHand
                        NewerUsed1 = NewUsed[a]
                        for Check in range(len(NewUsed3)):
                            NewerUsed=NewUsed3[Check]
                            if (NewerUsed[1]==NewerUsed1[1]):
                                NewUsed.append(NewUsed3[Check])
                                NewUsed3.pop(Check)
                            else:
                                NoneInHand
                    if (i == "2"):
                        a = CardinHand
                        NewerUsed1 = NewUsed1[a]
                        for Check in range(len(NewUsed3)):
                            NewerUsed=NewUsed3[Check]
                            if (NewerUsed[1]==NewerUsed1[1]):
                                NewUsed1.append(NewUsed3[Check])
                                NewUsed3.pop(Check)
                            else:
                                NoneInHand
                    if (i == "3"):
                        a = CardinHand
                        NewerUsed1 = NewUsed2[a]
                        for Check in range(len(NewUsed3)):
                            NewerUsed=NewUsed3[Check]
                            if (NewerUsed[1]==NewerUsed1[1]):
                                NewUsed2.append(NewUsed3[Check])
                                NewUsed3.pop(Check)
                            else:
                                NoneInHand
            StealerPage.destroy()
            for i in PlayerTurn:
                if (i == "1"):
                    NewerSteal = Toplevel()
                    NewerSteal.attributes("-topmost", 1)
                    Label(NewerSteal, text = "Choose a player to steal from \n (You Are Player 1)").grid(column = 0, row = 0)
                    try:
                        print(NewUsed1[1])
                        Button(NewerSteal, text = "Player 2",command = RandomCardTwo).grid(column = 1, row = 0)
                        try:
                            print(NewUsed2[1])
                            Button(NewerSteal, text = "Player 3", command = RandomCardThree).grid(column = 2, row = 0)
                            try:
                                print(NewUsed3[1])
                                Button(NewerSteal, text = "Player 4", command = RandomCardFour).grid(column = 3, row = 0)
                            except:
                                print ("No Fourth Player")
                        except:
                            print ("No third Player")
                    except:
                        print ("No Second Player")
                    
                if (i == "2"):
                    NewerSteal = Toplevel()
                    NewerSteal.attributes("-topmost", 1)
                    Label(NewerSteal, text = "Choose a player to steal from \n (You Are Player 2)").grid(column = 0, row = 0)
                    try:
                        print(NewUsed1[1])
                        Button(NewerSteal, text = "Player 1",command = RandomCardOne).grid(column = 1, row = 0)
                        try:
                            print(NewUsed2[1])
                            Button(NewerSteal, text = "Player 3", command = RandomCardThree).grid(column = 2, row = 0)
                            try:
                                print(NewUsed3[1])
                                Button(NewerSteal, text = "Player 4", command = RandomCardFour).grid(column = 3, row = 0)
                            except:
                                print ("No Fourth Player")
                        except:
                            print ("No third Player")
                    except:
                        print ("No Second Player")

                if (i == "3"):
                    NewerSteal = Toplevel()
                    NewerSteal.attributes("-topmost", 1)
                    Label(NewerSteal, text = "Choose a player to steal from \n (You Are Player 3)").grid(column = 0, row = 0)
                    try:
                        print(NewUsed1[1])
                        Button(NewerSteal, text = "Player 1",command = RandomCardOne).grid(column = 1, row = 0)
                        try:
                            print(NewUsed2[1])
                            Button(NewerSteal, text = "Player 2", command = RandomCardTwo).grid(column = 2, row = 0)
                            try:
                                print(NewUsed3[1])
                                Button(NewerSteal, text = "Player 4", command = RandomCardFour).grid(column = 3, row = 0)
                            except:
                                print ("No Fourth Player")
                        except:
                            print ("No third Player")
                    except:
                        print ("No Second Player")
                    

                if (i == "4"):
                    NewerSteal = Toplevel()
                    NewerSteal.attributes("-topmost", 1)
                    Label(NewerSteal, text = "Choose a player to steal from \n (You Are Player 4)").grid(column = 0, row = 0)
                    try:
                        print(NewUsed1[1])
                        Button(NewerSteal, text = "Player 1",command = RandomCardOne).grid(column = 1, row = 0)
                        try:
                            print(NewUsed2[1])
                            Button(NewerSteal, text = "Player 2", command = RandomCardTwo).grid(column = 2, row = 0)
                            try:
                                print(NewUsed3[1])
                                Button(NewerSteal, text = "Player 3", command = RandomCardThree).grid(column = 3, row = 0)
                            except:
                                print ("No Fourth Player")
                        except:
                            print ("No third Player")
                    except:
                        print ("No Second Player")


        Button(StealerPage, text = "Steal a chosen players card randomly", command = RandomSteal).grid(column = 0, row = 0)
        if (CardinHand != NONE):
            JokerInHand = False
            for i in NewUsed:
                if (i[0]=="J"):
                    JokerInHand = True
            for i in NewUsed1:
                if (i[0]=="J"):
                    JokerInHand = True
            for i in NewUsed2:
                if (i[0]=="J"):
                    JokerInHand = True
            for i in NewUsed3:
                if (i[0]=="J"):
                    JokerInHand = True
            if (JokerInHand != True):
                Button(StealerPage, text = "Steal a Card that is equal in value to this Card", command = StealChosenCard).grid(column = 0, row = 1)
            else:
                Label(StealerPage, text = "Joker Is In Play").grid(column = 0, row = 1)
        StealerPage.mainloop()
    else:
        StealerPage.destroy()
        root = Toplevel()
        root.attributes("-topmost", 1)
        Label(root, text="Error: You Already Stole A Card This Turn").pack()
        root.after(1500, lambda: root.destroy())
        root.mainloop()

def CardArt():
    global CardinHand
    for jade in PlayerTurn:
        if (jade == '1'):
            print("This is where it creates insances of cards for first person")
            for i in range(len(NewUsed)):
                CardinHand = i
                def DiscardCard():
                    UsedPile.append(NewUsed[i])
                    NewUsed.pop(i)

                SmallNewUsed = NewUsed[i]
                print(SmallNewUsed)
                if (SmallNewUsed[0]=="S"):
                        Spades = Toplevel()
                        Spades.wm_attributes("-topmost", 1)
                        def exit_btn():
                            Spades.quit()
                            Spades.destroy()
                            Spades.update()

                            # Adjust size 
                        Spades.geometry("250x323")

                                    # Add image file
                        filename = str(Spade)
                        print (filename)
                        bg = PhotoImage(file = filename)
                        print(Spade)

                            # Show image using label
                        label1 = Label( Spades, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Spades, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                            # Create Frame
                        frame1 = Frame(Spades)
                        frame1.grid(row=2,column=3)

                            # Add buttons
                        button1 = Button(frame1,text="Next Card", command = exit_btn)
                        button1.grid(row=2,column=4)

                        button2 = Button( frame1, text = "Steal", command = StealCard)
                        button2.grid(row=2,column=5)

                        button3 = Button( frame1, text = "Discard", command= DiscardCard)
                        button3.grid(row=2,column=6)

                            # Execute tkinter
                        Spades.mainloop()
                elif (SmallNewUsed[0] == "D"):
                        Diamonds = Toplevel()
                        Diamonds.wm_attributes("-topmost", 2)
                        def exit_btn():
                            Diamonds.quit()
                            Diamonds.destroy()
                            Diamonds.update()
                        # Adjust size 
                        Diamonds.geometry("250x323")

                                # Add image file
                        filename = str(Diamond)
                        bg = PhotoImage(file = filename)
                        print(Diamond)

                        # Show image using label
                        label1 = Label( Diamonds, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Diamonds, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                        # Create Frame
                        frame1 = Frame(Diamonds)
                        frame1.grid(row=2,column=3)

                        # Add buttons
                        button1 = Button(frame1,text="Next Card",command = exit_btn)
                        button1.grid(row=2,column=4)

                        button2 = Button( frame1, text = "Steal",command = StealCard)
                        button2.grid(row=2,column=5)

                        button3 = Button( frame1, text = "Discard", command= DiscardCard)
                        button3.grid(row=2,column=6)

                        # Execute tkinter
                        Diamonds.mainloop()
                elif (SmallNewUsed[0] == "C"):
                        Clubs = Toplevel()
                        Clubs.wm_attributes("-topmost", 2)
                        def exit_btn():
                            Clubs.quit()
                            Clubs.destroy()
                            Clubs.update()
                        

                        # Adjust size 
                        Clubs.geometry("250x323")

                                # Add image file
                        filename = str(Club)
                        bg = PhotoImage(file = filename)
                        print(Clubs)

                        # Show image using label
                        label1 = Label( Clubs, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Clubs, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                        # Create Frame
                        frame1 = Frame(Clubs)
                        frame1.grid(row=2,column=3)

                        # Add buttons
                        button1 = Button(frame1,text="Next Card", command=exit_btn)
                        button1.grid(row=2,column=4)

                        button2 = Button( frame1, text = "Steal",command = StealCard)
                        button2.grid(row=2,column=5)

                        button3 = Button( frame1, text = "Discard", command= DiscardCard)
                        button3.grid(row=2,column=6)

                        # Execute tkinter
                        Clubs.mainloop()

                elif (SmallNewUsed[0] == "H"):
                        Hearts = Toplevel()
                        Hearts.wm_attributes("-topmost", 2)
                        def exit_btn():
                            Hearts.quit()
                            Hearts.destroy()
                            Hearts.update()

                        # Adjust size 
                        Hearts.geometry("250x323")

                                # Add image file
                        filename = str(Heart)
                        bg = PhotoImage(file = filename)
                        print(Heart)

                        # Show image using label
                        label1 = Label( Hearts, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Hearts, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                        # Create Frame
                        frame1 = Frame(Hearts)
                        frame1.grid(row=2,column=3)

                        # Add buttons
                        button1 = Button(frame1,text="Next Card", command= exit_btn)
                        button1.grid(row=2,column=4)

                        button2 = Button( frame1, text = "Steal",command = StealCard)
                        button2.grid(row=2,column=5)

                        button3 = Button( frame1, text = "Discard", command= DiscardCard)
                        button3.grid(row=2,column=6)
                        Hearts.wm_attributes("-topmost", 2)
                        # Execute tkinter
                        Hearts.mainloop()
                elif (SmallNewUsed[0] == "J"):
                        Joking = Toplevel()
                        Joking.wm_attributes("-topmost", 2)
                        def exit_btn():
                            Joking.quit()
                            Joking.destroy()
                            Joking.update()

                        # Adjust size 

                                # Add image file
                        Label (Joking, text = "You Have The Joker,\n You May Not Discard It").pack()

                        # Show image using label
                        

                        # Create Frame
                        frame1 = Frame(Joking)
                        frame1.grid(row=2,column=3)

                        # Add buttons
                        button1 = Button(frame1,text="Next Card", command= exit_btn)
                        button1.grid(row=2,column=4)
                        # Execute tkinter
                        Joking.mainloop()

        if (jade == '2'):
            print("This is where it creates instances of cards for second person")
            for i in range(len(NewUsed1)):
                CardinHand = i
                SmallNewUsed = NewUsed1[i]
                print(SmallNewUsed)
                def DiscardCard():
                    UsedPile.append(NewUsed1[i])
                    NewUsed1.pop(i)

                if (SmallNewUsed[0]=="S"):
                        Spades = Toplevel()
                        Spades.wm_attributes("-topmost", 1)
                        def exit_btn():
                            Spades.quit()
                            Spades.destroy()
                            Spades.update()

                            # Adjust size 
                        Spades.geometry("250x323")

                                    # Add image file
                        filename = str(Spade)
                        print (filename)
                        bg = PhotoImage(file = filename)
                        print(Spade)

                            # Show image using label
                        label1 = Label( Spades, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Spades, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                            # Create Frame
                        frame1 = Frame(Spades)
                        frame1.grid(row=2,column=3)

                            # Add buttons
                        button1 = Button(frame1,text="Next Card", command = exit_btn)
                        button1.grid(row=2,column=4)

                        button2 = Button( frame1, text = "Steal",command = StealCard)
                        button2.grid(row=2,column=5)

                        button3 = Button( frame1, text = "Discard", command= DiscardCard)
                        button3.grid(row=2,column=6)

                            # Execute tkinter
                        Spades.mainloop()
                elif (SmallNewUsed[0] == "D"):
                        Diamonds = Toplevel()
                        Diamonds.wm_attributes("-topmost", 2)
                        def exit_btn():
                            Diamonds.quit()
                            Diamonds.destroy()
                            Diamonds.update()
                        # Adjust size 
                        Diamonds.geometry("250x323")

                                # Add image file
                        filename = str(Diamond)
                        bg = PhotoImage(file = filename)
                        print(Diamond)

                        # Show image using label
                        label1 = Label( Diamonds, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Diamonds, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                        # Create Frame
                        frame1 = Frame(Diamonds)
                        frame1.grid(row=2,column=3)

                        # Add buttons
                        button1 = Button(frame1,text="Next Card",command = exit_btn)
                        button1.grid(row=2,column=4)

                        button2 = Button( frame1, text = "Steal",command = StealCard)
                        button2.grid(row=2,column=5)

                        button3 = Button( frame1, text = "Discard", command= DiscardCard)
                        button3.grid(row=2,column=6)

                        # Execute tkinter
                        Diamonds.mainloop()
                elif (SmallNewUsed[0] == "C"):
                        Clubs = Toplevel()
                        Clubs.wm_attributes("-topmost", 2)
                        def exit_btn():
                            Clubs.quit()
                            Clubs.destroy()
                            Clubs.update()
                        

                        # Adjust size 
                        Clubs.geometry("250x323")

                                # Add image file
                        filename = str(Club)
                        bg = PhotoImage(file = filename)
                        print(Clubs)

                        # Show image using label
                        label1 = Label( Clubs, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Clubs, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                        # Create Frame
                        frame1 = Frame(Clubs)
                        frame1.grid(row=2,column=3)

                        # Add buttons
                        button1 = Button(frame1,text="Next Card", command=exit_btn)
                        button1.grid(row=2,column=4)

                        button2 = Button( frame1, text = "Steal",command = StealCard)
                        button2.grid(row=2,column=5)

                        button3 = Button( frame1, text = "Discard", command= DiscardCard)
                        button3.grid(row=2,column=6)

                        # Execute tkinter
                        Clubs.mainloop()

                elif (SmallNewUsed[0] == "H"):
                        Hearts = Toplevel()
                        Hearts.wm_attributes("-topmost", 2)
                        def exit_btn():
                            Hearts.quit()
                            Hearts.destroy()
                            Hearts.update()

                        # Adjust size 
                        Hearts.geometry("250x323")

                                # Add image file
                        filename = str(Heart)
                        bg = PhotoImage(file = filename)
                        print(Heart)

                        # Show image using label
                        label1 = Label( Hearts, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Hearts, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                        # Create Frame
                        frame1 = Frame(Hearts)
                        frame1.grid(row=2,column=3)

                        # Add buttons
                        button1 = Button(frame1,text="Next Card", command= exit_btn)
                        button1.grid(row=2,column=4)

                        button2 = Button( frame1, text = "Steal",command = StealCard)
                        button2.grid(row=2,column=5)

                        button3 = Button( frame1, text = "Discard", command= DiscardCard)
                        button3.grid(row=2,column=6)
                        Hearts.wm_attributes("-topmost", 2)
                        # Execute tkinter
                        Hearts.mainloop()

        if (jade == '3'):
            print("This is where it creates insances of cards for third person")
            for i in range(len(NewUsed2)):
                CardinHand = i
                SmallNewUsed = NewUsed2[i]
                print(SmallNewUsed)
                def DiscardCard():
                    UsedPile.append(NewUsed2[i])
                    NewUsed2.pop(i)

                if (SmallNewUsed[0]=="S"):
                        Spades = Toplevel()
                        Spades.wm_attributes("-topmost", 1)
                        def exit_btn():
                            Spades.quit()
                            Spades.destroy()
                            Spades.update()

                            # Adjust size 
                        Spades.geometry("250x323")

                                    # Add image file
                        filename = str(Spade)
                        print (filename)
                        bg = PhotoImage(file = filename)
                        print(Spade)

                            # Show image using label
                        label1 = Label( Spades, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Spades, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                            # Create Frame
                        frame1 = Frame(Spades)
                        frame1.grid(row=2,column=3)

                            # Add buttons
                        button1 = Button(frame1,text="Next Card", command = exit_btn)
                        button1.grid(row=2,column=4)

                        button2 = Button( frame1, text = "Steal",command = StealCard)
                        button2.grid(row=2,column=5)

                        button3 = Button( frame1, text = "Discard", command= DiscardCard)
                        button3.grid(row=2,column=6)

                            # Execute tkinter
                        Spades.mainloop()
                elif (SmallNewUsed[0] == "D"):
                        Diamonds = Toplevel()
                        Diamonds.wm_attributes("-topmost", 2)
                        def exit_btn():
                            Diamonds.quit()
                            Diamonds.destroy()
                            Diamonds.update()
                        # Adjust size 
                        Diamonds.geometry("250x323")

                                # Add image file
                        filename = str(Diamond)
                        bg = PhotoImage(file = filename)
                        print(Diamond)

                        # Show image using label
                        label1 = Label( Diamonds, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Diamonds, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                        # Create Frame
                        frame1 = Frame(Diamonds)
                        frame1.grid(row=2,column=3)

                        # Add buttons
                        button1 = Button(frame1,text="Next Card",command = exit_btn)
                        button1.grid(row=2,column=4)

                        button2 = Button( frame1, text = "Steal",command = StealCard)
                        button2.grid(row=2,column=5)

                        button3 = Button( frame1, text = "Discard", command= DiscardCard)
                        button3.grid(row=2,column=6)

                        # Execute tkinter
                        Diamonds.mainloop()
                elif (SmallNewUsed[0] == "C"):
                        Clubs = Toplevel()
                        Clubs.wm_attributes("-topmost", 2)
                        def exit_btn():
                            Clubs.quit()
                            Clubs.destroy()
                            Clubs.update()
                        

                        # Adjust size 
                        Clubs.geometry("250x323")

                                # Add image file
                        filename = str(Club)
                        bg = PhotoImage(file = filename)
                        print(Clubs)

                        # Show image using label
                        label1 = Label( Clubs, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Clubs, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                        # Create Frame
                        frame1 = Frame(Clubs)
                        frame1.grid(row=2,column=3)

                        # Add buttons
                        button1 = Button(frame1,text="Next Card", command=exit_btn)
                        button1.grid(row=2,column=4)

                        button2 = Button( frame1, text = "Steal",command = StealCard)
                        button2.grid(row=2,column=5)

                        button3 = Button( frame1, text = "Discard", command= DiscardCard)
                        button3.grid(row=2,column=6)

                        # Execute tkinter
                        Clubs.mainloop()

                elif (SmallNewUsed[0] == "H"):
                        Hearts = Toplevel()
                        Hearts.wm_attributes("-topmost", 2)
                        def exit_btn():
                            Hearts.quit()
                            Hearts.destroy()
                            Hearts.update()

                        # Adjust size 
                        Hearts.geometry("250x323")

                                # Add image file
                        filename = str(Heart)
                        bg = PhotoImage(file = filename)
                        print(Heart)

                        # Show image using label
                        label1 = Label( Hearts, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Hearts, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                        # Create Frame
                        frame1 = Frame(Hearts)
                        frame1.grid(row=2,column=3)

                        # Add buttons
                        button1 = Button(frame1,text="Next Card", command= exit_btn)
                        button1.grid(row=2,column=4)

                        button2 = Button( frame1, text = "Steal",command = StealCard)
                        button2.grid(row=2,column=5)

                        button3 = Button( frame1, text = "Discard", command= DiscardCard)
                        button3.grid(row=2,column=6)
                        Hearts.wm_attributes("-topmost", 2)
                        # Execute tkinter
                        Hearts.mainloop()

        if (jade == '4'):
            print("This is where it creates insances of cards for first person")
            for i in range(len(NewUsed3)):
                CardinHand = i
                SmallNewUsed = NewUsed3[i]
                print(SmallNewUsed)
                def DiscardCard():
                    UsedPile.append(NewUsed3[i])
                    NewUsed3.pop(i)

                if (SmallNewUsed[0]=="S"):
                        Spades = Toplevel()
                        Spades.wm_attributes("-topmost", 1)
                        def exit_btn():
                            Spades.quit()
                            Spades.destroy()
                            Spades.update()

                            # Adjust size 
                        Spades.geometry("250x323")

                                    # Add image file
                        filename = str(Spade)
                        print (filename)
                        bg = PhotoImage(file = filename)
                        print(Spade)

                            # Show image using label
                        label1 = Label( Spades, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Spades, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                            # Create Frame
                        frame1 = Frame(Spades)
                        frame1.grid(row=2,column=3)

                            # Add buttons
                        button1 = Button(frame1,text="Next Card", command = exit_btn)
                        button1.grid(row=2,column=4)

                        button2 = Button( frame1, text = "Steal",command = StealCard)
                        button2.grid(row=2,column=5)

                        button3 = Button( frame1, text = "Discard", command= DiscardCard)
                        button3.grid(row=2,column=6)

                            # Execute tkinter
                        Spades.mainloop()
                elif (SmallNewUsed[0] == "D"):
                        Diamonds = Toplevel()
                        Diamonds.wm_attributes("-topmost", 2)
                        def exit_btn():
                            Diamonds.quit()
                            Diamonds.destroy()
                            Diamonds.update()
                        # Adjust size 
                        Diamonds.geometry("250x323")

                                # Add image file
                        filename = str(Diamond)
                        bg = PhotoImage(file = filename)
                        print(Diamond)

                        # Show image using label
                        label1 = Label( Diamonds, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Diamonds, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                        # Create Frame
                        frame1 = Frame(Diamonds)
                        frame1.grid(row=2,column=3)

                        # Add buttons
                        button1 = Button(frame1,text="Next Card",command = exit_btn)
                        button1.grid(row=2,column=4)

                        button2 = Button( frame1, text = "Steal",command = StealCard)
                        button2.grid(row=2,column=5)

                        button3 = Button( frame1, text = "Discard", command= DiscardCard)
                        button3.grid(row=2,column=6)

                        # Execute tkinter
                        Diamonds.mainloop()
                elif (SmallNewUsed[0] == "C"):
                        Clubs = Toplevel()
                        Clubs.wm_attributes("-topmost", 2)
                        def exit_btn():
                            Clubs.quit()
                            Clubs.destroy()
                            Clubs.update()
                        

                        # Adjust size 
                        Clubs.geometry("250x323")

                                # Add image file
                        filename = str(Club)
                        bg = PhotoImage(file = filename)
                        print(Clubs)

                        # Show image using label
                        label1 = Label( Clubs, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Clubs, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                        # Create Frame
                        frame1 = Frame(Clubs)
                        frame1.grid(row=2,column=3)

                        # Add buttons
                        button1 = Button(frame1,text="Next Card", command=exit_btn)
                        button1.grid(row=2,column=4)

                        button2 = Button( frame1, text = "Steal",command = StealCard)
                        button2.grid(row=2,column=5)

                        button3 = Button( frame1, text = "Discard", command= DiscardCard)
                        button3.grid(row=2,column=6)

                        # Execute tkinter
                        Clubs.mainloop()

                elif (SmallNewUsed[0] == "H"):
                        Hearts = Toplevel()
                        Hearts.wm_attributes("-topmost", 2)
                        def exit_btn():
                            Hearts.quit()
                            Hearts.destroy()
                            Hearts.update()

                        # Adjust size 
                        Hearts.geometry("250x323")

                                # Add image file
                        filename = str(Heart)
                        bg = PhotoImage(file = filename)
                        print(Heart)

                        # Show image using label
                        label1 = Label( Hearts, image = bg)
                        label1.place(x = 0, y = 0)

                        label2 = Label( Hearts, text = SmallNewUsed[1])
                        label2.place(x = 190,y =0)

                        # Create Frame
                        frame1 = Frame(Hearts)
                        frame1.grid(row=2,column=3)

                        # Add buttons
                        button1 = Button(frame1,text="Next Card", command= exit_btn)
                        button1.grid(row=2,column=4)

                        button2 = Button( frame1, text = "Steal",command = StealCard)
                        button2.grid(row=2,column=5)

                        button3 = Button( frame1, text = "Discard", command= DiscardCard)
                        button3.grid(row=2,column=6)
                        Hearts.wm_attributes("-topmost", 2)
                        # Execute tkinter
                        Hearts.mainloop()
        CardinHand = NONE


try:
    f = open ("FileName.txt","x")
    f.close
    root = Tk()
    Label(root, text="Oops! \nLooks like your program isn't setup! \nDon't worry This will only take a minute...").pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
except:
    print("Yay! no setup!")
try:
    f = open ("CardBacking.txt","x")
    f.close
    root = Tk()
    Label(root, text="Oops! \nLooks like your program isn't setup! \nDon't worry This will only take a minute...").pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
except:
    print("Yay! no setup!")


#####################################
def NewGameMenu():
    Joker = False
    print("This is where you make a new match")
    try:
        root.destroy()
    except:
        print("No Tkinter window to destroy")
    root = Tk()
    root.wm_attributes("-topmost", 1)
    window_width = 275
    window_height = 200
    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

# find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# set the position of the window to the center of the screen
    def FileCreate():
        try:
            f = open("FileName.txt","w")
            for i in range(Players):
                newHand=str(Deck[random.randint(0,47)])+">"+str(Deck[random.randint(0,47)])+">"+str(Deck[random.randint(0,47)])+">"+str(Deck[random.randint(0,47)])+">"+str(Deck[random.randint(0,47)])+">!\n"
                f.write(newHand)
            f.close()
            f = open("FileName.txt","a")
            f.write(GameMode+">!\n")
            if (Joker==True):
                f.write("JJ>00>!\n")
            else:
                f.write("00>!\n")
            f.write("P1>!\n")
            f.write("END")
            f.close()
            FileCheck()
            root.destroy()
        except:
            errorHandling()
        
    def OnePlayer():
        global Players
        Players=1
        Register()
    def TwoPlayer():
        global Players
        Players=2
        Register()
    def ThreePlayer():
        global Players
        Players=3
        Register()
    def FourPlayer():
        global Players
        Players=4
        Register()
    def ChooseDeck():
        ChooseDeck = Tk()
        ChooseDeck.wm_attributes("-topmost", 1)
        window_width = 700
        window_height = 200

        # get the screen dimension
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        ChooseDeck.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        def ChooseHearts():
            global Heartfile
            Heartfile = filedialog.askopenfilename()

        def ChooseClubs():
            global Clubfile
            Clubfile = filedialog.askopenfilename()
        
        def ChooseDiamonds():
            global Diamondfile
            Diamondfile = filedialog.askopenfilename()
        
        def ChooseSpades():
            global Spadefile
            Spadefile = filedialog.askopenfilename()
            
        def inputCard():
            try:
                f = open("CardBacking.txt","w")
                f.write("")
                f.close()
                f = open("CardBacking.txt","a")
                f.write(Heartfile+">!")
                f.write(Clubfile+">!")
                f.write(Diamondfile+">!")
                f.write(Spadefile+">!")
                f.close()
                ChooseDeck.destroy()
                Register()
            except:
                errorHandling()
        Label (ChooseDeck, text = "This is where you can choose your artwork for the different suites,").grid(row=0,column=0)
        Label (ChooseDeck, text = " There are allready preloaded artwork in the file,").grid(row=0,column=1)
        Label (ChooseDeck, text = " however if you wish you may choose your own artwork.").grid(row=1,column=0)
        Label (ChooseDeck, text = " JUST REMEMBER TO USE A PNG").grid(row=1,column=1)
        Button (ChooseDeck, text = "Choose the Hearts Artwork", command = ChooseHearts).grid(row=2,column=0)
        Button (ChooseDeck, text = "Choose the Clubs Artwork", command = ChooseClubs).grid(row=2,column=1)
        Button (ChooseDeck, text = "Choose the Diamonds Artwork", command = ChooseDiamonds).grid(row=3,column=0)
        Button (ChooseDeck, text = "Choose the Spades Artwork", command = ChooseSpades).grid(row=3,column=1)
        Button (ChooseDeck, text = "Input your Card Artwork", command = inputCard).grid(row=4,column=0)
        ChooseDeck.mainloop()



    def FreePlay():
        global GameMode
        GameMode="FreePlay"
        Register()
    def JokerFix():
            global Joker
            Joker = True
            Register()
    Label (root, text="Which Deck Would You like to use?").grid(row=0, column=0)
    Button (root, text="Click to set up your deck", command=ChooseDeck).grid(row=1,column=0)
    Label (root, text="Which GameMode Would You Like?").grid(row=2,column=0)
    Button (root, text="FreePlay", command=FreePlay).grid(row=3,column=0)
    Label (root, text="How many people will be playing?").grid(row=4, column=0)
    Label (root, text="----------->").grid(row=5,column=0)
    Button (root, text="1", command=OnePlayer).grid(row=5,column=1)
    Button (root, text="2", command=TwoPlayer).grid(row=5,column=2)
    Button (root, text="3", command=ThreePlayer).grid(row=5,column=3)
    Button (root, text="4", command=FourPlayer).grid(row=5,column=4)
    Button (root, text="Click To Add One Joker To Your Deck", command=JokerFix).grid(row=6,column=0)
    Button (root, text="Input Your Choice", command=FileCreate).grid(row=7,column=0)
    root.mainloop()
######################################




def ChooseFile():
    def ChooseDeck():
        ChooseDeck = Tk()
        ChooseDeck.wm_attributes("-topmost", 1)
        window_width = 610
        window_height = 150

        # get the screen dimension
        screen_width = ChooseDeck.winfo_screenwidth()
        screen_height = ChooseDeck.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        ChooseDeck.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        def ChooseHearts():
            global Heartfile
            Heartfile = filedialog.askopenfilename()

        def ChooseClubs():
            global Clubfile
            Clubfile = filedialog.askopenfilename()
        
        def ChooseDiamonds():
            global Diamondfile
            Diamondfile = filedialog.askopenfilename()
        
        def ChooseSpades():
            global Spadefile
            Spadefile = filedialog.askopenfilename()
            
        def inputCard():
            try:
                f = open("CardBacking.txt","w")
                f.write("")
                f.close()
                f = open("CardBacking.txt","a")
                f.write(Heartfile+">!")
                f.write(Clubfile+">!")
                f.write(Diamondfile+">!")
                f.write(Spadefile+">!")
                f.close()
                ChooseDeck.destroy()
                Register()
            except:
                errorHandling()
        Label (ChooseDeck, text = "This is where you can choose your artwork for the different suites,").grid(row=0,column=0)
        Label (ChooseDeck, text = " There are allready preloaded artwork in the file,").grid(row=0,column=1)
        Label (ChooseDeck, text = " however if you wish you may choose your own artwork.").grid(row=1,column=0)
        Label (ChooseDeck, text = " JUST REMEMBER TO USE A PNG").grid(row=1,column=1)
        Button (ChooseDeck, text = "Choose the Hearts Artwork", command = ChooseHearts).grid(row=2,column=0)
        Button (ChooseDeck, text = "Choose the Clubs Artwork", command = ChooseClubs).grid(row=2,column=1)
        Button (ChooseDeck, text = "Choose the Diamonds Artwork", command = ChooseDiamonds).grid(row=3,column=0)
        Button (ChooseDeck, text = "Choose the Spades Artwork", command = ChooseSpades).grid(row=3,column=1)
        Button (ChooseDeck, text = "Input your Card Artwork", command = inputCard).grid(row=4,column=0)
        ChooseDeck.mainloop()
    a=0
    window = Tk()
    window_width = 300
    window_height = 75

# get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

# find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    def abba():
        window.destroy()
        FileCheck()
        LoadGame()

    root.destroy()
    Button(window, text="Press if you haven't set up your card backing images", command=ChooseDeck).grid(row=0,column=0)
    Button(window, text="Press to choose the game file (i.e. 'MultiplayerFiles.txt')", command=FileChecking).grid(row=1,column=0)
    Button(window, text="Press to input your choice ", command=abba).grid(row=2,column=0)
    window.mainloop()

###############################
def LoadGame():              
    print("This is where the game is loaded")
###############################

import tkinter as tk

root = tk.Tk()
root.title('QuickStartScreen')

window_width = 210
window_height = 125

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

Label (root, text="Welcome to the QuickStart \nfor Multiplayer cardgames").grid(row=0,column=0)
Button (root, text="If you have an existing game\n click here to choose your games save", command=ChooseFile).grid(row=1, column=0)
Button (root, text="If you wish to open a new game \n Click here!", command=NewGameMenu).grid(row=2, column=0)
root.mainloop()