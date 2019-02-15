#  Couple of things to remember before posting.
#  The name and handler must have the same name. The handler with .main,
#  must include runtime, python3.6


import json
import dragonchain_sdk
import base64

# DC_ID_ONE = 'DRAGONCHAIN_ID_HERE'
# AUTH_KEY_ID = 'PUT_IT_HERE'
# AUTH_KEY = 'PUT_IT_HERE'

# Setting a logger
dragonchain_sdk.set_stream_logger("dragonchain_sdk")
# client with your id.
dragonchain_client = dragonchain_sdk.client(
    dragonchain_id="385eb718-44e5-4407-b334-de1f2f6e3dac")  # fake id
# Grab the file to upload
# datafile = open("calculator2.zip", "rb")
# # Convert the file to base64
# code = base64.b64encode(datafile.read()).decode("utf8")

# tag = "calculator"
# handler = "calculator2.main"
# runtime = "python3.6"

txn_type = "calculator2"
name = txn_type
sc_type = "transaction"
payload = {
    "method": "multiplication",
    "parameters": {
        "numOne": 200,
        "numTwo": 6
    }
}


try:
    # Uncomment one after another
    # post_custom_contract = dragonchain_client.post_custom_contract(name, code, runtime, handlersc_type, True)
    # print(json.dumps(post_custom_contract,indent=4, sort_keys=True))
    # post_transaction = dragonchain_client.post_transaction(txn_type,payload)
    # print(json.dumps(post_transaction,indent=4, sort_keys=True))
    # query_transactions = dragonchain_client.query_transactions('invoker:"1222f388-a9, 55-4d32-a3af-002ee015b790"')
    # heap = dragonchain_client.get_sc_heap("sc_name", str("Ans"))
    # heap = dragonchain_client.list_sc_heap("main")
    # print(heap['response'])
    # print(json.dumps(heap,indent=4, sort_keys=True))
except TypeError as e:
    print({'error': str(e)})
