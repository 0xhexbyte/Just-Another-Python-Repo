class weird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# Here the cls parameter in the zero function is referring to the particular class and is same as initiating an object such as:
# weird_var = weird(0,0)
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def show(self):
        print(f"Value = {self.x}, {self.y}")


sample = weird.zero()
sample.show()
