"""
    Dragonchain-inc
    Dragonchain custom smart contract in Python
"""

import service

def main(paylaod):
    print(paylaod['payload'])
    try:
        payload = paylaod['payload']
        method = payload['method']
        parameters = payload['parameters']

        # Check for the function you are trying to call.
        if method == "addition":
            # The blockchain expects a json data or response error
            return {
                "Values": {
                    "numOne": parameters['numOne'],
                    "numTwo": parameters['numTwo']
                },
                "addition": service.addition(parameters)
            }

        if method == "subtraction":
           # The blockchain expects a json data or response error
            return {
                "Values": {
                    "numOne": parameters['numOne'],
                    "numTwo": parameters['numTwo']
                },
                "subtraction": service.subtraction(parameters)}

        if method == "multiplication":
            # The blockchain expects a json data or response error
            return {
                "Values": {
                    "numOne": parameters['numOne'],
                    "numTwo": parameters['numTwo']
                },

                "multiplication": service.multiplication(parameters)
            }
    except TypeError as e:
        return {'error': str(e)}
