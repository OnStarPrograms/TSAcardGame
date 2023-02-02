from tkinter import *
from tkinter import filedialog
import base64
import random
Modesy = "OG"

"""all Available variables for the game:
PlayersUnUsedHand - Current Players Hand (Minus the chosen card)
UsedPlayersCard - Current Players Chosen card (Minus the Players Hand)
PlayerWhosFighting - Current Players chosen person to fight
ArrayofWhosFighting - array of all other players chosen people to fight (i.e. A Random player is fighting player 1 and another player is fighting player 2 == [1, 2])
ArrayofFightersCards - array of all other players Chosen card


Inorder to get past stuff in replit (not other systems, dont worry), you just have to close that leftover tk window.
"""
################# Data Parser and file reader ############
""" This Parser, when called,
will return the current players hand aswell as an array of other players
attacking who AND other players chosen 'shield' card (sorry) """


def OldFileChecking(TheOriginalFilename):

  file = open(TheOriginalFilename, "r")
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
    CardOrder[i] = int(CardOrder[i])
  PlayersTurn = int(ListofData[7][1])

  if (PlayersTurn == 1):
    for i in UnUsed1PlayerHand:
      print(i + "/ / " + Used1PlayerCard)
    try:
      for i in UnUsed5PlayerHand:
        print(i + "/ / " + Used5PlayerCard)
    except:
      print("no 5th player Detected")

  if (PlayersTurn == 1):
    ArrayofFightersFighting = [
      Player2isFighting, Player3isFighting, Player4isFighting,
      Player5isFighting
    ]
    FightersUsingCards = [
      Used2PlayerCard, Used3PlayerCard, Used4PlayerCard, Used5PlayerCard
    ]
    return UnUsed1PlayerHand, Used1PlayerCard, Player1isFighting, ArrayofFightersFighting, FightersUsingCards, CardOrder, PlayersTurn, ListofData[
      13]

  if (PlayersTurn == 2):
    ArrayofFightersFighting = [
      Player1isFighting, Player3isFighting, Player4isFighting,
      Player5isFighting
    ]
    FightersUsingCards = [
      Used1PlayerCard, Used3PlayerCard, Used4PlayerCard, Used5PlayerCard
    ]
    return UnUsed2PlayerHand, Used2PlayerCard, Player2isFighting, ArrayofFightersFighting, FightersUsingCards, CardOrder, PlayersTurn, ListofData[
      13]

  if (PlayersTurn == 3):
    ArrayofFightersFighting = [
      Player1isFighting, Player2isFighting, Player4isFighting,
      Player5isFighting
    ]
    FightersUsingCards = [
      Used1PlayerCard, Used2PlayerCard, Used4PlayerCard, Used5PlayerCard
    ]
    return UnUsed3PlayerHand, Used3PlayerCard, Player3isFighting, ArrayofFightersFighting, FightersUsingCards, CardOrder, PlayersTurn, ListofData[
      13]

  if (PlayersTurn == 4):
    ArrayofFightersFighting = [
      Player1isFighting, Player2isFighting, Player3isFighting,
      Player5isFighting
    ]
    FightersUsingCards = [
      Used1PlayerCard, Used2PlayerCard, Used3PlayerCard, Used5PlayerCard
    ]
    return UnUsed4PlayerHand, Used4PlayerCard, Player4isFighting, ArrayofFightersFighting, FightersUsingCards, CardOrder, PlayersTurn, ListofData[
      13]

  if (PlayersTurn == 5):
    ArrayofFightersFighting = [
      Player1isFighting, Player2isFighting, Player3isFighting,
      Player4isFighting
    ]
    FightersUsingCards = [
      Used1PlayerCard, Used2PlayerCard, Used3PlayerCard, Used4PlayerCard
    ]
    return UnUsed5PlayerHand, Used5PlayerCard, Player5isFighting, ArrayofFightersFighting, FightersUsingCards, CardOrder, PlayersTurn, ListofData[
      13]


#######^ File Parser ^######


