import random as rd
sysnum= rd.randint(1,10)
print(sysnum)
attempts=1
while True:
    usernum=int(input("Enter any num between 1-10 : "))
    if(sysnum==usernum):
        print("Hurray! You Guessed it right!")
        print(f"You did it in {attempts} no guesses")
        break
    else:
        if sysnum > usernum:
            print("Oops!You guessed too low. Please guess again")
        else:
            print("Oops!You guessed too high. Please guess again")

        attempts += 1

    if attempts > 5:
        print("Game over!!You Have Exhausted the guess limit")
        break






