import random


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cardScores = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def randomCard():
    return random.choice(cardScores)
def winner():
    if sum(user_card) >= 21:
        print("You lose, Card went over 21.")
    elif sum(dealer_card) > 21:
        print("Opponent went over, You win")
    elif sum(user_card) < 21:
        if sum(user_card) > sum(dealer_card):
            print("You win")
        elif sum(user_card) < sum(dealer_card):
            print("You lose")
        elif sum(user_card) == sum(dealer_card):
            print("Draw")


start_game = True
while start_game == True:
    user_card = []
    dealer_card = []
    user_card.append(randomCard())
    user_card.append(randomCard())
    dealer_card.append(randomCard())
    dealer_card.append(randomCard())
    def game_restart():
        i = True
        while i == True:
            print(logo)
            print(f"Your cards: {user_card}")
            print(f"Computer's first card: {dealer_card[0]}")
            get_anotherCard = input(print("Type 'y' to get another card, type 'n' to pass: "))

            if sum(dealer_card) < 12:
                dealer_card.append((randomCard()))
            if get_anotherCard == "y":
                user_card.append(randomCard())
                print(logo)
                print(f"Your final hand {user_card}. Total score: {sum(user_card)}")
                print(f"Computer's final hand: {dealer_card}. Total score: {sum(dealer_card)}")
            elif get_anotherCard == "n":
                print(logo)
                print(f"Your final hand {user_card}")
                print(f"Computer's final hand: {dealer_card}")
            winner()
            i = False

    game_start = input(print("Do you want to play a game of Blackjack? Type 'y' or 'n': "))
    if game_start == "y":
        game_restart()
    else:
        start_game = False

