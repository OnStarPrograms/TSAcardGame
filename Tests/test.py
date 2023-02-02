from tkinter import *
from tkinter import filedialog
import base64
import random

"""all Available variables for the game:
PlayersUnUsedHand - Current Players Hand (Minus the chosen card)
UsedPlayersCard - Current Players Chosen card (Minus the Players Hand)
PlayerWhosFighting - Current Players chosen person to fight
ArrayofWhosFighting - array of all other players chosen people to fight (i.e. A Random player is fighting player 1 and another player is fighting player 2 == [1, 2])
ArrayofFightersCards - array of all other players Chosen card


Inorder to get past stuff in replit (not other systems, dont worry), you just have to close that leftover tk window.
"""

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

####Asks for Game File############

def AskForGameFile():
    root = Tk()
    def Upload():
        global a
        root.destroy()
        a = filedialog.askopenfilename()
    Button(root, text="Click to Choose the GameFile", command = Upload).pack()
    root.mainloop()
    return a


################# Data Parser and file reader ############
""" This Parser, when called,
will return the current players hand aswell as an array of other players
attacking who AND other players chosen 'shield' card (sorry) """


def OldFileChecking(TheOriginalFilename):

    file = open(TheOriginalFilename,"r")
    ListofData = file.read().split("\n")
    file.close()
    FirstPlayerHandFull = ListofData[0].split(">!")
    UnUsed1PlayerHand = FirstPlayerHandFull[0].split(">")
    Used1PlayerCard = FirstPlayerHandFull[1]
    Player1isFighting = int(ListofData[8])

    SecondPlayerHandFull = ListofData[1].split(">!")
    UnUsed2PlayerHand = SecondPlayerHandFull[0].split(">")
    Used2PlayerCard = SecondPlayerHandFull[1]
    Player2isFighting = int(ListofData[9])

    try:
        ThirdPlayerHandFull = ListofData[2].split(">!")
        UnUsed3PlayerHand = ThirdPlayerHandFull[0].split(">")
        Used3PlayerCard = ThirdPlayerHandFull[1]
        Player3isFighting = int(ListofData[10])
    except:
        ThirdPlayerHandFull = 0
        UnUsed3PlayerHand = 0
        Used3PlayerCard = 0
        Player3isFighting = 0

    try:
        FourthPlayerHandFull = ListofData[3].split(">!")
        UnUsed4PlayerHand = FourthPlayerHandFull[0].split(">")
        Used4PlayerCard = FourthPlayerHandFull[1]
        Player4isFighting = int(ListofData[11])
    except:
        FourthPlayerHandFull = 0
        UnUsed4PlayerHand = 0
        Used4PlayerCard = 0
        Player4isFighting = 0
    
    try:
        FifthPlayerHandFull = ListofData[4].split(">!")
        UnUsed5PlayerHand = FifthPlayerHandFull[0].split(">")
        Used5PlayerCard = FifthPlayerHandFull[1]
        Player5isFighting = int(ListofData[12])
    except:
        FifthPlayerHandFull = 0
        UnUsed5PlayerHand = 0
        Used5PlayerCard = 0
        Player5isFighting = 0

    CardOrder = ListofData[6].split(">")
    for i in range(len(CardOrder)):
      CardOrder[i] = int (CardOrder[i])
    PlayersTurn = int(ListofData[7][1])


    if (PlayersTurn == 1):
        for i in UnUsed1PlayerHand:
            print(i+"/ / "+Used1PlayerCard)
        try:
            for i in UnUsed5PlayerHand:
                print(i+"/ / "+Used5PlayerCard)
        except:
            print ("no 5th player Detected")

    if (PlayersTurn == 1):
        ArrayofFightersFighting = [Player2isFighting, Player3isFighting, Player4isFighting, Player5isFighting]
        FightersUsingCards = [Used2PlayerCard, Used3PlayerCard, Used4PlayerCard, Used5PlayerCard]
        return UnUsed1PlayerHand, Used1PlayerCard, Player1isFighting, ArrayofFightersFighting, FightersUsingCards, CardOrder, PlayersTurn
    
    if (PlayersTurn == 2):
        ArrayofFightersFighting = [Player1isFighting, Player3isFighting, Player4isFighting, Player5isFighting]
        FightersUsingCards = [Used1PlayerCard, Used3PlayerCard, Used4PlayerCard, Used5PlayerCard]
        return UnUsed2PlayerHand, Used2PlayerCard, Player2isFighting, ArrayofFightersFighting, FightersUsingCards, CardOrder, PlayersTurn

    if (PlayersTurn == 3):
        ArrayofFightersFighting = [Player1isFighting, Player2isFighting, Player4isFighting, Player5isFighting]
        FightersUsingCards = [Used1PlayerCard, Used2PlayerCard, Used4PlayerCard, Used5PlayerCard]
        return UnUsed3PlayerHand, Used3PlayerCard, Player3isFighting, ArrayofFightersFighting, FightersUsingCards, CardOrder, PlayersTurn

    if (PlayersTurn == 4):
        ArrayofFightersFighting = [Player1isFighting, Player2isFighting, Player3isFighting, Player5isFighting]
        FightersUsingCards = [Used1PlayerCard, Used2PlayerCard, Used3PlayerCard, Used5PlayerCard]
        return UnUsed4PlayerHand, Used4PlayerCard, Player4isFighting, ArrayofFightersFighting, FightersUsingCards, CardOrder, PlayersTurn

    if (PlayersTurn == 5):
        ArrayofFightersFighting = [Player1isFighting, Player2isFighting, Player3isFighting, Player4isFighting]
        FightersUsingCards = [Used1PlayerCard, Used2PlayerCard, Used3PlayerCard, Used4PlayerCard]
        return UnUsed5PlayerHand, Used5PlayerCard, Player5isFighting, ArrayofFightersFighting, FightersUsingCards, CardOrder, PlayersTurn

