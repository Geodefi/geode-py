.. _constants:

Constants
==========

The Geodefi contants module contains commonly used values.

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

    # The amount of Gwei in one Ether = 1e9
    geode.globals.constants.ETH2GWEI
    >> 1000000000

    # beacon to mainnet conversion rate = 1e9
    geode.globals.constants.BEACON_DENOMINATOR
    >> 1000000000

    # The denominator for calculations within geodefi packages = 1e10
    # DENOMINATOR = 1 or 100%.
    # Such as, 10% = DENOMINATOR/10
    geode.globals.constants.PERCENTAGE_DENOMINATOR
    >> 10000000000 

    # The amount of Wei in one Ether = 1e18
    geode.globals.constants.ETHER_DENOMINATOR
    >> 1000000000000000000

    #The amount of Wei in minimum deposit amount = 2**0 * ETHER_DENOMINATOR
    geode.globals.constants.MIN_DEPOSIT_AMOUNT
    >> 1000000000000000000

    #The amount of Wei in minimum deposit amount = 2**5 * ETHER_DENOMINATOR
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

    # The maximum try before raise exception 
    geode.globals.constants.MAX_ATTEMPT
    >> 10

    # The seconds value of refresh rate of the internal cache (s)
    geode.globals.constants.REFRESH_RATE
    >> 60

    # The interval between tries (s)
    geode.globals.constants.ATTEMPT_RATE
    >> 0.1 

