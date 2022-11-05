n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1
if(number_of_guesses>9):
    print("Game Over")
    print("The correct no is:",n)


'''i=0
while(True):
   if i+1<5:
       i+=1
       continue
   print(i+1)
   if i==44:
       break
   i+=1

i=0
while(i<=10):
    i+=1
    if i==5:
        continue
    print(i)
    if i==9:
        break'''


