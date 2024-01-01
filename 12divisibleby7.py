# 12. Define class with a generator which can iterate the numbers, 
# which are divisible by 7, between a given range 0 and n.

class Divisible7:
    def __init__(self, n):
        self.n = n

    def generate_numbers(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i

n = int(input("Enter the value for 'n' : "))

generator_instance = Divisible7(n)

print(f"Numbers divisible by 7 between 0 and {n}:")
for num in generator_instance.generate_numbers():
    print(num)
