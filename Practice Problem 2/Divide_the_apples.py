while 1:
    try:
        apples=int(input("enter the no of apples: "))
        mn=int(input("enter the minimum number to checK: "))
        mx=int(input("enter the maximum number to checK: "))

        if(mn==mx):
            if(apples%mx==0):
                print(f"{mx} is divisor of {apples}")

        elif(mn>mx):
            raise ValueError("mn cannot be greater than mx")
        
        else:
            for i in range(mn,mx+1):
                if apples%i==0:
                    print(f"{i} is divisor of {apples}")
                else:
                    print(f"{i} is not divisor of {apples}")    

    except ValueError as ve:
        print(ve)
        continue
    else:
        choice=input("want to rewind the program y/n ")
        
        if choice=='y':
            continue
        else:
            break

print("PROGRAM ENDED SUCCESFULLY")