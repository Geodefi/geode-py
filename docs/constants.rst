.. _constants:

Constants
=========

The Geode contants module contains commonly used values.

ZERO
****************

.. code-block:: python

    # The bytes(0) 
    geode.globals.constants.ZERO_BYTES 
    >> b''

    # The bytes32(0) value 
    geode.globals.constants.ZERO_BYTES32 
    >> b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    # The address(0) value 
    geode.globals.constants.ZERO_ADDRESS 
    >> "0x0000000000000000000000000000000000000000"
    

ETH-related
****************
.. code-block:: python

    #The amount of Gwei in one Ether
    geode.globals.constants.ETH2GWEI
    >> 1000000000

    # The denominator for calculations between beacon and mainnet
    geode.globals.constants.DENOMINATOR
    >> 10000000000 

    #The amount of Wei in one Ether
    geode.globals.constants.ETH
    >> 1000000000000000000

    #The amount of Wei in minimum deposit amount 1 Ether
    geode.globals.constants.MIN_DEPOSIT_AMOUNT
    >> 1000000000000000000

    #The amount of Wei in minimum deposit amount 32 Ether
    geode.globals.constants.MIN_DEPOSIT_AMOUNT
    >> 32000000000000000000   


Beacon Chain Execution specs
********************************
.. code-block:: python

    # Execution-spec constants taken from https://github.com/ethereum/consensus-specs/blob/dev/specs/phase0/beacon-chain.md
    geode.globals.constants.DOMAIN_DEPOSIT
    >> b'\x03\x00\x00\x00'

    geode.globals.constants.BLS_WITHDRAWAL_PREFIX
    >> b'\x00'

    geode.globals.constants.ETH1_ADDRESS_WITHDRAWAL_PREFIX
    >> b'\x01' 

Network
****************
.. code-block:: python

    # The seconds value of refresth rate of each request
    geode.globals.constants.REFRESH_RATE
    >> 60

    # The maximum try before raise exception
    geode.globals.constants.MAX_ATTEMPT
    >> 60

    # The second interval between tries
    geode.globals.constants.ATTEMPT_RATE
    >> 0.1 

