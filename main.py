import random

colours = ['Red', 'Yellow', 'Green', 'Blue']
cards = ['0', '1', '2', '3', '4', '5', '6',
         '7', '8', '9', 'Skip', 'Reverse', '+2']
wild = ['Wild', '+4']


def create_deck():
    deck = []
    for colour in colours:
        for card in cards:
            deck.append((colour, card))
            if card != '0':
                deck.append((colour, card))

    for i in range(4):
        deck.append(('Wild', 'Wild'))
        deck.append(('Wild', '+4'))

    random.shuffle(deck)
    return deck


def draw_cards(deck, count):
    new_cards = []
    for i in range(count):
        if len(deck) != 0:
            new_cards.append(deck.pop())

    return new_cards


def can_play(card, top_card):
    return card[0] == top_card[0] or card[1] == top_card[1] or card[0] == 'Wild'
