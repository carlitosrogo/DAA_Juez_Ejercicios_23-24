
def isFeasible(value, coin):
    return ((value// coin) != 0)


def isNotSol(value):
    return (value > 0)


def greedyCoins(value, cand, sol):
    currentCoin = 0

    while (isNotSol(value)):
        if not isFeasible(value, cand[currentCoin]):
            currentCoin += 1
        else:
            sol[currentCoin] += 1
            value -= cand[currentCoin]
    return sol

def printSol(sol, cand):
    for i in range(len(sol)):
        if sol[i] != 0:
            print(sol[i], "Billetes de ", cand[i], " euros")



#main program
cand = [500, 200, 100, 50, 20, 10, 5, 2, 1]
value = 437
sol =[0] * len(cand)

greedyCoins(value, cand, sol)
printSol(sol, cand)

