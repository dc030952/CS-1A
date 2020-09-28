#Imports
import time
import random
import replit

#Combat
def attackdice():
  print("Rolling for attack...")
  amin = 1
  amax = 6
  adiceroll = random.randint(amin, amax)
  Adiceroll = str(adiceroll)
  time.sleep(1.5)
  print("You rolled", Adiceroll, "for your attack.")
  global adice
  adice = adiceroll
adice = None

def defencedice():
  print("Rolling for defence...")
  dmin = 1
  dmax = 6
  ddiceroll = random.randint(dmin, dmax)
  Ddiceroll = str(ddiceroll)
  time.sleep(1.5)
  print("You rolled", Ddiceroll, "for your defense.")
  global ddice
  ddice = ddiceroll
ddice = None

#Battle Loops
battle1 = False
battle2 = False
battle3 = False

#Abilities
rougeamin = 1
rougeamax = 12
rougea = random.randint(rougeamin, rougeamax)

rougebmin = 1
rougebmax = 100
rougeb = random.randint(rougebmin, rougebmax)

#Shops
shop1 = ["Rusty Helmet", "Knight Helm", "Short Sword", "Rogue Dagger"]

#Inventory
inventory = []

#Weapon
weapon = []

#Headgear
head = []

#Armor
armor = []

#Party
party = []

#Floor Plans

#First Floor
firstfloorW = [1, 2, 3]
firstfloorE = [4, 5, 6]
firstfloorN = [7, 8, 9]
firstfloorS = [10, 11, 12]

#Second Floor
secondfloor = ["2r1", "2r2", "2r3", "2r4", "2r5", "2r6", "2r7", "2r8", "2r9", "2r10"]

#Outside Loop Stuff
Health = 20

