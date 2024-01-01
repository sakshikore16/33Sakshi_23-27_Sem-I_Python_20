# 7. Implement a class inheritance as following

class Devices:
    def __init__(self, brand, colour):
        self.brand = brand
        self.colour = colour

class Smartphone(Devices):
    def __init__(self, brand, colour, operating_system, model):
        super().__init__(brand, colour)
        self.operating_system = operating_system
        self.model = model

class Laptop(Devices):
    def __init__(self, brand, colour, processor, storage_capacity):
        super().__init__(brand, colour)
        self.processor = processor
        self.storage_capacity = storage_capacity

class SmartWatch(Devices):
    def __init__(self, brand, colour, waterproof, heartsensor):
        super().__init__(brand, colour)
        self.waterproof = waterproof
        self.heartsensor = heartsensor

smartphone = Smartphone("Samsung", "Black", "Android", "Galaxy S23 Ultra")
laptop = Laptop("Dell", "Silver", "Intel i7", "512GB SSD")
smartwatch = SmartWatch("Apple", "White", True, True)

print("Smartphone:", smartphone.__dict__)
print("Laptop:", laptop.__dict__)
print("Smartwatch:", smartwatch.__dict__)
