#! /usr/env/python3

from random import randint

def fruit_machine():
	"""a slot machine for terminal """
	#create a list with different symbols
	symbols = ['cherry', 'bell', 'lemon', 'orange', 'star', 'skull']
	credit = 1 # the start credit
	#three rolls all using the same symbol
	roll1 = symbols
	roll2 = symbols
	roll3 = symbols
	quit = False

	while credit > 0 or quit:
		print('%2.2f' % (credit))
		credit -= 0.2	# every turn will cost 0.20
		symbol1 = roll1[randint(0,5)]
		symbol2 = roll2[randint(0,5)]
		symbol3 = roll2[randint(0,5)]
		if symbol1 == symbol2 or symbol1 == symbol3 or symbol2 == symbol3:
			if symbol1 == 'skull' and symbol2 == 'skull' or (symbol2 == 'skull' and symbol3 == 'skull'):
				credit = credit - 1.0
				symbole = [symbol1, symbol2, symbol3]
			else:
				credit = credit + 0.5
				symbole = [symbol1, symbol2, symbol3]
			print(symbole)
			quit = play_again()
			if quit:
				if credit >= 0:
					print("you will get back %2.2f" % (credit))
				break

		#three skulls mean game over
		if symbol1=='skull' and symbol2=='skull' and symbol3 == 'skull':
			credit == 0
			symbole == [symbol1, symbol2, symbol3]
			print(symbole)
			print('Game Over')
			break

		if symbol1 == symbol2 and symbol1 == symbol3:
			if symbol1=='bell' and symbol2 == 'bell' or (symbol1=='bell' and symbol3 == 'bell'):
				credit = credit + 5.0
				quit = play_again()
				if quit:
					print("you will get back %2.2f" % (credit))
					break
			else:
				credit = credit + 1.0
				quit = play_again()
				if quit:
					print("you will get back %2.2f" % (credit))
					break
		if symbol1 != symbol2 and symbol1 != symbol3 and symbol2 != symbol3:
			symbole = [symbol1, symbol2, symbol3]
			print(symbole)
			quit = play_again()
			if quit:
				print("you will get back %2.2f" % (credit))
				break


def play_again():
	quit = input('noch eine spiel y/n ')
	end = True
	if quit == 'n':
		end = True
	elif quit == 'y':
		end = False
	else:
		end = True
	return end


if __name__ == "__main__":
	print(fruit_machine())