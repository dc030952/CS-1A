#Imports
import time
import random

#Inventory
inventory = []

#Floor Plans

#First Floor
firstfloorW = ["r1", "r2", "r3"]
firstfloorE = ["r4", "r5", "r6"]
firstfloorN = ["r7", "r8", "r9"]
firstfloorS = ["r10", "r11", "r12"]

#Second Floor
secondfloor = ["2r1", "2r2", "2r3", "2r4", "2r5", "2r6", "2r7", "2r8", "2r9", "2r10"]

#Game Stuff
end = "Y"
while(end == "Y"):
#Basic Info
  Health = 20
  Lives = 3
  name = input("What is your name? >> ")
  Money = 0
  Coins = str(Money)
  HP = str(Health)
  LifeC = str(Lives)
  Floor = 0



  #Gameplay


  #Life Count
  if(Health == 0):
    Lives = Lives - 1
    LifeC = str(Lives)
    print("You have " + LifeC + " lives/life remaining.")
    Health = Health + 20
  elif(Lives == 0):
    print("You have failed...")



  #First Direction
  print("Hello " + name +", you have three lives.")
  time.sleep(2)
  direction = input("Where will you go? N,S,E,W? >> ")
  if(direction == "W"):
    time.sleep(2)
    print("Traveling West...")
    time.sleep(2)
    if (random.choice(firstfloorW) == "r1"):
      print("You find an empty room.") 
    elif (random.choice(firstfloorW) == "r2"):
      print("You find a broken piece of chainmail on the ground.")
      time.sleep(1)
      brokenchainmail = input("Will you take it? Y/N >> ")
      if (brokenchainmail == "Y"):
        time.sleep(1)
        print("You have taken and equipped the chainmail.")
        inventory.append("Broken Chainmail")
      else:
        time.sleep(1)
        print("You leave the broken chainmail on the ground.")
    elif()
  elif(direction == "N"):
    time.sleep(2) 
    print("Traveling North...")
    time.sleep(2)
    print("An orc jumps you from the shadows and takes 1 health.")
    Health = Health - 1
    HP = str(Health)
    time.sleep(2)
    print("You have " + HP + " health remaining.")
  elif(direction == "S"):
    time.sleep(2)
    print("Traveling South...")
    time.sleep(2)
    print("You have found 3 gold coins.")
    time.sleep(2)
    Gold1 = input("Will you take it? Y/N >>")
    if(Gold1 == "Y"):
      Money = Money + random.randint(1,10)
      Coins = str(Money)
      time.sleep(2)
      print("You have acquired 3 gold coins.")
      time.sleep(2)
      print("You currently have " + Coins + " gold coins in your inventory.") 
    elif(Gold1 == "N"):
      time.sleep(2)
      print("You continue on your journey without picking up the coins.")
  elif(direction == "E"):
    time.sleep(2)
    print("You find a large room with a vault requiring a key and a giant rat protecting it. ")
    time.sleep(2)
    Leave = input("Do you wish to fight the giant rat? Y/N ")
    if(Leave == "Y"):
      time.sleep(2)
      grd1 = random.randint(0, 2)
      Grd1 = str(grd1)
      print("The giant rat has been killed and you have suffered " + Grd1 + " damage from the battle." )
      Health = Health - grd1
      HP = str(Health)
      time.sleep(2)
      print("You have " + HP + " health remaining.")
    elif(Leave == "N"):
      print("You decide to walk away from the room avoiding the rat.")



    #First Checkpoint
  if(Health == 0):
    Lives = Lives - 1
    LifeC = str(Lives)
    print("You have " + LifeC + " lives/life remaining.")
    Health = Health + 10
  elif(Lives == 0):
    print("You have failed...")
    time.sleep(2)
    end = input("Would you like to restart your journey? Y/N ")

    #Second Direction
  else:
    time.sleep(2)
    Floor = Floor + 1
    direction1 = input("Where will you go? N,S,E,W? ")
    if(direction1 == "N"):
      time.sleep(2)
      print("You find a fountain of youth that heals you to full health.")
      Health = Health + 20 - Health
      HP = str(Health)
      time.sleep(2)
      print ("You have " + HP + " health remaining.")
    elif(direction1 == "S" ):
      time.sleep(2)
      sneako1 = input("You enter a small dark room that has two sleeping orcs. Do you wish to fight the orcs or     attempt to sneak past them? Fight/Sneak ")
      orcs = random.randint(3, 9)
      sneakc = random.randint(1,4)
      Orcs = str(orcs)
      if(sneako1 == "Fight"):
        time.sleep(2)
        print("The orcs are defeated but you lost " + Orcs + "health.")
        time.sleep(2)
        Health = Health - orcs
        HP = str(Health)
        print ("You have " + HP + " health remaining.")
      elif(sneako1 == "Sneak"):  
        if(sneakc == 1):
          time.sleep(2)
          print("You successfully snuck past the orcs and continued on your journey.")
        elif(sneakc == 2 or 3 or 4):
          print("You wake up the sleeping orcs while you try to sneak past them.")
          time.sleep(2)
          



