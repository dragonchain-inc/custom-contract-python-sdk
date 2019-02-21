import json
import dragonchain_sdk
import base64


'''
    This is another way to run this code if you wish to go a little advanced.

    dragonchain_client = dragonchain_sdk.client()

    The code above works only if you have a file ~/.dragonchain/credentials on your local computer. 
    Check the README.md

'''


'''
    For this tutorial, you can paste your Dragonchain keys below.
'''

DC_ID_ONE = 'DRAGONCHAIN_ID_HERE'
AUTH_KEY_ID = 'PUT_IT_HERE'
AUTH_KEY = 'PUT_IT_HERE'
dragonchain_client = dragonchain_sdk.client(dragonchain_id=DC_ID_ONE)
dragonchain_client.override_credentials(AUTH_KEY, AUTH_KEY_ID)

# Setting a logger
dragonchain_sdk.set_stream_logger('dragonchain_sdk')
# This zip file should be in the same directory
datafile = open('calculator.zip', 'rb')
# # Convert the file to base64
code = base64.b64encode(datafile.read()).decode("utf8")

# Payload data
tag = 'calculator'
handler = 'calculator.main'
runtime = 'python3.6'
txn_type = 'main'
name = txn_type
sc_type = 'transaction'
payload = {
    'method': 'multiplication',
    'parameters': {
        'numOne': 200,
        'numTwo': 6
    }
}

try:
    # Uncomment one after another

    # Before posting payload to create custom smart contract, make sure that everything is good
    # post_custom_contract = dragonchain_client.post_custom_contract(name, code, runtime, handler, sc_type, True)
    # print(json.dumps(post_custom_contract, indent=4, sort_keys=True))

    # # Register a transaction if you would like to just post transactions. Comment out post_custom_contract code
    # register_transaction = dragonchain_client.register_transaction_type('Your_Transaction_Name', custom_indexes=[{
    #     'key': 'Unknown',
    #     'path': ''
    # }])

    # Post new transaction. Remember to comment out register_transaction_type code.
    # Copy the returned transaction_id and paste to the function below
    # post_transaction = dragonchain_client.post_transaction(txn_type, payload)
    # print(json.dumps(post_transaction, indent=4, sort_keys=True))

    #  Get the transaction_id above and comment out createTransaction code.
    # query_transactions = dragonchain_client.query_transactions('invoker:"ed487119-673f-47a8-ab87-c14e23ec8551"')
    # print(json.dumps(query_transactions, indent=4, sort_keys=True))

    # # Get data of your calculator smart contract. Ans is the key for the answer.
    # heap = dragonchain_client.get_sc_heap('calculator', str('Ans'))
    # print(json.dumps(heap, indent=4, sort_keys=True))

    query_transactions = dragonchain_client.query_contracts('*')
    print(json.dumps(query_transactions, indent=4, sort_keys=True))

except TypeError as e:
    print({'error': str(e)})
