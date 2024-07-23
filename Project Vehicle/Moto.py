from vehicle import vehicle


class mi_Moto(vehicle):
    def __init__(self, num_wheels, motorcycleType, Qt_passenger,matriculation, color, make, model, year, fuel_type):
        super().__init__(make, model, year, fuel_type)
        self.num_wheels = num_wheels
        self.motorcycleType = motorcycleType
        self.Qt_passenger = Qt_passenger
        self.matriculation = matriculation
        self.color = color

    def get_num_wheels(self):
        print(self.num_wheels)

    def get_motorcycleType(self):
        print(self.motorcycleType)

    def get_qt_passenger(self):
        if self.Qt_passenger > 2:
            print("This moto an take only two passengers")
        else:
            print(self.Qt_passenger)



    def get_matricul(self):
        print(self.matriculation)

    def get_color(self):
        print(self.color)

    def moto_info(self):
        print("********************************")
        print("Moto information")
        print("********************************")
        print("Moto's color :", self.color)
        print("Moto's matricule : ",self.matriculation)
        print("Take only : ", self.get_qt_passenger(),"passengers.")
        print("Qt's Wheels : ", self.num_wheels)
        print("Moto's brand : ", self.make)
        print("Moto's model : ",self.model)
        print("Moto's years : ", self.year)
        print("Moto's fuel : ", self.fuel_type)



