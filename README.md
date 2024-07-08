# geodefi

**geodefi**  is a Python library for interacting with [geode.fi](https://www.geode.fi) smart contract infrastructure.

[geode.fi](https://www.geode.fi) an open source **Decentralized Infrastructure Provider** aiming to create a secure closed-environment for the wider Decentralized Finance landscape.
Currently providing a set of smart contracts which allows anyone to create their own Staking Pool on Ethereum.
Soon, much more.

Built on top of [web3.py](https://web3py.readthedocs.io/en/stable) Geodefi offers a comprehensive set of functions and utilities that simplify the process of interacting with the protocol's smart contract infrastructure.

Whether you're looking to query contract data or execute transactions, **geodefi** Python SDK has you covered! With a user-friendly and highly efficient interface, this SDK also provides cool features such as built-in cache, easy wallet management etc.

## Features

- Supports Ethereum Holesky testnet (as of v2.1.0) where The Protocol is deployed.
- Provides a simple and intuitive API for managing validators, operators, pools, tokens, and other smart contracts/packages.
- Dynamically adapts to the contract upgrades.
- Mostly chain agnostic. However, might differ according to the unique PoS implementations.
- Compatible from Python 3.8 to Python 3.12.

## Installation

```sh
pip install geodefi
```

## Documentation

Detailed documentation for this project is available on [Geodefi SDK Read The Docs](https://sdk.geode.fi).

### Sphinx

If your feature needs to have additional section in [Read The Docs](https://sdk.geode.fi). Please check the docs in your local computer first.

> built docs page is located in docs/_build/html/index.html.

You will need a sphinx server to render rst files:

#### **Build**

```bash
sphinx-build docs docs/_build/html
```

#### **Auto-build**

```bash
sphinx-autobuild docs docs/_build/html
```

## Contributing

We welcome contributions from the community! To contribute to this project, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top right corner of this repository to create your own copy.

2. **Clone the Repository**: Clone the forked repository to your local machine using the following command:

   ```bash
   git clone https://github.com/<your_user_name>/geode-py.git
    ```

3. **Build from source**:
   Take a look at the [Build](#building) section

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

### Building

We do not recommend using `pip` and your *local* `python` installation.

Use `pipx` to manage your local packages, which in this case will be used to install pyenv.

Use `pyenv` to manage your python version.

Use `poetry` for dependency management and packaging.

#### Create virtual env

Simply do:

```bash
poetry shell
```

> This will create and activate a virtual environment.

If you want to set the python version from start you can also do:

```bash
poetry env use <python_version/3.9/3.9.19/etc>
```

This will output:

> Using virtualenv: <path_to_venv>
> copy <path_to_venv> and use it above to activate

```bash
source <path_to_venv>/bin/activate
```

#### Install deps

Install project dependencies with:

```bash
poetry install
```

## Release

Old method:

- Use main branch for releases.
- test with ``VERSION=1.0.0 python -m build`` if you want, then:

``` bash
    git tag -a "v0.0.1-beta" -m "beta version testing"
    git push --tags
```

New Method:

``` bash
poetry publish --build
```

## License

`geodefi` python sdk is licensed under MIT.
