class Car:
    all_object = []
    def __init__(self,name:str,model:str,max_speed:int):
        assert len(name)>1 , "Please enter number in range 1990 to 2023"
        assert len(model)==4 , "Please enter number in range 1990 to 2023"
        assert max_speed>0 , "Please enter number greater than 0"
        self.__name = name
        self.__model = model
        self.__max_speed = max_speed
        Car.all_object.append(self)
        
    def __str__(self):
        return f"An object from {self.__class__.__name__} Class"  
    
    def __repr__(self):
        return f"\nName : {self.__name}, Model : {self.__model}, Max_Speed : {self.__max_speed}\n"
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    
car_1 = Car("Lamborghini","2020",230)
car_2 = Car("Benz","2020",230)
car_3 = Car("Bmw","2020",230)
car_4 = Car("Peride","2020",180)
car_5 = Car("Pars","2020",200)

print(Car)
car_1.name = "Ferrari"
print(car_1.name)