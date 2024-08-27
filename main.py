import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2,
          'Three': 3, 
          'Four': 4,
          'Five': 5,
          'Six': 6, 
          'Seven': 7, 
          'Eight': 8,
          'Nine': 9,
          'Ten': 10, 
          'Jack': 10,
          'Queen': 10, 
          'King': 10, 
          'Ace': 11}

playing = True
# score variables
player_score = 0;
computer_score = 0


# CLASSES
class Card:  # Creates all the cards

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:  # creates a deck of cards

    def __init__(self):
        self.deck = []  # haven't created a deck yet
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle(self):  # shuffle all the cards in the deck
        random.shuffle(self.deck)

    def deal(self):  # pick out a card from the deck
        single_card = self.deck.pop()
        return single_card


class Hand:   # show all the cards that the dealer and player have

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # keep track of aces since they can be 1 or 11

    def add_card(self, card):  # add a card to the player's or dealer's hand
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            # change value of aces if over 21

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):   # hit or stand
    global playing
    global player_score
    global computer_score    

    while True:
        ask = input("\nWould you like to hit or stand? Please enter 'h' or 's': ")

        if ask.lower() == 'h':
            hit(deck, hand)
        elif ask.lower() == 's':
            print("Player stands, Dealer is playing.")
            playing = False
        else:
            print("Sorry! I did not understand that! Please try again!")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand: ")
    print(" card hidden")
    print("", dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

# game endings

def player_busts(player, dealer):
    print("PLAYER BUSTS!")
    global player_score
    global computer_score 
    computer_score += 1
 

def player_wins(player, dealer):
    print("PLAYER WINS!")
    global player_score
    global computer_score 
    player_score +=1


def dealer_busts(player, dealer):
    print("DEALER BUSTS!")
    global player_score
    global computer_score 
    player_score +=1


def dealer_wins(player, dealer):
    print("DEALER WINS!")
    global player_score
    global computer_score 
    computer_score += 1


def push(player, dealer):
    print("Player and Dealer tie!")
  
# Gameplay!

while True:
    print("Welcome to BlackJack!")
 
    print("player score is", player_score)
    print("computer score is", computer_score)


    # create an shuffle deck
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # show cards
    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand)
            break

        elif player_hand == 21:
          player_wins(player_hand, dealer_hand)
          break 
        # what happens if both have 21?

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand)


    new_game = input("\nWould you like to play again? Enter 'y' or 'n': ")
    if new_game.lower() == 'y':
        playing = True
        continue
    elif new_game.lower() == "n":
        print("\nThanks for playing!")
        break
    else:
      continue
