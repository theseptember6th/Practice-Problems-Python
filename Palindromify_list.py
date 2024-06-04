'''
AUTHOR:KRISTAL SHRESTHA
DATE:6/4/2024
PURPOSE:LEARNING AND PRACTICING PYTHON
'''

def next_palindrome(value):
    if(value<10):
        return value
    else:
        value+=1
        while not is_palindrome(value):
            value+=1
        return value
    

def is_palindrome(value):
    return str(value)==str(value)[::-1]

if __name__ =='__main__':
    list1=[]
    size=int(input("enter the size of the list: "))
    for i in range(size):
        number=int(input(f"enter the list1[{i}]: "))
        list1.append(number)

    print(list1) #original list

    for index,value in enumerate(list1):
        list1[index]=next_palindrome(value)

    print(list1) #after modifying the list
