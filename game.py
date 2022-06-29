import random

users = ['John', 'Jack']


def game_turn(active_player_, amount_):
    if active_player_ != bot:
        print(amount_ * '|')
        return input(f"{active_player_}'s turn!\n")
    elif active_player_ == bot:
        print(amount_ * '|')
        print(f"{active_player_}'s turn:")
        if amount_ % 4 == 0:
            number = '3'
        elif amount_ % 4 == 3:
            number = '2'
        elif amount_ % 4 == 2:
            number = '1'
        elif amount_ == 1:
            number = '1'
        else:
            number = random.choice(['1', '2', '3'])
        print(number)
        return number


print('How many pencils would you like to use:')
while True:
    amount = input()
    if not amount.isdigit():
        print("The number of pencils should be numeric")
    elif int(amount) == 0:
        print("The number of pencils should be positive")
    else:
        break

print(f"Who will be the first ({', '.join(users)}):")
while True:
    first_player = input()
    if first_player not in users:
        print(f"Choose between '{users[0]}' and '{users[1]}'")
    else:
        # bot = users[1] if first_player == users[0] else users[0]
        real_man = users[0]
        bot = users[1]
        active_player = first_player
        break

taken_amount = game_turn(first_player, int(amount))
while True:
    amount = int(amount)
    if not taken_amount.isdigit() or int(taken_amount) not in [1, 2, 3]:
        print("Possible values: '1', '2' or '3'")
        taken_amount = game_turn(active_player, amount)
    elif int(taken_amount) > amount:
        print("Too many pencils were taken")
        taken_amount = game_turn(active_player, amount)
    else:
        taken_amount = int(taken_amount)
        amount -= taken_amount
        active_player = bot if active_player == real_man else real_man
        if amount == 0:
            print(f"{active_player} won!")
            break
        taken_amount = game_turn(active_player, amount)
