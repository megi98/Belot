import random
from copy import deepcopy


class Card:

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit


    def __str__(self):

        return f'{self.rank}{self.suit}'


    def __repr__(self):

        return f'{self.rank}{self.suit}'


    def __eq__(self, other):

        return self.rank == other.rank and self.suit == other.suit
    

    def get_rank(self):

        if self.rank == '7':
            return 1
        elif self.rank == '8':
            return 2
        elif self.rank == '9':
            return 3
        elif self.rank == '10':
            return 4
        elif self.rank == 'J':
            return 5
        elif self.rank == 'Q':
            return 6
        elif self.rank == 'K':
            return 7
        else:
            return 8


    def get_suit(self):

        return self.suit


    
class Player:

    __cards = []

    def __init__(self, name):

        self.name = name


    def __str__(self):

        return f'{self.name}: {self.__cards}'


    def __repr__(self):

        return f'{self.name}: {self.__cards}'


    def get_name(self):

        return self.name


    def receive_card(self, card):

        self.__cards.append(card)


    def get_name(self):

        return self.name


    def show(self):

        print(self.__cards)
        return None

    def get_consecutiveness(self):

        consecutiveness = []
        
        carre = check_carre(self.__cards)

        copy_cards = deepcopy(self.__cards)

        if len(carre) != 0:
            for i in carre:
                for j in copy_cards:
                    if i[1] == j.get_rank():
                        copy_cards.remove(j)

        sort_cards(copy_cards)
        print(copy_cards)

        k = 0
        while k < len(copy_cards) - 1:

            check_consecutive = 1

            while copy_cards[k].get_rank() == (copy_cards[k+1].get_rank() - 1) and copy_cards[k].get_suit() == copy_cards[k+1].get_suit() and k < len(copy_cards) - 1:
                
                check_consecutive += 1
                k += 1
                if(k == len(copy_cards) - 1):
                    break

            consecutiveness.append((check_consecutive, copy_cards[k].get_rank()))
            k += 1

        return consecutiveness


    def announcements(self):
        carres = check_carre(self.__cards)
        consecutiveness = self.get_consecutiveness()   
        result = []

        for i in carres:
            result.append(i)

        for i in consecutiveness:
            if i[0] == 3:
                result.append('tierce ')
            if i[0] == 4:
                result.append('quarte ')
            if i[0] >= 5:
                result.append('quinte ')

        return result



class Team:

    def __init__(self, name, player1, player2):

        self.name = name
        self.player1 = player1
        self.player2 = player2


    def __str__(self):

        newline = '\n'
        return f'{self.name}:{newline}{self.player1}{newline}{self.player2}'


    def __repr__(self):

        newline = '\n'
        return f'{self.name}:{newline}{self.player1}{newline}{self.player2}'


    def get_player1(self):

        return self.player1.get_name()


    def get_player2(self):

        return self.player2.get_name()



class Game:

    __sequence = {}

    def __init__(self, team1, team2):

        self.team1 = team1
        self.team2 = team2

    def sequence(self):

        self.__sequence[self.team1.get_player1()] = 1
        self.__sequence[self.team2.get_player1()] = 2
        self.__sequence[self.team1.get_player2()] = 3
        self.__sequence[self.team2.get_player2()] = 4


    def __str__(self):

        newline = '\n'
        return f'{self.team1}{newline}{self.team2}{newline}{self.__sequence}'

    def __repr__(self):

        newline = '\n'
        return f'{self.team1}{newline}{self.team2}{newline}{self.__sequence}'


def deck():

    ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7']
    suits = ['c', 'd', 'h', 's']
    deck = []

    for rank in ranks:
        for suit in suits:
            deck.append(Card(rank,suit))

    return deck


def shuffle_deck():

    my_deck = deck()
    random.shuffle(my_deck)

    return my_deck 


def first_dealing(player, deck):

    for i in range(5):
        player.receive_card(deck[0])
        deck.pop(0)


def second_dealing(player, deck):

    for i in range(3):
        player.receive_card(deck[0])
        deck.pop(0)
        
        
def sort_cards(cards):

    n = len(cards)

    #sorting our cards by rank
    for i in range(n):
        for j in range(0, n-i-1):
            if cards[j].get_rank() > cards[j+1].get_rank():
                cards[j], cards[j+1] = cards[j+1], cards[j]

    #and then by suit
    for i in range(n):
        for j in range(0, n-i-1):
            if cards[j].get_suit() > cards[j+1].get_suit():
                cards[j], cards[j+1] = cards[j+1], cards[j]

    return cards


def check_carre(cards):

    carre = []

    for i in range(3,9):

        check_for_carre = 0

        for card in cards:
            if card.get_rank() == i:
                check_for_carre += 1

        carre.append((check_for_carre,i))

    have_carre = [] 

    for i in carre:
        if i[0] == 4:
            have_carre.append(('carre', i[1]))

    return have_carre

def game_type():
    
    types = ['All', 'None', 'c', 'd', 'h', 's']
    return random.choice(types)

def main():

    player1 = Player('player1')
    player2 = Player('player2')
    player3 = Player('player3')
    player4 = Player('player4')
    my_deck = deck()
    print(my_deck)
    my_deck = shuffle_deck()

    team1 = Team('Mecheta', player1, player2)
    team2 = Team('Koteta', player3, player4)
    game = Game(team1, team2)
    game.sequence()
    print(game)
    first_dealing(player1, my_deck)
    second_dealing(player1, my_deck)

    player1.show()

    print(player1.announcements())


if __name__ == "__main__":
    main()