############################
def EndFileWriter(PlayersUnUsedHand, UsedPlayersCard, PlayerWhosFighting,
                  ArrayofWhosFighting, ArrayofFightersCards, CardOrder,
                  PlayerTurn, TheOriginalFilename):
  file = open(TheOriginalFilename, "r")
  ListofData = file.read().split("\n")
  file.close()
  file = open(TheOriginalFilename, "w")
  file.write("")
  file.close()
  file = open(TheOriginalFilename, "a")

  if (PlayerTurn == 1):
    for i in range(len(PlayersUnUsedHand)):
      if (i != len(PlayersUnUsedHand) - 1):
        file.write(PlayersUnUsedHand[i] + ">")
    file.write(PlayersUnUsedHand[len(PlayersUnUsedHand) - 1] + ">!")
    file.write(UsedPlayersCard + "\n")
    file.write(ListofData[1] + "\n")
    file.write(ListofData[2] + "\n")
    file.write(ListofData[3] + "\n")
    file.write(ListofData[4] + "\n")
    file.write(ListofData[5] + "\n")
    file.write(ListofData[6] + "\n")
    file.write("P2\n")
    file.write(str(PlayerWhosFighting) + "\n")
    file.write(ListofData[9] + "\n")
    file.write(ListofData[10] + "\n")
    file.write(ListofData[11] + "\n")
    file.write(ListofData[12] + "\n")
    file.write(ListofData[13] + "\n")

  if (PlayerTurn == 2):
    file.write(ListofData[0] + "\n")
    for i in range(len(PlayersUnUsedHand)):
      if (i != len(PlayersUnUsedHand) - 1):
        file.write(PlayersUnUsedHand[i] + ">")
    file.write(PlayersUnUsedHand[len(PlayersUnUsedHand) - 1] + ">!")
    file.write(UsedPlayersCard + "\n")
    file.write(ListofData[2] + "\n")
    file.write(ListofData[3] + "\n")
    file.write(ListofData[4] + "\n")
    file.write(ListofData[5] + "\n")
    file.write(ListofData[6] + "\n")
    if (ArrayofFightersCards[1] != 0):
      file.write("P3\n")
    else:
      file.write("P1\n")
    file.write(ListofData[8] + "\n")
    file.write(str(PlayerWhosFighting) + "\n")
    file.write(ListofData[10] + "\n")
    file.write(ListofData[11] + "\n")
    file.write(ListofData[12] + "\n")
    file.write(ListofData[13] + "\n")

  if (PlayerTurn == 3):
    file.write(ListofData[0] + "\n")
    file.write(ListofData[1] + "\n")
    for i in range(len(PlayersUnUsedHand)):
      if (i != len(PlayersUnUsedHand) - 1):
        file.write(PlayersUnUsedHand[i] + ">")
    file.write(PlayersUnUsedHand[len(PlayersUnUsedHand) - 1] + ">!")
    file.write(UsedPlayersCard + "\n")
    file.write(ListofData[3] + "\n")
    file.write(ListofData[4] + "\n")
    file.write(ListofData[5] + "\n")
    file.write(ListofData[6] + "\n")
    if (ArrayofFightersCards[2] != 0):
      file.write("P4\n")
    else:
      file.write("P1\n")
    file.write(ListofData[8] + "\n")
    file.write(ListofData[9] + "\n")
    file.write(str(PlayerWhosFighting) + "\n")
    file.write(ListofData[11] + "\n")
    file.write(ListofData[12] + "\n")
    file.write(ListofData[13] + "\n")

  if (PlayerTurn == 4):
    file.write(ListofData[0] + "\n")
    file.write(ListofData[1] + "\n")
    file.write(ListofData[2] + "\n")
    for i in range(len(PlayersUnUsedHand)):
      if (i != len(PlayersUnUsedHand) - 1):
        file.write(PlayersUnUsedHand[i] + ">")
    file.write(PlayersUnUsedHand[len(PlayersUnUsedHand) - 1] + ">!")
    file.write(UsedPlayersCard + "\n")
    file.write(ListofData[4] + "\n")
    file.write(ListofData[5] + "\n")
    file.write(ListofData[6] + "\n")
    if (ArrayofFightersCards[3] != 0):
      file.write("P5\n")
    else:
      file.write("P1\n")
    file.write(ListofData[8] + "\n")
    file.write(ListofData[9] + "\n")
    file.write(ListofData[10] + "\n")
    file.write(str(PlayerWhosFighting) + "\n")
    file.write(ListofData[12] + "\n")
    file.write(ListofData[13] + "\n")

  if (PlayerTurn == 5):
    file.write(ListofData[0] + "\n")
    file.write(ListofData[1] + "\n")
    file.write(ListofData[2] + "\n")
    file.write(ListofData[3] + "\n")
    for i in range(len(PlayersUnUsedHand)):
      if (i != len(PlayersUnUsedHand) - 1):
        file.write(PlayersUnUsedHand[i] + ">")
    file.write(PlayersUnUsedHand[len(PlayersUnUsedHand) - 1] + ">!")
    file.write(UsedPlayersCard + "\n")
    file.write(ListofData[5] + "\n")
    file.write(ListofData[6] + "\n")
    file.write("P1\n")
    file.write(ListofData[8] + "\n")
    file.write(ListofData[9] + "\n")
    file.write(ListofData[10] + "\n")
    file.write(ListofData[11] + "\n")
    file.write(str(PlayerWhosFighting) + "\n")
    file.write(ListofData[13] + "\n")


"""
DO NOT CALL THIS FUNCTION UNLESS YOU TALK TO ME ABOUT WHERE IT GOES, ITS A BIT TOUCHY ON SOME THINGS
"""


############^ End of turn File Writer ^##############
def newGameSystem(AmountPlayers, gameMode):
  Player1cards = []
  Player2cards = []
  Player3cards = []
  Player4cards = []
  Player5cards = []
  Cards = [
    'K', '5', '9', '8', '7', '6', '5', '4', '2', 'A', 'J', 'K', '7', '9',
    '8', '7', '6', '5', '4', '2', 'A', 'J', 'K', '6', '9', '8', '7', '6', '5',
    '4', '2', 'A', 'K', '9', '9', '8', '7', '6', '5', '4', '2', 'A', 'K',
    '9', '9', '8', '7', '6', '5', '4', '2', 'A', 'J', 'K', '9', '9', '8',
    '7', '6', '5', '4', '2', 'A', 'J'
  ]
  if (AmountPlayers == 2):
    for i in range(8):
      Player1cards.append(random.choice(Cards))
      Player2cards.append(random.choice(Cards))
    Player3cards.append('0')
    Player4cards.append('0')
    Player5cards.append('0')

  if (AmountPlayers == 3):
    for i in range(8):
      Player1cards.append(random.choice(Cards))
      Player2cards.append(random.choice(Cards))
      Player3cards.append(random.choice(Cards))
    Player4cards.append('0')
    Player5cards.append('0')

  if (AmountPlayers == 4):
    for i in range(8):
      Player1cards.append(random.choice(Cards))
      Player2cards.append(random.choice(Cards))
      Player3cards.append(random.choice(Cards))
      Player4cards.append(random.choice(Cards))
    Player5cards.append('0')

  if (AmountPlayers == 5):
    for i in range(8):
      Player1cards.append(random.choice(Cards))
      Player2cards.append(random.choice(Cards))
      Player3cards.append(random.choice(Cards))
      Player4cards.append(random.choice(Cards))
      Player5cards.append(random.choice(Cards))

  try:
    f = open("GameTransferData.txt", "x")
    f.write("")
    f.close()
  except:
    print("No Need")
  f = open("GameTransferData.txt", "w")
  f.write("")
  f.close()
  f = open("GameTransferData.txt", "a")
  for i in range(len(Player1cards)):
    if (i < len(Player1cards) - 2):
      f.write(Player1cards[i] + ">")
    elif (i != len(Player1cards) - 1):
      f.write(Player1cards[i] + ">!")
  f.write(Player1cards[len(Player1cards) - 1] + "\n")

  for i in range(len(Player2cards)):
    if (i < len(Player2cards) - 2):
      f.write(Player2cards[i] + ">")
    elif (i != len(Player2cards) - 1):
      f.write(Player2cards[i] + ">!")
  f.write(Player2cards[len(Player2cards) - 1] + "\n")

  for i in range(len(Player3cards)):
    if (i < len(Player3cards) - 2):
      f.write(Player3cards[i] + ">")
    elif (i != len(Player3cards) - 1):
      f.write(Player3cards[i] + ">!")
  f.write(Player3cards[len(Player3cards) - 1] + "\n")

  for i in range(len(Player4cards)):
    if (i < len(Player4cards) - 2):
      f.write(Player4cards[i] + ">")
    elif (i != len(Player4cards) - 1):
      f.write(Player4cards[i] + ">!")
  f.write(Player4cards[len(Player4cards) - 1] + "\n")

  for i in range(len(Player5cards)):
    if (i < len(Player5cards) - 2):
      f.write(Player5cards[i] + ">")
    elif (i != len(Player5cards) - 1):
      f.write(Player5cards[i] + ">!")
  f.write(Player5cards[len(Player5cards) - 1] + "\n")

  f.write('0\n')
  f.write('10>9>8>7>6>5>4>3>2>1\n')
  f.write('P1\n')
  for i in range(5):
    f.write('0\n')
  f.write(gameMode)
  f.close()
  print("Finished Creating a new game!")

