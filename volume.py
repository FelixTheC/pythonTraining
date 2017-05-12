#! /usr/env/python3

class Volume():
	"""converting qudrat-meter, -dm/liter, -cm, -mm, under each other"""

	def toQm(volume, value):
		meter = 0
		if volume == 'qmm':
			meter = value /(1000**3)
		elif volume == 'qcm':
			meter = value /(1000**2)
		elif volume == 'qdm' or volume == 'liter':
			meter = value / 1000
		return format(meter, '.10f')

	
	def toQdm(volume, value):
		meter = 0
		if volume == 'qmm':
			meter = value / (1000**2)
		elif volume == 'qcm':
			meter = value / 1000
		elif volume == 'qm':
			meter = value * 1000
		return format(meter, '.6f')


	def toQcm(volume, value):
		meter = 0
		if volume == 'qmm':
			meter = value / 1000
		elif volume == 'qm':
			meter = value * (1000**2)
		elif volume == 'qdm' or volume == 'liter':
			meter = value * 1000
		return format(meter, '.2f')

	def toQmm(volume, value):
		meter = 0
		if volume == 'qm':
			meter = value * (1000**3)
		elif volume == 'qdm' or volume == 'liter':
			meter = value * (1000**2)
		elif volume == 'qcm':
			meter = value * 1000
		return format(meter, '.2f')