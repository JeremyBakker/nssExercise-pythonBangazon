import random

class Employee: 
	
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.restaurants = ["Local Taco", "Bobbie's Dairy Dip", "Miel", "Bajo Sexto", 
		"Caffee Nonna", "Coco's Italian Market"]

	def eat(self, food = False, companions = False):
		if food and companions == False:
			restaurant = "the office."
		else:
			restaurant = self.restaurants[random.randint(0,5)]

		if companions:
			companions = list(companions)

			if len(companions) == 1:
				companions = str(companions)
				companions_list = companions[2:-2]
			else:
				companions = str(companions)
				companions = companions[1:-1]
				companions_list = companions.replace("'", "")

		print("{} {} ate {} at {} with {}.".format(self.first_name, self.last_name, food, restaurant, companions_list))

