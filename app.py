def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of players (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Please enter a numeric number between 2 and 10.")
            continue

        print("Enter the number of players")
