class RadarDragon:
	region1: int
	region2: int
	def __init__(self, region1: int, region2: int):
		self.region1= region1
		self.region2= region2	
	def buscar_esferas(self):
		if  (self.region1 + self.region2) == 7: 
			print("Encontraste todas las esferas")
		elif self.region1 + self.region2  < 7:
			print ("Tienes",self.region1 + self.region2, "Te faltan conseguir",  7-(self.region1+self.region2))

radar_bulma = RadarDragon(3,2)
print(radar_bulma.buscar_esferas())
