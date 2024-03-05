.. _beacon:

======
Beacon 
======

.. py:module:: Beacon
.. py:currentmodule:: Beacon

.. contents:: :local:
    
.. py:class:: geodefi.Beacon

Allows user to query beaconchain data, with respect to the `provided api specification. <https://ethereum.github.io/beacon-APIs/?urls.primaryName=v2.4.0>`_
 
.. code-block:: python

    beacon = geode.beacon
    beacon.beacon_genesis()
    # {
    # 'genesis_time': '1695902400',
    # 'genesis_validators_root': '0x9143aa7c615a7f7115e2b6aac319c03529df8242ae705fba9df39b79c59fa8b1',
    # 'genesis_fork_version': '0x01017000'
    # }

API Requests
------------

.. note:: depending on your API provider's consensus client's version, some calls might fail.

.. py:method:: beacon_genesis()

.. py:method:: beacon_states_root(state_id: str)

.. py:method:: beacon_states_fork(state_id: str)

.. py:method:: beacon_states_finality_checkpoints(state_id: str)

.. py:method:: beacon_states_validators(state_id: str)

.. py:method:: beacon_states_validators_id(state_id: str, validator_id: str)

.. py:method:: beacon_states_validator_balances(state_id: str)

.. py:method:: beacon_states_committees(state_id: str)

.. py:method:: beacon_states_sync_committees(state_id: str)

.. py:method:: beacon_states_randao(state_id: str)

.. py:method:: beacon_headers()

.. py:method:: beacon_headers_id(block_id: str)

.. py:method:: beacon_blocks(block_id: str)

.. py:method:: beacon_blinded_blocks_(block_id: str)

.. py:method:: beacon_blocks_id(block_id: str)

.. py:method:: beacon_blocks_root(block_id: str)

.. py:method:: beacon_blocks_attestations(block_id: str)

.. py:method:: beacon_blob_sidecars(block_id: str)

.. py:method:: beacon_pool_attestations()

.. py:method:: beacon_pool_attester_slashings()

.. py:method:: beacon_pool_proposer_slashings()

.. py:method:: beacon_pool_voluntary_exits()

.. py:method:: beacon_pool_bls_to_execution_changes()

.. py:method:: beacon_deposit_snapshot()

.. py:method:: builder_states_expected_withdrawals(state_id: str)

.. py:method:: config_fork_schedule()

.. py:method:: config_spec()

.. py:method:: config_deposit_contract()

.. py:method:: debug_beacon_states(state_id: str)

.. py:method:: debug_beacon_heads()

.. py:method:: debug_fork_choice()

.. py:method:: node_peers()

.. py:method:: node_peers_id(peer_id: str)

.. py:method:: node_peer_count()

.. py:method:: node_version()

.. py:method:: node_syncing()

.. py:method:: node_health()
