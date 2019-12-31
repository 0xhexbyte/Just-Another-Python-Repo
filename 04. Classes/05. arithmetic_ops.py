class operate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return operate(self.x+other.x, self.y+other.y)


op1 = operate(1, 1)
op2 = operate(2, 2)
res_op = op1+op2
print(res_op)
print(res_op.x)
