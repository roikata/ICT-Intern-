
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like? "))
            if chips.bet <= 0:
                print("Please enter a number greater than 0.")
        except ValueError:

            print("Please enter a whole number.")
        else:
            if chips.bet > chips.total:
                print(f"Sorry you can't bet more than you have. You have {chips.total} chips.")
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()

def display_cards(player,dealer):

    print("\nDealer's hand: ")
    print("Fist card hidden!")
    print(dealer.cards[1])

    print("\nPlayer's hand: .")

    for card in player.cards:
        print(card)
    print(f"Player's value: {player.value}")

def show_all(player,dealer):
    print("\nDealer's hand: .")

    for card in dealer.cards:
        print(card)

    print(f"Value of Dealer's hand: {dealer.value}")

    print("\nPlayer's hand: ")

    for card in player.cards:
        print(card)
    print(f"Value of Player's hand: {player.value}")

def hit_or_stand(deck,hand):

    while True:
        decision = input("Would you like to hit or stand? Type h or s ").lower()
        if decision == "h":
            hit(deck,hand)
            print("\nYour hand:")
            for card in hand.cards:
                print(card)
            print(f"Your value: {hand.value}")

            if hand.value > 21:
                print("You Busted")
                break

        elif decision == "s":
            print("Player stands dealer's turn.")
            break

        else:
            print("Please enter either h or s.")

def player_busts(player,dealer,chips):
    print("Bust Player!")
    chips.lose()

def player_wins(player,dealer,chips):
    print("Player Wins!")
    chips.win()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win()

def dealer_wins(player,dealer,chips):
    print("Dealer Wins!")
    chips.lose()

def push():
    print("Dealer and Player tie! PUSH")