import physics

again = 'y'

while again == 'y' or again == 'Y' or again == '':
    print("1. Calculate Sound Travel Time")
    print("2. Calculate Light Travel Time")
    print("3. Calculate Fall Time on Earth")
    print("4. Calculate Fall Time on Moon")
    print("5. Calculate Weight on Moon")

    choice = int(input("Enter the number corresponding to the function: "))

    if choice == 1:
        distance_km = float(input("Enter distance (km): "))
        time = physics.sound_travel_time(distance_km)
        print(f"The sound travel time is {time} seconds")

    elif choice == 2:
        distance_km = float(input("Enter distance (km): "))
        time = physics.light_travel_time(distance_km)
        print(f"The light travel time is {time} seconds")

    elif choice == 3:
        height_m = float(input("Enter height (m): "))
        time = physics.fall_time(height_m)
        print(f"The fall time on Earth is {time} seconds")

    elif choice == 4:
        height_m = float(input("Enter height (m): "))
        time = physics.fall_time_moon(height_m)
        print(f"The fall time on Moon is {time} seconds")

    elif choice == 5:
        weight_kg = float(input("Enter weight (kg): "))
        weight = physics.weight_on_moon(weight_kg)
        print(f"The weight on Moon is {weight} kg")

    else:
        print("Invalid choice")

    again = input("Do you want to perform another calculation? (Y/n): ")
    if again.lower == 'n':
        print("Goodbye!")
        break