#######^ File Parser ^######
def EndFileWriter(PlayersUnUsedHand, UsedPlayersCard, PlayerWhosFighting, ArrayofWhosFighting, ArrayofFightersCards,  CardOrder, PlayerTurn, TheOriginalFilename):
  file = open(TheOriginalFilename,"r")
  ListofData = file.read().split("\n")
  file.close()
  print (ListofData)
  file = open(TheOriginalFilename,"w")
  file.write("")
  file.close()
  file = open(TheOriginalFilename, "a")

  
  if (PlayerTurn == 1):
    for i in range(len(PlayersUnUsedHand)):
      if (i != len(PlayersUnUsedHand)-1):
        file.write(PlayersUnUsedHand[i]+">")
    file.write(PlayersUnUsedHand[len(PlayersUnUsedHand)-1]+">!")
    file.write(UsedPlayersCard+"\n")
    file.write(ListofData[1]+"\n")
    file.write(ListofData[2]+"\n")
    file.write(ListofData[3]+"\n")
    file.write(ListofData[4]+"\n")
    file.write(ListofData[5]+"\n")
    file.write(ListofData[6]+"\n")
    file.write("P2\n")
    file.write(str(PlayerWhosFighting)+"\n")
    file.write(ListofData[9]+"\n")
    file.write(ListofData[10]+"\n")
    file.write(ListofData[11]+"\n")
    file.write(ListofData[12]+"\n")
    
  if (PlayerTurn == 2):
    file.write(ListofData[0]+"\n")
    for i in range(len(PlayersUnUsedHand)):
      if (i != len(PlayersUnUsedHand)-1):
        file.write(PlayersUnUsedHand[i]+">")
    file.write(PlayersUnUsedHand[len(PlayersUnUsedHand)-1]+">!")
    file.write(UsedPlayersCard+"\n")
    file.write(ListofData[2]+"\n")
    file.write(ListofData[3]+"\n")
    file.write(ListofData[4]+"\n")
    file.write(ListofData[5]+"\n")
    file.write(ListofData[6]+"\n")
    if (ArrayofWhosFighting[1] !=0):
      file.write("P3\n")
    else:
      file.write("P1\n")
    file.write(ListofData[8]+"\n")
    file.write(str(PlayerWhosFighting)+"\n")
    file.write(ListofData[10]+"\n")
    file.write(ListofData[11]+"\n")
    file.write(ListofData[12]+"\n")
  if (PlayerTurn == 3):
    file.write(ListofData[0]+"\n")
    file.write(ListofData[1]+"\n")
    for i in range(len(PlayersUnUsedHand)):
      if (i != len(PlayersUnUsedHand)-1):
        file.write(PlayersUnUsedHand[i]+">")
    file.write(PlayersUnUsedHand[len(PlayersUnUsedHand)-1]+">!")
    file.write(UsedPlayersCard+"\n")
    file.write(ListofData[3]+"\n")
    file.write(ListofData[4]+"\n")
    file.write(ListofData[5]+"\n")
    file.write(ListofData[6]+"\n")
    if (ArrayofWhosFighting[2] !=0):
      file.write("P4\n")
    else:
      file.write("P1\n")
    file.write(ListofData[8]+"\n")
    file.write(ListofData[9]+"\n")
    file.write(str(PlayerWhosFighting)+"\n")
    file.write(ListofData[11]+"\n")
    file.write(ListofData[12]+"\n")
    
  if (PlayerTurn == 4):
    file.write(ListofData[0]+"\n")
    file.write(ListofData[1]+"\n")
    file.write(ListofData[2]+"\n")
    for i in range(len(PlayersUnUsedHand)):
      if (i != len(PlayersUnUsedHand)-1):
        file.write(PlayersUnUsedHand[i]+">")
    file.write(PlayersUnUsedHand[len(PlayersUnUsedHand)-1]+">!")
    file.write(UsedPlayersCard+"\n")
    file.write(ListofData[4]+"\n")
    file.write(ListofData[5]+"\n")
    file.write(ListofData[6]+"\n")
    if (ArrayofWhosFighting[3] !=0):
      file.write("P5\n")
    else:
      file.write("P1\n")
    file.write(ListofData[8]+"\n")
    file.write(ListofData[9]+"\n")
    file.write(ListofData[10]+"\n")
    file.write(str(PlayerWhosFighting)+"\n")
    file.write(ListofData[12]+"\n")
    
    
  if (PlayerTurn == 5):
    file.write(ListofData[0]+"\n")
    file.write(ListofData[1]+"\n")
    file.write(ListofData[2]+"\n")
    file.write(ListofData[3]+"\n")
    for i in range(len(PlayersUnUsedHand)):
      if (i != len(PlayersUnUsedHand)-1):
        file.write(PlayersUnUsedHand[i]+">")
    file.write(PlayersUnUsedHand[len(PlayersUnUsedHand)-1]+">!")
    file.write(UsedPlayersCard+"\n")
    file.write(ListofData[5]+"\n")
    file.write(ListofData[6]+"\n")
    file.write("P1\n")
    file.write(ListofData[8]+"\n")
    file.write(ListofData[9]+"\n")
    file.write(ListofData[10]+"\n")
    file.write(ListofData[11]+"\n")
    file.write(str(PlayerWhosFighting)+"\n")

gameFilePlace = AskForGameFile()
PlayersUnUsedHand, UsedPlayersCard, PlayerWhosFighting, ArrayofWhosFighting, ArrayofFightersCards, CardOrder, PlayerTurn = OldFileChecking(gameFilePlace)
print (ArrayofWhosFighting)
print (ArrayofFightersCards)
EndFileWriter(PlayersUnUsedHand, UsedPlayersCard, PlayerWhosFighting, ArrayofWhosFighting, ArrayofFightersCards, CardOrder, PlayerTurn, gameFilePlace)
#####^ Returned Variable From the Data parser^#####
