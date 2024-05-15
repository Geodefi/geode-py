.. _creating_validators:

===================
Creating Validators
===================

.. warning::
    | **DEPRECATED**
    | We highly recommend using our new geodefi validator client ``Geonius`` instead of going through the above documentation.

Validators are created in 2 steps: `proposeStake()` and `stake()`

    1. proposeStake() will send 1 eth to beacon chain
    2. stake() will send 31 eth to beacon chain

Take a look at this: https://docs.geode.fi/operator-marketplace/a-validators-lifecycle

Any Staking Pool can work with any Operator. It is up to them choosing their own subset. This is done by the `delegate` function, and is observed with the `allowance` function.

0. Get Prepared
===============

Keep your `mnemonic` in mind
----------------------------

You can use a new mnemonic for every single pool, or you can use a one global mnemonic and increase its index over time. 
But, it is very important that you keep some consistency on your mnemonic usage, while keeping it safe.

Detect which pools you can stake for
------------------------------------

You can basically loop through all pools periodically and check the `allowance` function, or you can listen for `Delegation` event. It is totally up to you how you handle this.
However, keep in mind, other node operators racing with you to grab delegations every time pool `surplus` hits to 32 eth.

This is particularly important because proposeStake function can be called to propose multiple validators for one pool.
stake() function, on the other hand can be called with multiple validator pubkeys from mulitple pools.
These function calls will be kind of expensive. So, be wise spending your gas :)

> Pro tip: order your pubkeys according to their pools to save gas. For example use `[pool1, pool1, pool1, pool2, pool2, pool3]` instead of 
`[pool1, pool2, pool3, pool1, pool2, pool1].`


  .. code-block:: python
    
    # Delegation Event ABI:
    ...
        {
          "anonymous": false,
          "inputs": [
            {
              "indexed": false,
              "internalType": "uint256",
              "name": "poolId",
              "type": "uint256"
            },
            {
              "indexed": true,
              "internalType": "uint256",
              "name": "operatorId",
              "type": "uint256"
            },
            {
              "indexed": false,
              "internalType": "uint256",
              "name": "allowance",
              "type": "uint256"
            }
          ],
          "name": "Delegation",
          "type": "event"
        }
    ...

1. Create deposit-data: 
=======================

    * 1 eth for proposing
    * 31 eth for staking 

One of the most important thing here is to use pool's `withdrawal_contract` as `eth1_withdrawal_address`
This can be done easily by:

  .. code-block:: shell

    python3 ./staking_deposit/deposit.py existing-mnemonic --num_validators = {{number_of_proposal}} --amount = 1 --chain=holesky --eth1_withdrawal_address {{withdrawal_contract}}

    python3 ./staking_deposit/deposit.py existing-mnemonic --num_validators = {{number_of_proposal}} --amount = 31 --chain=holesky --eth1_withdrawal_address {{withdrawal_contract}}

2. Validate deposit-data: 
=========================

  .. code-block:: python

    from geode.utils.bls import validate_deposit_data_file
    from geode.globals import DEPOSIT_SIZE, Network
    propose_data_path="deposit_data/deposit_data-1691635838.json"
    stake_data_path="deposit_data/deposit_data-1691635870.json"

    # doesn't look for deposit_message_root and deposit_data_root issues as they are not used.
    validate_deposit_data_file(
        deposit_data_path=stake_data_path,
        amount=DEPOSIT_SIZE.STAKE,
        credential=myPool.withdrawalCredential[2:], # remove the 0x part 
        network= Network.holesky
    )

    validate_deposit_data_file(
        deposit_data_path=propose_data_path,
        amount=DEPOSIT_SIZE.PROPOSAL, 
        credential=myPool.withdrawalCredential[2:], # can also use Validator.withdrawalCredentials * if already actively validating validator *
        network= Network.holesky
    )

3. Prepare the data with provided functions 
===========================================

.. code-block:: python

    pubkeys1, sig1 = myPool.prepareProposeStake(deposit_data_path=propose_data_path)
    pubkeys31, sig31 = myPool.prepareStake(deposit_data_path=stake_data_path)

.. note:: 
    ``pub1`` should be same with the provided ``pub31``. Since they are actually used to deposit into the same validator. So, be careful about the `index` prompt while using existing-mnemonic.

.. py:method:: prepareProposeStake(deposit_data_path: str)

   * Signed Ether Amount: 1 ETH

   This method prepares for a validator proposal.
   It reads deposit data from a file path, validates it, and returns the ``public keys`` and ``signature`` for the proposal stake.


.. py:method:: prepareStake(deposit_data_path: str)

    * Signed Ether Amount: 31 ETH

    This function prepares a beacon stake by taking the path to a deposit data file as input.
    The deposit data file is validated by checking that it contains the required amount of Ether
    for the Beacon chain, that it is meant for the specified network, and that it is associated
    with the withdrawal credentials of the current operator.

    Once the deposit data has been validated, the function extracts the public keys and
    signatures from the deposit data and returns them as a tuple.

4. Propose!
===========
   
    .. code-block:: python

        portal.functions.proposeStake(myPool.ID, myOperator.ID, pubkeys1, sig1, sig31,).transact({"from": acct.address}) 

5. Wait until approval...
=========================

.. note::  It should take a day max. But, you can listen `VerificationIndexUpdated` event, which is emitted every time Oracle approves a batch of proposals. Or, simply check the `Portal.canStake(pubkey)` function periodically.

    .. code-block:: python

        # VerificationIndexUpdated Event ABI:
        ...
        {
        "anonymous": false,
        "inputs": [
            {
            "indexed": false,
            "internalType": "uint256",
            "name": "validatorVerificationIndex",
            "type": "uint256"
            }
        ],
        "name": "VerificationIndexUpdated",
        "type": "event"
        }
        ...

6. Stake!
=========

    .. code-block:: python

        portal.functions.stake(myOperator.ID, pubkeys1).transact({"from": acct.address})