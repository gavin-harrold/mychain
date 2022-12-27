from datetime import datetime
import hashlib
import json

class Block():
    def __init__(self, data, previousHash):
        '''
        Construct Block object representing a block in the blockchain

        Inputs:
        - data (Type: String)
        - previousHash (Type: String)

        Attributes:
        - data : whatever data the block contains
        - previousHash : the hash of the previous block, 0 if founder
        - timeStamp : timestamp this block was created
        - hash : the block's current hash
        '''
        self.data = data
        self.previousHash = previousHash
        timeStamp = datetime.now()
        self.timeStamp = timeStamp.strftime("%d/%m/%Y %H:%M:%S")
        self.hash = self.calculateHash()

    def calculateHash(self):
        '''
        calculateHash: Calculates hash using util class method

        Returns:
        Hash for current Block using SHA256 in hexadecimal form
        '''
        return HashUtil.applyHash(
                    self.previousHash +
                    self.timeStamp +
                    self.data)

    def toJson(self):
        blockObject = {
            "data" : self.data,
            "hash" : self.hash,
            "previousHash" : self.previousHash,
            "timestamp" : self.timeStamp
        }
        return blockObject

class HashUtil():
    def applyHash(hash):
        '''
        applyHash: applies SHA256 to hash string that has been converted to byte format

        Inputs:
        - hash (Type: String)

        Returns:
        Hexadecimal form of hash via SHA256
        '''
        encodedHash = repr(hash).encode()
        output = hashlib.sha256(encodedHash)
        output = output.hexdigest()
        return output



def main():
    blockchain = []
    blockchain.append(Block("First block data", "0"))
    #print("Hash for first block: ", founder.hash)

    blockchain.append(Block("second data here", blockchain[-1].hash))
    #print("hash of second block: ", second.hash)

    blockchain.append(Block("third block data section", blockchain[-1].hash))
    #print("hash for third block: ", third.hash)
    #pretty print blockchain
    print("The blockchain: \n [")
    for block in blockchain:
        print("    "+json.dumps(block.toJson(), sort_keys=True, indent=4)+ ",")
    print("]")


if __name__ == "__main__":
    main()