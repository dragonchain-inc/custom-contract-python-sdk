# Calculator Smart Contract Example (Python)

## This short tutorial aims to answer the following

* [Requirements](###Requirements)
* [Authentication Requirements](###Authentication-Requirements)
* [Creating a Smart Contract](###Creating-a-Smart-Contract)
* [Using Docker](###Using-Docker)
* [Posting a Smart Contract](###Posting-a-Smart-Contract)
* [Post a Transaction](###Post-a-Transaction)
* [Query a Transaction](###Query-a-Transaction)
* [Heap](###Heap)

### Requirements

> [Dragonchain Python SDK](https://pypi.org/project/dragonchain-sdk/)

* Must have python3 installed on the system
* Must use pip3 to download the dragonchain-sdk

### Creating a Smart Contract

```bash
→ git clone <project_link>
→ cd <project_name>
→ cd custom-contract-py
→ pip3 install dragonchain-sdk
```

### Using Docker

```bash
→ docker build -t <docker_username>/<contract_name> .
→ docker push <docker_username>/<contract_name>:<latest>
```

### Authentication Requirements

Create file called index.py and add the code below

```python
dragonchain_client = dragonchain_sdk.Client('<DC_ID>', '<AUTH_KEY>''AUTH_KEY_ID')
```

### Post Smart Contract

```py
response = dragonchain_client.post_contract(
    txn_type='calculator',
    image='taban/calculator_contract:<latest>',
    cmd='python',
    args=['-m', 'main'],
    execution_order='parallel',
    # cron='* * * * *',
    # auth='<docker_auth_token_if_private_repository>'
)
```

### Post a Transaction

You can verify your transaction by calling query_transaction function

```py
txn_type = 'calculator'
payload = {
    'method': 'multiplication',
    'parameters': {
        'numOne': 200,
        'numTwo': 6
        }
    }
}

# Post new transaction
post_transaction = dragonchain_client.post_transaction(txn_type, payload)
```

### Query a Transaction

```py
# Grab the transaction id from the response above and use it to query the transaction
query_transactions = dragonchain_client.query_transactions('txn_id:"5e1f1561-9a71-462e-b880-521899c10c24"')
print(query_transaction)
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
heap = dragonchain_client.get_sc_heap("contract_name", str("multiplication")) # returns the answer value
```