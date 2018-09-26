#Class that describes the game
from player import Player
from card import Card
import random

class Gameplay():

    def __init__(self):
        self.players = [Player('Dealer - Computer')]
        self.carddeck = []

        for i in [2,3,4,5,6,7,8,9,"J","Q","K","A"]:
            for c in ['♠', '♣', '♥', '♦']:
                self.carddeck.append(Card(i, c))
        print(''*5)
        print('Witaj w Blackjack!')

#dopisac test!
    def pick_a_card(self):
        card = self.carddeck[random.randint(0,len(self.carddeck)-1)]
        while card.taken == True:
            card = self.carddeck[random.randint(0,len(self.carddeck)-1)]
        card.taken = True
        return card


    def deal_cards(self):
        self.players[0].cards.append(self.pick_a_card())
        self.players[1].cards.append(self.pick_a_card())
        self.players[0].cards.append(self.pick_a_card())
        self.players[1].cards.append(self.pick_a_card())
        self.players[0].cards[1].covered = True


    def calculate_score(self):
        for p in self.players:
            p.calculate_score()


    def print_table(self):
        self.calculate_score()
        print(''*2)
        print(self.players[0].name + ", " + str(self.players[0].score))
        print(self.players[0].print_cards())
        print()
        print(self.players[1].name + ", " + str(self.players[1].score))
        print(self.players[1].print_cards())
        print(''*2)


    def hit(self, player):
        player.cards.append(self.pick_a_card())
    

    def play(self):
        self.players.append(Player(input('Podaj swoje imie: ')))

        q = input(self.players[1].name + ', czy chcesz rozpoczac gre? (T/N)')
        if q.lower() != 't':
            return

        print(''*3)
        print('Gramy!')

        self.deal_cards()
        self.print_table()

        q = input('Enter your choice: (H - hit, S - stand)')

        while q.lower() == 'h':
            self.hit(self.players[1])
            self.print_table()
            q = input('Enter your choice: (H - hit, S - stand)')

        self.players[0].reveal_cards()
        self.print_table()
