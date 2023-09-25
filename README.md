# geodefi

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

`geodefi` is a Python library which makes it easier to interact with the Proof of Stake networks that [The Staking Library](https://docs.geode.fi) is available.
It provides a simple and intuitive interface for accessing blockchain data, executing smart contract functions, and managing blockchain transactions related to Geode's Trustless staking solution.

## Features

- Supports Ethereum Goerli testnet (as of v1.1.2) where The Protocol is deployed.
- Provides a simple and intuitive API for managing validators, operators, pools, tokens, and other smart contracts/packages.
- Dynamically adapts to the contract upgrades.
- Mostly chain agnostic. However, might differ according to the unique PoS implementations.
- Compatible from Python 3.7 to Python 3.10.

## Installation

Using pip:

```sh
pip install geodefi
```

Using setup.py:

```sh
python3 setup.py .
```

## Usage Details
>
>Note that, Geode.Token refers to the chain-specific internal Token of The Staking Library. This token differs on different chains.

### Get the chain-specific internal Token

gETH on Ethereum, gGNO on Gnosis etc.

```python
# Get gETH token with all functionalities
gETH = Geode.Token
totalSupply = gETH.functions.totalSupply().call()
print(f"Total Supply: {totalSupply}")
```

## Contributing

We welcome contributions from the community! To contribute to this project, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top right corner of this repository to create your own copy.

2. **Clone the Repository**: Clone the forked repository to your local machine using the following command:

   ```bash
   git clone https://github.com/<your_user_name>/geode-py.git
    ```

3. **Virtual Environment (adviced)** Open virtual environment for python.

    ```bash
    sudo pip install virtualenv
    python3 -m venv {path}
    source {path}/bin/activate

    pip install -r requirements.txt
    ```

4. **Create a Branch**: Create a new branch for your contribution:

    ```bash
    git checkout -b feature/your-feature-name
    ```

5. **Stage Changes**: Stage your changes to be commited

    ```bash
    git add <your-modified-files>
    ```

6. **Commit Changes**: Commit your changes with a descriptive commit message:

    ```bash
    git commit -m "Add feature: your feature description"
    ```

7. **Push Changes**: Push your changes to your forked repository:

    ```bash
    git push origin feature/your-feature-name
    ```

8. **Create a Pull Request**: Go to the original repository on GitHub and click on the "Pull Request" button. Fill out the necessary information and submit the pull request. Your pull request will be reviewed by the maintainers. Be ready to respond to any feedback or changes requested. You might need to make additional commits based on the feedback.

9. **Celebrate**: Once your pull request is approved and merged, your contribution will be part of the project! Thank you for your contribution.

## Documentation

Detailed documentation for this project is available on [Geodefi SDK](https://sdk.geode.fi).

You can find information on how to install, use, and contribute to the project in the documentation. Whether you're a user or a developer, the documentation provides essential resources to help you get started.

1. **Update in documentations**
If your feature needs to have additional section in [Read The Docs](https://sdk.geode.fi). Please check the docs in your local computer first.

```bash
cd docs
make html
```

> built docs page is located in docs/_build/html/index.html.

# Releasing

- Use main branch for releases.
- Change .github/workflows/pipy_release.yml version first, then:

```
git tag 0.0.1 # or whatever version you want 
git push origin --tags
```

# License

`geodefi` is licensed under MIT.
