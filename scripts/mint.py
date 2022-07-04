from scripts.helpful_scripts import (
    get_account,
)
from brownie import VyperPyConNFT, PyConNFT, network, config

def mint(ERC721, account):
    URIs = [
        'ipfs://QmXmnahgjkeaUerkF4fQyDopPni7NxNCkg1kjX4j9eLEzn',
        'ipfs://QmW1GUzNXePoxxPUr5cvGPGUPRUHL5cqDWMXVgW92meXUu',
        'ipfs://QmcNG8nrELwXQA97yWAcx5qdT6RA7wYctUL3Psh9G58yEc',
        'ipfs://QmcaFWN3UDRkwvbku6qZAiPymoo7uqTyp9JM42M6mhKt6m',
    ]
    for uri in URIs:
        tx = ERC721.mint(account.address, uri, {"from": account})
        tx.wait(1)
    
    if(network.show_active() == "polygon-test"):
        print(f"Minted, view it at https://testnets.opensea.io/assets/mumbai/{ERC721.address}/{ERC721.tokenCounter() - 1}")
    else:
        print("Mint Success")

def main():
    account = get_account()
    # -1 is the one you just deployed
    # Can use VyperPyConNFT (Vyper) or PyConNFT (Solidity)
    # ERC721 = VyperPyConNFT[-1]
    ERC721 = PyConNFT[-1]
    mint(ERC721, account)