"""
    Dragonchain-inc
    Dragonchain custom smart contract

"""
import os
# from calculatorService 
calculatorService = os.path.abspath(os.path.dirname("calculatorService"))


# Entry point


def main(event, context):
    # Event will have a paylaod.
    print("New payload: ")
    print(event['payload'])

    try:
        payload = event['payload']
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
                "Ans": calculatorService.addition(parameters)
            }

        if method == "subtraction":
           # The blockchain expects a json data or response error
            return {
                "Values": {
                    "numOne": parameters['numOne'],
                    "numTwo": parameters['numTwo']
                },
                "Ans": calculatorService.subtraction(parameters)}

        if method == "multiplication":
            # The blockchain expects a json data or response error
            return {
                "Values": {
                    "numOne": parameters['numOne'],
                    "numTwo": parameters['numTwo']
                },
                "Ans": calculatorService.multiplication(parameters)
            }

    except TypeError as e:
        return {'error': str(e)}

payload = {
    "version": "1",
    "txn_type": "calculator",
    "payload": {
        "method": "multiplication",
        "parameters": {
            "numOne": 3,
            "numTwo": 3
        }
    }
}

result = main(payload, "")
print(result)