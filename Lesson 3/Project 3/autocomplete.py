## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        result = []

        if self.is_word and len(suffix):
            result += [suffix] # can't return the result here as it could be a word with children
        
        for key in self.children:
            new_suffix = suffix + key
            result += self.children[key].suffixes(new_suffix)

        return result
        
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        
        current_node.is_word = True

    def exists(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            
            current_node = current_node.children[char]
        
        return current_node.is_word

    def find(self, prefix):
        ## Find the Trie node that represents this prefix

        if type(prefix) is not str:
            raise ValueError("Input must be a string")

        if prefix is None or not len(prefix):
            return None

        current_node = self.root
        
        for char in prefix:
            if char not in current_node.children:
                return None
        
            current_node = current_node.children[char]
        
        return current_node


# ===== UTILS ===== #
def create_trie(words):
    trie = Trie()

    for word in words:
        trie.insert(word)

    return trie

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

def run_trie_tests():
    word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
    word_trie = create_trie(word_list)

    # Exists
    test("'bear' is in trie", word_trie.exists("bear"), True)
    test("'apple' is in trie", word_trie.exists("apple"), True)
    test("'hello' is not trie", word_trie.exists("hello"), False)

    # Prefix
    test("prefix 're' returns None because it can't be found", word_trie.find("re"), None)
    test("prefix 'go' has one child", len(word_trie.find("go").children), 1)
    test("prefix 'goo' has one child", len(word_trie.find("goo").children), 2)
    test("prefix 'good' has three children", len(word_trie.find("good").children), 3)
    test("prefix 'z' has one child", len(word_trie.find("z").children), 1)

    # Suffix
    test("prefix 'z' returns 'ebra' as suffix", word_trie.find("z").suffixes(), ["ebra"])
    test("prefix 'good' returns 'bye, s, will' as suffixes", word_trie.find("good").suffixes(), ["bye", "s", "will"])
    test("prefix 'zebra' returns empty array", word_trie.find("zebra").suffixes(), [])

    # Invalid input
    test("empty input returns None", word_trie.find(""), None)  

    try:
        test("empty input returns None", word_trie.find(None), None)
    except ValueError:
        test("invalid input (None) type raises exception", True, True)

    try:
        word_trie.find(1)
    except ValueError:
        test("invalid input (int) type raises exception", True, True)

run_trie_tests()


