from datetime import datetime
import hashlib

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
    
    def prettyPrint(self):
        '''
        prettyPrint: prints information about blocks

        TODO: rewrite to be less brute force
        '''
        print("    {")
        print("        'data': '"+self.data+"',")
        print("        'hash': '"+self.hash+"',")
        print("        'previousHash': '"+self.previousHash+"',")
        print("        'timestamp': '"+self.timeStamp+"'")
        print("    },")

    def mineBlock(self, difficulty):
        target = str(difficulty).replace('\0', '0')
        while str(self.hash)[:difficulty] != target:
            self.hash = self.calculateHash()
        print("Block mined: "+self.hash)

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


def validChain(blockchain):
    '''
    validChain: checks hashes to verify integrity of blockchain

    Inputs:
    - blockchain (Type: Array/List)

    Returns:
    - True if hashes match, false if not
    '''
    for x in range(1, len(blockchain)):
        currentBlock = blockchain[x]
        previousBlock = blockchain[x-1]

        #compare registered and calc'd hash
        if(currentBlock.hash != currentBlock.calculateHash()):
            print("Current hashes not equal")
            return False
        #comparing previous registered and previous calc'd hash
        if(previousBlock.hash != previousBlock.calculateHash()):
            print("Previous hashes not equal")
            return False
    return True    

def main():
    difficulty = 3
    '''
    main: runs program and creates blocks
    '''
    blockchain = []
    blockchain.append(Block("First block data", "0"))
    print("attempting to mine first block...")
    blockchain[0].mineBlock(difficulty)

    blockchain.append(Block("second data here", blockchain[-1].hash))
    print("attempting to mine second block...")
    blockchain[1].mineBlock(difficulty)

    blockchain.append(Block("third block data section", blockchain[-1].hash))
    print("attempting to mine third block...")
    blockchain[2].mineBlock(difficulty)

    print("Blockchain is valid: "+validChain(blockchain))

    #pretty print blockchain
    print("The blockchain: \n [")
    #block info here!
    for block in blockchain:
        block.prettyPrint()
    print("]")
    


if __name__ == "__main__":
    main()