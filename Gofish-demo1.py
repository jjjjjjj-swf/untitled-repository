import random
import time

# Main program
code = input("Type 'gofish' to enter the game: ")
if code == "gofish":
    for x in range(5):
        b = "Loading[" + "=" * x + "]"
        print(b, end="\r")
        time.sleep(0.5)

    # Setup
    cardtypes = ['dollars', 'euros', 'yens', 'rubles', 'pounds', 'wons']
    symbols = {
        'dollars': '$:',
        'euros': '€:',
        'yens': '¥:',
        'rubles': '₽:',
        'pounds': '£:',
        'wons': '₩:'
    }

    deck = cardtypes * 4
    random.shuffle(deck)

    p1 = [deck.pop() for _ in range(7)]
    bot2 = [deck.pop() for _ in range(7)]

    bot_asked_cards = set()

    # Game loop
    while deck or p1:
        # Show player's card counts
        print("\nCard values (Player's hand):")
        for card in cardtypes:
            print(f"{symbols[card]} {p1.count(card)}")

        # Player's turn
        ask = input("\nAsk the bot for a card: ").strip().lower()
        if ask in bot2:
            print(f"Yes, I have a {symbols[ask]}🤖")
            bot2.remove(ask)
            p1.append(ask)
        else:
            print("Go Fish!")
            if deck:
                drawn = deck.pop()
                p1.append(drawn)
                print(f"You drew: a {symbols[drawn]} {drawn}")
            else:
                print("Deck is empty!")

        # Show updated player's card counts after their turn
        print("\nAfter your turn (Player's hand):")
        for card in cardtypes:
            print(f"{symbols[card]} {p1.count(card)}")

        # Bot's turn
        if bot2:
            available_cards = [card for card in cardtypes if card not in bot_asked_cards and card in bot2]

            if available_cards:
                bot_ask = random.choice(available_cards)
                print(f"\nBot asks: Do you have any {bot_ask}?")

                if bot_ask in p1:
                    print(f"You: Yes, I have one {bot_ask}!")
                    p1.remove(bot_ask)
                    bot2.append(bot_ask)
                else:
                    print("You: Go Fish!")
                    if deck:
                        bot_drawn = deck.pop()
                        bot2.append(bot_drawn)
                        print(f"Bot drew a {symbols[bot_drawn]} {bot_drawn}")
                    else:
                        print("Deck is empty!")

                # Add the card to the set of asked cards
                bot_asked_cards.add(bot_ask)
            else:
                print("\nBot has no more cards to ask for!")

        # game end conditions
        if not p1 or not bot2:
            print("\nGame Over!")
            if not p1:
                print("You lost! Better luck next time.")
            else:
                print("You win!")
            break
