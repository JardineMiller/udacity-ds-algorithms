import sys

class TreeNode:
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right

def get_frequencies_dict(string):
    frequencies = {}

    for char in string:
        entry = frequencies.get(char, None)

        if entry:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    return frequencies

def construct_huffman_table(node, bin_string=""):
    result = {}

    if type(node) is str:
        result[node] = bin_string
        return result

    if node.left:
        result.update(construct_huffman_table(node.left, bin_string + "0"))
    if node.right:
        result.update(construct_huffman_table(node.right, bin_string + "1"))
    
    return result

def construct_tree(freq_dict):
    tuples_list = sorted(freq_dict.items(), key = lambda tup:tup[1]) 

    if len(tuples_list) == 1:
        value1, count1 = tuples_list.pop(0)
        return TreeNode(value1)

    while len(tuples_list) > 1:
        # Take first two tuples and remove the from list
        value1, count1 = tuples_list.pop(0)
        value2, count2 = tuples_list.pop(0)

        # Create a parent node with each tuple values as children
        parent_node = TreeNode(value1, value2)

        # Attach the node back into the list, the new count being the combined count of the children
        tuples_list.append((parent_node, count1 + count2))

        # Re-sort the list so we retain priority
        tuples_list = sorted(tuples_list, key = lambda tup:tup[1])

    return tuples_list[0][0]

def encode_string(string, huffman_table):
    encoded_data = ""

    for char in string:
        encoded_data += huffman_table[char]

    return encoded_data

def huffman_encoding(data):
    if data is None or len(data) == 0:
        raise ValueError("String must not be null or empty")

    frequencies = get_frequencies_dict(data)
    tree = construct_tree(frequencies)
    huffman_table = construct_huffman_table(tree)
    encoded_data = encode_string(data, huffman_table)

    return (encoded_data, tree)

def decode_char(bit_arr, node):
    if type(node) is str:
        return node

    bit = bit_arr.pop(0)
    
    if bit == "0":
        return decode_char(bit_arr, node.left)
    else:
        return decode_char(bit_arr, node.right)
    

def huffman_decoding(bit_string, tree):
    decoded_string = ""
    bit_arr = [bit for bit in bit_string]

    while len(bit_arr) > 0:
        decoded_string += decode_char(bit_arr, tree)

    return decoded_string


if __name__ == "__main__":
    print("==== TEST 1 ====")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


    print("==== TEST 2 ====")
    a_great_sentence = "This is another test string"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


    print("==== TEST 3 ====")
    a_great_sentence = "aaaaa"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    try:
        print("==== TEST 4 ====")
        a_great_sentence = ""

        print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = huffman_encoding(a_great_sentence)

        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))
    except ValueError:
        print("Oops, looks like you provided an invalid input")


    
