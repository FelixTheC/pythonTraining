#! /usr/env/python3
class Temprature():
	
	def toKelvin(einheit, grad):
		if einheit == 'celsius':
			kelvin = int(grad) + 273.15
		elif einheit == 'fahrenheit':
			kelvin = (grad + 459.67)/1.8
		else:
			kelvin = 0
		return kelvin

	def toCelsius(einheit, grad):
		if einheit == 'kelvin':
			celsius = int(grad) - 273.15
		elif einheit == 'fahrenheit':
	 		celsius = (grad/1.8) - 32
		else:
			celsius = 0
		return celsius

	def toFahrenheit(einheit, grad):
		if einheit == 'celsius':
			fahrenheit = (grad * 1.8) + 32
		elif einheit == 'kelvin':
			fahrenheit = (grad * 1.8) - 459.67
		else:
			fahrenheit = 0
		return fahrenheit