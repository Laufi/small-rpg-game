from random import randint
import random
import math
MonsterList = [{'MonsterType': 'Skeleton',
               'MonsterHealth': 8,
               'MonsterMinDamage': 1,
               'MonsterMaxDamage': 3,
               'Phases' : 0,
               'AlwaysAmbush' : False,
               'NeverAmbush' : False,
               'WeakToFire': False,
               'WeakToIce': False}, 
               {'MonsterType': 'Bat',
               'MonsterHealth': 3,
               'MonsterMinDamage': 3,
               'MonsterMaxDamage': 5,
               'Phases': 0,
               'AlwaysAmbush' : False,
               'NeverAmbush' : False,
               'WeakToFire': True,
               'WeakToIce': False},
               {'MonsterType' : 'Alligator',
               'MonsterHealth': 4,
               'MonsterMinDamage': 2,
               'MonsterMaxDamage': 7,
               'Phases': 0,
               'AlwaysAmbush' : False,
               'NeverAmbush' : False,
               'WeakToFire': False,
               'WeakToIce': True},
               {'MonsterType' : 'Ninja',
               'MonsterHealth': 3,
               'MonsterMinDamage': 8,
               'MonsterMaxDamage': 10,
               'Phases': 0,
               'AlwaysAmbush' : False,
               'NeverAmbush' : False,
               'WeakToFire': True,
               'WeakToIce': False},
               {'MonsterType' : 'Muddy Crab',
               'MonsterHealth': 3,
               'MonsterMinDamage': 100,
               'MonsterMaxDamage': 100,
               'Phases': 0,
               'AlwaysAmbush' : False,
               'NeverAmbush' : True,
               'WeakToFire': True,
               'WeakToIce': True},
               {'MonsterType' : 'Zombie',
               'MonsterHealth': 6,
               'MonsterMinDamage': 2,
               'MonsterMaxDamage': 4,
               'Phases': 1,
               'AlwaysAmbush' : False,
               'NeverAmbush' : True,
               'WeakToFire': True,
               'WeakToIce': False},
               {'MonsterType' : 'Rat',
               'MonsterHealth': 3,
               'MonsterMinDamage': 1,
               'MonsterMaxDamage': 1,
               'Phases': 0,
               'AlwaysAmbush': True,
               'AmbushMessage': 'You are shocked when you only see a rat!',
               'NeverAmbush' : False,
               'WeakToFire': False,
               'WeakToIce': True},
               {'MonsterType' : 'Frog',
               'MonsterHealth': 2,
               'MonsterMinDamage': 3,
               'MonsterMaxDamage': 3,
               'Phases': 0,
               'AlwaysAmbush': False,
               'NeverAmbush' : True,
               'WeakToFire': True,
               'WeakToIce': True}
               ]
