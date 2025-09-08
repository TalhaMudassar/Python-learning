class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def get_engine_info(self):
        # returns e.g. "150 HP Engine"
        return f"{self.horsepower} HP Engine"


class Vehicle:
    total_vehicles = 0   # class attribute

    def __init__(self, brand, model, engine: Engine):
        if not isinstance(engine, Engine):
            raise TypeError("engine must be an Engine instance")
        self.brand = brand
        self.model = model
        self.engine = engine

        # increment class counter
        Vehicle.total_vehicles += 1

        # default rental price
        self._rental_price = 0

    def get_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Engine: {self.engine.get_engine_info()}"

    @staticmethod
    def get_vehicle_type():
        return "Generic Vehicle"

    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles

    @property
    def rental_price(self):   # getter
        return self._rental_price

    @rental_price.setter
    def rental_price(self, value):   # setter
        if not isinstance(value, (int, float)):
            raise TypeError("rental_price must be a number")
        if value < 0:
            raise ValueError("Rental price cannot be negative.")
        self._rental_price = value


class Car(Vehicle):   # inheritance
    def __init__(self, brand, model, engine: Engine, seats):
        super().__init__(brand, model, engine)
        self.seats = seats

    def get_details(self):   # overriding parent method
        return f"{super().get_details()}, Seats: {self.seats}"


# --------- Usage ---------
engine1 = Engine(150)
car1 = Car("Toyota", "Corolla", engine1, 5)
car1.rental_price = 3000
print(car1.get_details())       # Brand: Toyota, Model: Corolla, Engine: 150 HP Engine, Seats: 5
print("Rental Price:", car1.rental_price)  # 3000

print("Vehicle Type:", Car.get_vehicle_type())  # Generic Vehicle
print("Total Vehicles:", Vehicle.get_total_vehicles())  # 1

