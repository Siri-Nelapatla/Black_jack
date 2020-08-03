

import random
suits=('Hearts','Diamonds','Spades','Clubs')

ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,
        "Queen":10,'King':10,'Ace':11}
playing = True        

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + ' of ' +self.suit

class Deck:

    def __init__(self):
        self.deck = []
        for suit  in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp=' '
        for card in self.deck:
            deck_comp+='\n'+card.__str__()
        return 'The deck has:'+deck_comp
    def shuffle(self):
        random.shuffle(self.deck)     
    def deal(self):
        single_card = self.deck.pop()
        return single_card       
test_deck = Deck()

class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank =='Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value >21 and self.aces:
            self.value -=10
            self.aces -=1
        
class Chips:
    def __init__(self):
        self.total = 100
        self.best = 0
    def win_bet(self):
        self.total += self.best
    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?'))
        except ValueError:
            print('sorry, a bet muct be an integer')
        else:
            if chips.bet>chips.total:
                print('sorry, your bet cant exceed',chips.total) 
            else:
                break       

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x= input('would you like to Hit or Stand? Enter H or S')    
        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            print('player stands. dealer is playing')
            playing = False
        else:
            print('sorry, try again')
            continue
        break


def show_some(player,dealer):
    print('\n Dealers Hand:')
    print('<card hidden>')
    print('',dealer.cards[1])
    print('\nPlayers hand:',*player.cards,sep='\n')

def show_all(player,dealer):
    print('\nDealers hand:',*dealer.cards,sep='\n') 
    print('Dealers Hand: ',dealer.value)
    print('\nPlayers Hand:',*player.cards,sep='\n')
    print('players hand=',player.value)   

def player_busts(player,dealer,chips):
    print('player busts!')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('Player wins!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Dealer busts!')
    chips.lose_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()    

def push(player,dealer):
    print('dealer and player tie! its a push')  

while True:
    print('welcome to BlackJack!, get as close as 21 as you can without goind more than 21\n\ Dealer hits until she reaches 17. Aces counts as 1 or 11 ') 
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())    

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:

        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value<=21:
        while dealer_hand.value<17:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value>21:
            dealer_busts(player_hand,dealer_hand,player_chips) 
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)  
        elif dealer_hand.value<player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    print('\n Players winning stand are:',player_chips.total)
    
    new_game= input('would you like to play again? Y or N)')
    if new_game[0].lower()=='y':
        playing = True
        continue
    else:
        print('Thanks for playing')
        break



