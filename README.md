# Capstone
Making the game Uno as my capstone project

# Methods

create_deck
- Creates a standard Uno deck - 108 cards total
- For each colour (red, yellow, green, blue):
    - One 0
    - Two 1-9
    - Two Skip
    - Two +2
    - Two Reverse
    - Four Wild
    - Four Wild +4

- The deck is shuffled in the beginning of the game

draw_cards
- Takes in current deck and number of cards to be drawn. If deck is not empty, the first(top) card is removed from the deck and added to the player's hand

can_play
- Checks if card chosen by the user is able to be played (same colour or number or wild)

main
