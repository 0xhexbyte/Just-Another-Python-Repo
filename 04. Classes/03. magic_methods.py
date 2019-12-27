# Magic methods are the ones which have two underscore at beginning and end of their name.
# These methods are called automatically by python interpreter.
# Google for 'python3 magic methods'.


class travel:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"({self.a},{self.b})"


me_go = travel(1, 1)
print(me_go)
