from scripts.helpful_scripts import (
    get_account,
)
from brownie import Contract, VyperPyConNFT, PyConNFT, network, config
from scripts.mint import mint
import json


def load_ERC721(account):
    with open("./build/contracts/PyConNFT.json", "r") as f:
        abi = json.load(f)["abi"]
        ERC721 = Contract.from_abi(
            "ERC721",
            "0xE6FC4ef5543490FaFA318B035D77097c79199292",
            abi,
        )
    return ERC721


def main():
    account = get_account()
    ERC721 = load_ERC721(account)
    uri = ERC721.contractURI()
    print(uri)
