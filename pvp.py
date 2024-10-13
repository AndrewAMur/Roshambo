from pve import user_choice

choices = ["Rock", "Paper", "Scissors"]

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

def roshambo(first, second):
    if first == second:
        return "It's a tie"

    tupled_choices = (first, second)
    winning = (("Rock", "Scissors"), ("Scissors", "Paper"), ("Paper", "Rock"))

    if tupled_choices in winning:
        return "Player 1 won!"
    else:
        return "Player 2 won!"

def main():
    print("Player 1")
    p1 = user_choice()
    print("Player 2")
    p2 = user_choice()
    print(roshambo(p1, p2))

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
