# geodefi

geodefi is a Python library which makes it easier to interact with the blockchain networks that The Staking Library is available.
It provides a simple and intuitive interface for accessing blockchain data, executing smart contract functions, and managing blockchain transactions related to Geode's Trustless staking solution.

## Features

- Supports Ethereum mainnet, gnosis and testnet (Goerli) where The Protocol is deployed.
- Provides a simple and intuitive API for managing validators, operators, pools, tokens, and other smart contracts/modules
- Dynamically, adapts to contract updates (might require changing the abi files)
- Compatible with Python 3.7 and above

## Installation

Using pip:

```sh
pip install geodefi
```

Using setup.py:

```sh
python3 setup.py
```

## Usage

Here's a simple example of how to use Geode Library to interact with the Geode Finance Systems:

```python
from geode import Geode

#### STRONGLY RECOMMENDED TO SET THESE VARIABLES IN LOCAL ENVIROMENT
# Initialize a Geode instance with the Ethereum JSON-RPC endpoint
url = "https://mainnet.infura.io/v3/your-project-id"
# For Beacon functionalities
# get a key from https://beaconcha.in
consensus_key = "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

geode = Geode(exec_api=url, cons_key = consensus_key)
```

### Get A Pool

```python
# Get Pool from Portal
pid = 50016835115526216130031110555486827201953559012021267556883950029143900999178
myPool = geode.Portal.pool(pid)

print("NAME:",myPool.NAME)
print("CONTROLLER:",myPool.CONTROLLER)
print("initiated:",myPool.initiated)
print("maintainer:",myPool.maintainer)
print("surplus:",myPool.allowance(operator=myOperator.ID))
print("activeValidators:",myPool.activeValidators(operator=myOperator.ID))
```

### Get A Operator

```python
# Get Operator from Portal
oid = 114391297015478800753082638170652680401082080549997516459063441314156612391510
myOp = geode.Portal.operator(pid)

print("NAME:",myOp.NAME)
print("CONTROLLER:",myOp.CONTROLLER)
print("initiated:",myOp.initiated)
print("maintainer:",myOp.maintainer)
print("totalProposedValidators:",myOp.totalProposedValidators)
print("totalActiveValidators:",myOp.totalActiveValidators)
print("feeSwitch:",myOp.feeSwitch)
print("priorFee:",myOp.priorFee)
print("fee:",myOp.fee)
```

### Get A Validator

```python
# Get Validator from pool
myVal=myPool.validators(0)

# Validator state on execution layer
print("state:",myVal.state)
print("index:",myVal.index)
print("poolId:",myVal.poolId)
print("operatorId:",myVal.operatorId)
print("poolFee:",myVal.poolFee)
print("operatorFee:",myVal.operatorFee)

# Validator state on consensus layer
print("slashed:",myVal.slashed)
print("status:",myVal.status)
print("validatorindex:",myVal.validatorIndex)
print("withdrawalcredentials:",myVal.withdrawalCredentials)
print("total_withdrawals:",myVal.totalWithdrawals)
```

### Call functions of the Portal Contract

```python
# Call functions of the Portal Contract
Portal = geode.Portal
stakingParams = Portal.functions.StakingParams().call()
```

### Get the chain-specific internal Token

gETH on Ethereum, gGNO on gnosis etc.

```python
# Get gETH token with all functionalities
gETH = geode.Token
totalSupply = gETH.functions.totalSupply().call()
print(f"Total Supply: {totalSupply}")
```

# Documentation

Documentation for Geode is available on Read the Docs:
> put the link here

# Contributing

Contributions to Geode are welcome! Please see the contributing guidelines for more information.

# License

geodefi is licensed under MIT.
