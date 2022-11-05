Player = "O"
Agent = "X"

DEFAULT_ALG="minmax"
comparisions = 0

playarea = {1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}

def printplayarea(playarea):
    print(playarea[1] + ' | ' + playarea[2] + ' | ' + playarea[3])
    print("--+---+--")
    print(playarea[4] + ' | ' + playarea[5] + ' | ' + playarea[6])
    print("--+---+--")
    print(playarea[7] + ' | ' + playarea[8] + ' | ' + playarea[9])
    print("\n")
#printplayarea()

def boxisfree(position):
    if (playarea[position] == ' '):
        return True
    else:
        return False

def checkDraw():
    for keys in playarea.keys():
        if (playarea[keys] == ' '):
            return False
    
    return True

def checkWin():
    if(playarea[1] == playarea[2] and playarea[1] == playarea[3] and playarea[1] != ' '):
        return True
    elif(playarea[4] == playarea[5] and playarea[4] == playarea[6] and playarea[4] != ' '):
        return True
    elif(playarea[7] == playarea[8] and playarea[7] == playarea[9] and playarea[7] != ' '):
        return True
    elif(playarea[1] == playarea[4] and playarea[1] == playarea[7] and playarea[1] != ' '):
        return True
    elif(playarea[2] == playarea[5] and playarea[2] == playarea[8] and playarea[2] != ' '):
        return True
    elif(playarea[3] == playarea[6] and playarea[3] == playarea[9] and playarea[3] != ' '):
        return True
    elif(playarea[1] == playarea[5] and playarea[1] == playarea[9] and playarea[1] != ' '):
        return True
    elif(playarea[7] == playarea[5] and playarea[7] == playarea[3] and playarea[7] != ' '):
        return True
    else:
        return False

def checkScore(mark):
    if playarea[1] == playarea[2] and playarea[1] == playarea[3] and playarea[1] == mark:
        return True
    elif (playarea[4] == playarea[5] and playarea[4] == playarea[6] and playarea[4] == mark):
        return True
    elif (playarea[7] == playarea[8] and playarea[7] == playarea[9] and playarea[7] == mark):
        return True
    elif (playarea[1] == playarea[4] and playarea[1] == playarea[7] and playarea[1] == mark):
        return True
    elif (playarea[2] == playarea[5] and playarea[2] == playarea[8] and playarea[2] == mark):
        return True
    elif (playarea[3] == playarea[6] and playarea[3] == playarea[9] and playarea[3] == mark):
        return True
    elif (playarea[1] == playarea[5] and playarea[1] == playarea[9] and playarea[1] == mark):
        return True
    elif (playarea[7] == playarea[5] and playarea[7] == playarea[3] and playarea[7] == mark):
        return True
    else:
        return False

import sys
def insertLetter(letter, position):
    global comparisions
    if boxisfree(position):
        playarea[position] = letter
        #printplayarea(playarea)
        if (checkDraw()):
            print("Draw!")
            print("The number of comparisions: {}".format(comparisions))
            exit()
        if checkWin():
            if (letter == "X"):
                print("Agent wins!")
                print("The number of comparisions: {}".format(comparisions))
                exit()
            else:
                print("Player wins!")
                print("The number of comparisions: {}".format(comparisions))
                exit()

        return

    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return

def PlayerTurn():
    global comparisions
    position = int(input("Enter a position to insert 'O'"))
    insertLetter(Player,position)

def AgentTurn(alg):
    global comparisions
    bestscore = -1000
    bestmove = 0

    for key in playarea.keys():
        if(playarea[key]==' '):
            playarea[key]=Agent
            match alg:
                case "minmax":
                    score= minmax(playarea,False)
                case "alphabetaPruning":
                    score= minmax_AlphaBetaPruning(playarea,False,float("-inf") ,float("inf"))
            playarea[key]=' '
            if(score>bestscore):
                #comparisions = comparisions + 1
                bestscore = score
                bestmove = key

    insertLetter(Agent,bestmove)
    return 




def minmax(playarea, isMaximizing):
    global comparisions
    if (checkScore(Agent)):
        return 1
    elif (checkScore(Player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in playarea.keys():
            if (playarea[key] == ' '):
                playarea[key] = Agent
                score= minmax(playarea, False)
                playarea[key] = ' '
                if (score > bestScore):
                    #comparisions += 1
                    bestScore = score
        comparisions += 1
        return bestScore

    else:
        bestScore = 800
        for key in playarea.keys():
            if (playarea[key] == ' '):
                playarea[key] = Player
                score= minmax(playarea, True)
                playarea[key] = ' '
                if (score < bestScore):
                    bestScore = score
        comparisions += 1
        return bestScore



def minmax_AlphaBetaPruning(playarea, isMaximizing, alpha, beta):
    global comparisions
    if (checkScore(Agent)):
        return 1
    elif (checkScore(Player)):
        return -1
    elif (checkDraw()):
        return 0    

    
    if (isMaximizing):
        bestScore = -800
        for key in playarea.keys():
            if (playarea[key] == ' '):
                playarea[key] = Agent
                score= minmax_AlphaBetaPruning(playarea, False,float("-inf") ,float("inf"))
                playarea[key] = ' '
                if (score > bestScore):
                    #comparisions += 1
                    bestScore = score
                beta=max(beta,bestScore)
                if (beta <= alpha):
                    break
        comparisions += 1
        return bestScore

    else:
        bestScore = 800
        for key in playarea.keys():
            if (playarea[key] == ' '):
                playarea[key] = Player
                score= minmax_AlphaBetaPruning(playarea, True,float("-inf") ,float("inf"))
                playarea[key] = ' '
                if (score < bestScore):
                    #comparisions += 1
                    bestScore = score
                beta=min(beta,bestScore)
                if (beta <= alpha):
                    #comparisions += 1
                    break
        comparisions += 1
        return bestScore

def main():
    global comparisions
    print("The initial game board")
    printplayarea(playarea)
    print("Game Begins")

    while not checkWin():
        #AgentTurn(DEFAULT_ALG)
        AgentTurn("alphabetaPruning")
        printplayarea(playarea)
        PlayerTurn()
        printplayarea(playarea)
main()