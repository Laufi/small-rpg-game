from random import randint
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
MonsterFromList = randint(0,4) #FOR FUTURE - CALL THIS IN LOOP TOO!
FloorFromList = randint(0,6)
playerHealth = 20
MinDamage = 1
MaxDamage = 4
MinHeal = 2
MaxHeal = 4
InputValid = 1
ShownPossibleDamage = f"{MinDamage}-{MaxDamage}"
ShownPossibleHeal = f"{MinHeal} - {MaxHeal}"
MonsterHealth = MonsterList[MonsterFromList]['MonsterHealth'] #FOR FUTURE - CALL THIS IN LOOP TOO!
MonsterPossibleDamage = randint(MonsterList[MonsterFromList]['MonsterMinDamage'], MonsterList[MonsterFromList]['MonsterMaxDamage'])
DefeatedMonsters = 0
print(f"You are fighting against a *{MonsterList[MonsterFromList]['MonsterType']}* on a *{FloorTypes[FloorFromList]['FloorType']}* floor! \n"
            f"The *{MonsterList[MonsterFromList]['MonsterType']}* has *{MonsterHealth}* HP! \n" 
            f"It can deal *{MonsterList[MonsterFromList]['MonsterMinDamage']}-{MonsterList[MonsterFromList]['MonsterMaxDamage']}* damage! \n"
            f"You can deal *{ShownPossibleDamage}* damage! \n"
            f"You can heal for *{ShownPossibleHeal}* HP! \n"
            f"You have *{playerHealth}* health! \n"
            f"You can FIGHT, HEAL or RUN! \n"
            )
while playerHealth > 0:
    playerAction = input("Enter your action: ")
    PossibleDamage = randint(MinDamage, MaxDamage)
    PossibleHeal = randint(MinHeal, MaxHeal)
    MonsterPossibleDamage = randint(MonsterList[MonsterFromList]['MonsterMinDamage'], MonsterList[MonsterFromList]['MonsterMaxDamage'])
    if playerAction == "FIGHT":
            MonsterHealth = MonsterHealth - (PossibleDamage*FloorTypes[FloorFromList]['DamageDealToMonster'])
            print(f"You attack the *{MonsterList[MonsterFromList]['MonsterType']}* for *{PossibleDamage}* with a floor modifier of *{FloorTypes[FloorFromList]['DamageDealToMonster']}*, resulting in *{PossibleDamage * FloorTypes[FloorFromList]['DamageDealToMonster']}* damage! \n"
            f"It now has *{MonsterHealth}* HP left!")
    elif playerAction == "HEAL":
            playerHealth = playerHealth + PossibleHeal*FloorTypes[FloorFromList]['HealModifier']
            print(f"You heal for *{PossibleHeal}* with a modifier of *{FloorTypes[FloorFromList]['HealModifier']}* for a total of *{PossibleHeal*FloorTypes[FloorFromList]['HealModifier']}*! You now have *{playerHealth}* HP!")
    elif playerAction == "RUN":
            print("You run away! A cowardly choice to be certain, alas, the tower remains a danger to humanity...\n" 
                "================ C O W A R D L Y W A Y O U T ================")
            break
    else:
            print("Invalid input!")
            InputValid = 0
    if InputValid == 1 and MonsterHealth > 0:
            playerHealth = playerHealth - MonsterPossibleDamage
            print(f"*{MonsterList[MonsterFromList]['MonsterType']}* attacks you for *{MonsterPossibleDamage}*!")
            if FloorTypes[FloorFromList]['Poison'] >0:
                    playerHealth = playerHealth - FloorTypes[FloorFromList]['Poison']
                    print(f"The poison on the floor damages you for *{FloorTypes[FloorFromList]['Poison']}* HP!")
            else:
                    pass
            print(f"You now have *{playerHealth}* HP left!")
    elif InputValid == 1 and MonsterHealth <= 0:
            DefeatedMonsters += 1
            print(f"The *{MonsterList[MonsterFromList]['MonsterType']}* has been defeated! You have defeated *{DefeatedMonsters}* monsters so far!\n"
            "\n"
            "================ M O N S T E R D E F E A T E D ================ \n"
            "\n"
            )
            if DefeatedMonsters == 10:
                print("THE PLAYER HAS DEFEATED THE FINAL ENEMY! THE TOWER IS NOW FREE! \n"
                "================    Y O U A R E W I N N E R    ================")
                break
            else:
                MonsterFromList = randint(0,4)
                FloorFromList = randint(0,6)
                MonsterHealth = MonsterList[MonsterFromList]['MonsterHealth']
                MonsterPossibleDamage = randint(MonsterList[MonsterFromList]['MonsterMinDamage'], MonsterList[MonsterFromList]['MonsterMaxDamage'])
                print(f"You are fighting against a *{MonsterList[MonsterFromList]['MonsterType']}* on a *{FloorTypes[FloorFromList]['FloorType']}* floor! \n"
                    f"The *{MonsterList[MonsterFromList]['MonsterType']}* has *{MonsterHealth}* HP! \n" 
                    f"It can deal *{MonsterList[MonsterFromList]['MonsterMinDamage']}-{MonsterList[MonsterFromList]['MonsterMaxDamage']}* damage! \n"
                    f"You can deal *{ShownPossibleDamage}* damage! \n"
                    f"You can heal for *{ShownPossibleHeal}* HP! \n"
                    f"You have *{playerHealth}* health! \n"
                    f"You can FIGHT, HEAL or RUN! \n"
                    )
    elif InputValid == 0:
            InputValid = 1
    if playerHealth <= 0:
            print("The player has run out of health! \n"
            "\n"
            f"You defeated *{DefeatedMonsters}* monsters!\n"
            "\n"
            "================        G A M E L O S T        ================"
            )
