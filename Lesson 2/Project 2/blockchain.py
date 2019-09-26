import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous = None):
        self.previous = previous
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()

        if self.previous:
            previous_hash = str(self.previous.hash)
        else:
            previous_hash = ""
            
        string = previous_hash + str(self.timestamp) + str(self.data)
        hash_str = string.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.size = 0
        self.tail = self.create_genesis_block()

    def create_genesis_block(self):
        self.size += 1
        return Block(datetime(2000, 1, 1), "genesis block")

    def get_latest_block(self):
        return self.tail

    def get_block_by_hash(self, hash):
        block = self.tail

        while block:        
            if block.hash == hash:
                return block

            block = block.previous

        return None

    def create_block(self, timestamp, data):
        return Block(timestamp, data, self.tail)

    def add_block(self, timestamp, data):
        block = self.create_block(timestamp, data)
        self.tail = block
        self.size += 1

    def print_blockchain(self):
        for block in self:
            print("Hash:", block.hash)
            print("Data:", block.data)
            if block.previous:
                print("Previous:", block.previous.hash)
                print("     |     ")
                print("     V     ")

    def __iter__(self):
        block = self.tail

        while block:
            yield block
            block = block.previous

def test(scenario, result, expected):
	separator = "-------------------------"
	scenario = "Scenario: " + scenario
	status = "Status: PASS" if result == expected else "Status: FAIL"
	result_str = "Result: " + str(result)
	expected_str = "Expected: " + str(expected)

	print(scenario)
	print(result_str)
	print(expected_str)
	print(status)
	print(separator)

def run_tests():
    blockchain = Blockchain()
    test("Blockchain starts with a size of 1 (because of genesis block)", blockchain.size, 1)

    blockchain.add_block(datetime(2019, 9, 20), 'This is some data')
    test("Adding a block increases the size by 1", blockchain.size, 2)
    test("Latest block contains new block", blockchain.get_latest_block().data, "This is some data")

    genesis_hash = blockchain.get_latest_block().previous.hash
    genesis_block = blockchain.get_block_by_hash(genesis_hash)

    test("Latest block previous is genesis block", genesis_block.data, "genesis block")

    blockchain.add_block(datetime(2019, 9, 21), 'This is some more data')
    test("Adding a block increases the size by 1", blockchain.size, 3)
    test("Latest block contains new block", blockchain.get_latest_block().data, "This is some more data")

    blockchain.print_blockchain()
    

run_tests()


