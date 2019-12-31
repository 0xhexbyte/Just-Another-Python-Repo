class compareAll:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


pt = compareAll(2, 3)
ot = compareAll(2, 3)
gt = compareAll(10, 20)
print(pt == ot)
print(gt < ot)  # We defined for greater than so python interpreter automatically understood for the less than operator
