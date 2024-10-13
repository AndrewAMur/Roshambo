import random

choices = ["Rock", "Paper", "Scissors"]

def robot_choice():
    robot_choice = random.choice(choices)
    return robot_choice

def user_choice():
    for i in range(len(choices)):
        print(f"{i + 1}: {choices[i]}")

    loop_flag = True

    while loop_flag:
        user_choice = input("Select one of the options: ")
        try:
            parsed = int(user_choice)
            if parsed in [1, 2, 3]:
                return choices[parsed - 1]
        except:
            continue

def roshambo(user, robot):
    if user == robot:
        return "It's a tie"

    tupled_choices = (user, robot)
    winning = (("Rock", "Scissors"), ("Scissors", "Paper"), ("Paper", "Rock"))

    if tupled_choices in winning:
        return "You won!"
    else:
        return "You lost!"

def main():
    user = user_choice()
    robot = robot_choice()
    print(f"You chose: {user}")
    print(f"Robot chose: {robot}")
    print(roshambo(user, robot))

if __name__ == "__main__":
    main()

    flag = True
    
    while flag:
        print("Do you want to play again?")
        print("[1] Yes")
        print("[2] No")
        play_again = input("Your choice: ")
        try:
            parsed = int(play_again)
            if parsed == 1:
                main()
            elif parsed == 2:
                flag = False
        except:
            continue
