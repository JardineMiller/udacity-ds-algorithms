# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        for sub_path in paths:
            if sub_path is None or not len(sub_path):
                continue

            if sub_path not in current_node.children:
                current_node.insert(sub_path)

            current_node = current_node.children[sub_path]

        current_node.handler = handler

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        for sub_path in paths:
            if not len(sub_path):
                continue

            if sub_path is None or sub_path not in current_node.children:
                return None
            
            current_node = current_node.children[sub_path]

        return current_node if current_node.handler is not None else None

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, sub_path):
        self.children[sub_path] = RouteTrieNode()

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if path is None or type(path) is not str:
            raise ValueError("Path must be of type string")

        if handler is None or type(handler) is not str:
            raise ValueError("Handler must be of type string")
        
        paths = self.split_path(path)
        self.trie.insert(paths, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path is None or type(path) is not str:
            raise ValueError("Path must be of type string")

        paths = self.split_path(path)
        leaf = self.trie.find(paths)

        return leaf.handler if leaf is not None else self.not_found_handler 

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.split("/")

# Here are some test cases and expected outputs you can use to test your implementation
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

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

def run_tests():
    # Happy path
    test("'/' lookup returns root handler", router.lookup("/"), "root handler")
    test("'/home/about' lookup returns about handler", router.lookup("/home/about"), "about handler")
    test("'/home/about/' lookup returns about handler - handles trailing slash", router.lookup("/home/about/"), "about handler")

    # Not found
    test("'/home' lookup returns 404", router.lookup("/home"), "not found handler")
    test("'/home/about/me' returns 404", router.lookup("/home/about/me"), "not found handler")

    # Edge case
    try:
        router.add_handler(None, None)
    except ValueError:
        test("add_handler: invalid input (incorrect type) raises exception", True, True)

    try:
        router.lookup(1)
    except ValueError:
        test("lookup: invalid input (incorrect type) raises exception", True, True)

    try:
        router.lookup(None)
    except ValueError:
        test("lookup: invalid input (None param) raises exception", True, True)

run_tests()