def StartGame():
  global gameFilePlace
  gameFilePlace = filedialog.askopenfilename()

def Fight(UsedPlayersCard, ArrayofFightersCards, ArrayofWhosFighting, CardOrder, PlayerTurn):
  temp1 = 0
  LostTo = []
  if (UsedPlayersCard == "K"):
    UsedPlayersCard = 11
  elif (UsedPlayersCard == "A"):
    UsedPlayersCard = 0
  else:
    UsedPlayersCard = int(UsedPlayersCard)
  for i in range(len(CardOrder)):
    CardOrder[i] = int(CardOrder[i])
  for k in ArrayofWhosFighting:
    if (int(k)==PlayerTurn):
        for j in range(len(ArrayofFightersCards)):
          if (temp1 == 0):
            temp1 = None
          if (ArrayofFightersCards[j] == "K"):
            temp1 = 11
          elif (ArrayofFightersCards[j] == "A"):
            temp1 = 0
          else:
            temp1 = int(ArrayofFightersCards[j])
            if (temp1 == 0):
              temp1 = UsedPlayersCard
          if (temp1 > UsedPlayersCard):
              if (temp1 != 11):
                if (UsedPlayersCard != 0):
                  LostTo.append(temp1)
          if (temp1 == 0 and UsedPlayersCard == 11):
            LostTo.append(1)
  return LostTo

###########################
def changeChosenCard(a, PlayersUnUsedHand, UsedPlayerCard):
  global UpdatedUnUsedPlayersHand
  global UsedPlayersCard
  for i in range(len(PlayersUnUsedHand)):
    if (PlayersUnUsedHand[i] == a):
      PlayersUnUsedHand.append(UsedPlayerCard)
      UsedPlayerCard = PlayersUnUsedHand[i]
      PlayersUnUsedHand.pop(i)
  UpdatedUnUsedPlayersHand = PlayersUnUsedHand
  UsedPlayersCard = UsedPlayerCard
  GameControl(UpdatedUnUsedPlayersHand, UsedPlayersCard, PlayerWhosFighting,
            ArrayofWhosFighting, ArrayofFightersCards, CardOrder,
            PlayerTurn, GameMode, gameFilePlace)

def Chat():
  None

###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
def LostFightsRules(arrayoflostfights, UnUsedPlayersHand):
  lostcards = 0
  for i in arrayoflostfights:
    if (i<=11 and i>=8):
      UnUsedPlayersHand.pop(random.randrange(0,len(UnUsedPlayersHand)))
      lostcards += 1
    elif (i<=7 and i>=4):
      UnUsedPlayersHand.pop(random.randrange(0,len(UnUsedPlayersHand)))
      UnUsedPlayersHand.pop(random.randrange(0,len(UnUsedPlayersHand)))
      lostcards += 2
    elif (i==3):
      UnUsedPlayersHand.pop(random.randrange(0,len(UnUsedPlayersHand)))
      UnUsedPlayersHand.pop(random.randrange(0,len(UnUsedPlayersHand)))
      UnUsedPlayersHand.pop(random.randrange(0,len(UnUsedPlayersHand)))
      lostcards += 3
    elif (i<=2 and i>=0):
      UnUsedPlayersHand.pop(random.randrange(0,len(UnUsedPlayersHand)))
      UnUsedPlayersHand.pop(random.randrange(0,len(UnUsedPlayersHand)))
      UnUsedPlayersHand.pop(random.randrange(0,len(UnUsedPlayersHand)))
      UnUsedPlayersHand.pop(random.randrange(0,len(UnUsedPlayersHand)))
      lostcards += 4
  textofloss = "You Lost "+str(lostcards)+" Cards This Round\nDue to Losing Your Fights"
  root = Tk()
  root.wm_attributes("-topmost", 1)
  root.configure(bg='black')
  window_width = 200
  window_height = 100

    # get the screen dimension
  screen_width = root.winfo_screenwidth()
  screen_height = root.winfo_screenheight()

    # find the center point
  center_x = int(screen_width / 2 - window_width / 2)
  center_y = int(screen_height / 2 - window_height / 2)

    # set the position of the window to the center of the screen
  root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
  Label(root, text = textofloss, fg="#1F51FF",  bg = "black" ).pack()
  Button(root, text = "ok", command = root.destroy, highlightbackground = "#1F51FF", highlightthickness = 3, bg ="black" ,activebackground="#ADD8E6", fg="#1F51FF", activeforeground= "#1F51FF").pack()
  root.mainloop()

  return UnUsedPlayersHand


def UseJoker(ArrayofFightersCards):
  global UpdatedUnUsedPlayersHand
  for i in range(len(UpdatedUnUsedPlayersHand)):
    if (UpdatedUnUsedPlayersHand[i] == "J"):
      UpdatedUnUsedPlayersHand.pop(i)
      break
  b = 0
  rooty = Tk()
  rooty.configure(bg='black')
  window_width = 700
  window_height = 100

    # get the screen dimension
  screen_width = rooty.winfo_screenwidth()
  screen_height = rooty.winfo_screenheight()

    # find the center point
  center_x = int(screen_width / 2 - window_width / 2)
  center_y = int(screen_height / 2 - window_height / 2)

    # set the position of the window to the center of the screen
  rooty.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
  rooty.wm_attributes("-topmost", 1)
  if (PlayerTurn == 1):
    a = 2
    for i in ArrayofFightersCards:
      Label(rooty, text = "Player"+str(a)+" Chosen Card", fg="#1F51FF",  bg = "black").place(x = 0+b, y = 0)
      Label(rooty, text = i, fg="#1F51FF",  bg = "black").place(x =b, y = 50)
      a+=1
      b+=150
  if (PlayerTurn == 2):
    a = 1
    for i in ArrayofFightersCards:
      Label(rooty, text = "Player"+str(a)+" Chosen Card", fg="#1F51FF",  bg = "black").place(x = 0+b, y = 0)
      Label(rooty, text = i, fg="#1F51FF",  bg = "black").place(x = b, y = 50)
      if (a == 1):
        a+=2
      else:
        a+=1
      b += 150
  if (PlayerTurn == 3):
    a = 1
    for i in ArrayofFightersCards:
      Label(rooty, text = "Player"+str(a)+" Chosen Card", fg="#1F51FF",  bg = "black").place(x = 0+b, y = 0)
      Label(rooty, text = i, fg="#1F51FF",  bg = "black").place(x = b, y = 50)
      if (a == 2):
        a+=2
      else:
        a+=1
      b+=150
  if (PlayerTurn == 4):
    a = 1
    for i in ArrayofFightersCards:
      Label(rooty, text = "Player"+str(a)+" Chosen Card",fg="#1F51FF",  bg = "black").place(x = 0+b, y = 0)
      Label(rooty, text = i, fg="#1F51FF",  bg = "black").place(x = b, y = 50)
      if (a == 3):
        a+=2
      else:
        a+=1
      b+=150
  if (PlayerTurn == 5):
    a = 1
    for i in ArrayofFightersCards:
      Label(rooty, text = "Player"+str(a)+" Chosen Card", fg="#1F51FF",  bg = "black").place(x = 0+b, y = 0)
      Label(rooty, text = i, fg="#1F51FF",  bg = "black").place(x = b, y = 50)
      if (a == 4):
        a+=2
      else:
        a+=1
      b+=150
  rooty.mainloop()
  None


