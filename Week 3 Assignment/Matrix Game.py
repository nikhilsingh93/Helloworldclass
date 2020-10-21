# an object describing our player
matrixplayer = { 
    "name": "player1", 
    "score": 0,
    "skill" : ["Close Combat", "Gun Kata"],
    "friends" : [],
    "location" : "start"
}

import random # random numbers
import sys # system stuff for exiting

def rollDice(minNum, maxNum, difficulty):
    # any time a chance of something might happen, let's roll a die
    result = random.randint(minNum,maxNum)
    print "You roll a: " + str(result) + " out of " + str(maxNum)

    if result <= difficulty:
        print "trying again...."
        
        raw_input("press enter >")
        rollDice(minNum, maxNum, difficulty)

    return result

plot = {
    "plot1" : "Main Arena",
    "plot2" : "Meeting Oracle",
    "plot3" : "Final Encounter"
}

def printGraphic(name):
    if (name == "Elevator"):
        print '   ____________________________________________            '
        print '  |____________________________________________| '
        print '  |__||  ||___||  |_|___|___|__|  ||___||  ||__|  '
        print '  ||__|  |__|__|  |___|___|___||  |__|__|  |__||   '
        print '  |__||  ||___||  |_|___|___|__|  ||___||  ||__|   '
        print '  ||__|  |__|__|  |    || |    |  |__|__|  |__||   '
        print '  |__||  ||___||  |    || |    |  ||___||  ||__|    '
        print '  ||__|  |__|__|  |    || |    |  |__|__|  |__||     '
        print '  |__||  ||___||  |    || |    |  ||___||  ||__|      '
        print '  ||__|  |__|__|  |    || |    |  |__|__|  |__||                    '
        print '  |__||  ||___||  |   O|| |O   |  ||___||  ||__|          '
        print '  ||__|  |__|__|  |    || |    |  |__|__|  |__||  '
        print '  |__||  ||___||  |    || |    |  ||___||  ||__|  '
        print '  ||__|  |__|__|__|____||_|____|  |__|__|  |__||   '
        print '       Elevator        '

    if (name == "Secret Code"):
        print  '              ________________________________________________       '
        print  '     ________|    _     _    .      .   __  .     __   ___   |_______'
        print  '     \       |   /     / \   |\    /|  |__  |    |  |   |    |      /    '
        print  '      \      |   \_.  | - |  |  \/  |  |__  |__  |__|   |    |     /    '
        print  '      /      |_______________________________________________|     \     '
        print  '     /__________)                                        (__________\          '
        print  '     Secret Code    '

    if (name == "Cypher"):
        print  '                  ***     '
        print  '                *******      '
        print  '            /\* ### ### */\   '
        print  '            |    @ / @    |  '
        print  '            \/\    ^    /\/   '
        print  '               \  ===  /   '
        print  '                \_____/   '
        print  '                 _|_|_     '
        print  '              *$$$$$$$$$*         '
        print  '        I am Cypher '    

    if (name == "Morpheus"):
        print  '                  .......     '
        print  '              .:::::::::::::.      '
        print  '             .::-- ----- --::.   '
        print  '             :::           :::  '
        print  '             :::           :::   '
        print  '             ::'           '::   '
        print  '            : : /~~~' '~~~\ : :   '
        print  '            :(:   |   :):     '
        print  '             .:     / \     :.         '
        print  '              :    (. .)    :!        '
        print  '               .  .:::::.  .        '
        print  '               :  <----->  :         '
        print  '                .  ~:::~  .        '
        print  '                  \_____ /      '
        print  '        I am Morpheus '

    if (name == "Gun"):
        print  '      +--^----------,--------,-----,--------^-,    '
        print  '     | |||||||||   `---------     |          O.    '
        print  '      `+---------------------------^----------|     '
        print  '       `\_,---------,---------,--------------'
        print  '          / XXXXXX / |       /  '
        print  '         / XXXXXX /  `\    /     '
        print  '        / XXXXXX /`-------     '
        print  '       / XXXXXX /               '
        print  '      / XXXXXX /                '
        print  '     (________(                 '
        print  '      `------/                  '
        print  '        Booooooooooooooooooooom '

    if (name == "title"):
        print '--------------------------------------------------------------------------------------'
        print ' ___        __          _         _________.    _________         ___     __      __   '
        print ' \  \      / /          /\       |/  | |  \|    | _____  |        | |     \ \    / /   ' 
        print ' |\  \    // |         /. \          | |        | |____| |        | |      \ \  / /    '
        print ' ||\  \  //| |.       // \ \         | |        | ______ \        | |       \ \/ /     '
        print ' || \  \// | |.      //___\ \        | |        | |     \ \       | |       /    \     '
        print ' ||  \  /  | |.     //     \ \       | |        | |      \ \      | |      /  /\  \    ' 
        print '/_\   \/   /_\     /_\     /__\      /_\        |_|       \_\     |_|     /__/  \__\   '
        print '                                                                                       '
        print '--------------------------------------------------------------------------------------'

