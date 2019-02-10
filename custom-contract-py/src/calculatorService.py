# These actions can be taken out and put in a separate file.

class CalculatorService:

    def addition(self, param): # The value here will be stored on the blockchain
        return (int(param['numOne']) + int(param['numTwo']))

    def subtraction(self, param):
        # The value here will be stored on the blockchain
        return (int(param['numOne']) - int(param['numTwo']))

    def multiplication(self, param):
        # The value here will be stored on the blockchain
        return (int(param['numOne']) * int(param['numTwo']))


calculatorService = CalculatorService()