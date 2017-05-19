#! /usr/env/python3

import unittest

def thief(pin):
	"""get a four digit number an return a list, with lists of
		possible constelations of these numbers"""
	if len(str(pin)) == 4:
		liste = []
		nums = split(pin)
		for i in range(4):
			for h in range(4):
				for g in range(4):
					for j in range(4):
						liste.append([nums[i],nums[h], nums[g], nums[j]])
		return liste
	else:
		return "the pin must have four digits"


def split(number):
	""" split a number into a list, where each number has it's own index"""
	list = []
	number = str(number)
	for i in range(len(number)):
		list.append(int(number[i]))
	return list


class thiefTest(unittest.TestCase):
	def test_split(self):
		self.assertEqual(split(1234), [1,2,3,4])


if __name__ == '__main__':
	#unittest.main()
	pin = input('plz type in your four digit pin ')
	print(thief(pin))