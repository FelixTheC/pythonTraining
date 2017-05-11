#! /usr/env/python3
from temp import Temprature as t
from curency import Currency as c
from volume import Volume as v

def converter():
	"""convert for converting different types of subjects under each other
		types are = tempunits, currencyunits, volumeunits"""

	greetText = 'Hello and Welcome'
	infoText = "To quit insert 'q' or 'x', for help 'h' "
	tempInfo = "Tempature units: 'kelvin', 'celsius' and 'fahrenheit'"
	currencyInfo = "Currency units: 'euro', 'dollar', 'pfund' and 'yen'"
	volumeInfo = "Volume units: 'qm'-qudratmeter, 'qdm'-qudratdecimeter, 'qcm'-quadratcm,\ 'qmm'-quadratmillimeter"
	answerText = "your convertet value is "
	endText = "to try again hit 'r' or to quit hit 'q' "
	
	newValue = 0
	oldUnit = ""
	newUnit = ""
	temps = ['kelvin', 'celsius', 'fahrenheit']
	currens = ['euro', 'dollar', 'pfund', 'yen']
	volume = ['qm', 'qdm', 'qcm', 'qmm']
	print(greetText)

	while True:
		print(infoText)
		answer = input("to start hit 'r' and press 'enter' ")
		if answer.lower() == 'q' or answer.lower() == 'x':
			return False
		if answer.lower() == 'r':
			oldUnit = input('please type in your unit to covert from: ')
			if oldUnit.lower() == 'h':
				print( ' ', '')
				print(tempInfo, '')
				print(currencyInfo, '')
				print(volumeInfo, '')
				print(' ', '')
				oldUnit = input('please type in your unit to covert from: ')
			newUnit = input('please type in your unit to covert too: ')
			value = int(input('please type in your value'))

			if oldUnit in temps:
				if newUnit == temps[0]:
					newValue = t.toKelvin(oldUnit, value)
				elif newUnit == temps[1]:
					newValue = t.toCelsius(oldUnit, value)
				elif newUnit == temps[2]:
					newValue = t.toFahrenheit(oldUnit, value)
				else:
					newValue = -1

			if oldUnit in currens:
				if newUnit == currens[0]:
					newValue = c.toEuro(oldUnit, value)
				elif newUnit == currens[1]:
					newValue = c.toDollar(oldUnit, value)
				elif newUnit == currens[2]:
					newValue = c.toPfund(oldUnit, value)
				elif newUnit == currens[3]:
					newValue = c.toYen(oldUnit, value)
				else:
					newValue = -1

			if oldUnit in volume:
				if newUnit == volume[0]:
					newValue = v.toQm(oldUnit, value)
				elif oldUnit == volume[1]:
					newValue = v.toQdm(oldUnit, value)
				elif oldUnit == volume[2]:
					newValue = v.toQcm(oldUnit, value)
				elif oldUnit == volume[3]:
					newValue = v.toQmm(oldUnit, value)
				else:
					newValue = -1
		
		if int(newValue) == -1:
			print(newValue)
			print('there was an error with your input ')
			answer = input(endText)
		else:
			print(answerText+' '+ str(newValue))
			answer = input(endText)
			if answer.lower() == 'q':
				return False


if __name__ == "__main__":
	converter()
