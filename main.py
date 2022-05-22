from random import randint
import random
import math
MonsterList = [{'MonsterType': 'Skeleton',
               'MonsterHealth': 8,
               'MonsterMinDamage': 1,
               'MonsterMaxDamage': 3,
               'Phases' : 0}, 
               {'MonsterType': 'Bat',
               'MonsterHealth': 3,
               'MonsterMinDamage': 3,
               'MonsterMaxDamage': 5,
               'Phases': 0},
               {'MonsterType' : 'Alligator',
               'MonsterHealth': 4,
               'MonsterMinDamage': 2,
               'MonsterMaxDamage': 7,
               'Phases': 0},
               {'MonsterType' : 'Ninja',
               'MonsterHealth': 3,
               'MonsterMinDamage': 8,
               'MonsterMaxDamage': 10,
               'Phases': 0},
               {'MonsterType' : 'Muddy Crab',
               'MonsterHealth': 3,
               'MonsterMinDamage': 100,
               'MonsterMaxDamage': 100,
               'Phases': 0},
               {'MonsterType' : 'Zombie',
               'MonsterHealth': 6,
               'MonsterMinDamage': 2,
               'MonsterMaxDamage': 4,
               'Phases': 1} 
               ]
Bosses = [{
         'MonsterType': 'Massive Mosquitoe',
         'MonsterHealth': 30,
         'MonsterMinDamage': 2,
         'MonsterMaxDamage': 6,
         'Phases': 0
        }
]
MonsterTraits = [{'Title': 'Regular',
                  'DamageModifier': 1,
                  'HealthModifier': 1
                 },
                 {
                  'Title': 'Weak',
                  'DamageModifier': 0.5,
                  'HealthModifier': 1       
                 },
                 {
                  'Title': 'Strong',
                  'DamageModifier': 1.5,
                  'HealthModifier': 1       
                 },
                 {
                  'Title': 'Wounded',
                  'DamageModifier': 1,
                  'HealthModifier': 0.5       
                 },
                 {
                  'Title': 'Sturdy',
                  'DamageModifier': 1,
                  'HealthModifier': 1.5       
                 },
                 {
                  'Title': 'Elite',
                  'DamageModifier': 1.5,
                  'HealthModifier': 2       
                 },
                 {
                  'Title': 'Ultra',
                  'DamageModifier': 2,
                  'HealthModifier': 3       
                 },
                 {
                  'Title': 'Boss',
                  'DamageModifier': 1,
                  'HealthModifier': 1       
                 }
]
FloorTypes = [{'FloorType': 'Regular',
               'HealModifier': 1,
               'Poison': 0,
               'DamageDealToMonster': 1},
               {'FloorType': 'Poisonous',
               'HealModifier': 1,
               'Poison': 1,
               'DamageDealToMonster': 1},
               {'FloorType': 'Spiky',
               'HealModifier': 1,
               'Poison': 0,
               'DamageDealToMonster': 1.5},
               {'FloorType': 'Sating',
               'HealModifier': 1.5,
               'Poison': 0,
               'DamageDealToMonster': 1
               },
               {'FloorType': 'Ultra Poisonous',
               'HealModifier': 1,
               'Poison': 2,
               'DamageDealToMonster': 1
               },
               {'FloorType': 'Ultra Spiky',
                'HealModifier': 1,
                'Poison': 0,
                'DamageDealToMonster': 3},
                {'FloorType': 'Ultra Sating', 
                'HealModifier': 3, 
                'Poison': 0, 
                'DamageDealToMonster': 1}
                ]

Weapons = [{
            'Name': 'Stick',
            'BaseDamageBoost': 0.5
           },
           {
            'Name': 'Dagger',
            'BaseDamageBoost': 0.75
           },
           {
            'Name': 'Shortsword',
            'BaseDamageBoost': 1
           },
           {
            'Name': 'Longsword',
            'BaseDamageBoost': 1.25       
           },
           {
            'Name': 'Estoc',
            'BaseDamageBoost': 1.5      
           },
           {
            'Name': 'Mace',
            'BaseDamageBoost': 1.75       
           },
           {
            'Name': 'Sabre',
            'BaseDamageBoost': 2     
           }
          ]
