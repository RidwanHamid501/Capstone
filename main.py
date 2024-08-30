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


def main():
    deck = create_deck()
    players = [draw_cards(deck, 7), draw_cards(deck, 7)]
    top_card = deck.pop()
    turn = 0
    direction = 1

    while True:
        player_turn = turn % 2
        print(f"PLayer's turn\n" if player_turn == 0 else f"Bot's turn")
        print(f"Top card: {top_card}")
        print(f"Your cards: {players[player_turn]}")

        playable_cards = [card for card in players[player_turn]
                          if can_play(card, top_card)]
        if len(playable_cards) == 0:
            print("No playable cards, drawing a card...")
            drawn = draw_cards(deck, 1)[0]
            print(f"Drew: {drawn}")
            if can_play(drawn, top_card):
                print("Playing drawn card")
                if drawn[0] != 'Wild':
                    top_card = drawn
            else:
                players[player_turn].append(drawn)
        else:
            for n, card in enumerate(playable_cards):
                print(f"{n + 1}: {card}")
            choice = int(
                input(f"Choose a card to play (1-{len(playable_cards)}): ")) - 1
            chosen_card = playable_cards[choice]
            players[player_turn].remove(chosen_card)
            top_card = chosen_card
            print(f"Played: {top_card}")

            if top_card[1] == 'Skip':
                print("Next player skipped!")
                turn += direction
            elif top_card[1] == 'Reverse':
                print("Reversing direction!")
                direction *= -1
            elif top_card[1] == '+2':
                next_player = (turn + direction) % 2
                print("Next player draws 2 cards!")
                players[next_player].extend(draw_cards(deck, 2))
            elif top_card[1] == 'Wild':
                chosen_color = input(
                    "Choose a color (Red, Yellow, Green, Blue): ")
                top_card = (chosen_color, top_card[1])
            elif top_card[1] == '+4':
                chosen_color = input(
                    "Choose a color (Red, Yellow, Green, Blue): ")
                top_card = (chosen_color, top_card[1])
                next_player = (turn + direction) % 2
                print("Next player draws 4 cards!")
                players[next_player].extend(draw_cards(deck, 4))

        if len(players[player_turn]) == 0:
            print(f"PLayer wins!\n" if player_turn == 0 else f"Bot wins!")
            break

        turn += direction


if __name__ == "__main__":
    main()
