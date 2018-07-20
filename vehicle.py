#vehicle
class vehicle:
	speed=0
	def __init__(self,wheels):
		self.wheels=wheels
		if(self.wheels>=4):
			print('big vehicle')
		else:
			print('two wheeler')
	def start(self):
		vehicle.speed=vehicle.speed+20
		print(vehicle.speed)
	def accelert(self,increase):
			vehicle.speed=vehicle.speed+increase
			print(vehicle.speed)
			if(vehicle.speed>120):
				print('speed limit xceded ,applying brake')
				self.brake(vehicle.speed-120)
	def brake(self,dec):
		vehicle.speed=vehicle.speed-dec
		if(vehicle.speed<0):
			vehicle.speed=0
		print(vehicle.speed)
bike=vehicle(2)
bike.start()
bike.accelert(20)
bike.brake(80)
bike.accelert(130)