## Welcome to the Dragonchain code sample repository

> These code samples are an example of Dragonchain custom smart contract. You will be deploying a calculator2 smart contract and post some transactions.
There are currently two SDKs with more to come that can communicate with Dragonchain platform. Please go check out our SDKs for more information in the links below.

> [Python SDK](https://pypi.org/project/dragonchain-sdk/)


## How to test each custom smart contract locally
#### First clone the code

```bash
→ git clone <this_repo_link_here>
→ cd <into_this_repo_you_cloned>
```

#### Using the Python Dragonchain Smart Contract
> To be able to run your javascript code, please make sure you are inside your javascript directory.

```bash
→ cd custom-contract-py
→ ls 

calculator2.py calculator2Service.py
```


> In order to start building custom contract with third party libraries, you must run 

#### To test this example, run the following:
```bash
→ python3 calculator2.py

New payload:
{'method': 'multiplication', 'parameters': {'numOne': 3, 'numTwo': 3}}
{'Values': {'numOne': 3, 'numTwo': 3}, 'Ans': 9}
```

If your custom smart contract requires third party libraries, then you would need to add them in the root directy of the your custom smart contract.

#### Note: For custom Contract with additional dependencies [read about AWS Lambda Function](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)


#### At this point, zip your calculator2 with this files included only.

![Custom smart contract](https://github.com/dragonchain-inc/custom-contract-python-sdk/blob/master/assets/py.png)
```
calculator2.py calculator2Service.py
```


#### Change the values your key's values.

```py
DC_ID_ONE = 'DRAGONCHAIN_ID_HERE'
AUTH_KEY_ID = 'PUT_IT_HERE'
AUTH_KEY = 'PUT_IT_HERE'
```

#### Before posting the calculator2 custom smart contract, make sure that you have your calculator2.zip ready to upload. Your code should be under using_sdk_py root or reference it from anywhere.

It should look similar to this example.

```py
import json
import dragonchain_sdk

dragonchain_client = dragonchain_sdk.client(dragonchain_id=DC_ID_ONE)
# Grab the file to upload
datafile = open('calculator2Python.zip', 'rb') 
# Convert the file to base64
code = base64.b64encode(datafile.read()).decode('utf8')

```

#### Here is the payload to pass to the Dragonchain ```post_custom_contract```

```py
name = "calculator2"
code = "base64"
runtime = "python3.6"
sc_type = "transaction"
serial = True
handler = "handler.main"


post_custom_contract = dragonchain_client.post_custom_contract(name, code, runtime, sc_type, serial)
```

#### To use the Python SDK to post the calculator2 contract, run this command

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

#### Congratulations! :boom: :dragon:  You are one step away from posting your first transaction to your calculator2 smart contract

#### Here is how to post transction to your calulator
Before posting your transcation, comment out the     
```py


try:
    # post_custom_contract = dragonchain_client.post_custom_contract(name, code, handler runtime,sc_type, True)
    # print(json.dumps(post_custom_contract,indent=4, sort_keys=True))

except TypeError as e:
    print({'error': str(e)})
```

Then run this command.
```py

txn_type = "calculator2"
tag = "calculator2"

payload = {
    "method": "multiplication",
    "parameters": {
        "numOne": 3,
        "numTwo": 3
    }
}

try:
    post_transaction = dragonchain_client.post_transaction(txn_type,payload,tag)
    print(json.dumps(post_transaction,indent=4, sort_keys=True))
except TypeError as e:
    print({'error': str(e)})
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

heap = dragonchain_client.get_sc_heap("sc_name", str("Ans")) # returns the answer value

```