"""
    Dragonchain-inc
    Dragonchain custom smart contract

"""

# These actions can be taken out and put in a separate file.
# You can use Dragonchain sdk within your smart contract to perfrom advance operations.
# This is how you can leverage dragonchain's smart contract.
#-----------------------------------------------------------------------------------

#import json
#import os
#import time
#import datetime
#import dragonchain_sdk

# api = os.environ['API_KEY']
# sc_name = os.environ['SMART_CONTRACT_NAME']
# auth_key = os.environ['AUTH_KEY']
# auth_id = os.environ['AUTH_KEY_ID']
# dcid = os.environ['DRAGONCHAIN_ID']

# Event will have a paylaod.
from src.calculatorService import calculatorService

# Main entry
def main(event, context):
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


# For test only
# payload = {
#     "version": "1",
#     "txn_type": "calculator",
#     "payload": {
#         "method": "multiplication",
#         "parameters": {
#             "numOne": 10,
#             "numTwo": 3
#         }
#     }
# }
# result = main(payload, "")
# print(result)