Bosses = [{
         'MonsterType': 'Massive Mosquito',
         'MonsterHealth': 30,
         'MonsterMinDamage': 2,
         'MonsterMaxDamage': 6,
         'Phases': 0,
         'AlwaysAmbush': False,
         'NeverAmbush' : False,
         'WeakToFire': True,
         'WeakToIce': False,
         'BossIntroductionMessage': 'You hear the buzz of a massive mosquito...'
        },
        {
         'MonsterType': 'Giant Dragon',
         'MonsterHealth': 45,
         'MonsterMinDamage': 2,
         'MonsterMaxDamage': 4,
         'Phases': 0,
         'AlwaysAmbush': True,
         'AmbushMessage': 'You are stunned in awe at the size of the dragon!',
         'NeverAmbush': False,
         'WeakToFire': False,
         'WeakToIce': True,
         'BossIntroductionMessage': 'It is a massive, old dragon!'       
        },
        {
         'MonsterType': 'Rogue Knight',
         'MonsterHealth': 20,
         'MonsterMinDamage': 2,
         'MonsterMaxDamage': 5,
         'Phases': 0,
         'AlwaysAmbush': True,
         'AmbushMessage': 'The experience of your opponent makes them attack first!',
         'NeverAmbush': False,
         'WeakToFire': False,
         'WeakToIce': False,
         'BossIntroductionMessage': 'A rogue hero, who has gone against his morality.'       
        },
        {
         'MonsterType': 'Humongous Turtle',
         'MonsterHealth': 60,
         'MonsterMinDamage': 1,
         'MonsterMaxDamage': 2,
         'Phases': 0,
         'AlwaysAmbush': False,
         'NeverAmbush': True,
         'WeakToFire': False,
         'WeakToIce': False,
         'BossIntroductionMessage': 'You hear the stomps of a giant turtle...'       
        },
        {
         'MonsterType': 'Flying Bird',
         'MonsterHealth': 15,
         'MonsterMinDamage': 12,
         'MonsterMaxDamage': 16,
         'Phases': 0,
         'AlwaysAmbush': False,
         'NeverAmbush': False,
         'WeakToFire': True,
         'WeakToIce': False,
         'BossIntroductionMessage': 'You can see a small, speedy bird dash around...'       
        },
        {'MonsterType': 'Skeleton Knight',
        'MonsterHealth': 20,
        'MonsterMinDamage': 8,
        'MonsterMaxDamage': 10,
        'Phases': 1,
        'AlwaysAmbush': False,
        'NeverAmbush': True,
        'WeakToFire': False,
        'WeakToIce': True,
        'BossIntroductionMessage': 'You can hear the neighs of a horse...'
        },
        {'MonsterType': 'Bug Mother',
        'MonsterHealth': 10,
        'MonsterMinDamage': 10,
        'MonsterMaxDamage': 12,
        'Phases': 3,
        'AlwaysAmbush': False,
        'NeverAmbush': True,
        'WeakToFire': True,
        'WeakToIce': False,
        'BossIntroductionMessage': 'You can hear thousands of bugs...'}
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
        FinalScore = (4*TotalDamageDealt) + (2*TotalMagicDamage) + (TotalHealingDone*(-1)) + (10*DefeatedMonsters)
        print(f"You managed to kill *{DefeatedMonsters}* monsters! \n"
        f"You healed for *{TotalHealingDone}* HP! \n"
        f"You did a total of *{TotalMagicDamage}* magic damage! \n"
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
    global PlayerMagicDamage
    global PlayerPoisonDamage
    if DefeatedMonsters < 9:
        print(f"You are fighting against a *{MonsterTraits[MonsterTrait]['Title']} {MonsterList[MonsterFromList]['MonsterType']}* on a *{FloorTypes[FloorFromList]['FloorType']}* floor! \n"
              f"The *{MonsterTraits[MonsterTrait]['Title']} {MonsterList[MonsterFromList]['MonsterType']}* has *{MonsterHealth}* HP! \n" 
              f"It can deal *{MonsterMinDamage}-{MonsterMaxDamage}* damage! \n"
              f"You can deal *{ShownPossibleDamage}* damage!")
        if PlayerMagic != 'POISSON':
                if PlayerMagic == 'HEAL':
                        print(f"You can cast heal MAGIC for *{ShownPossibleHeal}* HP by using *3* Mana!")
                elif PlayerMagic == 'FIREBALL':
                        print(f"You can cast fire MAGIC for *{PlayerMagicDamage}* damage by using *4* Mana!")
                elif PlayerMagic == 'ICE':
                        print(f"You can cast ice MAGIC for *{PlayerMagicDamage}* damage by using *4* Mana!")
                print(f"You have *{playerMana}* Mana out of a maximum of *{MaxMana}*!")
        elif PlayerMagic == 'POISSON' and PoisonMagicUsed == False:
                print(f"You can cast POISSON magic!")
        elif PlayerMagic == 'POISSON' and PoisonMagicUsed == True:
                print(f"You have already used POISSON this floor!")
        print(f"You have *{playerHealth}* health and you can block *{PlayerBlock}* damage!\n"
              f"You can FIGHT, cast MAGIC, RUN or check INVENTORY! \n")
            
    elif DefeatedMonsters == 9:
        print(f"You are fighting against a *{MonsterTraits[MonsterTrait]['Title']} {Bosses[MonsterFromList]['MonsterType']}* on a *{FloorTypes[FloorFromList]['FloorType']}* floor! \n"
              f"The *{MonsterTraits[MonsterTrait]['Title']} {Bosses[MonsterFromList]['MonsterType']}* has *{MonsterHealth}* HP! \n" 
              f"It can deal *{MonsterMinDamage}-{MonsterMaxDamage}* damage! \n"
              f"You can deal *{ShownPossibleDamage}* damage!")
        if PlayerMagic != 'POISSON':
                if PlayerMagic == 'HEAL':
                        print(f"You can cast heal MAGIC for *{ShownPossibleHeal}* HP by using *3* Mana!")
                elif PlayerMagic == 'FIREBALL':
                        print(f"You can cast fire MAGIC for *{PlayerMagicDamage}* damage by using *4* Mana!")
                elif PlayerMagic == 'ICE':
                        print(f"You can cast ice MAGIC for *{PlayerMagicDamage}* damage by using *4* Mana!")
                print(f"You have *{playerMana}* Mana out of a maximum of *{MaxMana}*!")
        elif PlayerMagic == 'POISSON' and PoisonMagicUsed == False:
                print(f"You can cast POISSON magic!")
        elif PlayerMagic == 'POISSON' and PoisonMagicUsed == True:
                print(f"You have already used POISSON this floor!")
        print(f"You have *{playerHealth}* health and you can block *{PlayerBlock}* damage!\n"
              f"You can FIGHT, cast MAGIC, RUN or check INVENTORY! \n")
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
    global PlayerBaseBlock
    global PlayerBlock
    global PlayerBaseMagicDamage
    global PlayerBaseMagicPoison
    global PlayerMagicDamage
    global PlayerPoisonDamage
    global PlayerMagic
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
            PlayerMagicDamage = PlayerBaseMagicDamage + NewBookMagic
            PlayerPoisonDamage = PlayerBaseMagicPoison + NewBookMagic
            if PlayerMagic == 'HEAL':
                print(f"You now heal *{MinHeal}* to *{MaxHeal}* HP!")
            elif PlayerMagic == 'ICE' or PlayerMagic == 'FIREBALL':
                print(f"You now deal *{PlayerMagicDamage}* Magic damage!")
            elif PlayerMagic == 'POISSON':
                print(f"You now deal {PlayerPoisonDamage} Poison damage!")

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
            PlayerBlock = PlayerBaseBlock + PlayerChestplateBlock
            print(f"You can now block {PlayerBlock} damage!") 
    else:
        print("Every item type should be available, so if you do get this, this is an error!")

MonsterFromList = randint(0,6) #FOR FUTURE - CALL THIS IN LOOP TOO!
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
PlayerBaseMagicDamage = 5
PlayerBaseMagicPoison = 3
PoisonMagicUsed = False
PlayerMagicDamage = 5
PlayerPoisonDamage = 3
PoisonTimeLeft = 0

PlayerChestplate = None
PlayerChestplateTrait = None
PlayerChestplateBlock = 0
PlayerBaseBlock = 0
PlayerBlock = 0

InputValid = 1
difference = 0

TotalMagicDamage = 0
TotalHealingDone = 0
TotalDamageDealt = 0
DefeatedMonsters = 0
FinalScore = 0
AntiPoisonBug = False
print("========================== \n"
      "Welcome to the game! \n"
      "You are a hero tasked with clearing a tower of it's monsters(adversaries)!")
while True:
        GuideChoice = input("Would you like to learn about MAGIC, COMBAT, FLOORS, EQUIPMENT, BOSS, ADVERSARIES, CLASS or START the game? \n"
        "Input your choice here: ")
        if GuideChoice == "Magic" or GuideChoice == "MAGIC" or GuideChoice == "Magic" or GuideChoice == "m" or GuideChoice == "M":
                print("Currently there is one type of magic in the game! \n"
                "Each Magic costs 3 Mana to cast! \n"
                "Effects of magic are: \n"
                "- Heal : You heal yourself for an amount of health! \n"
                "The amount you heal is based on your EQUIPMENT and your class!")
        elif GuideChoice == "Combat" or GuideChoice == "COMBAT" or GuideChoice == "combat" or GuideChoice == "C" or GuideChoice == "c":
                print("The player is able to deal damage to monsters by Fighting! \n"
                "If you are not ambushed,  you are always the first to attack! \n"
                "Remember, there is always a 5 percent chance of you being ambushed! \n"
                "There is also a chance of either the monster or player dodging an attack! \n"
                "The amount of damage you deal is based on your EQUIPMENT and your class! \n"
                "With some equipment, the player is able to get a BLOCK! \n"
                "BLOCK blocks an amount of damage from each attack you take!")
        elif GuideChoice == "Floors" or GuideChoice == "FLOORS" or GuideChoice == "floors" or GuideChoice == "F" or GuideChoice == "f":
                print("Each fight happens on a different 'Floor' type! \n"
                "Some floor types, such as Poison, deal a set amount of damage to the player after every turn! \ņ"
                "There are currently 4 floor types in the game, with 3 ultra variants: \n"
                "- Regular : Healing modifier 1x; Damage dealt to monster 1x; 0 poison \n"
                "- Sating : Healing modifier 1.5x; Damage dealt to monster 1x; 0 poison \n"
                "- Poisonous : Healing modifier 1x; Damage dealt to monster 1x; 1 poison \n"
                "- Spiky : Healing modifier 1x; Damage dealt to monster 1.5x; 0 poison \n"
                "Remember: The 'Ultra' floor variants have twice as big of an effect!")
        elif GuideChoice == "Equipment" or GuideChoice == "EQUIPMENT" or GuideChoice == "equipment" or GuideChoice == "E" or GuideChoice == "e":
                print("Each time you defeat a monster, you get a new piece of equipment! \n"
                "There are 3 types of equipment: \n"
                "- WEAPON : You deal additional damage with your attacks! \n"
                "- ARMOR : You BLOCK some damage from monster's attacks! \n"
                "- MAGIC BOOK : You do extra magic! \n"
                "Remember: There is a slight chance to get Ultra equipment, which is stronger!")        
        elif GuideChoice == "Boss" or GuideChoice == "BOSS" or GuideChoice == "boss" or GuideChoice == "B" or GuideChoice == "b":
                print("On the 10th floor lies a boss! \n"
                "You must defeat it to win the game!")
        elif GuideChoice == "Adversaries" or GuideChoice == "ADVERSARIES" or GuideChoice == "adversaries" or GuideChoice == "A" or GuideChoice == "a":
                print("There is one monster on each floor! \n"
                "To get to the next floor, you must defeat it! \n"
                "Some monsters are weak to FIRE, ICE! \n"
                "There are multiple monster types, each with their own stats!")
        elif GuideChoice == "Start" or GuideChoice == "START" or GuideChoice == "start" or GuideChoice == "S" or GuideChoice == "s":
                print("Starting the game!")
                print("==========================")     
                print("\n")  
                break
        else:
                print("Invalid input!")
        print("\n")
while True:
        ClassChoice = input("You can be a WARRIOR, MAGE, TANK, KNIGHT! \n What do you want to be?: ")
        print("\n")
        if ClassChoice == "WARRIOR" or ClassChoice == "warrior" or ClassChoice == "W" or ClassChoice == "w":
                PlayerBaseMinHeal = 1
                PlayerBaseMaxHeal = 3
                PlayerBaseMinDamage = 2
                PlayerBaseMaxDamage = 5
                playerHealth = 25
                MaxMana = 8
                playerMana = 8
                PlayerBaseMagicDamage = 3
                PlayerBaseMagicPoison = 2
                break
        elif ClassChoice == "MAGE" or ClassChoice == "mage" or ClassChoice == "m" or ClassChoice == "M":
                PlayerBaseMinHeal = 3
                PlayerBaseMaxHeal = 5
                PlayerBaseMinDamage = 1
                PlayerBaseMaxDamage = 4
                PlayerHealth = 15
                MaxMana = 12
                playerMana = 12
                PlayerBaseMagicDamage = 6
                PlayerBaseMagicPoison = 4
                break
        elif ClassChoice == "TANK" or ClassChoice == "tank" or ClassChoice == "T" or ClassChoice == "t":
                PlayerBaseMinHeal = 2
                PlayerBaseMaxHeal = 4
                PlayerBaseMinDamage = 1
                PlayerBaseMaxDamage = 4
                PlayerHealth = 30
                MaxMana = 8
                playerMana = 8
                PlayerBaseMagicDamage = 5
                PlayerBaseMagicPoison = 3
                break
        elif ClassChoice == "KNIGHT" or ClassChoice == "knight" or ClassChoice == "K" or ClassChoice == "k":
                MaxMana = 10
                playerMana = 10 
                playerHealth = 25
                PlayerBaseMinHeal = 2
                PlayerBaseMaxHeal = 4
                PlayerBaseMinDamage = 1
                PlayerBaseMaxDamage = 4
                PlayerBaseMagicDamage = 4
                PlayerBaseMagicPoison = 4
                break
        else:
                print("Invalid input!")
while True:
    PlayerMagicChoice = input("You can select HEAL, FIREBALL, ICE, POISSON as your magic! \n What magic do you want? :")
    if PlayerMagicChoice == "HEAL" or PlayerMagicChoice == "heal" or PlayerMagicChoice == "Heal" or PlayerMagicChoice == "H" or PlayerMagicChoice == "h":
        print("Player Magic is HEAL! \n")
        PlayerMagic = "HEAL"
        break
    elif PlayerMagicChoice == "FIREBALL" or PlayerMagicChoice == "fireball" or PlayerMagicChoice == "Fireball" or PlayerMagicChoice == "F" or PlayerMagicChoice == "f":
        print("Player magic is FIREBALL! \n")
        PlayerMagic = "FIREBALL"
        break
    elif PlayerMagicChoice == "ICE" or PlayerMagicChoice == "ice" or PlayerMagicChoice == "Ice" or PlayerMagicChoice == "I" or PlayerMagicChoice == "i":
        print("Player magic is ICE! \n")
        PlayerMagic = "ICE"
        break
    elif PlayerMagicChoice == "POISSON" or PlayerMagicChoice == "poisson" or PlayerMagicChoice == "Poisson" or PlayerMagicChoice == "P" or PlayerMagicChoice == "p":
        print("Player magic is POISSON! \n")
        PlayerMagic = "POISSON"
        break
    else:
        print("Invalid input! \n")


MinHeal = PlayerBaseMinHeal
MaxHeal = PlayerBaseMaxHeal
MinDamage = PlayerBaseMinDamage
MaxDamage = PlayerBaseMaxDamage
MonsterTrait = randint(0,5)
ShownPossibleDamage = f"{MinDamage}-{MaxDamage}"
ShownPossibleHeal = f"{MinHeal}-{MaxHeal}"
MonsterHealth = MonsterList[MonsterFromList]['MonsterHealth']*MonsterTraits[MonsterTrait]['HealthModifier']*(0.5**PhasesDefeated)
MonsterMinDamage = math.ceil(MonsterList[MonsterFromList]['MonsterMinDamage']*MonsterTraits[MonsterTrait]['DamageModifier']*(0.5**PhasesDefeated))
MonsterMaxDamage = math.ceil(MonsterList[MonsterFromList]['MonsterMaxDamage']*MonsterTraits[MonsterTrait]['DamageModifier']*(0.5**PhasesDefeated))
MonsterPossibleDamage = randint(MonsterMinDamage, MonsterMaxDamage)
PrintIntroduction()
while playerHealth > 0:
    if PoisonTimeLeft > 0:
            if AntiPoisonBug == False:
                MonsterHealth -= PlayerPoisonDamage
                TotalMagicDamage += PlayerPoisonDamage
                PoisonTimeLeft -= 1
                print(f"The poison damages the monster for {PlayerPoisonDamage} damage!")
                print(f"It now has {MonsterHealth} HP!")
                print(f"It is still poisoned for {PoisonTimeLeft} turns!")
                print("\n")
            elif AntiPoisonBug == True:
                AntiPoisonBug = False
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
    elif playerAction == "MAGIC" or playerAction == "magic" or playerAction == "m" or playerAction == "M":
            if PlayerMagic == 'HEAL':
                if playerMana >= 3:
                        playerHealth = playerHealth + PossibleHeal*FloorTypes[FloorFromList]['HealModifier']
                        playerMana -= 3
                        TotalHealingDone += PossibleHeal*FloorTypes[FloorFromList]['HealModifier']
                        print(f"You heal for *{PossibleHeal}* with a modifier of *{FloorTypes[FloorFromList]['HealModifier']}* for a total of *{PossibleHeal*FloorTypes[FloorFromList]['HealModifier']}*! You now have *{playerHealth}* HP!")
                        print(f"You use up *3* Mana! You now have *{playerMana}* Mana left!")
                else:
                        InputValid = 0
                        print(f"You do not have enough Mana to cast HEAL!")
            if PlayerMagic == 'FIREBALL':
                if playerMana >= 4:
                        if DefeatedMonsters < 9:
                                MonsterWeakToFire = MonsterList[MonsterFromList]['WeakToFire']
                        elif DefeatedMonsters == 9:
                                MonsterWeakToFire = Bosses[MonsterFromList]['WeakToFire']
                        if MonsterWeakToFire == True:
                                MonsterHealth -= PlayerMagicDamage*1.5
                                print("The monster is weak to fire!")
                                print(f"You deal {PlayerMagicDamage*1.5} damage!")
                                TotalMagicDamage += PlayerMagicDamage*1.5
                        elif MonsterWeakToFire == False:
                                MonsterHealth -= PlayerMagicDamage
                                print(f"You deal {PlayerMagicDamage} damage!")
                                TotalMagicDamage += PlayerMagicDamage
                        print(f"The monster has {MonsterHealth} HP left!")
                        playerMana -= 4
                        print(f"You have *{playerMana}* Mana left!")
                else:
                        InputValid = 0
                        print(f"You do not have enough Mana to cast FIREBALL!")
            if PlayerMagic == 'ICE':
                if playerMana >= 4:    
                        if DefeatedMonsters < 9:
                                MonsterWeakToIce = MonsterList[MonsterFromList]['WeakToIce']
                        elif DefeatedMonsters == 9:
                                MonsterWeakToIce = Bosses[MonsterFromList]['WeakToIce']
                        if MonsterWeakToIce == True:
                                MonsterHealth -= PlayerMagicDamage*1.5
                                print("The monster is weak to ice!")
                                print(f"You deal {PlayerMagicDamage*1.5} damage!")
                                TotalMagicDamage += PlayerMagicDamage*1.5
                        elif MonsterWeakToIce == False:
                                MonsterHealth -= PlayerMagicDamage
                                print(f"You deal {PlayerMagicDamage} damage!")
                                TotalMagicDamage += PlayerMagicDamage
                        print(f"The monster has {MonsterHealth} HP left!")
                        playerMana -= 4
                        print(f"You have *{playerMana}* Mana left!")
                else:
                        InputValid = 0
                        print(f"You do not have enough Mana to cast ICE!")
            if PlayerMagic == 'POISSON':
                if PoisonMagicUsed == False:
                        PoissonRoll = randint(0, 100)
                        if PoissonRoll >= 50:
                                PoisonTimeLeft = 3
                                PoisonMagicUsed = True
                                print("The Poisson magic poisons the enemy!")
                        elif PoissonRoll < 50:
                                MonsterFromList = 7
                                MonsterHealth = MonsterList[MonsterFromList]['MonsterHealth']
                                MonsterMinDamage = MonsterList[MonsterFromList]['MonsterMinDamage']
                                MonsterMaxDamage = MonsterList[MonsterFromList]['MonsterMaxDamage']
                                PoisonMagicUsed = True
                                print("The Poisson magic turns the enemy into a frog!")
                                PrintIntroduction()
                                MonsterPossibleDamage = randint(MonsterMinDamage, MonsterMaxDamage)
                else:
                        InputValid = 0
                        print("You have already used POISSON this floor!")
                        AntiPoisonBug = True
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
                if PlayerBlock - MonsterPossibleDamage >= 0:
                        print(f"You block all damage you take from the monster!")
                else: 
                  if DefeatedMonsters < 9:
                        playerHealth = playerHealth - MonsterPossibleDamage + PlayerBlock
                        print(f"*{MonsterList[MonsterFromList]['MonsterType']}* attacks you for *{MonsterPossibleDamage}* but you block for *{PlayerBlock}* DMG!")
                  elif DefeatedMonsters == 9:
                        playerHealth = playerHealth - MonsterPossibleDamage + PlayerBlock
                        print(f"*{Bosses[MonsterFromList]['MonsterType']}* attacks you for *{MonsterPossibleDamage}* but you block for *{PlayerBlock}* DMG!")
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
            AmbushCheck = randint(0, 100)
            PoisonMagicUsed = False
            PoisonTimeLeft = 0
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
                MonsterFromList = randint(0,6)
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
                RandomFloorEventCheck = randint(0, 100) #This is for random events!
                if RandomFloorEventCheck > 30:
                    pass
                elif RandomFloorEventCheck <= 30:
                        RandomFloorEvent = randint(0, 3)
                        if RandomFloorEvent == 0:
                                playerHealth += 10
                                print("You find a fountain!")
                                print(f"It heals you for *10* HP! You now have *{playerHealth}*")
                                print("\n")
                        elif RandomFloorEvent == 1:
                                PlayerBaseMinDamage += 1
                                PlayerBaseMaxDamage += 1
                                MinDamage += 1
                                MaxDamage += 1
                                ShownPossibleDamage = f"{MinDamage}-{MaxDamage}"
                                print("You find a strength potion! \n")
                                print(f"It increases your damage by *1*! You can now deal *{ShownPossibleDamage} damage!*")
                                print("\n")
                        elif RandomFloorEvent == 2:
                                PlayerBaseBlock += 1
                                PlayerBlock += 1
                                print("You find an Iron-Skin potion!")
                                print(f"It increases your block by *1*! You can now block *{PlayerBlock}* damage!")
                                print("\n")
                        elif RandomFloorEvent == 3:
                                playerMana = MaxMana
                                print("You find a Mana potion!")
                                print(f"You regain all your Mana! You now have *{playerMana}* MP!")
                                print("\n")
                MonsterHealth = MonsterList[MonsterFromList]['MonsterHealth']*MonsterTraits[MonsterTrait]['HealthModifier']*(0.5**PhasesDefeated)
                MonsterMinDamage = math.ceil(MonsterList[MonsterFromList]['MonsterMinDamage']*MonsterTraits[MonsterTrait]['DamageModifier']*(0.5**PhasesDefeated))
                MonsterMaxDamage = math.ceil(MonsterList[MonsterFromList]['MonsterMaxDamage']*MonsterTraits[MonsterTrait]['DamageModifier']*(0.5**PhasesDefeated))
                MonsterPossibleDamage = randint(MonsterMinDamage, MonsterMaxDamage)
                if MonsterList[MonsterFromList]['NeverAmbush'] == False and AmbushCheck <= 5 or MonsterList[MonsterFromList]['AlwaysAmbush'] == True:
                        if MonsterList[MonsterFromList]['AlwaysAmbush'] == False:
                                print("As you arrive at the new floor, you are ambushed!")
                                print(f"A *{MonsterTraits[MonsterTrait]['Title']} {MonsterList[MonsterFromList]['MonsterType']}* attacks you for *{MonsterPossibleDamage}*!")
                        elif MonsterList[MonsterFromList]['AlwaysAmbush'] == True:
                                print(MonsterList[MonsterFromList]['AmbushMessage'])
                                print(f"It attacks you for *{MonsterPossibleDamage}*!")
                        playerHealth -= MonsterPossibleDamage
                        print(f"You now have *{playerHealth}* HP!")
                        print("\n")
                        if playerHealth > 0:
                                PrintIntroduction()
                        else:
                                print("The player has run out of health! \n"
                                "\n"
                                f"You defeated *{DefeatedMonsters}* monsters!\n"
                                "\n"
                                "================        G A M E L O S T        ================"
                                )
                                PrintFinalResults()
                                break
                else:
                        PrintIntroduction()
                PhasesLeft = MonsterList[MonsterFromList]['Phases']
            elif DefeatedMonsters == 9:
                #print("Boss battle coming up here!")
                #print(f"CHECK: defeated {DefeatedMonsters} monsters ")
                MonsterFromList = randint(0,6)
                FloorFromList = randint(0,6)
                MonsterTrait = 7
                MonsterHealth = Bosses[MonsterFromList]['MonsterHealth']*MonsterTraits[MonsterTrait]['HealthModifier']
                MonsterMinDamage = math.ceil(Bosses[MonsterFromList]['MonsterMinDamage']*MonsterTraits[MonsterTrait]['DamageModifier'])
                MonsterMaxDamage = math.ceil(Bosses[MonsterFromList]['MonsterMaxDamage']*MonsterTraits[MonsterTrait]['DamageModifier'])
                MonsterPossibleDamage = randint(MonsterMinDamage, MonsterMaxDamage)
                PhasesLeft = Bosses[MonsterFromList]['Phases']
                print("================= B O S S F I G H T ===========")
                if Bosses[MonsterFromList]['NeverAmbush'] == False and AmbushCheck <= 5 or Bosses[MonsterFromList]['AlwaysAmbush'] == True:
                        if Bosses[MonsterFromList]['AlwaysAmbush'] == False:
                                print("As you arrive at the new floor, you are ambushed!")
                                print(f"A *{MonsterTraits[MonsterTrait]['Title']} {Bosses[MonsterFromList]['MonsterType']}* attacks you for *{MonsterPossibleDamage}*!")
                        elif Bosses[MonsterFromList]['AlwaysAmbush'] == True:
                                print(Bosses[MonsterFromList]['AmbushMessage'])
                                print(f"It attacks you for *{MonsterPossibleDamage}*!")
                        playerHealth -= MonsterPossibleDamage
                        print(f"You now have *{playerHealth}* HP!")
                        print("\n")
                        if playerHealth > 0:
                                print(Bosses[MonsterFromList]['BossIntroductionMessage'])
                                PrintIntroduction()
                        else:
                                print("The player has run out of health! \n"
                                "\n"
                                f"You defeated *{DefeatedMonsters}* monsters!\n"
                                "\n"
                                "================        G A M E L O S T        ================"
                                )
                                print(Bosses[MonsterFromList]['BossIntroductionMessage'])
                                PrintFinalResults()
                                break
                else:
                        print(Bosses[MonsterFromList]['BossIntroductionMessage'])
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
            AntiPoisonBug = True
    if playerHealth <= 0:
            print("The player has run out of health! \n"
            "\n"
            f"You defeated *{DefeatedMonsters}* monsters!\n"
            "\n"
            "================        G A M E L O S T        ================"
            )
            PrintFinalResults()
