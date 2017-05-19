#! /usr/env/python3

import unittest

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



class FaktorTest(unittest.TestCase):
	
	def test_faktor_null(self):
		self.assertEqual(faktor(0),1)

	def test_Faktor(self)
		self.assertEqual(Faktor(3),6)

	def test_faktor_exception(self):
		self.assertTrue(faktor("1"))



if __name__ == '__main__':
	#unittest.main()
	number = int(input('plz type in a number '))
	print(faktor(number))



		