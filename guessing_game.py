
Secrete_name = "Jimmy Fox"
guess = ""
guess_count = 0
guess_limit = 4
out_of_guess = False


while guess != Secrete_name and not (out_of_guess):
    if guess_count < guess_limit:
         guess = input("Try gueesing my name: ")
         guess_count +=1
    else:
        out_of_guess = True

if out_of_guess:
    print("Hey! YOU LOOOOOOSE...Better luck next time")

else:
    print("heeeey...YOU WIN..")

