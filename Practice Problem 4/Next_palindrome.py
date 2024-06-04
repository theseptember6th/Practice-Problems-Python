'''
Author: KRISTAL SHRESTHA
DATE:6/4/2024
PURPOSE:LEARNING PROBLEM 4
'''

def next_palindrome(n):
    n+=1
    while not is_palindrome(n): #if returned false , it will be overall true
        n+=1
    return n #gets out of loop if it gets the palindrome
def is_palindrome(n):   #checks whether it is palindrome or not
    return str(n)==str(n)[::-1]  #very simple but logical concept
#returns true if palindrome and false if not palindrome

if __name__ == '__main__':
    numbers=[]
    size=int(input("Enter the no of testing numbers to find their next palindrome\n "))
    for i in range(size):
        numbers.append(int(input(f"enter for numbers[{i}]: ")))
    print(numbers)

    for index,value in enumerate(numbers):
        print(f"The {value}'s next palindrome is {next_palindrome(numbers[index])}")

