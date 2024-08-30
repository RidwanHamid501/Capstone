# Capstone
Making the game Uno as my capstone project

# Methods

create_deck
- Creates a standard Uno deck - 108 cards total
- For each colour (red, yellow, green, blue):
    One 0
    Two 1-9
    Two Skip
    Two +2
    Two Reverse
    Four Wild
    Four Wild +4

- The deck is shuffled in the beginning of the game

draw_cards

can_play
- Checks if card chosen by the user is able to be played (same colour or number or wild)

main
