from random import randint

MonsterList = [{'MonsterType': 'Skeleton',
               'MonsterHealth': 10,
               'MonsterMinDamage': 1,
               'MonsterMaxDamage': 3}, 
               {'MonsterType': 'Bat',
               'MonsterHealth': 5,
               'MonsterMinDamage': 3,
               'MonsterMaxDamage': 5},
               {'MonsterType' : 'Alligator',
               'MonsterHealth': 15,
               'MonsterMinDamage': 5,
               'MonsterMaxDamage': 7},
               {'MonsterType' : 'Ninja',
               'MonsterHealth': 8,
               'MonsterMinDamage': 8,
               'MonsterMaxDamage': 10}]
MonsterFromList = randint(0,3) #FOR FUTURE - CALL THIS IN LOOP TOO!
playerHealth = 20
MinDamage = 1
MaxDamage = 4
MinHeal = 1
MaxHeal = 2
InputValid = 1
ShownPossibleDamage = f"{MinDamage}-{MaxDamage}"
ShownPossibleHeal = f"{MinHeal} - {MaxHeal}"
MonsterHealth = MonsterList[MonsterFromList]['MonsterHealth'] #FOR FUTURE - CALL THIS IN LOOP TOO!
MonsterPossibleDamage = randint(MonsterList[MonsterFromList]['MonsterMinDamage'], MonsterList[MonsterFromList]['MonsterMaxDamage'])
while playerHealth > 0:
    print(f"You are fighting against a {MonsterList[MonsterFromList]['MonsterType']} \n"
            f"The {MonsterList[MonsterFromList]['MonsterType']} has {MonsterHealth} HP! \n" 
            f"It can deal {MonsterList[MonsterFromList]['MonsterMinDamage']}-{MonsterList[MonsterFromList]['MonsterMaxDamage']} damage! \n"
            f"You can deal {ShownPossibleDamage} damage! \n"
            f"You can heal for {ShownPossibleHeal} HP! \n"
            f"You have {playerHealth} health! \n"
            f"You can FIGHT, HEAL or RUN! \n"
            )
            # BTW THIS SHOULD NOT BE IN THE LOOP, HAVE THIS GO OUTSIDE THE WHILE FIGHTINGMONSTER LOOP!!!!
    playerAction = input("Enter your action: ")
    PossibleDamage = randint(MinDamage, MaxDamage)
    PossibleHeal = randint(MinHeal, MaxHeal)
    if playerAction == "FIGHT":
            MonsterHealth = MonsterHealth - PossibleDamage
            print(f"You attack the {MonsterList[MonsterFromList]['MonsterType']} for {PossibleDamage}! \n"
            "It now has {MonsterHealth} HP left!")
    elif playerAction == "HEAL":
            playerHealth = playerHealth + PossibleHeal
            print(f"You heal for {PossibleHeal}! You now have {playerHealth} HP!")
    elif playerAction == "RUN":
            print("You run away!")
            break
    else:
            print("Invalid input!")
            InputValid = 0
    if InputValid == 1:
            playerHealth = playerHealth - MonsterPossibleDamage
            print(f"{MonsterList[MonsterFromList]['MonsterType']} attacks you for {MonsterPossibleDamage}! \n"
            f"You now have {playerHealth} HP left!")
    else:
            InputValid = 1