ItemTraits = [{
         'Title': 'Rusty',
         'Modifier': 0.5        
        },
        {
         'Title': 'Regular',
         'Modifier': 1
        },
        {
         'Title': 'Steel',
         'Modifier': 1.5       
        },
        {
         'Title': 'Titanium',
         'Modifier': 2
        },
        {
         'Title': 'Ultra',
         'Modifier': 4       
        }
        ]       
BookTypes = [{
         'Name': 'Piece of paper',
         'BaseHealBoost': 0.5
        },
        {
         'Name': 'Scroll',
         'BaseHealBoost': 0.75
        },
        {
         'Name': 'Light Book',
         'BaseHealBoost': 1   
        },
        {
         'Name': 'Basic Book',
         'BaseHealBoost': 1.25   
        },
        {
         'Name': 'Heavy Book',
         'BaseHealBoost': 1.5   
        },
        {
         'Name': 'Encyclopedia',
         'BaseHealBoost': 1.75   
        },
        {
         'Name': 'Mobile Library',
         'BaseHealBoost': 2   
        }
]
BookTraits = [{
         'Title': 'Torn-up',
         'Modifier': 0.5
        },
        {
         'Title': 'Regular',
         'Modifier': 1   
        },
        {
         'Title': 'Magic',
         'Modifier': 1.5   
        },
        {
         'Title': 'Enchanted',
         'Modifier': 2
        },
        {
         'Title': 'Ultra',
         'Modifier': 4       
        }
]
ChestplateTypes = [{
         'Name': 'Clay vest',
         'BaseBlock': 0.25
        },
        {
         'Name': 'Leather vest',
         'BaseBlock': 0.5   
        },
        {
         'Name': 'Light armor',
         'BaseBlock': 0.75   
        },
        {
         'Name': 'Full-body armor',
         'BaseBlock': 1   
        }
]

def PrintFinalResults():
        FinalScore = (4*TotalDamageDealt) + (TotalHealingDone*(-1)) + (10*DefeatedMonsters)
        print(f"You managed to kill *{DefeatedMonsters}* monsters! \n"
        f"You healed for *{TotalHealingDone}* HP! \n"
        f"You dealt a total of *{TotalDamageDealt}* damage! \n"
        f"Your final score is *{FinalScore}*!")
        if FinalScore < 125:
                print("With a score like that, even my grandma is better!")
        elif FinalScore >= 125 and FinalScore < 175:
                print("Well, starting to get somewhere! Okay score!")
        elif FinalScore >= 175 and FinalScore < 225:
                print("Good score! Keep it up!")
        elif FinalScore >= 225 and FinalScore < 300:
                print("Now that is really good!")
        elif FinalScore >= 300 and FinalScore < 350:
                print("Well, if you've gotten a score like that you've probably beaten the game! Good job!")
        elif FinalScore >= 350:
                print("Wow! God-tier gamer!")

