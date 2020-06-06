class Adder:
    def __init__(self, number: int):
        self.number = number
    
    def __call__(self, other: int):
        return other + self.number



add_3 = Adder(3)
print(add_3(5))