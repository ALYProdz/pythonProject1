#Import the vehicle, Car and Moto module
from vehicle import vehicle
from Car import Car
from Moto import mi_Moto

#Create the first car and a vehicle
car1 = Car(23, True, "123 km/h","TOYOTA","BMW",2021,4, "Gazoline")

v1 = vehicle("Honda","CV", 2022,"Gaz")

#Verify the info 

car1.vehicle_info()
car1.all_info_Car()
v1.vehicle_info()

#Create a first Moto
m1 = mi_Moto(2,"125CC",2,"C13456","Blue and Black","Platina", "Baja",2024,"Gasoline")
m1.vehicle_info()
m1.moto_info()

#Create a second moto

m2 = mi_Moto(2,"250CC",5,"C45656","Red and Black","TVS", "Koss",2022,"Propane")
m2.moto_info()
