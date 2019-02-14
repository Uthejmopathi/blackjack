import io
import random
import math
 #First here we have created some global variables
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11,}
playing = True

#Now create a class for card with two attributes suit and rank and we can print these two when called
class Card():
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank + " of " + self.suit

#This is to add all the numbers and symbols to make 52 cards. We did this by creating a empty list self.deck
#And then in that added using for loops. We can display the deck of cards using __str__() function
#
class Deck():
	def __init__(self):
		self.deck = []  # EMpty list
		for suit in suits:
			for rank in ranks: 
				self.deck.append(Card(suit,rank))

	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp += "\n" + card.__str__()
		return "Deck has : " + deck_comp

	def shuffle(self):
		random.shuffle(self.deck)

# We deal by popping that selected object and display it to the user
	def deal(self):
		single_card = self.deck.pop()
		return single_card




class Hand():
	def __init__(self):
		self.cards = []
		self.value =0
		self.aces = 0

	def add_card(self,card):
		self.cards.append(card)
		self.value += values[card.rank]

		if card.rank == 'Ace':
			self.aces += 1
#If Value is more than 21 and has ace in it then change the value to -10 and reduce the ace count as aces can either be 1 or 11
	def adjust_for_ace(self):
		while (self.value >21 and self.aces > 0):
			self.value -= 10
			self.aces -=1


class Chips():
	def __init__(self,total=100):
		self.total = total
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet


def take_bet(chips):
	while True:

		try:
			chips.bet = int(input("Enter the number of chips to bet: "))

		except ValueError:
			print("Wrongly entered. Enter a integer, not a letter you idiot")

		else:
			if chips.bet > chips.total:
				print("No chips left")
				print("You have only {}".format(chips.total)) 
			else:
				break


def hit(deck,hand):
	single_card = deck.deal()
	hand.add_card(single_card)
	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
	global playing

	while True:
		x = input("Enter either h for hit or s for stand  :  ")

		if x[0].lower() == 'h':
			hit(deck,hand)

		elif x[0].lower() == 's':
			print("Player Standing: ")
			playing = False

		else:
			print("Please Enter again: ")
			continue
		break

def show_some(player,dealer):
	print("Dealer's hand :  ")
	print("One card hidden")
	print(dealer.cards[1])
	print("\n")
	print("Player's hand :  ")
	for card in player.cards:
		print(card)

def show_all(player,dealer):
	print("Dealer's hand :  ")
	for card in dealer.cards:
		print(card)
	print("\n")
	print("Player's hand :  ")
	for card in player.cards:
		print(card)
	



def player_busts(dealer,player,chips):
	print("Player Lost and chips deducted")
	chips.lose_bet()

def player_wins(dealer,player,chips):
	print("Player Won and chips increased")
	chips.win_bet()

def dealer_busts(dealer,player,chips):
	print("Dealer Lost ")
	chips.win_bet()

def dealer_wins(dealer,player,chips):
	print("Dealer Won ")
	chips.lose_bet()

def push(dealer,player):
	print("Both have same total , TIE TIE.. Let's PUSH ")


while True:
	print("Welcome to Uthej's Casino for Blackjack")

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

		if player_hand.value > 21:
			player_busts(player_hand,dealer_hand,player_chips)


		break

	if player_hand.value <= 21:

		while dealer_hand.value < player_hand.value:
			hit(deck,dealer_hand)

		show_all(player_hand,dealer_hand)

		if dealer_hand.value > 21:
			dealer_busts(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value == player_hand.value:
			push(player_hand,dealer_hand)



	print("Total chips ar {}".format(player_chips.total))

	new_game = input("One more game Y or N? : ")
	if new_game[0].lower() == 'y':
		playing = True
		continue

	else:
		print("Thank you and Come back soon")
		break


'''

test_deck=Deck()
test_deck.shuffle()

test_player = Hand()
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)

'''























