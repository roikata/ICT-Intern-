from general import values


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        hand_comp = ""

        for card in self.cards:
            hand_comp += "\n" + str(card)
        return "Hand: " + hand_comp

    def add_card(self, card):
        if card.rank == 'A':
            self.aces += 1

        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1