// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CreditRegistry {
    struct CreditInfo {
        string ipfsHash;
        uint256 score;
        uint256 timestamp;
    }

    mapping(address => CreditInfo[]) public history;

    function storeResult(string memory ipfsHash, uint256 score) public {
        history[msg.sender].push(CreditInfo(ipfsHash, score, block.timestamp));
    }

    function getHistory(address user) public view returns (CreditInfo[] memory) {
        return history[user];
    }
}