import random,sys

def player1(random_number,a,b):
    print("         PLAYER 1        ")
    count=1
    print(f"Guess the number betn {a} and {b}")
    while 1:
        choice=int(input())
        if choice==random_number:
            print(f"Player 1 won on {count} attempt")
            break
        elif choice > random_number:
            print("enter number lower")
        else:
            print("enter number higher")
        count+=1
    return count

def player2(random_number,a,b):
    print("         PLAYER 2       ")
    count=1
    print(f"Guess the number betn {a} and {b}")
    while 1:
        choice=int(input())
        if choice==random_number:
            print(f"Player 2 won on {count} attempt")
            break
        elif choice > random_number:
            print("enter number lower")
        else:
            print("enter number higher")
        count+=1
    return count

if __name__=='__main__':
    print("enter the lower limit: ")
    a=int(input())
    print("enter the upper limit: ")
    b=int(input())
    random_number=random.randint(a,b)

    print("Players cant look each other guesses in terminal")
    while 1:
        print("STARTING THE GAME")
        x=player1(random_number,a,b)
        y=player2(random_number,a,b)
        print(f''' PLAYER    ATTEMPTS
                       Player1  - {x}
                        Player2 - {y} 
                        ''')
        if(x<y):
            print("player 1 won")
        elif(x>y):
            print("player 2 won")
        else:
            print("its a draw")

        print("rewind the game y/n")
        choice=input().strip().lower()
        if choice=='y':
            continue
        else:
            sys.exit()