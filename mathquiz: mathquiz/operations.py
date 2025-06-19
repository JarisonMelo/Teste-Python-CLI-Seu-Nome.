import operator

class Operation:
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def __call__(self, a, b):
        return self.func(a, b)

OPERATIONS = {
    "+": Operation("+", operator.add),
    "-": Operation("-", operator.sub),
    "*": Operation("*", operator.mul),
    "/": Operation("/", operator.truediv),
}
