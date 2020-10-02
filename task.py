def main():

    forename = str(input("Enter your first name: "))
    surname = str(input("Enter your last name: "))
    score = int(input("Enter your score: "))
    name = forename + " " + surname

    if score > 100:
        print("Error: Score cannot be larger than 100")

    elif score < 0:
        print("Error: score cannot be smaller that 0")

    elif score > 60:
        print("Congratulations", name, "you have passed!")

    elif score < 60:
        print("We're sorry", name, "but unfortunately you have not passed.")

    restart = str(input("Would you like to restart?\n"))
    if restart == "yes":
        main()

    else:
        exit()

main()