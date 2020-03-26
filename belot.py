import random


class Card:

	def __init__(self, rank, suit):

		self.rank = rank
		self.suit = suit


	def __str__(self):

		return f'{self.rank}{self.suit}'


	def __repr__(self):

		return f'{self.rank}{self.suit}'



class Player:

	__cards = []

	def __init__(self, name):

		self.name = name


	def __str__(self):

		return f'{self.name}: {self.__cards}'


	def __repr__(self):

		return f'{self.name}: {self.__cards}'


	def receive_card(self, card):

		self.__cards.append(card)




class Team:

	def __init__(self, player1, player2):

		self.player1 = player1
		self.player2 = player2


	def __str__(self):

		newline = '\n'
		return f'{self.player1}{newline}{self.player2}'


	def __repr__(self):

		newline = '\n'
		return f'{self.player1}{newline}{self.player2}'



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