def Register():
  root = Tk()
  root.configure(bg='black')
  Label(root, text="Button Input Registered", fg="#1F51FF",  bg = "black").pack()
  root.after(1500, lambda: root.destroy())
  root.mainloop()


def errorHandling():
  root = Tk()
  root.configure(bg='black')
  Label(root, text="Error: please input all required buttons", fg="#1F51FF",  bg = "black").pack()
  root.after(1500, lambda: root.destroy())
  root.mainloop()


def FinishedWriting():
  root = Tk()
  root.configure(bg='black')
  Label(
    root,
    text=
    "Finished Writing game info,\n Search for 'GameTransferData.txt'\n Send game file to the next player in turn.\n Restart the game client."
  , fg="#1F51FF",  bg = "black").pack()
  root.after(15000, lambda: root.destroy())
  root.mainloop()

def Choosefight():
  global PlayerWhosFighting
  rooty = Tk()
  rooty.configure(bg='black')
  window_width = 200
  window_height = 200

    # get the screen dimension
  screen_width = rooty.winfo_screenwidth()
  screen_height = rooty.winfo_screenheight()

    # find the center point
  center_x = int(screen_width / 2 - window_width / 2)
  center_y = int(screen_height / 2 - window_height / 2)

    # set the position of the window to the center of the screen
  rooty.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

  def input():
        global PlayerWhosFighting
        NewInsert = str(inputtxt.get("1.0", "end"))
        NewInsert1 = NewInsert.split("\n")
        PlayerWhosFighting = NewInsert1[0]
        rooty.destroy()
        rooti = Tk()
        rooti.configure(bg='black')
        Label(rooti, text = "Registered: Attack Player "+NewInsert, fg="#1F51FF",  bg = "black").pack()
        rooti.after(1500, lambda: rooti.destroy())
        rooti.mainloop()


  Label(rooty, text = "Type in player # you wish to attack.", fg="#1F51FF",  bg = "black").place(x = 0, y = 0)
  Label(rooty, text = "Player Number: ", fg="#1F51FF",  bg = "black").place(x = 0, y = 50)
  inputtxt = Text(rooty,  height = 1, width = 1)
  inputtxt.bind("<FocusIn>", lambda args: inputtxt.delete('1.0', 'end'))
  inputtxt.place(x = 100, y = 50)
  Button (rooty, text = "Input your Person", command = input, highlightbackground = "#1F51FF", highlightthickness = 3, bg ="black" ,activebackground="#ADD8E6", fg="#1F51FF", activeforeground= "#1F51FF").place(x = 70, y = 100)
  rooty.mainloop()


####Asks for Game File############

def CreateNewGamey():
  root = Tk()
  root.configure(bg='black')
  root.attributes("-topmost", 1)
  window_width = 700
  window_height = 200

  # get the screen dimension
  screen_width = root.winfo_screenwidth()
  screen_height = root.winfo_screenheight()

  # find the center point
  center_x = int(screen_width / 2 - window_width / 2)
  center_y = int(screen_height / 2 - window_height / 2)

  def FreePlay():
    global Modesy
    Modesy = "OG"
    Register()

  def FileCreate():
    root.destroy()
    newGameSystem(Players, Modesy)

  def FivePlayer():
    global Players
    Players = 5
    Register()

  def TwoPlayer():
    global Players
    Players = 2
    Register()

  def ThreePlayer():
    global Players
    Players = 3
    Register()

  def FourPlayer():
    global Players
    Players = 4
    Register()

  # set the position of the window to the center of the screen
  root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

  Label(root, text="Which GameMode Would You Like?", fg="#1F51FF",  bg = "black").grid(row=2, column=0)
  Button(root, text="FreePlay", command=FreePlay, highlightbackground = "#1F51FF", highlightthickness = 3, bg ="black" ,activebackground="#ADD8E6", fg="#1F51FF", activeforeground= "#1F51FF").grid(row=3, column=1)
  #Button(root, text="Randomize Card", command=FreePlay).grid(row=3, column=2)
  Label(root, text="How many people will be playing?", fg="#1F51FF",  bg = "black").grid(row=4, column=0)
  Label(root, text="----------->", fg="#1F51FF",  bg = "black").grid(row=5, column=0)
  Button(root, text="2", command=TwoPlayer,highlightbackground = "#1F51FF", highlightthickness = 3, bg ="black" ,activebackground="#ADD8E6", fg="#1F51FF", activeforeground= "#1F51FF" ).grid(row=5, column=1)
  Button(root, text="3", command=ThreePlayer,highlightbackground = "#1F51FF", highlightthickness = 3, bg ="black" ,activebackground="#ADD8E6", fg="#1F51FF", activeforeground= "#1F51FF" ).grid(row=5, column=2)
  Button(root, text="4", command=FourPlayer,highlightbackground = "#1F51FF", highlightthickness = 3, bg ="black" ,activebackground="#ADD8E6", fg="#1F51FF", activeforeground= "#1F51FF" ).grid(row=5, column=3)
  Button(root, text="5", command=FivePlayer,highlightbackground = "#1F51FF", highlightthickness = 3, bg ="black" ,activebackground="#ADD8E6", fg="#1F51FF", activeforeground= "#1F51FF" ).grid(row=5, column=4)
  Button(root, text="Input Your Choice", command=FileCreate,highlightbackground = "#1F51FF", highlightthickness = 3, bg ="black" ,activebackground="#ADD8E6", fg="#1F51FF", activeforeground= "#1F51FF" ).grid(row=7,
                                                                  column=0)

  root.mainloop()


