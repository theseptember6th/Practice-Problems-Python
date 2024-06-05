'''
AUTHOR :KRISTAL SHRESTHA
DATE:6/5/2024
PURPOSE:LEARNING AND PRACTISING JUMBLED FUNNY NAMES PROGRAM
'''


import random

if __name__=="__main__":
    size=int(input("enter the number of friends"))
    print("Enter the name of your friends ")
    names1=[input() for _ in range(size)]
    print(names1)
    

    firstNames=[]
    lastNames=[]

    for name in names1:
        part=name.split(" ")
        firstNames.append(part[0])
        lastNames.append(" ".join(part[1::]))

    # print(part)
    # print(firstNames)
    # print(lastNames)

    random.shuffle(firstNames)
    random.shuffle(lastNames)

    jumbledNames=[f"{first} {last}" for first,last in zip(firstNames,lastNames)]
    print("\nPlease look at the jumbled Names")
    print(jumbledNames)
    
    