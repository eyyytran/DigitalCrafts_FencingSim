import time


def printTitleBorders():
    print('===' * 20)


def printContentBorders():
    print('---' * 20)


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
