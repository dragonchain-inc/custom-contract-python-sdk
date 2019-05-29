# Calculator Smart Contract Example (Python)

## Overview

* [Requirements](#requirements)
* [Authentication Requirements](#authentication-requirements)
* [Create a Smart Contract](#create-a-smart-contract)
* [Using Docker](#using-docker)
* [Post a Smart Contract](#post-a-smart-contract)
* [Post a Transaction](#post-a-transaction)
* [Query a Transaction](#query-a-transaction)
* [Heap](#heap)

### Requirements

> [Python SDK](https://pypi.org/project/dragonchain-sdk/)

* Must have python3 installed on the system
* Must have pip3 to download the dragonchain-sdk
* Have an Ide/editor like vscode from Microsoft to use or any editor you are comfortable with.

### Create a Smart Contract

```sh
git clone https://github.com/dragonchain-inc/custom-contract-python-sdk/tree/master
cd <project_name>
cd custom-contract-py
npm install
```

### Creating a Smart Contract

```bash
→ git clone <project_link>
→ cd <project_name>
→ cd custom-contract-py
→ pip3 install dragonchain-sdk
```

### Using Docker

```sh
docker build -t image_name.
docker push image_name
```

```py
New payload:
{'payload' {'version': '3', 'method': 'multiplication', 'parameters': {'numOne': 200, 'numTwo': 9}}}

# Results
{'Values': {'numOne': 3, 'numTwo': 3}, 'Ans': 9}
```

### Authentication requirements

* Click view chains and copy "ChainId"
* Locate "Generate New API Key": You will be given to two keys.
* Copy and paste the your keys below:

```py
import json
import dragonchain_sdk

client = dragonchain_sdk.Client(dragonchain_id='your_dc_id', auth_key_id='your_auth_id', auth_key='your_auth_key', endpoint='https://your_dc_id.api.dragonchain.com')
```

```py
response = dragonchain_client.post_contract(
    txn_type='calculator',
    image='image_name',
    cmd='python',
    args=['-m', 'main'],
    execution_order='parallel',
    # cron='* * * * *',
    # auth='<docker_auth_token_if_private_repository>'
)
```

### Create a Smart contract

```py
print(json.dumps(client.create_smart_contract(
    transaction_type='contract_name',
    image='image_name',
    cmd='node',
    args=['index.js'],
    execution_order='parallel',
    # registry_credentials='<docker_auth_token_if_private_repository>'
)))
```

### Create a Transaction

Here is how to post transction to your calculator

```py

print(dragonchain_client.create_transaction('example_contract', {
    'version': '1',
     "method": "multiplication",
     "parameters": {
        "numOne": 200,
        "numTwo": 6,
        }
    }
))

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

### Query a Transaction 

You can verify your transaction by calling query_transaction function

```py
print(dragonchain_client.query_transactions(lucene_query='your_query'))
```

#### Heap

> Dragonchain blockchain uses heap which stores data to the blockchain
What is a heap? A heap is a chain storage value where your smart contract state/data stored on the chain. Heap takes a (key, value). You can use the key to get data you stored on your blockchain. 
If you take a look at the calculator smart contract, you will notice that we are returning key value state/data. Example in the code:

```py
{
   "Values": {
    "numOne": parameters['numOne'],
    "numTwo": parameters['numTwo']
    },
   "multiplication": calculatorService.addition(parameters)
}
```

> The above key value is stored in the blockchain. To access the data, you do the following.
Keys: Values and Ans

```py
# Get single data from the heap
heap = dragonchain_client.get_smart_contract_object(key='transaction_or_smart_contract_name', smart_contract_id='multiplication') # returns the answer value

```

### How to register a Transaction

```py
# Register a transaction if you would like to just post transactions. Comment out post_custom_contract code
# Custom indexes can be used to query the transaction.
print(dragonchain_client.create_transaction_type(transaction_type='transaction_name', custom_indexes=[{
    'key': 'Unknown',
    'path': ''
}]))
```

### Post to your new Transaction

```py
print(dragonchain_client.create_transaction(transaction_type='transaction_name', payload='I am awesome'))

```