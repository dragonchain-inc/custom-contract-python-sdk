"""
    Dragonchain-inc
    Dragonchain custom smart contract in Python
"""

from .calculator import Calculator
import json


def handler(payload):
    try:
        j = json.loads(payload)["payload"]
        calculator = Calculator(**j)
        method = calculator.method
        parameters = calculator.parameters

        # Check for the function you are trying to call.
        if method == "addition":
            # The blockchain expects a json data or response error
            return {
                "Params": {
                    "numOne": parameters["numOne"],
                    "numTwo": parameters["numTwo"],
                },
                "addition_ans": calculator.addition(
                    parameters["numOne"], parameters["numTwo"]
                ),
                "tag": "addition",
            }

        if method == "subtraction":
            # The blockchain expects a json data or response error
            return {
                "Params": {
                    "numOne": parameters["numOne"],
                    "numTwo": parameters["numTwo"],
                },
                "subtraction_ans": calculator.subtraction(
                    parameters["numOne"], parameters["numTwo"]
                ),
                "tag": "subtraction",
            }

        if method == "multiplication":
            print(parameters["numOne"])
            print(parameters["numTwo"])

            # The blockchain expects a json data or response error
            return {
                "Params": {
                    "numOne": parameters["numOne"],
                    "numTwo": parameters["numTwo"],
                },
                "Ans": calculator.multiplication(
                    parameters["numOne"], parameters["numTwo"]
                ),
                "tag": "multiplicaiton",
            }
    except TypeError as e:
        return {"error": str(e)}