def PrintIntroduction():
    global DefeatedMonsters
    if DefeatedMonsters < 9:
        print(f"You are fighting against a *{MonsterTraits[MonsterTrait]['Title']} {MonsterList[MonsterFromList]['MonsterType']}* on a *{FloorTypes[FloorFromList]['FloorType']}* floor! \n"
              f"The *{MonsterTraits[MonsterTrait]['Title']} {MonsterList[MonsterFromList]['MonsterType']}* has *{MonsterHealth}* HP! \n" 
              f"It can deal *{MonsterMinDamage}-{MonsterMaxDamage}* damage! \n"
              f"You can deal *{ShownPossibleDamage}* damage! \n"
              f"You can heal for *{ShownPossibleHeal}* HP by using *3* Mana! \n"
              f"You have *{playerMana}* Mana out of a maximum of *{MaxMana}*! \n"
              f"You have *{playerHealth}* health and you can block *{PlayerChestplateBlock}* damage!\n"
              f"You can FIGHT, HEAL, RUN or check INVENTORY! \n"
            )
    elif DefeatedMonsters == 9:
        print(f"You are fighting against a *{MonsterTraits[MonsterTrait]['Title']} {Bosses[MonsterFromList]['MonsterType']}* on a *{FloorTypes[FloorFromList]['FloorType']}* floor! \n"
              f"The *{MonsterTraits[MonsterTrait]['Title']} {Bosses[MonsterFromList]['MonsterType']}* has *{MonsterHealth}* HP! \n" 
              f"It can deal *{MonsterMinDamage}-{MonsterMaxDamage}* damage! \n"
              f"You can deal *{ShownPossibleDamage}* damage! \n"
              f"You can heal for *{ShownPossibleHeal}* HP by using *3* Mana! \n"
              f"You have *{playerMana}* Mana out of a maximum of *{MaxMana}*! \n"
              f"You have *{playerHealth}* health and you can block *{PlayerChestplateBlock}* damage!\n"
              f"You can FIGHT, HEAL, RUN or check INVENTORY! \n"
            )
def GetNewItem():
    global PlayerWeapon
    global PlayerWeaponDamage
    global PlayerWeaponTrait
    global MinDamage
    global MaxDamage
    global ShownPossibleDamage
    global PlayerBook
    global PlayerBookTrait
    global MinHeal
    global MaxHeal
    global PlayerBookMagic
    global ShownPossibleHeal
    global PlayerChestplate
    global PlayerChestplateBlock
    global PlayerChestplateTrait
    ItemTypes = ['Chestplate', 'Weapon', 'Book']
    WhatTypeItem = random.choice(ItemTypes)
    MinDamage = PlayerBaseMinDamage + PlayerWeaponDamage
    MaxDamage = PlayerBaseMaxDamage + PlayerWeaponDamage
    EquipmentUltraCheck = randint(1, 100)
    if WhatTypeItem == 'Weapon':
        NewWeapon = random.choice(Weapons)
        if EquipmentUltraCheck > 8:
                NewWeaponTrait = randint(0, 3)
        else:
                NewWeaponTrait = 4
        NewWeaponDamage = NewWeapon['BaseDamageBoost']*ItemTraits[NewWeaponTrait]['Modifier']
        NewWeaponDamage = math.ceil(NewWeaponDamage)
        if PlayerWeaponDamage > NewWeaponDamage:
            print("You find a new weapon, but your current weapon is already better!")
        else:
            print(f"You acquire a new *{ItemTraits[NewWeaponTrait]['Title']} {NewWeapon['Name']}*! \n"
            f"It deals an additional *{NewWeaponDamage}* damage!")
            PlayerWeapon = NewWeapon
            PlayerWeaponTrait = NewWeaponTrait
            PlayerWeaponDamage = NewWeaponDamage
            MinDamage = PlayerBaseMinDamage + NewWeaponDamage
            MaxDamage = PlayerBaseMaxDamage + NewWeaponDamage
            ShownPossibleDamage = f"{MinDamage}-{MaxDamage}"
            print(f"You now deal *{MinDamage}* to *{MaxDamage}* Damage!")
    elif WhatTypeItem == 'Book':
        NewBook = random.choice(BookTypes)
        if EquipmentUltraCheck > 8:
                NewBookTrait = randint(0,3)
        else:
                NewBookTrait = 4
        NewBookMagic = NewBook['BaseHealBoost']*BookTraits[NewBookTrait]['Modifier']
        NewBookMagic = math.ceil(NewBookMagic)
        if PlayerBookMagic > NewBookMagic:
            print("You find a new book, but your current book is already better!")
        else:
            print(f"You acquire a new *{BookTraits[NewBookTrait]['Title']} {NewBook['Name']}*")
            PlayerBook = NewBook
            PlayerBookTrait = NewBookTrait
            PlayerBookMagic = NewBookMagic
            MinHeal = PlayerBaseMinHeal + NewBookMagic
            MaxHeal = PlayerBaseMaxHeal + NewBookMagic
            ShownPossibleHeal = f"{MinHeal}-{MaxHeal}"
            print(f"You now heal *{MinHeal}* to *{MaxHeal}* HP!")
    elif WhatTypeItem == 'Chestplate':
        NewChestplate = random.choice(ChestplateTypes)
        if EquipmentUltraCheck > 8:
                NewChestplateTrait = randint(0,3)
        else:
                NewChestplateTrait = 4
        NewChestplateBlock = NewChestplate['BaseBlock']*ItemTraits[NewChestplateTrait]['Modifier']
        if PlayerChestplateBlock > NewChestplateBlock:
            print("You find a new chestplate, but your current chestplate is already better!")
        else:
            print(f"You acquire a new *{ItemTraits[NewChestplateTrait]['Title']} {NewChestplate['Name']}*!")
            PlayerChestplate = NewChestplate
            PlayerChestplateTrait = NewChestplateTrait
            PlayerChestplateBlock = NewChestplateBlock
            print(f"You can now block {PlayerChestplateBlock} damage!") 
    else:
        print("Every item type should be available, so if you do get this, this is an error!")

