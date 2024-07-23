from vehicle import vehicle

class Car(vehicle):
    def __init__(self, num_person, get_air, vitesse, make, model, year, num_door, fuel_type):
        super().__init__(make, model,year, fuel_type)
        self.num_person = num_person
        self.get_air = get_air
        self.vitesse = vitesse
        self.num_door = num_door
    def get_num_door(self):
        print(self.num_door)
    def get_num_person(self):
        print(self.num_person)
    def get_air(self):
        print(True)
    def get_vitesse(self):
        print(self.vitesse)

    def all_info_Car(self):
        print("*************************************")
        print("INFORMATION ABOUT THIS CAR")
        print("*************************************")
        print("\nThe number of the door are : ", self.num_door)
        print("Number of person are : ", self.num_person)
        print("The car has air : ", self.get_air)
        print("Vitesse is : ", self.vitesse)

