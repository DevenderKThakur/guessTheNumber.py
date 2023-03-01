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

# guessTheNumber(10)       Un -comment if you want to run the programme 


def guessTheNumberByPC(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if(low != high ):
          guess = random.randint(low, high) 
        else:
            guess = low   
        feedback = input(f'Is {guess }  too high(h) ,too low(l) , or correct(c)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback =='l':
            low = guess+1
    print(f'Congrats the numebr {guess}')    

 # guessTheNumberByPC(300)  


    