MonsterFromList = randint(0,5) #FOR FUTURE - CALL THIS IN LOOP TOO!
FloorFromList = randint(0,6)
PhasesLeft = MonsterList[MonsterFromList]['Phases']
PhasesDefeated = 0

MaxMana = 10
playerMana = 10 

playerHealth = 20

PlayerWeapon = None
PlayerWeaponTrait = None
PlayerBookMagic = 0
PlayerWeaponDamage = 0
PlayerBaseMinDamage = 1
PlayerBaseMaxDamage = 4
MinDamage = 1
MaxDamage = 4

MinHeal = 2
MaxHeal = 4
PlayerBook = None
PlayerBookTrait = None
PlayerBookMagic = 0
PlayerBaseMinHeal = 2
PlayerBaseMaxHeal = 4

PlayerChestplate = None
PlayerChestplateTrait = None
PlayerChestplateBlock = 0
PlayerBaseBlock = 0

InputValid = 1
difference = 0

TotalHealingDone = 0
TotalDamageDealt = 0
DefeatedMonsters = 0
FinalScore = 0

while True:
        ClassChoice = input("You can be a WARRIOR, MAGE, TANK, KNIGHT! \n What do you want to be?: ")
        if ClassChoice == "WARRIOR" or ClassChoice == "warrior" or ClassChoice == "W" or ClassChoice == "w":
                PlayerBaseMinHeal = 1
                PlayerBaseMaxHeal = 3
                PlayerBaseMinDamage = 2
                PlayerBaseMaxDamage = 5
                playerHealth = 25
                MaxMana = 8
                PlayerMana = 8
                break
        elif ClassChoice == "MAGE" or ClassChoice == "mage" or ClassChoice == "m" or ClassChoice == "M":
                PlayerBaseMinHeal = 3
                PlayerBaseMaxHeal = 5
                PlayerBaseMinDamage = 1
                PlayerBaseMaxDamage = 4
                PlayerHealth = 15
                MaxMana = 12
                PlayerMana = 12
                break
        elif ClassChoice == "TANK" or ClassChoice == "tank" or ClassChoice == "T" or ClassChoice == "t":
                PlayerBaseMinHeal = 2
                PlayerBaseMaxHeal = 4
                PlayerBaseMinDamage = 1
                PlayerBaseMaxDamage = 4
                PlayerHealth = 30
                MaxMana = 8
                PlayerMana = 8
                break
        elif ClassChoice == "KNIGHT" or ClassChoice == "knight" or ClassChoice == "K" or ClassChoice == "k":
                MaxMana = 10
                playerMana = 10 
                playerHealth = 20
                PlayerBaseMinHeal = 2
                PlayerBaseMaxHeal = 4
                PlayerBaseMinDamage = 1
                PlayerBaseMaxDamage = 4
                break
        else:
                print("Invalid input!")
