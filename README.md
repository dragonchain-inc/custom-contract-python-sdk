## Welcome to the Dragonchain code sample repository

> These code samples are an example of Dragonchain custom smart contract. You will be deploying a calculator2 smart contract and post some transactions.
There are currently two SDKs with more to come that can communicate with Dragonchain platform. Please go check out our SDKs for more information in the links below.

> [Python SDK](https://pypi.org/project/dragonchain-sdk/)

### System requirements
* Must have python3 installed on the system
* Must have pip3 to download the dragonchain-sdk

## How to test each custom smart contract locally
#### First clone the code

```bash
→ git clone <this_repo_link_here>
→ cd <into_this_repo_you_cloned>
```

#### Using the Python Dragonchain Smart Contract
> To be able to run your python code, please make sure you are inside your custom-contract directory.
Remember to uncomment the code below:

```py
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
```

```bash
→ cd custom-contract-py
```

> Then run it like:

```py
→ python3 calculator.py

New payload:
{'method': 'multiplication', 'parameters': {'numOne': 3, 'numTwo': 3}}
{'Values': {'numOne': 3, 'numTwo': 3}, 'Ans': 9}
```

If your custom smart contract requires third party libraries, then you would need to add them in the root directy of your custom smart contract.

#### Note: For custom Contract with additional dependencies [read about AWS Lambda Function](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)


#### At this point, zip your calculator with this files included only.

![Custom smart contract](https://github.com/dragonchain-inc/custom-contract-python-sdk/blob/master/assets/py.png)


#### Change the values of the right values with real values to work

```py
import json
import dragonchain_sdk
import base64

DC_ID_ONE = 'DRAGONCHAIN_ID_HERE'
AUTH_KEY_ID = 'PUT_IT_HERE'
AUTH_KEY = 'PUT_IT_HERE'

# Setting a logger
dragonchain_sdk.set_stream_logger('dragonchain_sdk')

# client with your id.
dragonchain_client = dragonchain_sdk.client(dragonchain_id=DC_ID_ONE)
dragonchain_client.override_credentials(AUTH_KEY, AUTH_KEY_ID)

# This zip file should be in the same directory
datafile = open('calculator.zip', 'rb')

# Convert the file to base64
code = base64.b64encode(datafile.read()).decode("utf8")

```

#### Before posting the calculator custom smart contract, make sure that you have your calculator.zip ready for upload. Your code should be under using_sdk_py root or reference it from anywhere

#### Here is the payload to pass to the Dragonchain ```post_custom_contract```

```py
# Payload data
tag = 'calculator'
handler = 'calculator.main'
runtime = 'python3.6'
txn_type = 'main'
name = txn_type
sc_type = 'transaction'

post_custom_contract = dragonchain_client.post_custom_contract(name, code, runtime, handler, sc_type, True)
print(json.dumps(post_custom_contract, indent=4, sort_keys=True))
```

#### To use the Python SDK to post the custom calculator contract, run this command

```bash
$ python3 index.py
{
    "ok": true,
    "response": {
        "success": "Contract creation in progress."
    },
    "status": 201
}
```

#### Here is how to post transction to your calculator
```py

# Post new transaction. Remember to comment out register_transaction_type code.
# Copy the returned transaction_id and paste to the function below
post_transaction = dragonchain_client.post_transaction(txn_type, payload)
print(json.dumps(post_transaction, indent=4, sort_keys=True))

```

```bash
$ python3 index.py

{
    "ok": true,
    "response": {
        "transaction_id": "5e1f1561-9a71-462e-b880-521899c10c24"
    },
    "status": 201
}
```


#### You can verify your transaction by calling the

```py

try:
    query_transactions = dragonchain_client.query_transactions('invoker:"5e1f1561-9a71-462e-b880-521899c10c24"')
    print(json.dumps(query_transactions,indent=4, sort_keys=True))
except TypeError as e:
    print({'error': str(e)})
```

#### How do you access your data in the blockchain?
> Dragonchain blockchain uses heap which stores data to the blockchain. 

>What is a heap? A heap is a chain storage value where your smart contract state/data stored on the chain. Heap takes a (key, value). You can use the key to get data you stored on your blockchain. 
If you take a look at the calculator smart contract, you will notice that we are returning key value state/data. Example in the code:
```py

"Values": {
    "numOne": parameters['numOne'],
    "numTwo": parameters['numTwo']
},
"Ans": calculatorService.addition(parameters)
}
```


> The above key value is stored in the blockchain. To access the data, you do the following.
Keys: Values and Ans
```py

# Get single data from the heap
heap = dragonchain_client.get_sc_heap("sc_name", str("Ans")) # returns the answer value

```
### How to register a Transaction

```py
# Register a transaction if you would like to just post transactions. Comment out post_custom_contract code
# Custom indexes can be used to query the transaction.
register_transaction = dragonchain_client.register_transaction_type('Your_Transaction_Name', custom_indexes=[{
    'key': 'Unknown',
    'path': ''
}])
```


#### Post to your new Transaction.

```py
post_transaction = dragonchain_client.post_transaction('Your_Transaction_Name', payload={"I am awesome"})
print(json.dumps(post_transaction, indent=4, sort_keys=True))
```
Congratulations! :boom: :dragon:  You have done it. Feel free to reach so we can improve our sdk. 