import random
import replit
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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play():
    print(logo)
    def situation():
        """printing the current situation"""
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f" Cumputer's first card: {computer_cards[0]} \n")

    def final():
        """printing the final situation"""
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
    def score(list_of_cards):
        """calculating if ass should be 1 or 11"""
        real_score = sum(list_of_cards)
        if (real_score > 21) and (11 in list_of_cards):
            real_score = sum(list_of_cards)-10
            return real_score
        else:
            return real_score

    keep_play = True
    computer_cards = [random.choice(cards)]
    computer_score = sum(computer_cards)
    player_cards = random.choices(cards,k=2)
    player_score = sum(player_cards)
    situation()
    while computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = sum(computer_cards)
    while computer_score > 21 and 11 in computer_cards:
        computer_cards.append(random.choice(cards))
        computer_score = score(computer_cards)


    while keep_play == True:
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            #player is less than 21 - player decide to pull a card
            if player_score <= 21:
                player_cards.append(random.choice(cards))
                player_score = score(player_cards)
                situation()
            # player is over 21 - loosing
            if player_score > 21:
                final()
                print(f"you went over, you lose :(")
                keep_play = False
        else:
            keep_play = False


    #player diceded not to pull a card
    if player_score <=21 and computer_score > 21:
        final()
        print("you win :)")
    elif player_score <= 21 and player_score > computer_score:
        final()
        print("you win :) ")
    elif player_score <=21 and player_score == computer_score:
        final()
        print("its a draw!")
    elif player_score < computer_score:
        final()
        print("you lose :( ")
    another_game = input("do you want to play another game? 'y' or 'n' ")
    if another_game == "y":
        replit.clear()
        play()
    else:
        print("thank you for playing, goodbye")

play()



