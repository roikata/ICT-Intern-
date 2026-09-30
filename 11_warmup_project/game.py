
from deck import Deck
from player import Player



def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    deck = Deck()
    deck.shuffle()

    while deck.all_cards:
        player1.add_card(deck.deal_one())
        player2.add_card(deck.deal_one())

    playing = True
    round_num = 0
    while playing:
        round_num += 1
        print(f"Round {round_num}")
        if len(player1.all_cards) == 0:
            print(f"{player1.name} out of cards. {player2.name} wins!")
            playing = False
            break

        if len(player2.all_cards) == 0:
            print(f"{player2.name} out of cards. {player1.name} wins!")
            playing = False
            break

        card1 = player1.remove_one()
        card2 = player2.remove_one()
        print(f"{player1.name} has {card1}")
        print(f"{player2.name} has {card2}")
        rounds_cards = [card1, card2]

        if card1.value > card2.value:
            player1.add_card(rounds_cards)
            print(f"{player1.name} wins the round!")

        elif card2.value > card1.value:
            player2.add_card(rounds_cards)
            print(f"{player2.name} wins the round!")

        else:
            print("War!")
            at_war = True
            while at_war:

                if len(player1.all_cards) < 4:
                    player2.add_card(rounds_cards)
                    playing = False
                    at_war = False
                    break

                if len(player2.all_cards) < 4:
                    player1.add_card(rounds_cards)
                    playing = False
                    at_war = False
                    break

                for i in range(3):
                    rounds_cards.append(player1.remove_one())
                    rounds_cards.append(player2.remove_one())

                rounds_card1 = player1.remove_one()
                rounds_card2 = player2.remove_one()

                rounds_cards.append(rounds_card1)
                rounds_cards.append(rounds_card2)

                print(f"{player1.name}: {rounds_card1}")
                print(f"{player2.name}: {rounds_card2}")

                if rounds_card1.value > rounds_card2.value:
                    player1.add_card(rounds_cards)
                    print(f"{player1.name} wins the war!")
                    at_war = False

                elif rounds_card2.value > rounds_card1.value:
                    player2.add_card(rounds_cards)
                    print(f"{player2.name} wins the war!")
                    at_war = False

                else:
                    print("WAR!")
if __name__ == "__main__":
    main()














