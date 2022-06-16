from random import randint
from gameStateFile import gameState
from playerFile import Player
from opponentFile import Opponent
from styles import printContentBorders, printTitleBorders, printGameStartMessage, scene1, scene2


def initOpponents():
    opponents = [
        Opponent('Aron Szilagyi', 'GOAT', 900, 1000),
        Opponent('Kim Jung Hwan', 'A', 1000, 800),
        Opponent('Olga Kharlan', 'A', 800, 800),
        Opponent('Chloe Fox-Gitomer', 'B', 70, 70),
        Opponent('Esther Lu', 'C', 50, 50),
        Opponent('Isak Swaim', 'D', 30, 30),
        Opponent('Mark Zuckerberg', 'E', 20, 20),
        Opponent('Joe Schmoe', 'U', 10, 10)
    ]
    for opponent in opponents:
        gameState.addOpponent(opponent)


def doTraining():
    while True:
        trainingChoice = input(
            "\nWhich what would you like to work on today?\n1)Bladework\n2)Conditioning\n")
        if trainingChoice == '1':
            gameState.player.skill += randint(0, 10)
            print("\nYou work on bladework drills.\nYour skill attribute is now " +
                  str(gameState.player.skill) + '.\n')
            break
        if trainingChoice == '2':
            gameState.player.speed += randint(0, 10)
            print("\nYou work on conditioning.\nYou masochist ;)\nYour speed attribute is now " +
                  str(gameState.player.speed) + '.\n')
            break
        print('Invalid Input. Try typing 1 or 2.\n')
    print("It's time for your next match.")


def setPlayer():
    name = input('What is your name?\n')
    gameState.setPlayer(Player(name))


def selectOpponent():
    printOpponentChoices()
    index = None
    while True:
        index = input('\nEnter a number to select your opponent: ')
        if index.isdigit():
            index = int(index) - 1
            if index in range(len(gameState.listOfOpponents)):
                break
            print('Invalid input: Try inputing a number from the list.')
        elif index.isdigit() == False:
            print('Invalid input: Try inputing a number from the list.')
    selectedOpponent = gameState.listOfOpponents[index]
    gameState.setOpponent(selectedOpponent)


def printOpponentChoices():
    for index, opponent in enumerate(gameState.listOfOpponents):
        index = index + 1
        print(index, ')', opponent)


def getPlayerChoice():
    return input(
        'Choose an action:\n1)Attack\n2)Parry\n3)Attack in Preparation\n4)Exit the Game\n')


def getOpponentAction():
    opponentAction = randint(1, 3)
    if gameState.player.lastAction == '1':
        opponentAction = randint(1, 2)
    if gameState.player.lastAction == '2':
        opponentAction = randint(2, 3)
    if gameState.player.lastAction == '3':
        opponentAction = 1
    return opponentAction


def checkPoints():
    if gameState.player.points == 5:
        printContentBorders()
        print(gameState.player.name +
              ' has won the bout.\nSalute and shake hands.')
        printTitleBorders()
        gameState.setResult('player won')
    elif gameState.opponent.points == 5:
        printContentBorders()
        print(gameState.opponent.name +
              ' has won the bout.\nSalute and shake hands.')
        printTitleBorders()
        gameState.setResult('opponent won')


def printPoints():
    print('\nScore is:\n' + gameState.player.name + ' - ' + str(gameState.player.points) +
          '\n' + gameState.opponent.name + ' - ' + str(gameState.opponent.points) + '\n')


def handleResult():
    gameState.player.resetAction()
    print(gameState.player.lastAction)
    while True:
        train = input(
            'Your bout is over. Would you like to train before your next one? (Y/N)\n')
        if train.lower() == 'y':
            doTraining()
            break
        if train.lower() == 'n':
            break
        print('Invalid Input: Try typing Y or N')

    while True:
        replay = input('Would you like to fence again? (Y/N)\n')
        if replay.lower() == 'y':
            gameState.playAgain()
            selectOpponent()
            printGameStartMessage()
            printContentBorders()
            break
        elif replay.lower() == 'n':
            gameState.exit()
            break
        print('Invalid Input: Try typing Y or N')


