from scripts.helpful_scripts import (
    get_account,
)
from brownie import VyperPyConNFT, PyConNFT, network, config

URIs = [
    "ipfs://QmbQWXNLcuVnpx4GAMQhg1hPCnz4PHVbinuwUy8EDKF1ak",
    "ipfs://QmSCUJcYsYxXe4WZ8WNpwYyYDdht18hCb1oEnimXqVWZMu",
    "ipfs://QmZsVZfzUGDTpaxGUioRXa8mytFsYzPBqbgmxy7qmBCR76",
    "ipfs://QmfMBXbB5T1Aa4M9tFNJEKhz3iYh7M9DFWiFnLeZfqqu3h",
]


def mint(ERC721, account):
    for uri in URIs:
        tx = ERC721.mint(account.address, uri, {"from": account})
        tx.wait(1)

    if network.show_active() == "rinkeby":
        print(
            f"Minted, view it at https://testnets.opensea.io/assets/rinkeby/{ERC721.address}/{ERC721.tokenCounter() - 1}"
        )
    else:
        print("Mint Success")


def main():
    account = get_account()
    # -1 is the one you just deployed
    # Can use VyperPyConNFT (Vyper) or PyConNFT (Solidity)
    # ERC721 = VyperPyConNFT[-1]
    ERC721 = PyConNFT[-1]
    mint(ERC721, account)
