import random

colors = ['Red', 'Yellow', 'Green', 'Blue']
cards = ['0', '1', '2', '3', '4', '5', '6',
         '7', '8', '9', 'Skip', 'Reverse', '+2']
wild = ['Wild', '+4']


def create_deck():
    deck = []
    for color in colors:
        for card in cards:
            deck.append((color, card))
            if card != '0':
                deck.append((color, card))

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


def choose_color(turn):
    if turn % 2 == 0:
        chosen_color = input(
            "Choose a color (Red, Yellow, Green, Blue): ")
        while chosen_color not in colors:
            print("Error: Choose a valid color.")
            chosen_color = input(
                "Choose a color (Red, Yellow, Green, Blue): ")
    else:
        chosen_color = random.choice(
            ['Red', 'Yellow', 'Green', 'Blue'])

    return chosen_color


def add_accumulated(playable, players, next_player, deck, accumulated_draw):
    if len(playable) == 0:
        players[next_player].extend(draw_cards(deck, accumulated_draw))
        print(f"Next player draws {accumulated_draw} cards!")
        accumulated_draw = 0

    return accumulated_draw, players


def handle_special_cards(top_card, turn, direction, players, deck, accumulated_draw):
    if top_card[1] == 'Skip':
        print("Next player skipped!")
        turn += direction
    elif top_card[1] == 'Reverse':
        print("Reversing direction!")
        if len(players) == 2:
            turn += direction
        else:
            direction *= -1
    elif top_card[1] == '+2':
        next_player = (turn + direction) % 2
        accumulated_draw += 2
        playable_plus2 = [card for card in players[next_player]
                          if card[1] == '+2' or card[1] == '+4']
        accumulated_draw, players = add_accumulated(playable_plus2, players,
                                                    next_player, deck, accumulated_draw)
    elif top_card[1] == 'Wild':
        chosen_color = choose_color(turn)
        top_card = (chosen_color, top_card[1])
    elif top_card[1] == '+4':
        chosen_color = choose_color(turn)
        top_card = (chosen_color, top_card[1])
        next_player = (turn + direction) % 2
        accumulated_draw += 4
        playable_plus4 = [card for card in players[next_player]
                          if card[1] == '+4']
        accumulated_draw, players = add_accumulated(playable_plus4, players,
                                                    next_player, deck, accumulated_draw)

    return top_card, turn, direction, players, deck, accumulated_draw


def main():
    deck = create_deck()
    players = [draw_cards(deck, 7), draw_cards(deck, 7)]
    top_card = deck.pop()
    while top_card[0] == 'Wild':
        top_card = deck.pop()
    turn = 0
    direction = 1
    accumulated_draw = 0

    while True:
        player_turn = turn % 2

        if player_turn == 0:

            print("PLayer's turn\n")
            print(f"Top card: {top_card} \n")
            print(f"Your cards: {players[0]} \n")
        else:
            print("Bot's turn\n")
            print(f"Top card: {top_card} \n")
            print(f"Bot's cards: {players[1]} \n")

        playable_cards = [card for card in players[player_turn]
                          if can_play(card, top_card)]
        if len(playable_cards) == 0:
            print("No playable cards, drawing a card...")
            drawn = draw_cards(deck, 1)[0]
            print(f"Drew: {drawn}")
            if can_play(drawn, top_card):
                print("Playing drawn card")
                top_card = drawn
                top_card, turn, direction, players, deck, accumulated_draw = handle_special_cards(
                    top_card, turn, direction, players, deck, accumulated_draw)
            else:
                players[player_turn].append(drawn)
        else:
            if player_turn == 0:
                for n, card in enumerate(playable_cards):
                    print(f"{n + 1}: {card}")
                choice = int(
                    input(f"\nChoose a card to play (1-{len(playable_cards)}): ")) - 1
            else:
                playable_plus2 = [card for card in players[player_turn]
                                  if card[1] == '+2' or card[1] == '+4']
                playable_plus4 = [card for card in players[player_turn]
                                  if card[1] == '+4']
                if len(playable_plus4) != 0 and top_card[1] == '+2' or top_card[1] == '+4':
                    choice = playable_cards.index(playable_plus4[0])
                elif len(playable_plus2) != 0 and top_card[1] == '+2':
                    choice = playable_cards.index(playable_plus2[0])
                else:
                    choice = 0
            chosen_card = playable_cards[choice]
            players[player_turn].remove(chosen_card)
            top_card = chosen_card
            print(f"Played: {top_card}")

            top_card, turn, direction, players, deck, accumulated_draw = handle_special_cards(
                top_card, turn, direction, players, deck, accumulated_draw)

        if player_turn == 0:
            print(f"New cards: {players[0]} \n")
        else:
            print(f"Bot's new cards: {players[1]} \n")

        if len(players[player_turn]) == 0:
            print(f"PLayer wins!\n" if player_turn == 0 else f"Bot wins!")
            break

        input("Ready to continue? Press Enter")

        turn += direction


if __name__ == "__main__":
    main()