def handleChoice1(opponentAction, chance):
    gameState.player.lastAction = '1'
    if opponentAction == 3:
        print("Halt!\nAttack. Attack in Preparation.")
        gameState.player.addPoint()
    if opponentAction == 2:
        if gameState.player.speed > gameState.opponent.skill:
            print('Halt!\nParry Riposte - No. Attack Touche.')
            gameState.player.addPoint()
        if gameState.player.speed == gameState.opponent.skill:
            if chance <= 50:
                print('Halt!\nParry Riposte - No. Attack Touche.')
                gameState.player.addPoint()
            if chance > 50:
                print('Halt!\nAttack. Parry Riposte Touche.')
                gameState.opponent.addPoint()
        if gameState.player.speed < gameState.opponent.skill:
            print('Halt!\nAttack. Parry Riposte Touche.')
            gameState.opponent.addPoint()
    if opponentAction == 1:
        if gameState.player.speed > gameState.opponent.speed:
            print('Halt!\nAttack. Contre Attack.')
            gameState.player.addPoint()
        if gameState.player.speed == gameState.opponent.speed:
            if chance <= 50:
                print('Halt!\nAttack. Contre Attack.')
                gameState.player.addPoint()
            if chance > 50:
                print('Halt!\nAttack. Contre Attack.')
                gameState.opponent.addPoint()
        if gameState.player.speed < gameState.opponent.speed:
            print('Halt!\nAttack. Contre Attack.')
            gameState.opponent.addPoint()


def handleChoice2(opponentAction, chance):
    gameState.player.lastAction = '2'
    if opponentAction == 1:
        if gameState.player.skill > gameState.opponent.speed:
            print('Halt!\nAttack. Parry Riposte Touche.')
            gameState.player.addPoint()
        if gameState.player.skill == gameState.opponent.speed:
            if chance <= 50:
                print('Halt!\nAttack. Parry Riposte Touche.')
                gameState.player.addPoint()
            if chance > 50:
                print('Halt!\nAttack Touche.')
                gameState.opponent.addPoint()
        if gameState.player.skill < gameState.opponent.speed:
            print('Halt!\nAttack Touche.')
            gameState.opponent.addPoint()
    if opponentAction == 2:
        print(
            "Both fencers hesitate off the line.\nWhat's your next move?\n")
    if opponentAction == 3:
        print('Halt!\nAttack Touche.')
        gameState.opponent.addPoint()


def handleChoice3(opponentAction, chance):
    gameState.player.lastAction = '3'
    if opponentAction == 1:
        print('Halt!\nAttack. Attack in Preparation.')
        gameState.opponent.addPoint()
    if opponentAction == 2:
        print('Halt!\nAttack Touche')
        gameState.player.addPoint()
    if opponentAction == 3:
        if gameState.player.speed > gameState.opponent.speed:
            print('Halt!\nAttack. Counter Attack.')
            gameState.player.addPoint()
        if gameState.player.speed == gameState.opponent.speed:
            if chance <= 50:
                print('Halt!\nAttack. Counter Attack.')
                gameState.player.addPoint()
            if chance > 50:
                print('Halt!\nAttack. Counter Attack.')
                gameState.opponent.addPoint()
        if gameState.player.speed < gameState.opponent.speed:
            print('Halt!\nAttack. Counter Attack.')
            gameState.opponent.addPoint()


def runGame():
    scene1()
    setPlayer()
    scene2()
    selectOpponent()
    printGameStartMessage(gameState.player.name, gameState.opponent.name)
    while not gameState.status == 'exit':
        playerChoice = getPlayerChoice()
        opponentAction = getOpponentAction()
        chance = randint(0, 100)

        if playerChoice == '1':
            handleChoice1(opponentAction, chance)
            printPoints()
            checkPoints()
        elif playerChoice == '2':
            handleChoice2(opponentAction, chance)
            printPoints()
            checkPoints()
        elif playerChoice == '3':
            handleChoice3(opponentAction, chance)
            printPoints()
            checkPoints()
        elif playerChoice == '4':
            gameState.setStatus('exit')
            break
        else:
            print("Invalid Input: Try typing in a number.\n")

        if gameState.result:
            handleResult()


initOpponents()
runGame()
