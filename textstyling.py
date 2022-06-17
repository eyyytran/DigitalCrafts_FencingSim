from re import X
import time


def printTitleBorders():
    print('===' * 20)


def printContentBorders():
    print('---' * 20)


def getPlayerChoice():
    return input(
        'Choose an action:\n1)Attack\n2)Parry\n3)Attack in Preparation\n4)Exit the Game\n')


def printGameStartMessage(player, opponent):
    print('\nWill ' + player + ' and ' +
          opponent + ' step onto the piste?\n')
    printContentBorders()
    print("\nSalute your opponent\n")
    time.sleep(1)
    print("Engarde")
    time.sleep(1)
    print("Prete")
    time.sleep(2)
    print("Allez!\n")
    printContentBorders()


def scene1():
    printTitleBorders()
    print("Welcome to Digital Crafts Fencing Club!\nYou've arrived just in time for open fencing.\nI heard that you're a complete beginner.\nThere's no better way to learn than to actually fence.\nLet's get you started!\n\n")


def scene2():
    printContentBorders()
    print("\nIf you'll take a look around, you can see that we've got quite a crowd today.\nOur benefactors have spared no expense to attract only the very best talent.\nDon't be shy!\nWhy don't you ask someone to fence?\n")
    printContentBorders()
    time.sleep(1)
    print("\n")


def attackCounterattack1():
    print("\n*You can see your opponent holding.*")
    print("*You both step off the line.*")
    print("*Now's your chance!*")
    time.sleep(1)
    print("Halt!\nAttack. Attack in Preparation.\n")


def attackCounterattack2():
    print("\n*You hesitate for a split second.*")
    print("*You both cut towards an open area*")
    time.sleep(1)
    print("Halt!\nAttack. Contre Attack.\n")


def parryRiposteNo1():
    print("\n*Your opponent put up a parry, but they're not in time.*\n")
    time.sleep(1)
    print("Halt!\nParry Riposte - No. Attack Touche.\n")


def parryRiposteNo2():
    print("\n*You can see where your opponent will attack.*")
    print("*But you can't parry in time!*")
    print("Halt!\nAttack Touche.\n")


def parryRiposte1():
    print("\n*You can see where your opponent will attack*")
    time.sleep(1)
    print("*You set up a parry at the last second.*")
    print("Halt!\nAttack. Parry Riposte Touche.\n")


def parryRiposte2():
    print("\n*You cut towards an open area.*")
    print("*The opponent puts up a parry just in time!*")
    time.sleep(1)
    print('Halt!\nAttack. Parry Riposte Touche.\n')


def feint1():
    print("\n*You come off the line.*")
    print("*Your opponent is prematurely defending.*")
    time.sleep(1)
    print("*You launch a feint attack.*")
    print('Halt!\nAttack Touche\n')


def feint2():
    print("\n*Your opponent is coming!")
    print("*Is that an attack?*")
    print("*You move your blade to block.*")
    time.sleep(1)
    print("*It was a fake out.*")
    print('Halt!\nAttack Touche.\n')


def longAttack2():
    print("\n*You come off the line for a long attack.*")
    print("*But your opponent is ready!*")
    print('Halt!\nAttack. Attack in Preparation.\n')


def doubleHold():
    print("\n*Both fencers hold. Both attack*\n")
    print("Halt! Simultaneous.\n")


def failedAttack():
    print("\n*You come off the line to attack.*")
    time.sleep(1)
    print("*And it fails!*\n")


def failedFeint():
    print("\n*You set up a long attack and feint.*")
    time.sleep(1)
    print("\nBut your opponent manages to parry you anyway!*\n")


def failedParry():
    print("\n*You see the attack coming*")
    time.sleep(1)
    print("*You set up your parry.*")
    time.sleep(1)
    print("*And it fails!*")