def QuickStartScreen():

  root = Tk()
  root.configure(bg='black')
  root.title('QuickStartScreen')
  root.attributes("-topmost", 1)
  root.configure(bg='black')

  window_width = 280
  window_height = 225

  # get the screen dimension
  screen_width = root.winfo_screenwidth()
  screen_height = root.winfo_screenheight()

  # find the center point
  center_x = int(screen_width / 2 - window_width / 2)
  center_y = int(screen_height / 2 - window_height / 2)

  # set the position of the window to the center of the screen
  root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

  def NewGame():
    global gameFilePlace
    root.destroy()
    CreateNewGamey()
    gameFilePlace = "GameTransferData.txt"

  def StartingGame():
    root.destroy()
    StartGame()

  Label(root,
        text="Welcome to the QuickStart \nfor Multiplayer cardgames",  bg = "black", fg = "#1F51FF").grid(
          row=0, column=0)
  Button(
    root,
    text="If you have an existing game\n click here to choose your games save",
    command=StartingGame, highlightbackground = "#1F51FF", highlightthickness = 3, bg ="black" ,activebackground="#ADD8E6", fg="#1F51FF", activeforeground= "#1F51FF").grid(row=1, column=0)
  Button(root,
         text="If you wish to open a new game \n Click here!",
         command=NewGame, highlightbackground = "#1F51FF", highlightthickness = 3, bg ="black" ,activebackground="#ADD8E6", fg="#1F51FF", activeforeground= "#1F51FF").place(x=15, y=100)
  root.mainloop()



  ##########################

def ShowLoss(textofloss):
  root = Tk()
  root.configure(bg='black')
  root.wm_attributes("-topmost", 1)
  window_width = 200
  window_height = 100

  # get the screen dimension
  screen_width = root.winfo_screenwidth()
  screen_height = root.winfo_screenheight()

  # find the center point
  center_x = int(screen_width / 2 - window_width / 2)
  center_y = int(screen_height / 2 - window_height / 2)

  # set the position of the window to the center of the screen
  root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
  Label(root, text = textofloss, fg="#1F51FF",  bg = "black").pack()
  Button(root, text = "ok", command = root.destroy,highlightbackground = "#1F51FF", highlightthickness = 3, bg ="black" ,activebackground="#ADD8E6", fg="#1F51FF", activeforeground= "#1F51FF" ).pack()
  root.mainloop()

def MainMenu():
  root = Tk()
  root.configure(bg='black')
  root.attributes("-topmost", 1)
  root.configure(bg='black')
  window_width = root.winfo_screenwidth()
  window_height = root.winfo_screenwidth()
  root.geometry(f'{window_width}x{window_height}+{0}+{0}')
  def startgame():
    root.destroy()
  def HowtoPlay():
    toplvl = Toplevel()
    toplvl.attributes("-topmost", 1)
    toplvl.configure(bg="black")
    Label(toplvl, text = "the goal of this game is to be that last person with cards", fg="#1F51FF",  bg = "black").pack()
    Label(toplvl, text = "you are given 12 cards to be in your hand", fg="#1F51FF",  bg = "black").pack()
    Label(toplvl, text = "",  bg = "black").pack()
    Label(toplvl, text = "the cards from highest to lowest is king, 9, 8, 7, 6, 5, 4, 3, 2, Ace", fg="#1F51FF",  bg = "black").pack()
    Label(toplvl, text = "Ace has special rules, when it is played against the King it wins, otherwise the Ace will always loose", fg="#1F51FF",  bg = "black").pack()
    Label(toplvl, text = "There is even a special card!: the Jack. The Jack is a card that can be used to see all other players choice cards (just incase you want to attack someone and win)\n THE JACK CAN NOT HELP YOU DECIDE ON A CHOSEN CARD", fg="#1F51FF",  bg = "black").pack()
    Label(toplvl, text = "",  bg = "black").pack()
    Label(toplvl, text = "each round you may choose one card from your hand and put it into play; this card protects you from incoming attacks while also attacking a chosen player.", fg="#1F51FF",  bg = "black").pack()
    Label(toplvl, text = "after you have chosen your card, you must choose a player to attack", fg="#1F51FF",  bg = "black").pack()
    Label(toplvl, text = "",  bg = "black").pack()
    Label(toplvl, text = "The turn based system is classified as 'Ongoing', attacks aimed at you are played out at the start of your turn", fg="#1F51FF",  bg = "black").pack()
    Label(toplvl, text = " if the attacking players card is higher than the defenders card, the attacker wins and the defender suffers the punishment of the attacking card", fg="#1F51FF",  bg = "black").pack()
    Label(toplvl, text = "",  bg = "black").pack()
    Label(toplvl, text = "Card punishments: King to 7 - discard 1 card; 6 to 4 - discard 2 cards; 3 - discard 3 cards; 2 & Aces - discard 4 cards", fg="#1F51FF",  bg = "black").pack()
    Label(toplvl, text = "if the defender wins against the attackers no punishments are used. After the round ends all played cards get removed from the game", fg="#1F51FF",  bg = "black").pack()
    Label(toplvl, text = "",  bg = "black").pack()
    Label(toplvl, text = "",  bg = "black").pack()
    Label(toplvl, text = "This game is a game of strategy and having the ability to 'decode' the other players choices. you can even create pacts with other players!", fg="#1F51FF",  bg = "black").pack()
    Label(toplvl, text = "",  bg = "black").pack()
    Label(toplvl, text = "This game is better played with the usage of private messaging, then you can brutally backstab whoever you want :)", fg="#1F51FF",  bg = "black").pack()
    
    Label(toplvl, text = "",  bg = "black").pack()
    Button(toplvl, text = "ok", command = toplvl.destroy, highlightbackground = "#1F51FF", highlightthickness = 3, bg ="black" ,activebackground="#ADD8E6", fg="#1F51FF", activeforeground= "#1F51FF").pack()
    toplvl.mainloop()
  # set the position of the window to the center of the screen
  Label(root, text = "—---  \\    /  1==   1 \\  / ==  \\    \\\\  //  /  11\\  -===11111==111  /111     101       01 \nI  |  \\  \\  |  (        /  /\\_\\|F/    \\  \\    \\V/  |F/    \\\\        10|         |   |    ||     11  1101     01  \nI  |   )  }|   =1=|  (  _ |0\\_  /_/    1|   1  \\_ 1/        |  1         |01    ||     11  11101   11  \nI  |  /  /  |0(        \\  \\/  /|  |  \\01     ||   |01             |01         101   11   11  11   10111  \n—---  /    \\  ===  \\_  /  |_|    10\\  |1   101            101      11111  1111    11     1001 \n", fg="#1F51FF",  bg = "black", justify= LEFT).place(x=160, y=50)
  Button(root, text="Start Game", command = startgame, highlightbackground = "#1F51FF", highlightthickness = 3, bg ="black" ,activebackground="#ADD8E6", fg="#1F51FF", activeforeground= "#1F51FF", height=2, width=10).place(x = 350, y = 200)
  Button(root, text="How to play", command = HowtoPlay, highlightbackground = "#1F51FF", highlightthickness = 3, bg ="black", activebackground="#ADD8E6", fg="#1F51FF", activeforeground= "#1F51FF",height=2, width=10).place(x = 350, y = 300)
  

  root.mainloop()



