#! /usr/env/python3

class Currency():
	"""convert euro, dollar, pfund and yen to each other"""

	def toEuro(currency, value):
		if currency.lower() == 'dollar':
			euro = value * 0.9
		elif currency.lower() == 'pfund':
			euro = value * 1.1887
		elif currency.lower() == 'yen':
			euro = value * 124.2085
		return format(euro, '.2f')

	def toDollar(currency, value):
		if currency.lower() == 'euro':
			dollar = value * 0.918
		elif curreny.lower() == 'pfund':
			dollar = value * 0.7732
		elif currency.lower() == 'yen':
			dollar = value * 114
		return format(dollar, '.2f')

	def toPfund(currency, value):
		if currency.lower() == 'euro':
			dollar = value * 0.8413
		elif curreny.lower() == 'dollar':
			dollar = value * 1.2993
		elif currency.lower() == 'yen':
			dollar = value * 147.684
		return format(dollar, '.2f')

	def toYen(currency, value):
		if currency.lower() == 'euro':
			dollar = value * 0.00805
		elif curreny.lower() == 'pfund':
			dollar = value * 0.00677
		elif currency.lower() == 'dollar':
			dollar = value * 0.0087
		return format(dollar, '.2f')