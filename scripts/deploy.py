from scripts.helpful_scripts import (
    get_account,
    OPENSEA_URL,
)
from brownie import VyperPyConNFT, PyConNFT, network, config


def deploy_and_create():
    account = get_account()
    
    # We want to be able to use the deployed contracts if we are on a testnet
    # Otherwise, we want to deploy some mocks and use those
    # Rinkeby
    ERC721 = VyperPyConNFT.deploy(
        {"from": account}
    )
    print(f"New ERC721 has been deployed at {ERC721.address}")

    tx = ERC721.mint(account.address, 'https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json')
    tx.wait(1)
    
    if(network.show_active() == "polygon-test"):
        print(f"Minted, view it at https://testnets.opensea.io/assets/mumbai/{ERC721.address}/{ERC721.tokenCounter() - 1}")
    else:
        print("Mint Success")
    


def main():
    deploy_and_create()