def GameControl(PlayersUnUsedHand, UsedPlayersCard, PlayerWhosFighting,
                ArrayofWhosFighting, ArrayofFightersCards, CardOrder,
                PlayerTurn, GameMode, gamefilePlace):
  root = Tk()
  root.configure(bg='black')                
  window_width = root.winfo_screenwidth()
  window_height = root.winfo_screenwidth()
  root.geometry(f'{window_width}x{window_height}+{0}+{0}')
  a = 0
  b = 0
  test = 0
  test1 = 0
  for i in PlayersUnUsedHand:
    if (i == '0' or i == 0):
      test+=1
  for i in ArrayofFightersCards:
    if (i == '0' or i == 0):
      test1+=1
  if (test != len(PlayersUnUsedHand)):
    if (test1 != len(ArrayofFightersCards)):
      if (UsedPlayersCard == 'K'):
        Label(root, text="KKKKKKKKKKKKKKKKKKKK\nKKK KKKKK  KKKKK KKK\nKKK  KKKK  KKKK  KKK\nKKK   KK    KK   KKK\nKKK    K    K    KKK\nKKK              KKK\nKKKKKKKKKKKKKKKKKKKK\nKKKKK  KKKKKK  KKKKK\nKKKKKKKK    KKKKKKKK\nKKKKKKKKKKKKKKKKKKKK", fg="#9D00FF",  bg = "black").place(x=500, y=350)
        Label(root, text="'Chosen Card'", fg="#9D00FF",  bg = "black").place(x=500, y=500)
      if (UsedPlayersCard == '9'):
        Label(root, text="99999999999999999999\n9999                        9999\n999        999999        999\n999    9999999999    999\n999       999999         999\n9999                          999\n9999999999999        999\n9999    999999        9999\n99999                  999999\n99999999999999999999", fg="#FF3131",  bg = "black").place(x=500, y=350)
        Label(root, text="'Chosen Card'", fg="#FF3131",  bg = "black").place(x=500, y=500)
      if (UsedPlayersCard == '8'):
        Label(root, text="8888888888888888888\n88888                  88888\n888      8888888      888\n888      8888888      888\n8888      88888      8888\n88888                  88888\n8888      88888      8888\n888      8888888      888\n88888                  88888\n8888888888888888888", fg="#FF3131",  bg = "black").place(x=500, y=350)
        Label(root, text="'Chosen Card'", fg="#FF3131",  bg = "black").place(x=500, y=500)
      if (UsedPlayersCard == '7'):
        Label(root, text="77777777777777777777\n7777                            77\n777                              77\n77777777777777        77\n7777777777777          77\n777777777777          777\n77777777777          7777\n7777777777          77777\n777777777          777777\n77777777777777777777", fg="#FF3131",  bg = "black").place(x=500, y=350)
        Label(root, text="'Chosen Card'", fg="#FF3131",  bg = "black").place(x=500, y=500)
      if (UsedPlayersCard == '6'):
        Label(root, text="66666666666666666666\n6666666                66666\n66666     666666     6666\n6666      6666666666666\n666                          6666\n666        666666        666\n666    6666666666    666\n666        666666        666\n6666                        6666\n66666666666666666666", fg="#FF3131",  bg = "black").place(x=500, y=350)
        Label(root, text="'Chosen Card'", fg="#FF3131",  bg = "black").place(x=500, y=500)
      if (UsedPlayersCard == '5'):
        Label(root, text="55555555555555555555\n5555                          555\n5555      5555555555555\n5555      5555555555555\n5555                          555\n55555555555555        55\n555555555555555      55\n5555   55555555        555\n5555                          555\n55555555555555555555", fg="#FFFF33",  bg = "black").place(x=500, y=350)
        Label(root, text="'Chosen Card'", fg="#FFFF33",  bg = "black").place(x=500, y=500)
      if (UsedPlayersCard == '4'):
        Label(root, text="4444444444444444\n4444444      444444\n444444        444444\n44444    44   444444\n4444    444   444444\n444    4444   444444\n444                     444\n444444444   444444\n444444444   444444\n44444444444444444", fg="#FFFF33",  bg = "black").place(x=500, y=350)
        Label(root, text="'Chosen Card'", fg="#FFFF33", bg = "black").place(x=500, y=500)
      if (UsedPlayersCard == '3'):
        Label(root, text="33333333333333333333\n3333                        3333\n33       333333333       33\n333333333333333      33\n3333333333333        333\n333333333            33333\n3333333333333        333\n33       333333333       33\n3333                          333\n33333333333333333333", fg="#FFFF33",  bg = "black").place(x=500, y=350)
        Label(root, text="'Chosen Card'", fg="#FFFF33").place(x=500, y=500)
      if (UsedPlayersCard == '2'):
        Label(root, text="22222222222222222222\n222222                222222\n2222      22222      22222\n222     22222222     2222\n22222222222222    2222\n22222222222        22222\n222222            22222222\n2222        222222222222\n222                             222\n22222222222222222222", fg="#FFFF33",  bg = "black").place(x=500, y=350)
        Label(root, text="'Chosen Card'", fg="#FFFF33",  bg = "black").place(x=500, y=500)
      if (UsedPlayersCard == 'A'):
        Label(root, text="AAAAAAAAAAAAAAAAAAAA\nAAAAAAAA                AAAAAA\nAAAAAAA                   AAAAAA\nAAAAAA         A          AAAAAA\nAAAAA         AA          AAAAAA\nAAAA         AAA          AAAAAA\nAAA         AAAA          AAAAAA\nAA         AAAAA          AAAAAA\n                                         AAAAA\nA       AAAAAAA          AAAAAA", fg="#FF10F0",  bg = "black").place(x=500, y=350)
        Label(root, text="'Chosen Card'", fg="#FF10F0",  bg = "black").place(x=500, y=500)
      if (UsedPlayersCard == 'J'):
        Label(root, text="JjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJj\nJjJj   JjJjJjJjJjJjJjJjJjJj   JjJj\nJj JjJj    JjJjJjJj    JjJj Jj\nJjJjJjJjJj    JjJj    JjJjJjJjJj\nJjJjJj              JjJjJj\nJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJj\nJjJjJjJj JjJjJjJjJjJjJjJjJjJj JjJjJjJj\nJjJjJj Jj JjJjJjJjJjJjJjJj Jj JjJjJj\nJjJjJjJj JjJjJj    JjJjJj JjJjJjJj\nJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJj", fg="#39FF14",  bg = "black").place(x=500, y=350)
        Label(root, text="'Chosen Card'", fg="#39FF14",  bg = "black").place(x=500, y=500)
      if (UsedPlayersCard == '0'):
        Label(root, text="You Have Lost Your Chosen Card", fg="#1F51FF",  bg = "black").place(x=500, y=350)
        Label(root, text="'Chosen Card'", fg="#1F51FF",  bg = "black").place(x=500, y=500)
      for i in PlayersUnUsedHand:
    
        def ChosenCardK():
          root.destroy()
          changeChosenCard('K', PlayersUnUsedHand, UsedPlayersCard)
    
        def ChosenCard9():
          root.destroy()
          changeChosenCard('9', PlayersUnUsedHand, UsedPlayersCard)
    
        def ChosenCard8():
          root.destroy()
          changeChosenCard('8', PlayersUnUsedHand, UsedPlayersCard)
    
        def ChosenCard7():
          root.destroy()
          changeChosenCard('7', PlayersUnUsedHand, UsedPlayersCard)
    
        def ChosenCard6():
          root.destroy()
          changeChosenCard('6', PlayersUnUsedHand, UsedPlayersCard)
    
        def ChosenCard5():
          root.destroy()
          changeChosenCard('5', PlayersUnUsedHand, UsedPlayersCard)
    
        def ChosenCard4():
          root.destroy()
          changeChosenCard('4', PlayersUnUsedHand, UsedPlayersCard)
    
        def ChosenCard3():
          root.destroy()
          changeChosenCard('3', PlayersUnUsedHand, UsedPlayersCard)
    
        def ChosenCard2():
          root.destroy()
          changeChosenCard('2', PlayersUnUsedHand, UsedPlayersCard)
    
        def ChosenCarda():
          root.destroy()
          changeChosenCard('A', PlayersUnUsedHand, UsedPlayersCard)
    
        def ChosenCardj():
          UseJoker(ArrayofFightersCards)
    
        if (i == 'K'):
          Label(root, text="KKKKKKKKKKKKKKKKKKKK\nKKK KKKKK  KKKKK KKK\nKKK  KKKK  KKKK  KKK\nKKK   KK    KK   KKK\nKKK    K    K    KKK\nKKK              KKK\nKKKKKKKKKKKKKKKKKKKK\nKKKKK  KKKKKK  KKKKK\nKKKKKKKK    KKKKKKKK\nKKKKKKKKKKKKKKKKKKKK", fg="#9D00FF",  bg = "black").place(x=50 + a,
                                                                 y=50 + b)
          Button(root, text="Use as your 'Chosen Card'",
                 command=ChosenCardK, highlightbackground = "#9D00FF", highlightthickness = 3, bg ="black" ,activebackground="#CBC3E3", fg="#9D00FF", activeforeground= "#9D00FF").place(x=50 + a, y=250 + b)
        if (i == '9'):
          Label(root, text="99999999999999999999\n9999                        9999\n999        999999        999\n999    9999999999    999\n999       999999         999\n9999                          999\n9999999999999        999\n9999    999999        9999\n99999                  999999\n99999999999999999999", fg="#FF3131",  bg = "black").place(x=50 + a,
                                                                 y=50 + b)
          Button(root, text="Use as your 'Chosen Card'",
                 command=ChosenCard9,highlightbackground = "#FF3131", highlightthickness = 3, bg ="black" ,activebackground="#FFCCCB", fg="#FF3131", activeforeground= "#FF3131" ).place(x=50 + a, y=250 + b)
        if (i == '8'):
          Label(root, text="8888888888888888888\n88888                  88888\n888      8888888      888\n888      8888888      888\n8888      88888      8888\n88888                  88888\n8888      88888      8888\n888      8888888      888\n88888                  88888\n8888888888888888888", fg="#FF3131",  bg = "black").place(x=50 + a,
                                                                  y=50 + b)
          Button(root, text="Use as your 'Chosen Card'",
                 command=ChosenCard8, highlightbackground = "#FF3131", highlightthickness = 3, bg ="black" ,activebackground="#FFCCCB", fg="#FF3131", activeforeground= "#FF3131" ).place(x=50 + a, y=250 + b)
        if (i == '7'):
          Label(root, text="77777777777777777777\n7777                            77\n777                              77\n77777777777777        77\n7777777777777          77\n777777777777          777\n77777777777          7777\n7777777777          77777\n777777777          777777\n77777777777777777777", fg="#FF3131",  bg = "black").place(x=50 + a,
                                                                  y=50 + b)
          Button(root, text="Use as your 'Chosen Card'",
                 command=ChosenCard7, highlightbackground = "#FF3131", highlightthickness = 3, bg ="black" ,activebackground="#FFCCCB", fg="#FF3131", activeforeground= "#FF3131" ).place(x=50 + a, y=250 + b)
        if (i == '6'):
          Label(root, text="66666666666666666666\n6666666                66666\n66666     666666     6666\n6666      6666666666666\n666                          6666\n666        666666        666\n666    6666666666    666\n666        666666        666\n6666                        6666\n66666666666666666666", fg="#FF3131",  bg = "black").place(x=50 + a, y=50 + b)
          Button(root, text="Use as your 'Chosen Card'",
                 command=ChosenCard6, highlightbackground = "#FF3131", highlightthickness = 3, bg ="black" ,activebackground="#FFCCCB", fg="#FF3131", activeforeground= "#FF3131" ).place(x=50 + a, y=250 + b)
        if (i == '5'):
          Label(root, text="55555555555555555555\n5555                          555\n5555      5555555555555\n5555      5555555555555\n5555                          555\n55555555555555        55\n555555555555555      55\n5555   55555555        555\n5555                          555\n55555555555555555555", fg="#FFFF33",  bg = "black").place(x=50 + a,
                                                                 y=50 + b)
          Button(root, text="Use as your 'Chosen Card'",
                 command=ChosenCard5, highlightbackground = "#FFFF33", highlightthickness = 3, bg ="black" ,activebackground="#FFFFE0", fg="#FFFF33", activeforeground= "#FFFF33" ).place(x=50 + a, y=250 + b)
        if (i == '4'):
          Label(root, text="4444444444444444\n4444444      444444\n444444        444444\n44444    44   444444\n4444    444   444444\n444    4444   444444\n444                     444\n444444444   444444\n444444444   444444\n44444444444444444", fg="#FFFF33",  bg = "black").place(x=50 + a,
                                                                 y=50 + b)
          Button(root, text="Use as your 'Chosen Card'",
                 command=ChosenCard4, highlightbackground = "#FFFF33", highlightthickness = 3, bg ="black" ,activebackground="#FFFFE0", fg="#FFFF33", activeforeground= "#FFFF33" ).place(x=50 + a, y=250 + b)
        if (i == '3'):
          Label(root, text="33333333333333333333\n3333                        3333\n33       333333333       33\n333333333333333      33\n3333333333333        333\n333333333            33333\n3333333333333        333\n33       333333333       33\n3333                          333\n33333333333333333333", fg="#FFFF33",  bg = "black").place(x=50 + a,
                                                                  y=50 + b)
          Button(root, text="Use as your 'Chosen Card'",
                 command=ChosenCard3, highlightbackground = "#FFFF33", highlightthickness = 3, bg ="black" ,activebackground="#FFFFE0", fg="#FFFF33", activeforeground= "#FFFF33" ).place(x=50 + a, y=250 + b)
        if (i == '2'):
          Label(root, text="22222222222222222222\n222222                222222\n2222      22222      22222\n222     22222222     2222\n22222222222222    2222\n22222222222        22222\n222222            22222222\n2222        222222222222\n222                             222\n22222222222222222222", fg="#FFFF33",  bg = "black").place(x=50 + a, y=50 + b)
          Button(root, text="Use as your 'Chosen Card'",
                 command=ChosenCard2, highlightbackground = "#FFFF33", highlightthickness = 3, bg ="black" ,activebackground="#FFFFE0", fg="#FFFF33", activeforeground= "#FFFF33" ).place(x=50 + a, y=250 + b)
        if (i == 'A'):
          Label(root, text="AAAAAAAAAAAAAAAAAAAA\nAAAAAAAA                AAAAAA\nAAAAAAA                   AAAAAA\nAAAAAA         A          AAAAAA\nAAAAA         AA          AAAAAA\nAAAA         AAA          AAAAAA\nAAA         AAAA          AAAAAA\nAA         AAAAA          AAAAAA\n                                         AAAAA\nA       AAAAAAA          AAAAAA",fg="#FF10F0",  bg = "black").place(x=50 + a, y=50 + b)
          Button(root, text="Use as your 'Chosen Card'",
                 command=ChosenCarda, highlightbackground = "#FF10F0", highlightthickness = 3, bg ="black" ,activebackground="#FFB6C1", fg="#FF10F0", activeforeground= "#FF10F0" ).place(x=50 + a, y=250 + b)
        if (i == 'J'):
          Label(root, text="JjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJj\nJjJj   JjJjJjJjJjJjJjJjJjJj   JjJj\nJj JjJj    JjJjJjJj    JjJj Jj\nJjJjJjJjJj    JjJj    JjJjJjJjJj\nJjJjJj              JjJjJj\nJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJj\nJjJjJjJj JjJjJjJjJjJjJjJjJjJj JjJjJjJj\nJjJjJj Jj JjJjJjJjJjJjJjJj Jj JjJjJj\nJjJjJjJj JjJjJj    JjJjJj JjJjJjJj\nJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJj", fg="#39FF14",  bg = "black").place(x=50 + a,
                                                                  y=50 + b)
          Button(root, text="See other players Cards",
                 command=ChosenCardj, highlightbackground = "#39FF14", highlightthickness = 3, bg ="black" ,activebackground="#90EE90", fg="#39FF14", activeforeground= "#39FF14" ).place(x=50 + a, y=250 + b)
      
        a += 200
        if (a + 50 >= window_width):
          b += 300
          a = 0
    else:
      Label(root, text = "You Have Won, If you would like to play again, please start a new game.", fg="#1F51FF",  bg = "black").place(x = 100, y = 100)
  else:
    Label(root, text = "You Have lost, please quietly send to the next player in line", fg="#1F51FF",  bg = "black").place(x = 100, y = 100)
  def Finished():
    root.destroy()
  Label(root, text = "You are Player "+str(PlayerTurn), fg="#1F51FF",  bg = "black").place(x = 0, y = 0)
  Button(root, text="Input Data", command=Finished, highlightbackground = "#1F51FF", highlightthickness = 3, bg ="black" ,activebackground="#ADD8E6", fg="#1F51FF", activeforeground= "#1F51FF" ).place(x=50, y=600)
  Button(root, text="Choose Someone to Fight",
         command=Choosefight, highlightbackground = "#1F51FF", highlightthickness = 3, bg ="black" ,activebackground="#ADD8E6", fg="#1F51FF", activeforeground= "#1F51FF" ).place(x=150, y=600)
  root.mainloop()

