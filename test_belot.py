import unittest
from belot import (Card, Player, Team, Game, deck)


class TestCard(unittest.TestCase):

	def test_string_representation(self):


		card1 = Card('K', 's')
		card2 = Card('10', 'd')
		
		expected1 = 'Ks'
		expected2 = '10d'

		self.assertEqual(str(card1), expected1)
		self.assertEqual(str(card2), expected2)


	def test_get_rank(self):

		card1 = Card('K', 's')
		card2 = Card('10', 'd')

		result1 = card1.get_rank()
		result2 = card2.get_rank()

		self.assertEqual(result1, 7)
		self.assertEqual(result2, 4)


	def test_get_suit(self):

		card = Card('K', 's')

		suit = card.get_suit()

		self.assertEqual(suit, 's')



class TestPlayer(unittest.TestCase):

	def test_receive_card(self):

		player = Player('name')
		card1 = Card('K', 'd')
		card2 = Card('10', 's')

		player.receive_card(card1)
		player.receive_card(card2)
		expected = 'name: [Kd, 10s]'

		self.assertEqual(str(player), expected)


	def test_for_carre(self):

		player = Player('name')
		player.receive_card(Card('K', 's'))
		player.receive_card(Card('K', 'd'))
		player.receive_card(Card('K', 'c'))
		player.receive_card(Card('K', 'h'))
		player.receive_card(Card('7', 's'))
		player.receive_card(Card('10', 'c'))
		player.receive_card(Card('A', 'h'))
		player.receive_card(Card('Q', 's'))

		result = player.announcements()

		self.assertEqual(result, [('carre', 7)])


	def test_for_tierce(self):

		player = Player('name')
		player.receive_card(Card('7', 'c'))
		player.receive_card(Card('8', 'c'))
		player.receive_card(Card('9', 'c'))
		player.receive_card(Card('K', 'h'))
		player.receive_card(Card('7', 's'))
		player.receive_card(Card('J', 'c'))
		player.receive_card(Card('A', 'h'))
		player.receive_card(Card('Q', 's'))

		result = player.announcements()

		self.assertEqual(result, ['tierce'])


	def test_for_quarte(self):

		player = Player('name')
		player.receive_card(Card('7', 'c'))
		player.receive_card(Card('8', 'c'))
		player.receive_card(Card('9', 'c'))
		player.receive_card(Card('10', 'c'))
		player.receive_card(Card('7', 's'))
		player.receive_card(Card('A', 'c'))
		player.receive_card(Card('A', 'h'))
		player.receive_card(Card('Q', 's'))

		result = player.announcements()

		self.assertEqual(result, ['quarte'])


	def test_for_quinte(self):

		player = Player('name')
		player.receive_card(Card('7', 'c'))
		player.receive_card(Card('8', 'c'))
		player.receive_card(Card('9', 'c'))
		player.receive_card(Card('10', 'c'))
		player.receive_card(Card('7', 's'))
		player.receive_card(Card('J', 'c'))
		player.receive_card(Card('A', 'h'))
		player.receive_card(Card('Q', 's'))

		result = player.announcements()

		self.assertEqual(result, ['quarte'])



class TestTeam(unittest.TestCase):

	pass


if __name__ == '__main__':
	unittest.main()



