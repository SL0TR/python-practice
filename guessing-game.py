secret_game = "giraffe"
guess = ""
tries = 0
try_limit = 3
out_of_tries = False

while guess != secret_game and not(out_of_tries):
    if tries < try_limit:
        guess = input("Enter guess: ")
        tries += 1
    else:
        out_of_tries = True
if out_of_tries:
    print("You are out of tries, YOU LOSE :(")
else:
    print("You win! :)")