####################################################################################
MainMenu()
QuickStartScreen()
PlayersUnUsedHand, UsedPlayersCard, PlayerWhosFighting, ArrayofWhosFighting, ArrayofFightersCards, CardOrder, PlayerTurn, GameMode = OldFileChecking(
  gameFilePlace)
if (UsedPlayersCard == "J"):
  rando = random.randrange(0,len(PlayersUnUsedHand))
  UsedPlayersCard = PlayersUnUsedHand[rando]
  PlayersUnUsedHand.pop(rando)
  PlayersUnUsedHand.append("J")
ArrOfLostFights = Fight(UsedPlayersCard, ArrayofFightersCards, ArrayofWhosFighting, CardOrder, PlayerTurn)
UpdatedUnUsedPlayersHand = LostFightsRules(ArrOfLostFights, PlayersUnUsedHand)
print(PlayerTurn)
print(ArrayofWhosFighting)
print(ArrayofFightersCards)
print(ArrOfLostFights)
if (PlayerWhosFighting != 0):
  UsedPlayersCard = "0"
GameControl(UpdatedUnUsedPlayersHand, UsedPlayersCard, PlayerWhosFighting,
            ArrayofWhosFighting, ArrayofFightersCards, CardOrder,
            PlayerTurn, GameMode, gameFilePlace)
EndFileWriter(UpdatedUnUsedPlayersHand, UsedPlayersCard, PlayerWhosFighting,
                  ArrayofWhosFighting, ArrayofFightersCards, CardOrder,
                  PlayerTurn, gameFilePlace)
FinishedWriting()
# EndFileWriter(PlayersUnUsedHand, UsedPlayersCard, PlayerWhosFighting,
#               ArrayofWhosFighting, ArrayofFightersCards, CardOrder, PlayerTurn,
#               gameFilePlace)
#####^ Returned Variable From the Data parser ^#####MainMenu
 