def choosenOne():

    printGraphic("Morpheus")

    print "-------------------------------"
    print "Like the Oracle had predicted! You're the Chosen one"
    print "name: " + matrixplayer["name"]
    print "score: " + str(matrixplayer["score"])
    return

def finalEncounter():
    print "You run straight to a building as the agents are still chasing you."
    print "You notice an elevator there. There's also a side door."
    printGraphic("Elevator")
    raw_input("press enter >")

    print "You consider your options."
    print "options: [ call for elevator, side door, go back]"

    pcmd = raw_input(">")

    if (pcmd == "call for elevator"): 
        print "Which floor should you choose?"
        print "Let's roll a dice here. You press the floor corresponding to the dice number."

        difficulty = 10
        roll = rollDice(0, 20, difficulty)
        
        if (roll >= difficulty):

            print "You enter the corresponding floor. Right across, you meet Morpheus who tells you to remember a secret code!"
            print "Do you agree?"
            
            printGraphic("Secret Code")

            pcmd = raw_input("yes or no >")

            if (pcmd == "no"):
                print "You leave it there."
                finalEncounter()

            elif (pcmd == "yes"):
                print "You remember it and return to the main arena"
                matrixplayer["skills"].append("Secret Code")
                matrixplayer["score"] += 100
                meetingOracle()

            else:
                print "You leave it there."
                mainArena()

        else:
            print "Turns out it's nothing... oh well."
            mainArena()

    elif (pcmd == "side door"):
        print "You went inside the door to realize that the other side is locked."
        print "You decide to rush back to the elevator as that's the only option left"
        finalEncounter()

    elif (pcmd == "go back"):
        print "You decide to go back."
        pcmd = raw_input(">")
        mainArena()

    else:
        print "You can't do that!"
        finalEncounter()

