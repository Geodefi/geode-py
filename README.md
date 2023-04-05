# Geode

Geode is a Python library for interacting with blockchain networks. It provides a simple and intuitive interface for accessing blockchain data, executing smart contract functions, and managing blockchain transactions related to Geode Finance.

## Features

- Supports Ethereum mainnet and testnets (Goerli and Gnosis)
- Provides a simple and intuitive API for managing Geode Finance validators, operators, pools, tokens, and other smart contracts
- Dynamically, adapts to contract updates
- Compatible with Python 3.6 and above

## Installation

You can install Geode using pip:

```sh
pip install geode
```

## Usage

Here's a simple example of how to use Geode Library to interact with the Geode Finance Systems:

```python
from geode import Geode

#### STRONGLY RECOMMENDED TO SET THESE VARIABLES IN LOCAL ENVIROMENT
# Initialize a Geode instance with the Ethereum JSON-RPC endpoint
url = "https://mainnet.infura.io/v3/your-project-id"
# For Beacon functionalities
consensus_key = "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


geode = Geode(exec_api=url, cons_key = consensus_key)
```

### Get Pool

```python
# Get Pool
pid = 50016835115526216130031110555486827201953559012021267556883950029143900999178
myPool = geode.Portal.pool(pid)

print("NAME:",myPool.NAME)
print("CONTROLLER:",myPool.CONTROLLER)
print("initiated:",myPool.initiated)
print("maintainer:",myPool.maintainer)
print("surplus:",myPool.surplus)
```

### Call functions of the Portal Contract

```python
# Call functions of the Portal Contract
Portal = geode.Portal
name = Portal.functions.readBytesForId(pid, toBytes32("NAME")).call()
```

### Get the Token

```python
# Get gETH token with all functionalities
gETH = geode.Token
totalSupply = gETH.contract.functions.totalSupply().call()
print(f"Total Supply: {totalSupply}")
```

# Documentation

Documentation for Geode is available on Read the Docs.

# Contributing

Contributions to Geode are welcome! Please see the contributing guidelines for more information.

# License

Geode is licensed under the MIT License.
