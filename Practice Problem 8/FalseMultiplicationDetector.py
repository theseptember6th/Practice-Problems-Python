'''
AUTHOR:KRISTAL SHRESTHA
DATE:6/4/2024
PURPOSE:FALSE MULTIPLICATION DETECTOR PRACTICE PROGRAM USING PYTHON
'''

import random

def falseMultiplicationTable(number):
    error=random.randint(1,9) #for index of table 1-9 not  10 because its easy to catch error of something*10
    false_table=[]
    for i in range(1,11): # 1 to 11-1
        false_table.append(i*number) #this table is genuine for now

    false_table[error]=false_table[error]+random.randint(0,9)  #creating error at random index betn 0 -9
    #now this table has error so it is named false table

    return false_table


def iscorrect(false_table,number):
    for i in range(1,11):
        if(false_table[i-1]!=i*number):
            return i #returns index if incorrect table
    else:
        return None  #if correct table



if __name__=="__main__":
    number=int(input("enter the number which you want multiplication table: "))
    false_table=falseMultiplicationTable(number)
    print(false_table)
    index=iscorrect(false_table,number)
    if index== None:
        print("The table is correct")
    else:
        print(f"The table has an error at {index}")

#to simplify things  i assumed only one error here 