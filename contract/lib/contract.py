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
    print(payload["method"])

    try:
        method = payload["method"]
        parameters = payload["parameters"]

        # Check for the function you are trying to call.
        if method == "addition":
            # The blockchain expects a json data or response error
            return {
                "Values": {
                    "numOne": parameters["numOne"],
                    "numTwo": parameters["numTwo"],
                },
                "addition": addition(parameters),
            }

        if method == "subtraction":
            # The blockchain expects a json data or response error
            return {
                "Values": {
                    "numOne": parameters["numOne"],
                    "numTwo": parameters["numTwo"],
                },
                "subtraction": subtraction(parameters),
            }

        if method == "multiplication":
            # The blockchain expects a json data or response error
            return {
                "Values": {
                    "numOne": parameters["numOne"],
                    "numTwo": parameters["numTwo"],
                },
                "multiplication": multiplication(parameters),
            }
    except TypeError as e:
        return {"error": str(e)}
