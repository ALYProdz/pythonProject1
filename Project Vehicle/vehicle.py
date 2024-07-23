class vehicle:
    def __init__(self, make, model, year, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type

    def get_make(self):
        print(self.make)

    def get_model(self):
        print(self.model)

    def get_year(self):
        print(self.year)


    def getfuelType(self):
        print(self.fuel_type)
        pass


    def vehicle_info(self):
        print("\n*************************************")
        print("INFORMATIONS ABOUT THIS VEHICLE ")
        print("*************************************")
        print("Vehicle's model  : ", self.model)
        print("Vehicle's brand  : ", self.make)
        print("Vehicle'year  : ", self.year)
        print("Fuel's type : ", self.fuel_type)
