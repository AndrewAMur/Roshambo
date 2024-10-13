import pve
import pvp

def main():
    print("Do you want to do PVP or PVE?")
    print("[1] PVP")
    print("[2] PVE")
    loop_flag = True
    while loop_flag:
        try:
            choice = input("Your choice: ")
            parsed = int(choice)
            if parsed in [1, 2]:
                if parsed == 1:
                    pvp.main()
                elif parsed == 2:
                    pve.main()
                loop_flag = False
        except:
            continue

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
