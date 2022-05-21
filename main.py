from random import randint
import random
import math
MonsterList = [{'MonsterType': 'Skeleton',
               'MonsterHealth': 8,
               'MonsterMinDamage': 1,
               'MonsterMaxDamage': 3}, 
               {'MonsterType': 'Bat',
               'MonsterHealth': 3,
               'MonsterMinDamage': 3,
               'MonsterMaxDamage': 5},
               {'MonsterType' : 'Alligator',
               'MonsterHealth': 4,
               'MonsterMinDamage': 2,
               'MonsterMaxDamage': 7},
               {'MonsterType' : 'Ninja',
               'MonsterHealth': 3,
               'MonsterMinDamage': 8,
               'MonsterMaxDamage': 10},
               {'MonsterType' : 'Muddy Crab',
               'MonsterHealth': 3,
               'MonsterMinDamage': 100,
               'MonsterMaxDamage': 100} 
               ]
Bosses = [{
         'MonsterType': 'Massive Mosquitoe',
         'MonsterHealth': 30,
         'MonsterMinDamage': 2,
         'MonsterMaxDamage': 6
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
        print(f"You are fighting against a *{MonsterList[MonsterFromList]['MonsterType']}* on a *{FloorTypes[FloorFromList]['FloorType']}* floor! \n"
              f"The *{MonsterList[MonsterFromList]['MonsterType']}* has *{MonsterHealth}* HP! \n" 
              f"It can deal *{MonsterList[MonsterFromList]['MonsterMinDamage']}-{MonsterList[MonsterFromList]['MonsterMaxDamage']}* damage! \n"
              f"You can deal *{ShownPossibleDamage}* damage! \n"
              f"You can heal for *{ShownPossibleHeal}* HP by using *3* Mana! \n"
              f"You have *{playerMana}* Mana out of a maximum of *{MaxMana}*! \n"
              f"You have *{playerHealth}* health and you can block *{PlayerChestplateBlock}* damage!\n"
              f"You can FIGHT, HEAL, RUN or check INVENTORY! \n"
            )
    elif DefeatedMonsters == 9:
        print(f"You are fighting against a *{Bosses[MonsterFromList]['MonsterType']}* on a *{FloorTypes[FloorFromList]['FloorType']}* floor! \n"
              f"The *{Bosses[MonsterFromList]['MonsterType']}* has *{MonsterHealth}* HP! \n" 
              f"It can deal *{Bosses[MonsterFromList]['MonsterMinDamage']}-{Bosses[MonsterFromList]['MonsterMaxDamage']}* damage! \n"
              f"You can deal *{ShownPossibleDamage}* damage! \n"
              f"You can heal for *{ShownPossibleHeal}* HP by using *3* Mana! \n"
              f"You have *{playerMana}* Mana out of a maximum of *{MaxMana}*! \n"
              f"You have *{playerHealth}* health and you can block *{PlayerChestplateBlock}* damage!\n"
              f"You can FIGHT, HEAL or RUN! \n"
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
    if WhatTypeItem == 'Weapon':
        NewWeapon = random.choice(Weapons)
        NewWeaponTrait = random.choice(ItemTraits)
        NewWeaponDamage = NewWeapon['BaseDamageBoost']*NewWeaponTrait['Modifier']
        NewWeaponDamage = math.ceil(NewWeaponDamage)
        if PlayerWeaponDamage > NewWeaponDamage:
            print("You find a new weapon, but your current weapon is already better!")
        else:
            print(f"You acquire a new *{NewWeaponTrait['Title']} {NewWeapon['Name']}*! \n"
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
        NewBookTrait = random.choice(BookTraits)
        NewBookMagic = NewBook['BaseHealBoost']*NewBookTrait['Modifier']
        NewBookMagic = math.ceil(NewBookMagic)
        if PlayerBookMagic > NewBookMagic:
            print("You find a new book, but your current book is already better!")
        else:
            print(f"You acquire a new *{NewBookTrait['Title']} {NewBook['Name']}*")
            PlayerBook = NewBook
            PlayerBookTrait = NewBookTrait
            PlayerBookMagic = NewBookMagic
            MinHeal = PlayerBaseMinHeal + NewBookMagic
            MaxHeal = PlayerBaseMaxHeal + NewBookMagic
            ShownPossibleHeal = f"{MinHeal}-{MaxHeal}"
            print(f"You now heal *{MinHeal}* to *{MaxHeal}* HP!")
    elif WhatTypeItem == 'Chestplate':
        NewChestplate = random.choice(ChestplateTypes)
        NewChestplateTrait = random.choice(ItemTraits)
        NewChestplateBlock = NewChestplate['BaseBlock']*NewChestplateTrait['Modifier']
        if PlayerChestplateBlock > NewChestplateBlock:
            print("You find a new chestplate, but your current chestplate is already better!")
        else:
            print(f"You acquire a new *{NewChestplateTrait['Title']} {NewChestplate['Name']}*!")
            PlayerChestplate = NewChestplate
            PlayerChestplateTrait = NewChestplateTrait
            PlayerChestplateBlock = NewChestplateBlock
            print(f"You can now block {PlayerChestplateBlock} damage!") 
    else:
        print("Every item type should be available, so if you do get this, this is an error!")

MonsterFromList = randint(0,4) #FOR FUTURE - CALL THIS IN LOOP TOO!
FloorFromList = randint(0,6)

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

ShownPossibleDamage = f"{MinDamage}-{MaxDamage}"
ShownPossibleHeal = f"{MinHeal}-{MaxHeal}"
MonsterHealth = MonsterList[MonsterFromList]['MonsterHealth'] #FOR FUTURE - CALL THIS IN LOOP TOO!
MonsterPossibleDamage = randint(MonsterList[MonsterFromList]['MonsterMinDamage'], MonsterList[MonsterFromList]['MonsterMaxDamage'])
PrintIntroduction()
while playerHealth > 0:
    playerAction = input("Enter your action: ")
    PossibleDamage = randint(MinDamage, MaxDamage)
    PossibleHeal = randint(MinHeal, MaxHeal)
    if DefeatedMonsters < 9:
        MonsterPossibleDamage = randint(MonsterList[MonsterFromList]['MonsterMinDamage'], MonsterList[MonsterFromList]['MonsterMaxDamage'])
    elif DefeatedMonsters == 9:
        MonsterPossibleDamage = randint(Bosses[MonsterFromList]['MonsterMinDamage'], Bosses[MonsterFromList]['MonsterMaxDamage'])
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
                print(f"Weapon: *{PlayerWeaponTrait['Title']} {PlayerWeapon['Name']}*: *{PlayerWeaponDamage}* damage")
            else:
                print("You do not have a *Weapon*!")
            if PlayerChestplateTrait != None:
                print(f"Chestplate: *{PlayerChestplateTrait['Title']} {PlayerChestplate['Name']}*: *{PlayerChestplateBlock}* block")
            else:
                print("You do not have a *Chestplate*!")
            if PlayerBookTrait != None:
                print(f"Magic scroll: *{PlayerBookTrait['Title']} {PlayerBook['Name']}*: *{PlayerBookMagic}* magic")
            else:
                print("You do not have a *Magic Book*!")
            InputValid = 0
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
                print(f"You now have *{playerHealth}* HP left!")
        else:
            print("You dodge the monster's attack!")
        if FloorTypes[FloorFromList]['Poison'] >0:
            playerHealth = playerHealth - FloorTypes[FloorFromList]['Poison']
            print(f"The poison on the floor damages you for *{FloorTypes[FloorFromList]['Poison']}* HP!")
        else:
            pass
    elif InputValid == 1 and MonsterHealth <= 0:
            DefeatedMonsters += 1
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
                            print(f"You regain *{difference}* Mana for clearing the floor! You now have *{playerMana}* Mana!")
                    else: 
                        playerMana += 5
                        print(f"You regain *5* Mana for clearing the floor! You now have *{playerMana}* Mana!")
            else:
                    pass
            if DefeatedMonsters == 10:
                print("THE PLAYER HAS DEFEATED THE FINAL ENEMY! THE TOWER IS NOW FREE! \n"
                "================    Y O U A R E W I N N E R    ================")
                PrintFinalResults()
                break
            elif DefeatedMonsters < 9:
                MonsterFromList = randint(0,4)
                FloorFromList = randint(0,6)
                MonsterHealth = MonsterList[MonsterFromList]['MonsterHealth']
                MonsterPossibleDamage = randint(MonsterList[MonsterFromList]['MonsterMinDamage'], MonsterList[MonsterFromList]['MonsterMaxDamage'])
                PrintIntroduction()
            elif DefeatedMonsters == 9:
                print("Boss battle coming up here!")
                print(f"CHECK: defeated {DefeatedMonsters} monsters ")
                MonsterFromList = randint(0,0)
                FloorFromList = randint(0,6)
                MonsterHealth = Bosses[MonsterFromList]['MonsterHealth']
                MonsterPossibleDamage = randint(Bosses[MonsterFromList]['MonsterMinDamage'], Bosses[MonsterFromList]['MonsterMaxDamage'])
                print("================= B O S S F I G H T ===========")
                PrintIntroduction()
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
