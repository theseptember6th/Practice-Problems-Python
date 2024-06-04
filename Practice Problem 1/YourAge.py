import sys

current_year = 2024
print(f"The current year is {current_year} AD")

while True:
    try:
        birth_year = None

        while birth_year is None:
            time_input = input("Enter your current age or birth year: ").strip()
            
            if not time_input.isdigit():
                raise ValueError("Input must be a number")
            
            time = int(time_input)
            
            if len(time_input) == 4:  # Input entered as year of birth
                birth_year = time
                age = current_year - birth_year
                
                if birth_year > current_year:
                    raise ValueError("You are not yet born")
                elif age > 120:
                    raise ValueError("You seem to be the oldest person alive")
                else:
                    print(f"You will be 100 years old in {birth_year + 100} AD")
            
            elif len(time_input) <= 3:  # Input entered as current age
                age = time
                birth_year = current_year - age
                
                if age > 120:
                    raise ValueError("You seem to be the oldest person alive")
                elif age < 0:
                    raise ValueError("Invalid age")
                else:
                    print(f"You will be 100 years old in {birth_year + 100} AD")
            else:
                raise ValueError("Invalid input length")
        
        choice = input("PRESS y/n to continue optional part: ").strip().lower()
        if choice != 'y':
            break
        
        while True:  # For optional part
            try:
                time_input = input("Enter the future year to calculate your age in that year: ").strip()

                if not time_input.isdigit():
                    raise ValueError("Input must be a number")
                
                future_year = int(time_input)

                if len(time_input) == 4:  # Input entered as future year
                    age_in_future_year = future_year - birth_year
                    
                    if age_in_future_year < 0:
                        raise ValueError("You are not yet born in that year")
                    elif age_in_future_year > 120:
                        raise ValueError("You seem to be the oldest person alive in that year")
                    else:
                        print(f"In the year {future_year}, you will be {age_in_future_year} years old")
                else:
                    raise ValueError("INVALID LENGTH, YOU COULD ONLY WRITE YEAR")
            
            except ValueError as e:
                print(f"Error: {e}")
                continue
            
            else:  # Program running successfully
                choice = input("PRESS y/n to continue program: ").strip().lower()
                if choice == 'y':
                    break
                elif choice == 'n':
                    sys.exit("Bye Bye")
                else:
                    print("Invalid choice")

    except ValueError as e:
        print(f"Error: {e}")
        continue

print("Program ended successfully")
