.. _releases:

=============
Release Notes
=============

3.0.0 (2024-07-07)
------------------
* Migrated to poetry to make things easier with a modern approach on project management.
* Improved CI-CD pipelines.
* Made improvements to multinet support in prep for the mainnet deployment.
* Deleted bls and merkle related codes as not needed anymore.
* Improved tests and overall coverage.

2.1.0 (2024-05-15)
------------------
* New holesky deployment.
* Exception names improved.

2.0.0 (2024-03-01)
------------------
* Added holesky deployment mirroring the mainnet deployment.
* Using a consensus client with `specified api <https://ethereum.github.io/beacon-APIs/?urls.primaryName=v2.3.0#/Beacon/getStateValidator>`_ instead of beaconcha.in api to fetch Beacon data.
* Improvements and bug fixes.
* Improved documentation.

1.3.0 (2023-09-25)
------------------
* Added websocket support to the internal web3.

1.2.0 (2023-09-25)
------------------
* Added the ability to create and return deposit data and keystore data given mnomanic and index.

1.1.1 (2023-08-11)
------------------
* Validator struct is fixed aligned with the changes on the contract 

1.1.0 (2023-07-24)
------------------
* Initial Release