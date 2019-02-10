#  Couple of things to remember before posting.
#  The name and handler must have the same name. The handler with .main, 
#  must include runtime, python3.6


import json
import dragonchain_sdk
import base64

# DC_ID_ONE = 'DRAGONCHAIN_ID_HERE'
# AUTH_KEY_ID = 'PUT_IT_HERE'
# AUTH_KEY = 'PUT_IT_HERE'

# client with your id.
dragonchain_client = dragonchain_sdk.client(dragonchain_id="385eb718-44e5-4407-b334-385eb718") # fake id
# Grab the file to upload
datafile = open("calculatorPython.zip", "rb") 
# Convert the file to base64
code = base64.b64encode(datafile.read()).decode("utf8")


txn_type = "calculatorPython"
tag = "calculator"
payload = {
    "payload": {
        "method": "multiplication",
        "parameters": {
            "numOne": 3,
            "numTwo": 3
        }
    }
}

try:
    # Uncomment one after another
    # post_custom_contract = dragonchain_client.post_custom_contract("calculatorPython", code, "python3.6","transaction", True)
    # print(json.dumps(post_custom_contract,indent=4, sort_keys=True))
    # post_transaction = dragonchain_client.post_transaction(txn_type,payload,tag)
    # print(json.dumps(post_transaction,indent=4, sort_keys=True))
    # query_transactions = dragonchain_client.query_transactions('invoker:"5e1f1561-9a71-462e-b880-521899c10c24"')
    # print(json.dumps(query_transactions,indent=4, sort_keys=True))

except TypeError as e:
    print({'error': str(e)})





