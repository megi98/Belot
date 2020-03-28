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


	def announcements(self):

		carre = []
		consecutiveness = []

		for i in range(3,9):

			check_for_carre = 0

			for card in self.__cards:
				if card.get_rank() == i:
					check_for_carre += 1

			carre.append((check_for_carre,i))

		#sorting our cards by rank
		for i in range(8):
			for j in range(0, 8-i-1):
				if self.__cards[j].get_rank() > self.__cards[j+1].get_rank():
					self.__cards[j], self.__cards[j+1] = self.__cards[j+1], self.__cards[j]

		#and then by suit
		for i in range(8):
			for j in range(0, 8-i-1):
				if self.__cards[j].get_suit() > self.__cards[j+1].get_suit():
					self.__cards[j], self.__cards[j+1] = self.__cards[j+1], self.__cards[j]

		print(self.__cards)

		k = 0
		while k < 7:

			check_consecutive = 1

			while self.__cards[k].get_rank() == (self.__cards[k+1].get_rank() - 1) and self.__cards[k].get_suit() == self.__cards[k+1].get_suit() and k < 7:
				
				check_consecutive += 1
				k += 1

			consecutiveness.append(check_consecutive)

			k += 1

		result = ''

		for i in carre:
			if i[0] == 4:
				result += f'carre {i[1]} '

		if result != '':
			return result

		for i in consecutiveness:
			if i == 3:
				result += 'tierce '
			if i == 4:
				result += 'quarte '
			if i >= 5:
				result += 'quinte '

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

