from random import randrange
class fg:
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[93m'
    lightblue='\033[94m'
    pink='\033[95m'
    lightcyan='\033[96m'
    reset='\033[0m'
def token():
    ans1 = input("Insert another token?:")
    ans1 = ans1.lower()
    if ans1[0] == "y":
        wordle()
    elif ans1[0] == "n":
        print("Fine, bye.")
    else:
        print("Pls say yes or no")
        token()
def wordle():
    l = 'qwertyuiopasdfghjklzxcvbnm'
    l = list(l)
    j = l.copy()
    file = open("words.txt", "r")
    text = file.read()
    text = text.split('\n')
    ran = randrange(len(text))
    gen = text[ran]
    win = 0
    x=0
    varRound = 1
    blank = "_____"
    bA = list(blank)
    pR = list()
    pR1 = list()
    print("Welcome to Terminal Wordle!",'\n',len(text),"words were used!\nGood luck guessing the proper one!")
    while x < 5:
        guesses = '\n'.join(pR)
        bA1 = bA.copy()
        bA1 = list(filter(('_').__ne__, bA1))
        print("Round:", varRound)
        print("You've Found:", len(bA1), "letters.")
        if varRound > 1:
            print("Guessed Words\n",guesses)
            print("Word Contains:",pR1)
        print("Current result:", bA)
        jcop = '|'.join(j)
        kp = jcop.find('p') + 1
        kl = jcop.find('l') + 1
        km = jcop.find('m') + 1
        print("Letters Used:\n", jcop[0:kp]+jcop[kp:kl]+jcop[kl:km])
        print(jcop)
        reg = False
        while reg == False:
            guess = input("Guess the 5 letter word:")
            print("\n\n\n")
            if not guess.isalpha():
                print("This is a letters game.")
            elif len(guess) !=5:
                print("You need to guess a 5 letter word.")
            elif guess.lower() not in text:
                print("This word was not found in the list.")
            else:
                reg = True
        if guess == gen:
            print("Congratulations,",guess.title(),"was the correct answer! You've won in:",varRound,"rounds!")
            token()
        sG = list(guess)
        sA = list(gen)
        cA = list([index for index, (a1, a2) in enumerate(zip(sG, sA)) if a1 == a2])
        for ind2, i2 in enumerate(sA):
            if i2 in sG and i2 not in pR1:
                pR1.append(i2)
                oG = ""
                oG1 = l.index(i2)
                oG += fg.green + l[oG1]
                oG += fg.reset
                j[oG1] = oG
                if sA.count(i2) > 1:
                    print("There seems to be more than one", "'",i2,"'", "in this word.")
        for ind1, i1 in enumerate(sG):
             i1 = i1.lower()
             strikeChar = l.index(i1)
             if l[strikeChar] not in pR1:
                 oR = ""
                 oR += fg.red + l[strikeChar]
                 oR += fg.reset
                 j[strikeChar] = oR
        for ind, index in enumerate(cA):
            bA[index] = sG[index]
        pR.append(guess)
        varRound+=1
        x+=1
        if x == 5:
            print("You did not guess the word in time, the word was:", gen.title())
            token()
token()