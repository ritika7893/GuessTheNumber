import random
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if   low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'Is {guess} too low(l) and too high(h) and correct(c)').lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
        elif feedback=='c':
            print("You guessed the number correctly")
            break
        else:
            print("Wrong Input")
computer_guess(1000)   
