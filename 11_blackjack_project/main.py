from card import Card
from deck import Deck
from chips import Chips
from hand import Hand

from game import *

player_chips = Chips()
while True:

    print("Welcome to BLACKJACK")

    print(f"You have {player_chips.total} chips.")

    take_bet(player_chips)

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    player_hand.adjust_for_aces()

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.adjust_for_aces()

    display_cards(player_hand,dealer_hand)

    hit_or_stand(deck,player_hand)

    if player_hand.value > 21:
        player_busts(player_hand,dealer_hand,player_chips)

    else:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)

        else:
                push()

    print(f"Total chips: {player_chips.total}")
    replay = input("Do you want to play again? Type yes or no: \n").lower()

    if replay == "yes":
        print("Play Again!")
    else:
        break


# Create a Deck
deck = Deck()
#Shuffle it
deck.shuffle()
# Create player and dealer hands
player_hand = Hand()
dealer_hand = Hand()






