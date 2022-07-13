import pytest

import brownie
from scripts.solidity_deploy_mint import deploy_Solidity_ERC721
from scripts.vyper_deploy_mint import deploy_Vyper_ERC721
from scripts.helpful_scripts import get_account, contractURI
from scripts.mint import mint, URIs as NFT_Metadatas


def test_solidity_ERC721():
    account = get_account()
    ERC721 = deploy_Solidity_ERC721(account)
    ERC721_test_script(ERC721, account)


def test_vyper_ERC721():
    account = get_account()
    ERC721 = deploy_Vyper_ERC721(account)
    ERC721_test_script(ERC721, account)


def ERC721_test_script(ERC721, account):
    assert contractURI == ERC721.contractURI()
    assert ERC721.tokenCounter() == 0

    mint(ERC721, account)
    assert ERC721.tokenCounter() == len(NFT_Metadatas)
    assert ERC721.ownerOf(0) == account.address
    for i, metadata in enumerate(NFT_Metadatas):
        assert ERC721.tokenURI(i) == NFT_Metadatas[i]
