import json

class Calculator(object):
    def __init__(self, version, method, parameters, *args):
        self.method = method
        self.parameters = parameters

    def addition(self, numOne, numTwo):
    # The value here will be stored on the blockchain
        return int(numOne) + int(numTwo)

    def subtraction(self, numOne, numTwo):
        # The value here will be stored on the blockchain
        return int(numOne) - int(numTwo)

    def multiplication(self, numOne, numTwo):
        # The value here will be stored on the blockchain
        return int(numOne) * int(numTwo)