def meetingOracle():
    print "It seems like you've dodged them for now."
    print "But there's still an uncertainity in the air."
    raw_input("press enter >")

    printGraphic("Cypher")
    print "You walk towards the alley. You can hazily see a man standing, awaiting for you"
    print "Welcome " + matrixplayer["name"] + ".'We have been waiting for you!', says the man in the alley."
    print "...Come with me. This way please."
    raw_input("press enter >")
    
    print "You consider your options."

    if ("Secret Code" in matrixplayer["skills"]):
        print "options: [ look around , talk to Cypher, Tell Secret Code ]"
    else:
        print "options: [ go back, talk to Cypher ]"

    pcmd = raw_input(">")

    # option 1: look at Cypher
    if (pcmd == "go back"):
        print "You go back..."
        mainArena() # try again
    
    # option 2: talk to Cypher
    elif (pcmd == "talk to Cypher"):
        print "Who is there inside?"
        print "'You'll find it out if you get the right number after rolling that dice', Cypher said."
        raw_input("press enter to roll >")

        difficulty = 5
        chanceRoll = rollDice(0,20,difficulty) # roll a dice between 0 and 20

        # if the roll is higher than 5... 75% chance
        if (chanceRoll >= difficulty):
            print "'It seems you are in luck! Let's go inside. She is waiting for you', Cypher said."
            matrixplayer["score"] += 50
        else:
            print "'I don't think you're ready to meet her. Come back later', Cypher said."
            mainArena() # try again
        
        # nested actions and ifs
        pcmd = raw_input("be friends with the Cypher? yes or no >")

        # yes
        if (pcmd == "yes"):

            print "Cypher becomes your friend!"

            matrixplayer["friends"].append("Cypher")
            matrixplayer["score"] = int(matrixplayer["score"]) + 100 # conversion
            print "Your score increased to: " + str(matrixplayer["score"])
            
            choosenOne()

        # no
        elif (pcmd == "no"):
            print "'You can leave now', Cypher said."
            mainArena()
        
        # try again
        else:
            meetingOracle()

    elif (pcmd == "Tell Secret Code"):
        print "You tell the Secret Code to Cypher!"
        raw_input("press enter>")
        printGraphic("Secret Code")
        choosenOne()


    # option 3: run
    elif (pcmd == "run"):
        print "You decided to run away!"
        mainArena() # back to start

    # try again
    else:
        print "I don't understand."
        meetingOracle() # path

def mainArena():
    print "You find yourself in the middle of Time Square."
    print "Suddenly, two agents spot you as they noticed an anamoly in your program."
    print "They are sentient computer programs disguised as human government agents, displaying a high-level of artificial intelligence."
    
    if (("Gun Kata" in matrixplayer["skill"]) and not ("Trinity" in matrixplayer["friends"])):
        print "Your options: [ look around, fight, run away, exit]"

    elif ("Gun Kata" in matrixplayer["skill"]):
        print "Your options: [ look around, fight, run away, exit]"

    else:
        print "Your options: [ look around, run away, deceive, exit]"

    pcmd = raw_input(">") # user input

    # player options
    if (pcmd == "look around"):
        print "You look around... and they seem to be coming from all corners now!"

        raw_input("press enter >")
        mainArena()

    # path option
    elif (pcmd == "fight"):
        print "You have decided to fight them"
        raw_input("press enter >")
        printGraphic("Gun")
        choosenOne()

    # path2 option
    elif (pcmd == "run away"):
        print "You start running towards a building entrance"
        raw_input("press enter >")
        finalEncounter() # path 2

    # exiting / catching errors and crazy inputs
    elif (pcmd == "exit"):
        print "you exit."
        return # exit the application

    # path3 option
    elif (pcmd == "deceive"):
        print "You hide yourself in the crowd"
        raw_input("press enter >")
        meetingOracle() # path 3

    else:
        print "I don't understand that"
        mainArena() # the beginning

def welcomeStory():
    # let's introduce them
    print "Hello there! Are you ready for the experience?"
    matrixplayer["name"] = raw_input("Please enter your name >")

    # intro story
    print "Welcome to the Matrix " + matrixplayer["name"] + "!"
    print "Human beings are connected to a program called The Matrix"
    print "Due to this program, the reality perceived by human beings is not the actual reality."
    print "It is a dream world which is almost similar to the real world."
    print "One day, as you keep dwelling in that dream world, you meet Morpheus who offers to show you the reality. Instead, he offers you two pills to make the choice yourself."
    print "Blue Pill - Unpleasant Truth/Reality or Red Pill - Blissful Ignorance."
    print "Which one do you choose?"

    pcmd = raw_input("please choose blue or red >")

    # the player can choose blue or red
    if (pcmd == "blue"):
        print "Great choice! Only those who attempt the absurd can achieve the impossible."
        raw_input("press enter >")
        mainArena()
    else:
        print "Seriously? Don't you really want to accept ignorance? Try again"
        pcmd = raw_input("press enter >")
        welcomeStory() # repeat over and over until the player chooses yes!

# main! most programs start with this.
def main():
    printGraphic("title")
    welcomeStory()

main()