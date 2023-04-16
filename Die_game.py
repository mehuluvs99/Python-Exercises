import random


start_place = 0
end_place = 40
user_place = 0
computer_place = 0
user_win = False
comupter_win = False
quit_game = False
while not user_win or not comupter_win:
    user_input = input('Enter "t" to toss a die , or "q" to end: ')
    if user_input == "q":
        quit_game = True
        break
    if user_input == "t":
        user_move = random.randint(1,6)
        user_place += user_move
        print("You move for " +str(user_move)+" steps.")
        if user_place > end_place:
            overshoot = user_place - end_place
            user_place = end_place - overshoot
        print("now you are at position " +str(user_place))
        if user_place == end_place:
            user_win = True
            break

    computer_move = random.randint(1,6)
    computer_place += computer_move
    print("Computer moves for "+str(computer_move)+" steps.")
    if computer_place > end_place:
        overshoot = computer_place - end_place
        computer_place = end_place - overshoot
    print("computer is at position " +str(computer_place))
    if computer_place == end_place:
        comupter_win = True
        break
if quit_game:
    print("You need "+ str(end_place - user_place)+ ' steps to win.')
elif user_win:
    print("You win!")
elif comupter_win:
    print("Computer Win.")