import random
import time
import json


class Team:
    def __init__(self, key, name, score, goaldif, goals, won, drawn, lost, attack, defense, luck, speed, stamina): 
        self.key = key
        self.name = name
        self.score = score
        self.goaldif = goaldif
        self.goals = goals
        self.won = won
        self.drawn = drawn
        self.lost = lost
        self.attack = attack
        self.defense = defense
        self.luck = luck
        self.speed = speed
        self.stamina = stamina
        self.red = False


team1 = Team('Team1', 1, 0, 0, 0, 0, 0, 0, 60, 60, 60, 60, 60)
team2 = Team('Team2', 1, 0, 0, 0, 0, 0, 0, 50, 50, 50, 50, 50)

match = [team1, team2]


def goal(team):
    print("Goal! " + str(team.name) + " scores! ")
    team.goals += 1

def yellow(team):
    print("Yellow Card for " + str(team.name) )

#when a red card is given, take away 50 points from each stat
rednum = 50
def red(team):
    if team.red == False:
        print("Red Card for " + str(team.name) )
        team.red = True
        team.attack -= rednum
        team.defense -= rednum
        team.luck -= rednum
        team.speed -= rednum
        team.stamina -= rednum
    else:
        pass

def quickgoal(team):
    team.goals += 1

#when a red card is given, take away 50 points from each stat
def quickred(team):
    if team.red == False:
        team.red = True
        team.attack -= rednum
        team.defense -= rednum
        team.luck -= rednum
        team.speed -= rednum
        team.stamina -= rednum
    else:
        pass

def quickprint(team):
    print(team.name + " " + str(team.attack))

def matchsim(match, json):
    #plays a game for 90 mins
    for i in range(0, 91):
        if i < 46:
            secondhalf = False
        elif i == 46:
            print('Half Time!')
            secondhalf = True
        else:
            secondhalf = True
        #picks a random number 1-300 for each game minute to determine what event happens
        n1 = random.randint(1, 300)
        #picks a random team for event to happen to
        n2 = random.randint(0,1)
        
        event = ""
        #nothing happening
        if n1 < 284:
            event = " "
        #VAR
        elif n1 < 286:
            print("VAR Decision: Checking Possible Foul!")
            time.sleep(5)
            #compares the random VAR number for each team plus their luck stat to determine who gets the penalty
            nVar = random.randint(0,10)
            nVar_1 = random.randint(1,100)
            nVar_2 = random.randint(1,100)
            if (match[0].luck + nVar_1) > (match[1].luck + nVar_2):
                varteam = match[0]
            else:
                varteam = match[1]
            #70% chance for a penalty to be given
            if nVar > 3:
                print("Penalty given for " + str(varteam.name) + "!")
                #75% chance to get a goal from penalty
                nVar_3 = random.randint(0,4)
                if nVar_3 > 1:
                    goal(varteam)
                else:
                    print("Penalty Missed! ")
            else:
                print("No Penalty Given! ")

        #goal
        elif n1 < 295:
            #generate new random number here for each team (plus stats) to compare
            n3_1 = random.randint(1,100)
            n3_2 = random.randint(1,100)
            if secondhalf == True:
                if ((match[0].attack - match[1].defense) + match[0].stamina + n3_1) > ((match[1].attack - match[0].defense) + match[1].stamina + n3_2):
                    goal(match[0])
                else:
                    goal(match[1])
            else:
                if ((match[0].attack - match[1].defense) + match[0].speed + n3_1) > ((match[1].attack - match[0].defense) + match[1].speed + n3_2):
                    goal(match[0])
                else:
                    goal(match[1])
        #yellow card
        elif n1 < 299:
            yellow(match[n2])
        #red card 
        else:
            red(match[n2])
        time.sleep(0.15)
        print(str(i) + """' """ + event)
    #adds goals for each of the teams at the end
    for team in match:
        for i in json:
            if i == team.name:
                json[i]["goals"] += team.goals 
    
    #declaring winner, loser or a draw
    winner = ""
    loser = ""
    draw = False
    if match[0].goals > match[1].goals:
        winner = match[0].name
        loser = match[1].name
    elif match[0].goals < match[1].goals:
        winner = match[1].name
        loser = match[0].name
    else:
        draw = True

    if draw == True:
        for i in json:
            for team in match:
                if i == team.name:
                    json[i]["drawn"] += 1
                    json[i]["score"] += 1
    else:
        for i in json:
            if i == winner:
                json[i]["score"] += 3
                json[i]["won"] += 1
            if i == loser:
                json[i]["lost"] += 1

    #prints final score         
    print(str(match[0].name) + ' ' + str(match[0].goals) + '-' + str(match[1].goals) + ' ' + str(match[1].name))

    return json
    

def quickmatchsim(match, json):
    #plays a game for 90 mins
    for i in range(0, 91):
        if i < 46:
            secondhalf = False
        elif i == 46:
            secondhalf = True
        else:
            secondhalf = True
        #picks a random number 1-300 for each game minute to determine what event happens
        n1 = random.randint(1, 300)
        #picks a random team for event to happen to
        n2 = random.randint(0,1)
        
        
        #nothing happening
        if n1 < 283:
            if match[0].red == True or match[1].red == True:
                pass
            else:
                pass
        #VAR
        elif n1 < 284:
            #compares the random VAR number for each team plus their luck stat to determine who gets the penalty
            nVar = random.randint(0,10)
            nVar_1 = random.randint(1,100)
            nVar_2 = random.randint(1,100)
            if (match[0].luck + nVar_1) > (match[1].luck + nVar_2):
                varteam = match[0]
            else:
                varteam = match[1]
            #70% chance for a penalty to be given
            if nVar > 3:
                #75% chance for a penalty to be scored
                nVar_3 = random.randint(0,4)
                if nVar_3 > 1:
                    quickgoal(varteam)
                else:
                    pass
            else:
                pass

        #goal
        elif n1 < 295:
            #generate new random number here for each team (plus stats) to compare
            n3_1 = random.randint(1,100)
            n3_2 = random.randint(1,100)
            if secondhalf == True:
                if ((match[0].attack - match[1].defense) + match[0].stamina + n3_1) > ((match[1].attack - match[0].defense) + match[1].stamina + n3_2):
                    quickgoal(match[0])
                else:
                    quickgoal(match[1])
            else:
                if ((match[0].attack - match[1].defense) + match[0].speed + n3_1) > ((match[1].attack - match[0].defense) + match[1].speed + n3_2):
                    quickgoal(match[0])
                else:
                    quickgoal(match[1])
        #yellow card
        elif n1 < 299:
            pass
        #red card 
        else:
            quickred(match[n2])
    for team in match:
        for i in json:
            if i == team.name:
                json[i]["goals"] += team.goals 
    winner = ""
    loser = ""
    draw = False
    if match[0].goals > match[1].goals:
        winner = match[0].name
        loser = match[1].name
    elif match[0].goals < match[1].goals:
        winner = match[1].name
        loser = match[0].name
    else:
        draw = True
    #prints final score 
    print(str(match[0].name) + ' ' + str(match[0].goals) + '-' + str(match[1].goals) + ' ' + str(match[1].name))

    if draw == True:

        for i in json:
            for team in match:
                if i == team.name:
                    json[i]["drawn"] += 1
                    json[i]["score"] += 1
    else:
        for i in json:
            if i == winner:
                json[i]["score"] += 3
                json[i]["won"] += 1
            if i == loser:
                json[i]["lost"] += 1

    return json