MonsterTrait = randint(0,5)
ShownPossibleDamage = f"{MinDamage}-{MaxDamage}"
ShownPossibleHeal = f"{MinHeal}-{MaxHeal}"
MonsterHealth = MonsterList[MonsterFromList]['MonsterHealth']*MonsterTraits[MonsterTrait]['HealthModifier']*(0.5**PhasesDefeated)
MonsterMinDamage = math.ceil(MonsterList[MonsterFromList]['MonsterMinDamage']*MonsterTraits[MonsterTrait]['DamageModifier']*(0.5**PhasesDefeated))
MonsterMaxDamage = math.ceil(MonsterList[MonsterFromList]['MonsterMaxDamage']*MonsterTraits[MonsterTrait]['DamageModifier']*(0.5**PhasesDefeated))
MonsterPossibleDamage = randint(MonsterMinDamage, MonsterMaxDamage)
PrintIntroduction()
while playerHealth > 0:
    playerAction = input("Enter your action: ")
    PossibleDamage = randint(MinDamage, MaxDamage)
    PossibleHeal = randint(MinHeal, MaxHeal)
    MonsterPossibleDamage = randint(MonsterMinDamage, MonsterMaxDamage)
    if playerAction == "FIGHT" or playerAction == "fight" or playerAction == "f" or playerAction == "F":
            MissChance = randint(1, 100)
            if MissChance > 20:
                MonsterHealth = MonsterHealth - (PossibleDamage*FloorTypes[FloorFromList]['DamageDealToMonster'])
                TotalDamageDealt += PossibleDamage*FloorTypes[FloorFromList]['DamageDealToMonster']
                if DefeatedMonsters < 9:
                        print(f"You attack the *{MonsterList[MonsterFromList]['MonsterType']}* for *{PossibleDamage}* with a floor modifier of *{FloorTypes[FloorFromList]['DamageDealToMonster']}*, resulting in *{PossibleDamage * FloorTypes[FloorFromList]['DamageDealToMonster']}* damage! \n"
                        f"It now has *{MonsterHealth}* HP left!")
                elif DefeatedMonsters == 9:
                        print(f"You attack the *{Bosses[MonsterFromList]['MonsterType']}* for *{PossibleDamage}* with a floor modifier of *{FloorTypes[FloorFromList]['DamageDealToMonster']}*, resulting in *{PossibleDamage * FloorTypes[FloorFromList]['DamageDealToMonster']}* damage! \n"
                        f"It now has *{MonsterHealth}* HP left!")                
                if playerMana < MaxMana:
                        playerMana += 1
                        print(f"You regain *1* Mana! You now have *{playerMana}* Mana!")
                else:
                        pass
            else:
                print("You try to attack but miss the opponent!")    
    elif playerAction == "HEAL" or playerAction == "heal" or playerAction == "h" or playerAction == "H":
            if playerMana >= 3:
                playerHealth = playerHealth + PossibleHeal*FloorTypes[FloorFromList]['HealModifier']
                playerMana -= 3
                TotalHealingDone += PossibleHeal*FloorTypes[FloorFromList]['HealModifier']
                print(f"You heal for *{PossibleHeal}* with a modifier of *{FloorTypes[FloorFromList]['HealModifier']}* for a total of *{PossibleHeal*FloorTypes[FloorFromList]['HealModifier']}*! You now have *{playerHealth}* HP!")
                print(f"You use up *3* Mana! You now have *{playerMana}* Mana left!")
            else:
                InputValid = 0
                print(f"You do not have enough mana to cast Heal!")
    elif playerAction == "RUN" or playerAction == "run" or playerAction == "r" or playerAction == "R":
            print("You run away! A cowardly choice to be certain, alas, the tower remains a danger to humanity...\n" 
                "================ C O W A R D L Y W A Y O U T ================")
            PrintFinalResults()
            break
    elif playerAction == "INVENTORY" or playerAction == "I" or playerAction == "i" or playerAction == "inventory" or playerAction == "INV" or playerAction == "inv":
            if PlayerWeaponTrait != None:
                print(f"Weapon: *{ItemTraits[PlayerWeaponTrait]['Title']} {PlayerWeapon['Name']}*: *{PlayerWeaponDamage}* damage")
            else:
                print("You do not have a *Weapon*!")
            if PlayerChestplateTrait != None:
                print(f"Chestplate: *{ItemTraits[PlayerChestplateTrait]['Title']} {PlayerChestplate['Name']}*: *{PlayerChestplateBlock}* block")
            else:
                print("You do not have a *Chestplate*!")
            if PlayerBookTrait != None:
                print(f"Magic scroll: *{BookTraits[PlayerBookTrait]['Title']} {PlayerBook['Name']}*: *{PlayerBookMagic}* magic")
            else:
                print("You do not have a *Magic Book*!")
            InputValid = 0
            print("\n")
    else:
            print("Invalid input!")
            InputValid = 0    
    if InputValid == 1 and MonsterHealth > 0:
        DodgeChance = randint(1,100)
        if DodgeChance > 15:  
                if PlayerChestplateBlock - MonsterPossibleDamage >= 0:
                        print(f"You block all damage you take from the monster!")
                else: 
                  if DefeatedMonsters < 9:
                        playerHealth = playerHealth - MonsterPossibleDamage + PlayerChestplateBlock
                        print(f"*{MonsterList[MonsterFromList]['MonsterType']}* attacks you for *{MonsterPossibleDamage}* but you block for *{PlayerChestplateBlock}* DMG!")
                  elif DefeatedMonsters == 9:
                        playerHealth = playerHealth - MonsterPossibleDamage + PlayerChestplateBlock
                        print(f"*{Bosses[MonsterFromList]['MonsterType']}* attacks you for *{MonsterPossibleDamage}* but you block for *{PlayerChestplateBlock}* DMG!")
        else:
            print("You dodge the monster's attack!")
        if FloorTypes[FloorFromList]['Poison'] >0:
            playerHealth = playerHealth - FloorTypes[FloorFromList]['Poison']
            print(f"The poison on the floor damages you for *{FloorTypes[FloorFromList]['Poison']}* HP!")
        else:
            pass
        print(f"You now have *{playerHealth}* HP left!")
        print("\n")
    elif InputValid == 1 and MonsterHealth <= 0:
        if PhasesLeft == 0:
            DefeatedMonsters += 1
            PhasesDefeated = 0
            if DefeatedMonsters < 10:
                print(f"The *{MonsterList[MonsterFromList]['MonsterType']}* has been defeated! You have defeated *{DefeatedMonsters}* monsters so far!\n"
                "\n"
                "================ M O N S T E R D E F E A T E D ================ \n"
                "\n"
                )
                GetNewItem()
            elif DefeatedMonsters == 10:
                print(f"The *{Bosses[MonsterFromList]['MonsterType']}* has been defeated!")
            if playerMana < MaxMana and DefeatedMonsters != 10:
                    if playerMana + 5 > MaxMana:
                            difference = MaxMana - playerMana
                            playerMana += difference
                            print(f"You regain *{difference}* Mana for clearing the floor! You now have *{playerMana}* Mana! \n")
                    else: 
                        playerMana += 5
                        print(f"You regain *5* Mana for clearing the floor! You now have *{playerMana}* Mana! \n")
            else:
                    print("\n")
                    pass
            if DefeatedMonsters == 10:
                print("THE PLAYER HAS DEFEATED THE FINAL ENEMY! THE TOWER IS NOW FREE! \n"
                "================    Y O U A R E W I N N E R    ================")
                PrintFinalResults()
                break
            elif DefeatedMonsters < 9:
                MonsterFromList = randint(0,5)
                FloorFromList = randint(0,6)
                UltraCheck = randint(1,100)
                if UltraCheck > 8:
                        MonsterTrait = randint(0,5)
                        #print("New monster should be a normal one")
                        #print(MonsterTraits[MonsterTrait]['Title'])
                else:
                        MonsterTrait = 6
                        #print("New monster should be an ultra one")
                        #print(MonsterTraits[MonsterTrait]['Title'])
                MonsterHealth = MonsterList[MonsterFromList]['MonsterHealth']*MonsterTraits[MonsterTrait]['HealthModifier']*(0.5**PhasesDefeated)
                MonsterMinDamage = math.ceil(MonsterList[MonsterFromList]['MonsterMinDamage']*MonsterTraits[MonsterTrait]['DamageModifier']*(0.5**PhasesDefeated))
                MonsterMaxDamage = math.ceil(MonsterList[MonsterFromList]['MonsterMaxDamage']*MonsterTraits[MonsterTrait]['DamageModifier']*(0.5**PhasesDefeated))
                PrintIntroduction()
                PhasesLeft = MonsterList[MonsterFromList]['Phases']
            elif DefeatedMonsters == 9:
                #print("Boss battle coming up here!")
                #print(f"CHECK: defeated {DefeatedMonsters} monsters ")
                MonsterFromList = randint(0,0)
                FloorFromList = randint(0,6)
                MonsterTrait = 7
                MonsterHealth = Bosses[MonsterFromList]['MonsterHealth']*MonsterTraits[MonsterTrait]['HealthModifier']
                MonsterMinDamage = math.ceil(Bosses[MonsterFromList]['MonsterMinDamage']*MonsterTraits[MonsterTrait]['DamageModifier'])
                MonsterMaxDamage = math.ceil(Bosses[MonsterFromList]['MonsterMaxDamage']*MonsterTraits[MonsterTrait]['DamageModifier'])
                MonsterPossibleDamage = randint(MonsterMinDamage, MonsterMaxDamage)
                PhasesLeft = MonsterList[MonsterFromList]['Phases']
                print("================= B O S S F I G H T ===========")
                PrintIntroduction()
        elif PhasesLeft != 0:
                PhasesDefeated += 1
                PhasesLeft -= 1
                print("You thought you defeated the monster, but it rises up once more! \n")
                if DefeatedMonsters < 9:
                        MonsterHealth = (MonsterList[MonsterFromList]['MonsterHealth']*MonsterTraits[MonsterTrait]['HealthModifier'])*(0.5**PhasesDefeated)
                elif DefeatedMonsters == 9:
                        MonsterHealth = (Bosses[MonsterFromList]['MonsterHealth']*MonsterTraits[MonsterTrait]['HealthModifier'])*(0.5**PhasesDefeated)
                MonsterMinDamage = math.ceil(MonsterMinDamage*(0.5**PhasesDefeated))
                MonsterMaxDamage = math.ceil(MonsterMaxDamage*(0.5**PhasesDefeated))
                MonsterPossibleDamage = randint(MonsterMinDamage, MonsterMaxDamage)
                #print(PhasesLeft)
                PrintIntroduction()
        #print("Phase should be defeated here")
    elif InputValid == 0:
            InputValid = 1
    if playerHealth <= 0:
            print("The player has run out of health! \n"
            "\n"
            f"You defeated *{DefeatedMonsters}* monsters!\n"
            "\n"
            "================        G A M E L O S T        ================"
            )
            PrintFinalResults()
