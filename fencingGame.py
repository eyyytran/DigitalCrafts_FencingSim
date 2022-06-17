from random import randint
import time
from gameStateFile import gameState
from playerFile import Player
from opponentFile import Opponent
from textstyling import *


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


def getOpponentAction():
    opponentAction = randint(1, 3)
    rng = randint(0, 100)
    if gameState.player.lastAction == '1':
        if gameState.player.lastPoint == True:
            if rng <= 70:
                opponentAction = 2
            if rng > 30:
                opponentAction = 1
        if gameState.player.lastPoint == False:
            if rng <= 70:
                opponentAction = 1
            if rng > 30:
                opponentAction = 2
    if gameState.player.lastAction == '2':
        if gameState.player.lastPoint == True:
            if rng <= 70:
                opponentAction = 3
            if rng > 30:
                opponentAction = 2
        if gameState.player.lastPoint == False:
            if rng <= 70:
                opponentAction = 3
            if rng > 30:
                opponentAction = 1
    if gameState.player.lastAction == '3':
        if gameState.player.lastPoint == True:
            if rng <= 70:
                opponentAction = 1
            if rng > 30:
                opponentAction = 3
        if gameState.player.lastPoint == False:
            if rng <= 70:
                opponentAction = 1
            if rng > 30:
                opponentAction = 3
    gameState.player.resetLastPoint()
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
    time.sleep(1)
    printContentBorders()
    print('\nScore is:\n' + gameState.player.name + ' - ' + str(gameState.player.points) +
          '\n' + gameState.opponent.name + ' - ' + str(gameState.opponent.points) + '\n')
    printContentBorders()
    time.sleep(1)


def handleResult():
    gainedExperience = randint(0, 10)
    gameState.player.experience += gainedExperience
    print("\nYou gained ", gainedExperience,
          " experience points!\n Your experience level is now ", gameState.player.experience, '.')
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
            printGameStartMessage(gameState.player.name,
                                  gameState.opponent.name)
            printContentBorders()
            break
        elif replay.lower() == 'n':
            gameState.exit()
            break
        print('Invalid Input: Try typing Y or N')


def handleChoice1(opponentAction, chance, experienceBoost):
    gameState.player.lastAction = '1'
    if opponentAction == 3:
        if chance >= experienceBoost:
            attackCounterattack1()
            gameState.player.addPoint()
        if chance < experienceBoost:
            failedAttack()
            gameState.opponent.addPoint()
    if opponentAction == 2:
        if gameState.player.speed > gameState.opponent.skill:
            if chance >= experienceBoost:
                parryRiposteNo1()
                gameState.player.addPoint()
            if chance < experienceBoost:
                parryRiposte2()
                gameState.opponent.addPoint()
        if gameState.player.speed == gameState.opponent.skill:
            if chance <= 50:
                parryRiposteNo1()
                gameState.player.addPoint()
            if chance > 50:
                parryRiposte2()
                gameState.opponent.addPoint()
        if gameState.player.speed < gameState.opponent.skill:
            parryRiposte2()
            gameState.opponent.addPoint()
    if opponentAction == 1:
        if gameState.player.speed > gameState.opponent.speed:
            if chance >= experienceBoost:
                attackCounterattack1()
                gameState.player.addPoint()
            if chance < experienceBoost:
                failedAttack()
                gameState.opponent.addPoint()
        if gameState.player.speed == gameState.opponent.speed:
            if chance <= 50:
                attackCounterattack1()
                gameState.player.addPoint()
            if chance > 50:
                attackCounterattack2()
                gameState.opponent.addPoint()
        if gameState.player.speed < gameState.opponent.speed:
            attackCounterattack2()
            gameState.opponent.addPoint()


def handleChoice2(opponentAction, chance, experienceBoost):
    gameState.player.lastAction = '2'
    if opponentAction == 1:
        if gameState.player.skill > gameState.opponent.speed:
            if chance >= experienceBoost:
                parryRiposte1()
                gameState.player.addPoint()
            if chance < experienceBoost:
                failedParry()
                gameState.opponent.addPoint()
        if gameState.player.skill == gameState.opponent.speed:
            if chance <= 50:
                parryRiposte1()
                gameState.player.addPoint()
            if chance > 50:
                parryRiposteNo2()
                gameState.opponent.addPoint()
        if gameState.player.skill < gameState.opponent.speed:
            parryRiposteNo2()
            gameState.opponent.addPoint()
    if opponentAction == 2:
        doubleHold()
    if opponentAction == 3:
        feint2()
        gameState.opponent.addPoint()


def handleChoice3(opponentAction, chance, experienceBoost):
    gameState.player.lastAction = '3'
    if opponentAction == 1:
        longAttack2()
        gameState.opponent.addPoint()
    if opponentAction == 2:
        if chance >= experienceBoost:
            feint1()
            gameState.player.addPoint()
        if chance < experienceBoost:
            failedFeint()
            gameState.opponent.addPoint()
    if opponentAction == 3:
        if gameState.player.speed > gameState.opponent.speed:
            if chance >= experienceBoost:
                attackCounterattack1()
                gameState.player.addPoint()
            if chance < experienceBoost:
                failedAttack()
                gameState.opponent.addPoint()
        if gameState.player.speed == gameState.opponent.speed:
            if chance <= 50:
                attackCounterattack1()
                gameState.player.addPoint()
            if chance > 50:
                attackCounterattack2()
                gameState.opponent.addPoint()
        if gameState.player.speed < gameState.opponent.speed:
            attackCounterattack2()
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
        experienceBoost = 100-gameState.player.experience
        if playerChoice == '1':
            handleChoice1(opponentAction, chance, experienceBoost)
            printPoints()
            checkPoints()
        elif playerChoice == '2':
            handleChoice2(opponentAction, chance, experienceBoost)
            printPoints()
            checkPoints()
        elif playerChoice == '3':
            handleChoice3(opponentAction, chance, experienceBoost)
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
