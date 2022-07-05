// SPDX-License-Identifier: MIT
pragma solidity 0.8.1;

// https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract PyConNFT is ERC721URIStorage {
    uint256 public tokenCounter;
    address public minter;
    string public contractURI;

    constructor(string memory uri) public ERC721("PyConNFT", "PyCon") {
        minter = msg.sender;
        tokenCounter = 0;
        contractURI = uri;
    }

    function mint(address to, string memory tokenURI) public returns (uint256) {
        require(msg.sender == minter);
        require(to != address(0));
        uint256 newTokenId = tokenCounter;
        _safeMint(to, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        tokenCounter++;
        return newTokenId;
    }

    function burn(uint256 tokenId) public virtual {
        //solhint-disable-next-line max-line-length
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: caller is not token owner nor approved"
        );
        _burn(tokenId);
    }

    function setContractURI(string memory newURI) public {
        require(msg.sender == minter, "Caller is not the minter");
        contractURI = newURI;
    }
}
