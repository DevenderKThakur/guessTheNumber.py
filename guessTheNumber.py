import random 

def guessTheNumber(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'enter the number from 1 to {x} :'))
        if(guess > random_number):
            print('Sorry the number is too high ')
        elif(guess < random_number):
            print('Sorry the number is too low ')   

    print (f'Congrats the number is {random_number}')      

guessTheNumber(10)      




    