#Game Stuff
while(Health >= 1):
#Basic Info
  name = input("What is your name? >> ")
  Money = 0
  Coins = str(Money)
  HP = str(Health)
  Floor = 0
  Stairs = False
  Stairs2 = False


  #Gameplay
  print("Hello " + name +", you have three lives.")
  #First Direction
  while (Stairs == False):
    time.sleep(2)
    direction = input("Where will you go? N,S,E,W? >> ")
    if(direction == "W"):
      time.sleep(2)
      print("Traveling West...")
      time.sleep(2)
      if (len(firstfloorW) == 0):
        print("You cannot go in this direction any further.")
      elif int(random.choice(firstfloorW) == 1):
        print("You find an empty room.")
        firstfloorW.remove(1)
      elif int(random.choice(firstfloorW) == 2):
        print("You find a broken piece of chainmail on the ground.")
        time.sleep(1)
        brokenchainmail = input("Will you take it? Y/N >> ")
        if (brokenchainmail == "Y"):
          time.sleep(1)
          print("You have taken and equipped the chainmail.")
          armor.append("BrokenChainmail")
          firstfloorW.remove(2)
        else:
          time.sleep(1)
          print("You leave the broken chainmail on the ground.")
          firstfloorW.remove(2)
      elif int(random.choice(firstfloorW) == 3):
        print("You hear a cry for help.")
        time.sleep(1)
        helprogue = input("Do you go to help the person? Y/N >> ")
        if(helprogue == "Y"):
          print("You rush over to find a woman in a cloak being attacked by a troll. ")
          time.sleep(2)
          print("You sneak up on the troll and kill it with one attack to its back.")
          time.sleep(2)
          print("The woman appears to be a rogue and wants to join your party.")
          roguejoin = input("Do you allow the rogue to continue with you from this point forward? Y/N >> ")
          if (roguejoin == "Y"):
            time.sleep(1)
            party.append("Rouge")
            print("The rogue joins you on your journey and provides extra stealth and attack.")
            time.sleep(1)
            firstfloorW.remove(3)
          if(roguejoin == "N"):
            time.sleep(1)
            print("The rogue is disappointed but leaves alone on your journey.")
            time.sleep(1)
            firstfloorW.remove(3)
        elif(helprogue == "N"):
          print("You go on your way without acknowledging the cry for help.")
          firstfloorW.remove(3)
          time.sleep(2)
    elif(direction == "N"):
      time.sleep(2) 
      print("Traveling North...")
      time.sleep(2)
      if len(firstfloorN) == 0:
        print("You can't go any further in this direction.")
        time.sleep(1.5)
      elif int(random.choice(firstfloorN) == 7):
        odamage = random.randint(1, 3)
        Health = Health - odamage
        Odamage = str(odamage)
        HP = str(Health)  
        print("An orc jumps you from the shadows and takes " + Odamage +  " health.")
        time.sleep(2)
        print("You have " + HP + " health remaining.")
        time.sleep(1.5)
        print("A fight insues between you and the orc.")
        time.sleep(1.5)
        print("Orc") #Orc stats
        time.sleep(1)
        print("HP: 3") #Low health due to inevitable damage from jumping
        time.sleep(1)
        print("ATK: 2")
        time.sleep(1)
        fight1 = input("Do you wish to Fight or Run? Fight/Run >> ")
        time.sleep(1.5)
        orc1hp = 3
        while battle1 == False:
          if fight1 == "Fight":
            if "Rouge" in party:
              if "Rouge Dagger" in inventory:
                rougeamax = 10
                if rougea == 1: 
                  print("The rouge in your party has struck and killed the orc in one blow.")
                  time.sleep(1.5)
                  fight1end = random.randint(3, 10)
                  Fight1end = str(fight1end)  
                  print("You have found", Fight1end, "coins on the orc.")
                  time.sleep(1.5)
                  Money = Money + fight1end
                  Coins = str(Money)
                  print("You now have", Coins, "coins.")
                  time.sleep(1.5)
                  firstfloorN.remove(7)
                  break
                else:
                  attackdice()
                  time.sleep(1.5)
                  defencedice()
                  time.sleep(1.5)
                  if adice <= 2:
                    print("You do no damage to the orc.")
                    time.sleep(1.5)
                    if ddice <= 1:
                      orcrdamage = 2 - ddice
                      Orcrdamage = str(orcrdamage)
                      print("Orc did", Orcrdamage, "damage to you.")
                      Health = Health - Orcrdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                    elif ddice >= 2:
                      print("The orc did no damage to you.")
                  elif adice >= 3:
                    damage = adice - 2
                    Damage = str(damage)
                    orc1hp = orc1hp - damage
                    print("You did", Damage , "damage to the orc.")
                    time.sleep(1.5)
                    if orc1hp <= 0:
                      print("You have defeated the orc.")
                      time.sleep(1.5)
                      fight1end = random.randint(3, 10)
                      Fight1end = str(fight1end)  
                      print("You have found", Fight1end, "coins on the orc.")
                      time.sleep(1.5)
                      Money = Money + fight1end
                      Coins = str(Money)
                      print("You now have", Coins, "coins.")
                      time.sleep(1.5)
                      firstfloorN.remove(7)
                  else:
                     if ddice <= 1:
                      orcrdamage = 2 - ddice
                      Orcrdamage = str(orcrdamage)
                      print("Orc did", Orcrdamage, "damage to you.")
                      Health = Health - Orcrdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                      elif ddice >= 2:
                        print("The orc did no damage to you.")
                        time.sleep(1.5)
              else:
                if rougea == 1: 
                  print("The rouge in your party has struck and killed the orc in one blow.")
                  time.sleep(1.5)
                  fight1end = random.randint(3, 10)
                  Fight1end = str(fight1end)  
                  print("You have found", Fight1end, "coins on the orc.")
                  time.sleep(1.5)
                  Money = Money + fight1end
                  Coins = str(Money)
                  print("You now have", Coins, "coins.")
                  time.sleep(1.5)
                  firstfloorN.remove(7)
                  break
                else:
                  attackdice()
                  time.sleep(1.5)
                  defencedice()
                  time.sleep(1.5)
                  if adice <= 2:
                    print("You do no damage to the orc.")
                    time.sleep(1.5)
                    if ddice <= 1:
                      orcrdamage = 2 - ddice
                      Orcrdamage = str(orcrdamage)
                      print("Orc did", Orcrdamage, "damage to you.")
                      Health = Health - Orcrdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                    elif ddice >= 2:
                      print("The orc did no damage to you.")
                  elif adice >= 3:
                    damage = adice - 2
                    Damage = str(damage)
                    orc1hp = orc1hp - damage
                    print("You did", Damage , "damage to the orc.")
                    time.sleep(1.5)
                    if orc1hp <= 0:
                      print("You have defeated the orc.")
                      time.sleep(1.5)
                      fight1end = random.randint(3, 10)
                      Fight1end = str(fight1end)  
                      print("You have found", Fight1end, "coins on the orc.")
                      time.sleep(1.5)
                      Money = Money + fight1end
                      Coins = str(Money)
                      print("You now have", Coins, "coins.")
                      time.sleep(1.5)
                      firstfloorN.remove(7)
                  else:
                     if ddice <= 1:
                      orcrdamage = 2 - ddice
                      Orcrdamage = str(orcrdamage)
                      print("Orc did", Orcrdamage, "damage to you.")
                      Health = Health - Orcrdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                      elif ddice >= 2:
                        print("The orc did no damage to you.")
                        time.sleep(1.5) 
            else:
              attackdice()
              time.sleep(1.5)
              defencedice()
              time.sleep(1.5)
              if adice <= 2:
                print("You do no damage to the orc.")
                time.sleep(1.5)
                if ddice <= 1:
                      orcrdamage = 2 - ddice
                      Orcrdamage = str(orcrdamage)
                      print("Orc did", Orcrdamage, "damage to you.")
                      Health = Health - Orcrdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                elif ddice >= 2:
                  print("The orc did no damage to you.")
                  time.sleep(1.5)
              elif adice >= 3:
                damage = adice - 2
                Damage = str(damage)
                orc1hp = orc1hp - damage
                print("You did", Damage , "damage to the orc.")
                time.sleep(1.5)
                if orc1hp <= 0:
                  print("You have defeated the orc.")
                  fight1end = random.randint(3, 10)
                  Fight1end = str(fight1end)  
                  print("You have found", Fight1end, "coins on the orc.")
                  time.sleep(1.5)
                  Money = Money + fight1end
                  Coins = str(Money)
                  print("You now have", Coins, "coins.")
                  time.sleep(1.5)
                  firstfloorN.remove(7)
                  break
                else:
                  if ddice <= 1:
                    orcrdamage = 2 - ddice
                    Orcrdamage = str(orcrdamage)
                    print("Orc did", Orcrdamage, "damage to you.")
                    Health = Health - Orcrdamage
                    time.sleep(1.5)
                    print("You have", HP, "health remaining.")
                    time.sleep(1.5)
                    if Health <= 0:
                      break
                  elif ddice >= 2:
                    print("The orc did no damage to you.")
                    time.sleep(1.5)
          elif fight1 == "Run":
            run = random.randint(1,5)
            if run == 1:
              print("You have successfully ran away from the orc.")
              time.sleep(1.5)
              break
            else:
              print("You fail to run away and you must fight the orc.")
              time.sleep(1.5)
              attackdice()
              time.sleep(1.5)
              defencedice()
              time.sleep(1.5)
              if adice <= 2:
                print("You do no damage to the orc.")
                time.sleep(1.5)
                if ddice <= 1:
                      orcrdamage = 2 - ddice
                      Orcrdamage = str(orcrdamage)
                      print("Orc did", Orcrdamage, "damage to you.")
                      Health = Health - Orcrdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                elif ddice >= 2:
                  print("The orc did no damage to you.")
                  time.sleep(1.5)
              elif adice >= 3:
                damage = adice - 2
                Damage = str(damage)
                orc1hp = orc1hp - damage
                print("You did", Damage , "damage to the orc.")
                time.sleep(1.5)
                if orc1hp <= 0:
                  print("You have defeated the orc.")
                  fight1end = random.randint(3, 10)
                  Fight1end = str(fight1end)  
                  print("You have found", Fight1end, "coins on the orc.")
                  time.sleep(1.5)
                  Money = Money + fight1end
                  Coins = str(Money)
                  print("You now have", Coins, "coins.")
                  time.sleep(1.5)
                  firstfloorN.remove(7)
                  break
                else:
                  if ddice <= 1:
                    orcrdamage = 2 - ddice
                    Orcrdamage = str(orcrdamage)
                    print("Orc did", Orcrdamage, "damage to you.")
                    Health = Health - Orcrdamage
                    time.sleep(1.5)
                    print("You have", HP, "health remaining.")
                    time.sleep(1.5)
                    if Health <= 0:
                      break
                  elif ddice >= 2:
                    print("The orc did no damage to you.")
                    time.sleep(1.5) #Orc jump done
      elif int(random.choice(firstfloorN) == 8):
          print("You stumble into the next room and find a dead knight holding a key.")
          time.sleep(2)
          key1 = input("Do you take the key? Y/N >> ")
          if (key1 == "Y"):
            time.sleep(1)
            print("You take the key and put it in your inventory.")
            time.sleep (1.5)
            firstfloorN.remove(8)
          elif key1 == "N":
            print("You leave the key with the knight.")
            time.sleep(1.5)
            firstfloorN.remove(8)
            continue  
      elif int(random.choice(firstfloorN) == 9):
        print("A small spider appears in the room you are in.")
        time.sleep(1.5)  #Spider Combat
        print("The spider jumps you.")
        time.sleep(1.5)
        print("Small Spider") #Spider stats
        time.sleep(1)
        print("HP: 4") #Low health due to inevitable damage from jumping
        time.sleep(1)
        print("ATK: 2")
        time.sleep(1)
        fight2 = input("Do you wish to Fight or Run? Fight/Run >> ")
        time.sleep(1.5)
        spider1hp = 4
        while battle2 == False:
          if fight2 == "Fight":
            if "Rouge" in party:
              if "Rouge Dagger" in inventory:
                rougeamax = 10
                if rougea == 1: 
                  print("The rouge in your party has struck and killed the small spider in one blow.")
                  time.sleep(1.5)
                  fight2end = random.randint(3, 10)
                  Fight2end = str(fight2end)  
                  print("You have found", Fight2end, "coins on the spider.")
                  time.sleep(1.5)
                  Money = Money + fight2end
                  Coins = str(Money)
                  print("You now have", Coins, "coins.")
                  time.sleep(1.5)
                  firstfloorN.remove(9)
                  break
                else:
                  attackdice()
                  time.sleep(1.5)
                  defencedice()
                  time.sleep(1.5)
                  if adice <= 2:
                    print("You do no damage to the small spider.")
                    time.sleep(1.5)
                    if ddice <= 1:
                      spiderdamage = 2 - ddice
                      Spiderdamage = str(spiderdamage)
                      print("Spider did", Spiderdamage, "damage to you.")
                      Health = Health - Spiderdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                    elif ddice >= 2:
                      print("The spider did no damage to you.")
                  elif adice >= 3:
                    damage = adice - 2
                    Damage = str(damage)
                    spider1hp = spider1hp - damage
                    print("You did", Damage , "damage to the spider.")
                    time.sleep(1.5)
                    if spider1hp <= 0:
                      print("You have defeated the spider.")
                      time.sleep(1.5)
                      fight2end = random.randint(3, 10)
                      Fight2end = str(fight2end)  
                      print("You have found", Fight2end, "coins on the spider.")
                      time.sleep(1.5)
                      Money = Money + fight2end
                      Coins = str(Money)
                      print("You now have", Coins, "coins.")
                      time.sleep(1.5)
                      firstfloorN.remove(9)
                  else:
                     if ddice <= 1:
                      spiderdamage = 2 - ddice
                      Spiderdamage = str(spiderdamage)
                      print("Spider did", Spiderdamage, "damage to you.")
                      Health = Health - Spiderdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                      elif ddice >= 2:
                        print("The spider did no damage to you.")
                        time.sleep(1.5)
              else:
                if rougea == 1: 
                  print("The rouge in your party has struck and killed the spider in one blow.")
                  time.sleep(1.5)
                  fight2end = random.randint(3, 10)
                  Fight2end = str(fight2end)  
                  print("You have found", Fight2end, "coins on the spider.")
                  time.sleep(1.5)
                  Money = Money + fight2end
                  Coins = str(Money)
                  print("You now have", Coins, "coins.")
                  time.sleep(1.5)
                  firstfloorN.remove(9)
                  break
                else:
                  attackdice()
                  time.sleep(1.5)
                  defencedice()
                  time.sleep(1.5)
                  if adice <= 2:
                    print("You do no damage to the spider.")
                    time.sleep(1.5)
                    if ddice <= 1:
                      spiderdamage = 2 - ddice
                      Spiderdamage = str(spiderdamage)
                      print("Spider did", Spiderdamage, "damage to you.")
                      Health = Health - Spiderdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                    elif ddice >= 2:
                      print("The spider did no damage to you.")
                  elif adice >= 3:
                    damage = adice - 2
                    Damage = str(damage)
                    spider1hp = spider1hp - damage
                    print("You did", Damage , "damage to the spider.")
                    time.sleep(1.5)
                    if spider1hp <= 0:
                      print("You have defeated the spider.")
                      time.sleep(1.5)
                      fight2end = random.randint(3, 10)
                      Fight2end = str(fight2end)  
                      print("You have found", Fight2end, "coins on the spider.")
                      time.sleep(1.5)
                      Money = Money + fight2end
                      Coins = str(Money)
                      print("You now have", Coins, "coins.")
                      time.sleep(1.5)
                      firstfloorN.remove(9)
                  else:
                     if ddice <= 1:
                      spiderdamage = 2 - ddice
                      Spiderdamage = str(spiderdamage)
                      print("Spider did", Spiderdamage, "damage to you.")
                      Health = Health - Spiderdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                      elif ddice >= 2:
                        print("The spider did no damage to you.")
                        time.sleep(1.5) 
            else: #orc
              attackdice()
              time.sleep(1.5)
              defencedice()
              time.sleep(1.5)
              if adice <= 2:
                print("You do no damage to the spider.")
                time.sleep(1.5)
                if ddice <= 1:
                      spiderdamage = 2 - ddice
                      Spiderdamage = str(spiderdamage)
                      print("Spider did", Spiderdamage, "damage to you.")
                      Health = Health - Spiderdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                elif ddice >= 2:
                  print("The spider did no damage to you.")
                  time.sleep(1.5)
              elif adice >= 3:
                damage = adice - 2
                Damage = str(damage)
                spider1hp = spider1hp - damage
                print("You did", Damage , "damage to the spider.")
                time.sleep(1.5)
                if spider1hp <= 0:
                  print("You have defeated the small spider.")
                  fight2end = random.randint(3, 10)
                  Fight2end = str(fight2end)  
                  print("You have found", Fight2end, "coins on the spider.")
                  time.sleep(1.5)
                  Money = Money + fight2end
                  Coins = str(Money)
                  print("You now have", Coins, "coins.")
                  time.sleep(1.5)
                  firstfloorN.remove(9)
                  break #orc
                else:
                  if ddice <= 1:
                    spiderdamage = 2 - ddice
                    Spiderdamage = str(spiderdamage)
                    print("Spider did", Spiderdamage, "damage to you.")
                    Health = Health - Spiderdamage
                    time.sleep(1.5)
                    print("You have", HP, "health remaining.")
                    time.sleep(1.5)
                    if Health <= 0:
                      break
                  elif ddice >= 2:
                    print("The small spider did no damage to you.")
                    time.sleep(1.5)
          elif fight1 == "Run":
            run = random.randint(1,5)
            if run == 1:
              print("You have successfully ran away from the spider.")
              time.sleep(1.5)
              break
            else:
              print("You fail to run away and you must fight the spider.")
              time.sleep(1.5)
              attackdice()
              time.sleep(1.5)
              defencedice()
              time.sleep(1.5) #orc
              if adice <= 2:
                print("You do no damage to the spider.")
                time.sleep(1.5)
                if ddice <= 1:
                      spiderdamage = 2 - ddice
                      Spiderdamage = str(spiderdamage)
                      print("Spider did", Spiderdamage, "damage to you.")
                      Health = Health - Spiderdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                elif ddice >= 2:
                  print("The spider did no damage to you.")
                  time.sleep(1.5)
              elif adice >= 3:
                damage = adice - 2
                Damage = str(damage)
                spider1hp = spider1hp - damage
                print("You did", Damage , "damage to the small spider.")
                time.sleep(1.5)
                if spider1hp <= 0:
                  print("You have defeated the spider.")
                  fight2end = random.randint(3, 10)
                  Fight2end = str(fight2end)  
                  print("You have found", Fight2end, "coins on the spider.")
                  time.sleep(1.5)
                  Money = Money + fight2end
                  Coins = str(Money)
                  print("You now have", Coins, "coins.")
                  time.sleep(1.5)
                  firstfloorN.remove(9)
                  break
                else:
                  if ddice <= 1:
                    spiderdamage = 2 - ddice
                    Spiderdamage = str(spiderdamage)
                    print("Spider did", Spiderdamage, "damage to you.")
                    Health = Health - Spiderdamage
                    time.sleep(1.5)
                    print("You have", HP, "health remaining.")
                    time.sleep(1.5)
                    if Health <= 0:
                      break
                  elif ddice >= 2:
                    print("The spider did no damage to you.")
                    time.sleep(1.5) #Spider Combat Done
    elif(direction == "S"):
      time.sleep(2)
      print("Traveling South...")
      time.sleep(2)
      if len(firstfloorS) == 0:
        print("You cannot go any further in this direction.")
      elif random.choice(firstfloorS) == 10:
        print("You have found 3 gold coins.")
        time.sleep(2)
        Gold1 = input("Will you take it? Y/N >> ")
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
          time.sleep(1.5)
          firstfloorS.remove(10)
      elif random.choice(firstfloorS) == 11:
        print("You discover a dark room covered in webs.")
        time.sleep(1.5)
        web = input("Would you like to continue? Y/N >> ")
        time.sleep(1)
        if web == "Y":
          print("You continue further into the room and see spiders crawling up and down the walls.")
          time.sleep(2)
          print("As you walk further into the room you feel an unnerving presence, like something is watching you.")
          time.sleep(2)
          print("Some dirt falls from the ceiling.")
          time.sleep(1)
          print("As you look up you notice giant long legs that seem to belong to some kind of creature.")
          time.sleep(2)
          print("Once you finally look directly above you, you see what has to be a dozen red eyes watching you and realize it is a spider.")
          time.sleep(1.5)
          firstfloorS.remove(11)
          print("You are then attacked by the giant spider.") #Spider Boss (Combat)
          print("Spider Boss") #Spider Boss stats
        time.sleep(1)
        print("HP: 4") #Low health due to inevitable damage from jumping
        time.sleep(1)
        print("ATK: 2")
        time.sleep(1)
        fight3 = input("Do you wish to Fight or Run? Fight/Run >> ")
        time.sleep(1.5)
        spiderbosshp = 4
        while battle3 == False:
          if fight3 == "Fight":
            if "Rouge" in party:
              if "Rouge Dagger" in inventory:
                rougeamax = 10
                if rougea == 1: 
                  print("The rouge in your party has struck and killed the small spider in one blow.")
                  time.sleep(1.5)
                  fight3end = random.randint(10, 25)
                  Fight3end = str(fight3end)  
                  print("You have found", Fight3end, "coins on the spider.")
                  time.sleep(1.5)
                  Money = Money + fight3end
                  Coins = str(Money)
                  print("You now have", Coins, "coins.")
                  time.sleep(1.5)
                  firstfloorN.remove(9)
                  break
                else:
                  attackdice()
                  time.sleep(1.5)
                  defencedice()
                  time.sleep(1.5)
                  if adice <= 2:
                    print("You do no damage to the small spider.")
                    time.sleep(1.5)
                    if ddice <= 1:
                      spiderbossdamage = 2 - ddice
                      Spiderbossdamage = str(spiderbossdamage)
                      print("Spider did", Spiderbossdamage, "damage to you.")
                      Health = Health - Spiderbossdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                    elif ddice >= 2:
                      print("The spider did no damage to you.")
                  elif adice >= 3:
                    damage = adice - 2
                    Damage = str(damage)
                    spiderbosshp = spiderbosshp - damage
                    print("You did", Damage , "damage to the spider.")
                    time.sleep(1.5)
                    if spiderbosshp <= 0:
                      print("You have defeated the spider.")
                      time.sleep(1.5)
                      fight3end = random.randint(10, 25)
                      Fight3end = str(fight3end)  
                      print("You have found", Fight3end, "coins on the spider.")
                      time.sleep(1.5)
                      Money = Money + fight3end
                      Coins = str(Money)
                      print("You now have", Coins, "coins.")
                      time.sleep(1.5)
                      firstfloorN.remove(9)
                  else:
                     if ddice <= 1:
                      spiderbossdamage = 2 - ddice
                      Spiderbossdamage = str(spiderbossdamage)
                      print("Spider did", Spiderbossdamage, "damage to you.")
                      Health = Health - Spiderbossdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                      elif ddice >= 2:
                        print("The spider did no damage to you.")
                        time.sleep(1.5)
              else:
                if rougea == 1: 
                  print("The rouge in your party has struck and killed the spider in one blow.")
                  time.sleep(1.5)
                  fight3end = random.randint(10, 25)
                  Fight3end = str(fight3end)  
                  print("You have found", Fight3end, "coins on the spider.")
                  time.sleep(1.5)
                  Money = Money + fight3end
                  Coins = str(Money)
                  print("You now have", Coins, "coins.")
                  time.sleep(1.5)
                  firstfloorN.remove(9)
                  break
                else:
                  attackdice()
                  time.sleep(1.5)
                  defencedice()
                  time.sleep(1.5)
                  if adice <= 2:
                    print("You do no damage to the spider.")
                    time.sleep(1.5)
                    if ddice <= 1:
                      spiderbossdamage = 2 - ddice
                      Spiderbossdamage = str(spiderbossdamage)
                      print("Spider did", Spiderbossdamage, "damage to you.")
                      Health = Health - Spiderbossdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                    elif ddice >= 2:
                      print("The spider did no damage to you.")
                  elif adice >= 3:
                    damage = adice - 2
                    Damage = str(damage)
                    spiderbosshp = spiderbosshp - damage
                    print("You did", Damage , "damage to the spider.")
                    time.sleep(1.5)
                    if spiderbosshp <= 0:
                      print("You have defeated the spider.")
                      time.sleep(1.5)
                      fight3end = random.randint(10, 25)
                      Fight3end = str(fight3end)  
                      print("You have found", Fight3end, "coins on the spider.")
                      time.sleep(1.5)
                      Money = Money + fight3end
                      Coins = str(Money)
                      print("You now have", Coins, "coins.")
                      time.sleep(1.5)
                      firstfloorN.remove(9)
                  else:
                     if ddice <= 1:
                      spiderbossdamage = 2 - ddice
                      Spiderbossdamage = str(spiderbossdamage)
                      print("Spider did", Spiderbossdamage, "damage to you.")
                      Health = Health - Spiderbossdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                      elif ddice >= 2:
                        print("The spider did no damage to you.")
                        time.sleep(1.5) 
            else: #orc
              attackdice()
              time.sleep(1.5)
              defencedice()
              time.sleep(1.5)
              if adice <= 2:
                print("You do no damage to the spider.")
                time.sleep(1.5)
                if ddice <= 1:
                      spiderbossdamage = 2 - ddice
                      Spiderbossdamage = str(spiderbossdamage)
                      print("Spider did", Spiderbossdamage, "damage to you.")
                      Health = Health - Spiderbossdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                elif ddice >= 2:
                  print("The spider did no damage to you.")
                  time.sleep(1.5)
              elif adice >= 3:
                damage = adice - 2
                Damage = str(damage)
                spiderbosshp = spiderbosshp - damage
                print("You did", Damage , "damage to the spider.")
                time.sleep(1.5)
                if spiderbosshp <= 0:
                  print("You have defeated the small spider.")
                  fight3end = random.randint(10, 25)
                  Fight3end = str(fight3end)  
                  print("You have found", Fight3end, "coins on the spider.")
                  time.sleep(1.5)
                  Money = Money + fight3end
                  Coins = str(Money)
                  print("You now have", Coins, "coins.")
                  time.sleep(1.5)
                  firstfloorN.remove(9)
                  break #orc
                else:
                  if ddice <= 1:
                    spiderbossdamage = 2 - ddice
                    Spiderbossdamage = str(spiderbossdamage)
                    print("Spider did", Spiderbossdamage, "damage to you.")
                    Health = Health - Spiderbossdamage
                    time.sleep(1.5)
                    print("You have", HP, "health remaining.")
                    time.sleep(1.5)
                    if Health <= 0:
                      break
                  elif ddice >= 2:
                    print("The small spider did no damage to you.")
                    time.sleep(1.5)
          elif fight1 == "Run":
            run = random.randint(1,5)
            if run == 1:
              print("You have successfully ran away from the spider.")
              time.sleep(1.5)
              break
            else:
              print("You fail to run away and you must fight the spider.")
              time.sleep(1.5)
              attackdice()
              time.sleep(1.5)
              defencedice()
              time.sleep(1.5) 
              if adice <= 2:
                print("You do no damage to the spider.")
                time.sleep(1.5)
                if ddice <= 1:
                      spiderbossdamage = 2 - ddice
                      Spiderbossdamage = str(spiderbossdamage)
                      print("Spider did", Spiderbossdamage, "damage to you.")
                      Health = Health - Spiderbossdamage
                      time.sleep(1.5)
                      print("You have", HP, "health remaining.")
                      time.sleep(1.5)
                      if Health <= 0:
                        break
                elif ddice >= 2:
                  print("The spider did no damage to you.")
                  time.sleep(1.5)
              elif adice >= 3:
                damage = adice - 2
                Damage = str(damage)
                spiderbosshp = spiderbosshp - damage
                print("You did", Damage , "damage to the small spider.")
                time.sleep(1.5)
                if spiderbosshp <= 0:
                  print("You have defeated the spider.")
                  fight3end = random.randint(10, 25)
                  Fight3end = str(fight3end)  
                  print("You have found", Fight3end, "coins on the spider.")
                  time.sleep(1.5)
                  Money = Money + fight3end
                  Coins = str(Money)
                  print("You now have", Coins, "coins.")
                  time.sleep(1.5)
                  firstfloorN.remove(9)
                  break
                else:
                  if ddice <= 1:
                    spiderbossdamage = 2 - ddice
                    Spiderbossdamage = str(spiderbossdamage)
                    print("Spider did", Spiderbossdamage, "damage to you.")
                    Health = Health - Spiderbossdamage
                    time.sleep(1.5)
                    print("You have", HP, "health remaining.")
                    time.sleep(1.5)
                    if Health <= 0:
                      break
                  elif ddice >= 2:
                    print("The spider did no damage to you.")
                    time.sleep(1.5) #Spider Boss Combat Done
        if web == "N":
          print("You have a bad feeling about this room and decide to head back.")
          time.sleep(1.5)
          firstfloorS.remove(11)
      elif random.choice(firstfloorS) == 12:
        print("You find a dusty room with an old book on the ground.")
        time.sleep(1.5)
        book = input("Do you wish to take the book? Y/N >> ")
        if book == "Y":
          print("You take the book and wipe off some dust before you put into your bag.")
          inventory.append("Book")
          time.sleep(1.5)
    elif(direction == "E"):
      time.sleep(2)
      print("Traveling East...")
      time.sleep(2)
      if len(firstfloorE) == 0:
        print("You cannot go in this direction any further.")
        time.sleep(1.5)
      elif random.choice(firstfloorE) == 4:
        print("You find a large room with a vault requiring a key and a giant rat protecting it. ")
        time.sleep(2)
        Leave = input("Do you wish to fight the giant rat? Y/N >> ")
        if(Leave == "Y"):
          time.sleep(2)
          grd1 = random.randint(0, 2)
          Grd1 = str(grd1)
          print("The giant rat has been killed and you have suffered " + Grd1 + " damage from the battle." )
          Health = Health - grd1
          HP = str(Health)
          time.sleep(2)
          print("You have " + HP + " health remaining.")
          time.sleep(1.5)
          firstfloorE.remove(4)
        elif(Leave == "N"):
          print("You decide to walk away from the room avoiding the rat.")
          time.sleep(1)
          firstfloorE.remove(4)
      elif random.choice(firstfloorE) == 5:
        print("You find a shopkeeper that sells helpful items for your journey.")
        time.sleep(2)
        shopo1 = input("Would you like to purchase something from him? Y/N >> ")
        time.sleep(1.5)
        if shopo1 == "Y":
          shope1 = False
          while(shope1 == False):
            print("Here are the shopkeeper's items for sale.")
            time.sleep(1.5)
            print(shop1)
            time.sleep(1.5)
            buy = input("Which item would you like to look at? 1/2/3/4 >> ")
            if buy == "1":
              print("The Rusty Helmet provides very little defence.")
              time.sleep(1.5)
              print("Cost: 5 coins")
              time.sleep(1.5)
              rhb = input("Would you like to purchase this item? Y/N >> ")
              if rhb == "Y":
                if Money >= 5:
                  print("You have purchased the Rusty Helmet.")
                  time.sleep(1.5)
                  head.append("Rusty Helmet")
                  shop1.remove("Rusty Helmet")
                  Money = Money - 5
                  Coins = str(Money)
                  print("You have "+ Coins + " Coins remaining.")
                  continue1 = input("Would you like to return to the shop? Y/N >> ")
                  time.sleep(1.5)
                  if continue1 == "Y":
                    continue
                  elif continue1 == "N":
                    time.sleep(1.5)
                    firstfloorE.remove(5)
                    break
                elif Money < 5:
                  time.sleep(1.5)
                  print("You do not have enough coins to purchase this item.")
                  time.sleep(1.5)
                  continue3 = input("Would you like to return to the shop? Y/N >> ")
                  if continue3 == "Y":
                    time.sleep(1.5)
                    continue
                  elif continue3 == "N":
                    firstfloorE.remove(5)
                    time.sleep(1.5)
                    break
              elif rhb == "N":
                  time.sleep(1.5)
                  continue2 = input("Would you like to return to the shop? Y/N >> ")
                  if continue2 == "Y":
                    continue
                  elif continue2 == "N":
                    time.sleep(1.5)
                    firstfloorE.remove(5)
                    break
            if buy == "2":
              print("The Knight Helm provides little attack.")
              time.sleep(1.5)
              print("Cost: 7 coins")
              time.sleep(1.5)
              rhb = input("Would you like to purchase this item? Y/N >> ")
              if rhb == "Y":
                if Money >= 7:
                  print("You have purchased the Knight Helm.")
                  time.sleep(1.5)
                  head.append("Knight Helm")
                  shop1.remove("Knight Helm")
                  Money = Money - 7
                  Coins = str(Money)
                  print("You have "+ Coins + " Coins remaining.")
                  continue1 = input("Would you like to return to the shop? Y/N >> ")
                  time.sleep(1.5)
                  if continue1 == "Y":
                    continue
                  elif continue1 == "N":
                    time.sleep(1.5)
                    firstfloorE.remove(5)
                    break
                elif Money < 7:
                  time.sleep(1.5)
                  print("You do not have enough coins to purchase this item.")
                  time.sleep(1.5)
                  continue3 = input("Would you like to return to the shop? Y/N >> ")
                  if continue3 == "Y":
                    time.sleep(1.5)
                    continue
                  elif continue3 == "N":
                    firstfloorE.remove(5)
                    time.sleep(1.5)
                    break
              elif rhb == "N":
                  time.sleep(1.5)
                  continue2 = input("Would you like to return to the shop? Y/N >> ")
                  if continue2 == "Y":
                    continue
                  elif continue2 == "N":
                    time.sleep(1.5)
                    firstfloorE.remove(5)
                    break
            if buy == "3":
              print("The Short Sword provides little attack.")
              time.sleep(1.5)
              print("Cost: 4 coins")
              time.sleep(1.5)
              rhb = input("Would you like to purchase this item? Y/N >> ")
              if rhb == "Y":
                if Money >= 4:
                  print("You have purchased the Knight Helm.")
                  time.sleep(1.5)
                  weapon.append("Short Sword")
                  shop1.remove("Short Sword")
                  Money = Money - 4
                  Coins = str(Money)
                  print("You have "+ Coins + " Coins remaining.")
                  continue1 = input("Would you like to return to the shop? Y/N >> ")
                  time.sleep(1.5)
                  if continue1 == "Y":
                    continue
                  elif continue1 == "N":
                    time.sleep(1.5)
                    firstfloorE.remove(5)
                    break
                elif Money < 4:
                  time.sleep(1.5)
                  print("You do not have enough coins to purchase this item.")
                  time.sleep(1.5)
                  continue3 = input("Would you like to return to the shop? Y/N >> ")
                  if continue3 == "Y":
                    time.sleep(1.5)
                    continue
                  elif continue3 == "N":
                    firstfloorE.remove(5)
                    time.sleep(1.5)
                    break
              elif rhb == "N":
                  time.sleep(1.5)
                  continue2 = input("Would you like to return to the shop? Y/N >> ")
                  if continue2 == "Y":
                    continue
                  elif continue2 == "N":
                    time.sleep(1.5)
                    firstfloorE.remove(5)
                    break
            if buy == "4":
              print("The Rouge Dagger increases a Rouge's ability chance.")
              time.sleep(1.5)
              print("Cost: 12 coins")
              time.sleep(1.5)
              rhb = input("Would you like to purchase this item? Y/N >> ")
              if rhb == "Y":
                if Money >= 12:
                  print("You have purchased the Rouge Dagger.")
                  time.sleep(1.5)
                  inventory.append("Rouge Dagger")
                  shop1.remove("Rouge Dagger")
                  Money = Money - 12
                  Coins = str(Money)
                  print("You have "+ Coins + " Coins remaining.")
                  continue1 = input("Would you like to return to the shop? Y/N >> ")
                  time.sleep(1.5)
                  if continue1 == "Y":
                    continue
                  elif continue1 == "N":
                    time.sleep(1.5)
                    firstfloorE.remove(5)
                    break
                elif Money < 12:
                  time.sleep(1.5)
                  print("You do not have enough coins to purchase this item.")
                  time.sleep(1.5)
                  continue3 = input("Would you like to return to the shop? Y/N >> ")
                  if continue3 == "Y":
                    time.sleep(1.5)
                    continue
                  elif continue3 == "N":
                    firstfloorE.remove(5)
                    time.sleep(1.5)
                    break
              elif rhb == "N":
                  time.sleep(1.5)
                  continue2 = input("Would you like to return to the shop? Y/N >> ")
                  if continue2 == "Y":
                    continue
                  elif continue2 == "N":
                    time.sleep(1.5)
                    firstfloorE.remove(5)
                    break
        if shopo1 == "N":
          time.sleep(1.5)
          print("You leave the shop without looking at something")
          firstfloorE.remove(5)
          time.sleep(1.5)
      elif random.choice(firstfloorE) == 6:
        print("You find the stairs to the next floor.")
        time.sleep(1.5)
        upstairs1 = input("Would you like to continue searching the first floor or go to the next floor? Y/N ")
        if upstairs1 == "Y":
          print("You head up stairs to the next floor.")
          time.sleep(1.5)
          firstfloorE.remove(6)
          break
        elif upstairs1 == "N":
          print("You decide to go past the stairs and search the rest of the floor.")
          time.sleep(1.5)


  replit.clear()  #Second Floor
  while(Stairs2 == False):
    time.sleep(2)
    Floor = Floor + 1
    print("You arrive to the second floor.")
    time.sleep(1.5)
    direction1 = input("Where will you go? N,S,E,W? >> ")
    if(direction1 == "N"):
      time.sleep(2)
      print("You find a fountain of youth that heals you to full health.")
      Health = 20
      HP = str(Health)
      time.sleep(2)
      print ("You're health has been restored.")
    elif(direction1 == "S" ):
      time.sleep(2)
      sneako1 = input("You enter a small dark room that has two sleeping orcs. Do you wish to fight the orcs or     attempt to sneak past them? Fight/Sneak >> ")
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
while Health <= 0:
  print("You have failed....")
  time.sleep(1.5)
  loss = input("Would you like to try again? Y/N >> ")
  if loss == "Y":
    time.sleep(1.5)
