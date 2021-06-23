# Card game 
    # we need to design classes and objects which will show how a pack of cards are arranged and randomly shuffled and drawn a card from
    
    # we need to define players playing the game
        # players will have attributes name_id of player & cards in their hand
        
# Classes 
    # class Card - to display what the card and suit type is 
        # attributes - card type & value
        # methods - display card type(heart, diamond etc) and val
        
        
    # class Deck
        # attributes - data structure to hold cards
        # methods - build deck of cards
        #         - random shuffle
        #         - draw a card from the deck built
        
        
    # class Player
        # attributes - name_id
        # hand 0f cards - data structure
        
        # methods - draw a card
        #        - display what is in hand
        
import random        
class Cards:
    
    def __init__(self, suit_type, value):
        self.suit = suit_type
        self.value = value
        
    def display(self):
        print("{} of {}".format(self.suit, self.value))
        
        
class Deck:
    
    def __init__(self):
        self.deck_of_cards = []
        self.build()
        
        
    def build(self):
        for card_type in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for card_val in range(1, 14):
                self.deck_of_cards.append((Cards(card_type, card_val)))
                
    
    def shuffle(self):
        for idx in range(len(self.deck_of_cards) - 1, 0, -1):
            random_shuffle_idx = random.randint(0, idx)
            self.deck_of_cards[idx], self.deck_of_cards[random_shuffle_idx] = self.deck_of_cards[random_shuffle_idx], self.deck_of_cards[idx]
            
            
    def draw(self):
        return self.deck_of_cards.pop()
        
        
        
class Player:

    def __init__(self, player_id):
        self.player_id = player_id
        self.cards_in_hand = []
        
    def draw(self, deck):
        self.cards_in_hand.append(deck.draw())
        
    def display_cards_in_hand(self):
        for card in self.cards_in_hand:
            card.display()
            
            

deck = Deck()
deck.shuffle()

print("Anna has the following cards")
player_1 = Player('Anna')
player_1.draw(deck)
player_1.draw(deck)
player_1.draw(deck)
player_1.draw(deck)
player_1.draw(deck)

player_1.display_cards_in_hand()

print("Bob has the following cards")
player_2 = Player("Bob")
player_2.draw(deck)
player_2.draw(deck)
player_2.draw(deck)
player_2.draw(deck)

player_2.display_cards_in_hand()

        
