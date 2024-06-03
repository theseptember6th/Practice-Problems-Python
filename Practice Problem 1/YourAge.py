import sys

current_year = 2090

while True:
    try:
        time_input = input("Enter your current age or year of birth: ").strip()
        if not time_input.isdigit():
            raise ValueError("Input must be a number.")
        
        time = int(time_input)

        if len(time_input) == 4:  # Year of birth
            if time > current_year:
                raise ValueError("You are not yet born")
            elif current_year - time > 120:
                raise ValueError("You seem to be the oldest person alive")
            else:
                print("You will turn 100 years old in the year", time + 100)
        elif len(time_input) <= 3:  # Age
            if time < 0:
                raise ValueError("You are not yet born")
            elif time > 120:
                raise ValueError("You seem to be the oldest person alive")
            else:
                print("You will turn 100 years old in the year", current_year + (100 - time))
        else:
            raise ValueError("Invalid input length.")
    
    except ValueError as e:
        print(f"PLEASE TRY AGAIN: {e}")
        continue

    print("Do you want to continue to the optional part?")
    optional_part = input("Press y/n: ").strip().lower()
    if optional_part == 'n':
        break
    elif optional_part != 'y':
        print("Invalid input. Exiting.")
        break

    while True:
        try:
            future_year_input = input("Enter the year to calculate your age in that year: ").strip()
            if not future_year_input.isdigit():
                raise ValueError("Input must be a number.")
            
            future_year = int(future_year_input)
            
            if len(future_year_input) != 4:
                raise ValueError("This is not a valid year.")
            
            if future_year < current_year:
                raise ValueError("The year is in the past")
            
            if len(time_input) == 4:
                age_in_year = future_year - time
            else:
                age_in_year = time + (future_year - current_year)
            
            if age_in_year > 120:
                print("You seem to be the oldest person alive")
            else:
                print(f"Your age in the year {future_year} will be: {age_in_year}")

        except ValueError as e:
            print(f"PLEASE TRY AGAIN: {e}")
            continue
        else:
            print("Optional part ran successfully")
        
        rewind_choice = input("Do you want to rewind the program? -y for yes, -n for no: ").strip().lower()
        if rewind_choice == 'n':
            sys.exit()
        elif rewind_choice == 'y':
            break
        else:
            print("Invalid choice, press 'y' or 'n'")
            continue

print("Program has successfully ended.")
