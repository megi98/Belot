import random



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


	def marking_cards(self):

		sorted_deck = deck()                    #using the indexes of a sorted deck to mark our 8 cards with numbers
		mark_list = []

		for card in self.__cards:
			index_of_the_card = sorted_deck.index(card)
			mark_list.append(index_of_the_card)

		return sorted(mark_list)
		



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


def announcements():
	pass


