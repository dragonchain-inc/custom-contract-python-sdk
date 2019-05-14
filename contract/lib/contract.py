"""
    Dragonchain-inc
    Dragonchain custom smart contract in Python
"""
def addition(param):
    # The value here will be stored on the blockchain
    return int(param["numOne"]) + int(param["numTwo"])

def subtraction(param):
    # The value here will be stored on the blockchain
    return int(param["numOne"]) - int(param["numTwo"])

def multiplication(param):
    # The value here will be stored on the blockchain
    return int(param["numOne"]) * int(param["numTwo"])


def handler(payload):
    try:
        method = payload["method"]
        parameters = payload["parameters"]

        # Check for the function you are trying to call.
        if method == "addition":
            # The blockchain expects a json data or response error
            return {
                "Params": {
                    "numOne": parameters["numOne"],
                    "numTwo": parameters["numTwo"],
                },
                "addition_ans": addition(parameters),
                "tag": "addition"

            }

        if method == "subtraction":
            # The blockchain expects a json data or response error
            return {
                "Params": {
                    "numOne": parameters["numOne"],
                    "numTwo": parameters["numTwo"],
                },
                "subtraction_ans": subtraction(parameters),
                "tag": "subtraction"

            }

        if method == "multiplication":
            # The blockchain expects a json data or response error
            return {
                "Params": {
                    "numOne": parameters["numOne"],
                    "numTwo": parameters["numTwo"],
                },
                "Ans": multiplication(parameters),
                "tag": "multiplicaiton"
            }
    except TypeError as e:
        return {"error": str(e)}
