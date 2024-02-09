import logging
import typing as t
import eth_typing as et
from datetime import datetime

from geode.globals import Network, API_BASE
from geode.utils import httpRequest
from geode.exceptions import UnknownChainException


class Beacon(object):
    # https://ethereum.github.io/beacon-APIs/#
    # All of the GET end points that is specified within the Ethereum's Specification v2.3.0 is accesible.
    # Also some of the v2.4.0 is also accesible.
    api_base: str
    api_suffix: str
    last_update: datetime
    beacon_state: t.Dict

    def __init__(self, network: Network, cons_api: str, **kwargs):
        """
        Initializes a new instance of the class.

        Args:
            network: A `Network` object representing the blockchain network to connect to.
            cons_api: API that is compatible with beacon-APIs specification.
            **kwargs: Any additional keyword arguments to pass to the initializer.
        """
        # Get the API base URL for the specified `network`
        self.api_base = cons_api

        # Log a message indicating that the class instance is connected to the API base
        logging.info(f"Connected to beconchain")

    @httpRequest
    def beacon_genesis(self):
        # Retrieve details of the chain's genesis which can be used to identify chain.
        url = self.api_base + f"/eth/v1/beacon/genesis"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_states_root(self, state_id: str):
        # Calculates HashTreeRoot for state with given 'stateId'. # If stateId is root, same value will be returned.
        url = self.api_base + f"/eth/v1/beacon/states/{state_id}/root"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_states_fork(self, state_id: str):
        # Returns Fork object for state with given 'stateId'.
        url = self.api_base + f"/eth/v1/beacon/states/{state_id}/fork"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_states_finality_checkpoints(self, state_id: str):
        # Returns finality checkpoints for state with given 'stateId'.
        #  In case finality is not yet achieved, checkpoint should return epoch 0 and ZERO_HASH as root.
        url = self.api_base + f"/eth/v1/beacon/states/{state_id}/finality_checkpoints"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_states_validators(self, state_id: str):
        # Returns filterable list of validators with their balance, status and index.
        # Information will be returned for all indices or public key that match known validators.
        # If an index or public key does not match any known validator, no information will be returned but this will not cause an error.
        # There are no guarantees for the returned data in terms of ordering; both the index and public key are returned for each validator,
        # and can be used to confirm for which inputs a response has been returned.
        url = self.api_base + f"/eth/v1/beacon/states/{state_id}/validators"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_states_validators_id(self, state_id: str, validator_id: str):
        # Returns validator specified by state and id or public key along with status and balance.
        url = (
            self.api_base
            + f"/eth/v1/beacon/states/{state_id}/validators/{validator_id}"
        )
        print(url)
        return (url, False)

    @httpRequest
    def beacon_states_validator_balances(self, state_id: str):
        # Returns filterable list of validators balances.
        url = self.api_base + f"/eth/v1/beacon/states/{state_id}/validator_balances"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_states_committees(self, state_id: str):
        # Retrieves the committees for the given state.
        url = self.api_base + f"/eth/v1/beacon/states/{state_id}/committees"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_states_sync_committees(self, state_id: str):
        # Retrieves the current sync committee for the given state. Also returns the subcommittee assignments.
        url = self.api_base + f"/eth/v1/beacon/states/{state_id}/sync_committees"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_states_randao(self, state_id: str):
        # Fetch the RANDAO mix for the requested epoch from the state identified by state_id.
        # If an epoch is not specified then the RANDAO mix for the state's current epoch will be returned.
        # By adjusting the state_id parameter you can query for any historic value of the RANDAO mix.
        # Ordinarily states from the same epoch will mutate the RANDAO mix for that epoch as blocks are applied
        url = self.api_base + f"/eth/v1/beacon/states/{state_id}/randao"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_headers(self):
        # Retrieves block header for given block id.
        url = self.api_base + f"/eth/v1/beacon/headers"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_headers_id(self, block_id: str):
        # Retrieves block header for given block id.
        url = self.api_base + f"/eth/v1/beacon/headers/{block_id}"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_blocks(self, block_id: str):
        # Retrieves block details for given block id.
        url = self.api_base + f"/eth/v2/beacon/blocks/{block_id}"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_blinded_blocks_(self, block_id: str):
        # Retrieves blinded block for given block ID.
        url = self.api_base + f"/eth/v1/beacon/blinded_blocks/{block_id}"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_blocks_id(self, block_id: str):
        # Retrieves hashTreeRoot of BeaconBlock/BeaconBlockHeader
        url = self.api_base + f"/eth/v1/beacon/blocks/{block_id}"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_blocks_root(self, block_id: str):
        # Retrieves hashTreeRoot of BeaconBlock/BeaconBlockHeader
        url = self.api_base + f"/eth/v1/beacon/blocks/{block_id}/root"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_blocks_attestations(self, block_id: str):
        # Retrieves attestation included in requested block.
        url = self.api_base + f"/eth/v1/beacon/blocks/{block_id}/attestations"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_blob_sidecars(self, block_id: str):
        # Retrieves blob sidecars for a given block id.
        # If the indices parameter is specified, only the blob sidecars with the specified indices will be returned.
        # There are no guarantees for the returned blob sidecars in terms of ordering.
        url = self.api_base + f"/eth/v1/beacon/blob_sidecars/{block_id}"
        return (url, False)

    @httpRequest
    def beacon_pool_attestations(self):
        # Retrieves attestations known by the node but not necessarily incorporated into any block
        url = self.api_base + f"/eth/v1/beacon/pool/attestations"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_pool_attester_slashings(self):
        # Retrieves attester slashings known by the node but not necessarily incorporated into any block
        url = self.api_base + f"/eth/v1/beacon/pool/attester_slashings"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_pool_proposer_slashings(self):
        # Retrieves proposer slashings known by the node but not necessarily incorporated into any block
        url = self.api_base + f"/eth/v1/beacon/pool/proposer_slashings"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_pool_voluntary_exits(self):
        # Retrieves voluntary exits known by the node but not necessarily incorporated into any block
        url = self.api_base + f"/eth/v1/beacon/pool/voluntary_exits"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_pool_bls_to_execution_changes(self):
        # Retrieves BLS to execution changes known by the node but not necessarily incorporated into any block
        url = self.api_base + f"/eth/v1/beacon/pool/bls_to_execution_changes"
        print(url)
        return (url, False)

    @httpRequest
    def beacon_deposit_snapshot(self):
        # Retrieve EIP-4881 Deposit Tree Snapshot.
        url = self.api_base + f"/eth/v1/beacon/deposit_snapshot"
        print(url)
        return (url, False)

    @httpRequest
    def builder_states_expected_withdrawals(self, state_id: str):
        # Get the withdrawals computed from the specified state, that will be included in the block that gets built on the specified state.
        url = self.api_base + f"/eth/v1/builder/states/{state_id}/expected_withdrawals"
        print(url)
        return (url, False)

    @httpRequest
    def config_fork_schedule(self):
        # Retrieve all forks, past present and future, of which this node is aware.
        url = self.api_base + f"/eth/v1/config/fork_schedule"
        print(url)
        return (url, False)

    @httpRequest
    def config_spec(self):
        # Retrieve specification configuration used on this node
        url = self.api_base + f"/eth/v1/config/spec"
        print(url)
        return (url, False)

    @httpRequest
    def config_deposit_contract(self):
        # Retrieve Eth1 deposit contract address and chain ID.
        url = self.api_base + f"/eth/v1/config/deposit_contract"
        print(url)
        return (url, False)

    @httpRequest
    def debug_beacon_states(self, state_id: str):
        # Returns full BeaconState object for given stateId.
        url = self.api_base + f"/eth/v2/debug/beacon/states/{state_id}"
        print(url)
        return (url, True)

    @httpRequest
    def debug_beacon_heads(self):
        # Retrieves all possible chain heads (leaves of fork choice tree).
        url = self.api_base + f"/eth/v2/debug/beacon/heads"
        print(url)
        return (url, True)

    @httpRequest
    def debug_fork_choice(self):
        # Retrieves all current fork choice context.
        url = self.api_base + f"/eth/v1/debug/fork_choice"
        print(url)
        return (url, True)

    # @httpRequest
    # def events(self, topic: str):
    # This functionality is currently not available, and will be implemented later. Keeping it as a TODO.
    #     # Provides endpoint to subscribe to beacon node Server-Sent-Events stream.
    #     # Consumers should use eventsource implementation to listen on those events.
    #     # Servers may send SSE comments beginning with : for any purpose, including to keep the event stream connection alive in the presence of proxy servers.
    #     # https://html.spec.whatwg.org/multipage/server-sent-events.html the-eventsource-interface
    #     # Event types to subscribe to:
    #     # - head, block, attestation, voluntary_exit, finalized_checkpoint, chain_reorg, contribution_and_proof
    #     url = self.api_base + f"/eth/v1/events?topics={topic}"
    #     print(url)
    #     return (url, True)

    @httpRequest
    def node_peers(self):
        # Retrieves data about the node's network peers.# By default this returns all peers.# Multiple query params are combined using AND conditions
        url = self.api_base + f"/eth/v1/node/peers"
        print(url)
        return (url, False)

    @httpRequest
    def node_peers_id(self, peer_id: str):
        # Retrieves data about the given peer
        url = self.api_base + f"/eth/v1/node/peers/{peer_id}"
        print(url)
        return (url, False)

    @httpRequest
    def node_peer_count(self):
        # Retrieves number of known peers.
        url = self.api_base + f"/eth/v1/node/peer_count"
        print(url)
        return (url, False)

    @httpRequest
    def node_version(self):
        # Requests that the beacon node identify information about its implementation in a format similar to a HTTP User-Agent field.
        url = self.api_base + f"/eth/v1/node/version"
        print(url)
        return (url, False)

    @httpRequest
    def node_syncing(self):
        # Requests the beacon node to describe if it's currently syncing or not, and if it is, what block it is up to.
        url = self.api_base + f"/eth/v1/node/syncing"
        print(url)
        return (url, False)

    @httpRequest
    def node_health(self):
        # Returns node health status in http status codes. Useful for load balancers.
        url = self.api_base + f"/eth/v1/node/health"
        print(url)
        return (url, False)
