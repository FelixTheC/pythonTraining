#! /usr/env/python3

def faktor(number):
	"""Get a real number and returns the faktor of it,
		if it is not it will return an exception error"""
	try:
		if number == 0:
			faktorOfNum = 1
		else:
			faktorOfNum = number
			while number != 1:
				number -= 1
				faktorOfNum += number
		return faktorOfNum
	except TypeError:
		return "Eingabe ist keine ganzzahlige Zahl"


if __name__ == '__main__':
	number = int(input('plz type in a number '))
	print(faktor(number))