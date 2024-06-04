#input

lst1=[]
while 1:
    try:
        size=int(input("enter the size of lst1: "))
        for i in range(size):
            x=int(input(f"enter for the lst1[{i}]: "))
            lst1.append(x)
            
    except ValueError as ve:
        print(f"removing {lst1.pop()}")
        continue
    except Exception as e:
        print(e)
        continue
    else:
        break

# lst1.sort()
print(f"Your list is {lst1}")



#inbuilt method
reverse1=lst1.copy()  # or reverse1=lst1[:] another way to copy
reverse1.reverse() #.reverse returns nothing it changes the original list
print(reverse1)

#list slicing trick
reverse2=lst1.copy()
print(reverse2[::-1])

#ur own concept
#my C concept

reverse3=lst1.copy()

# temp=0
# for i in range(len(lst1)):
#     if(i<=len(lst1)/2):
#         temp=reverse3[i]
#         reverse3[i]=reverse3[len(reverse3)-1-i]
#         reverse3[len(reverse3)-1-i]=temp
# print(reverse3)
    
#my python concept

for i in range(len(reverse3)//2):
    reverse3[i],reverse3[len(reverse3)-1-i]=reverse3[len(reverse3)-1-i],reverse3[i]

print(reverse3)

