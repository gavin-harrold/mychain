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
    founder = Block("First block data", "0")
    print("Hash for first block: ", founder.hash)

    second = Block("second data here", founder.hash)
    print("hash of second block: ", second.hash)

    third = Block("third block data section", second.hash)
    print("hash for third block: ", third.hash)

if __name__ == "__main__":
    main()