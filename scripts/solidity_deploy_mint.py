from scripts.helpful_scripts import (
    get_account,
)
from brownie import VyperPyConNFT, PyConNFT, network, config
from scripts.mint import mint

def deploy_Solidity_ERC721(account):
    # We want to be able to use the deployed contracts if we are on a testnet
    # Otherwise, we want to deploy some mocks and use those
    # Rinkeby
    ERC721 = PyConNFT.deploy(
        "",
        {"from": account}
    )
    print(f"New ERC721 has been deployed at {ERC721.address}")

    return ERC721
    


def main():
    account = get_account()
    ERC721 = deploy_Solidity_ERC721(account)
    mint(ERC721, account)