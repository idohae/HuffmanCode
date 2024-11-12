class HuffmanNode:
    def __init__(self, frequency, symbol=None, left=None, right=None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right

    # Helper method to check if a node is a leaf (has no children)
    def is_leaf(self):
        return self.left is None and self.right is None


class HuffmanCoding:
    def __init__(self, frequencies): # frequencies -> dict, with char: freq
        # Initialize with a list of Huffman nodes for each character
        self.nodes = [HuffmanNode(freq, symbol) for symbol, freq in frequencies.items()]
        self.nodes = sorted(self.nodes, key=lambda x: x.frequency)

        while len(self.nodes)>1:
            min1 = self.nodes[0]
            min2 = self.nodes[1]
            self.nodes = self.nodes[2:]
            node = HuffmanNode(min1.frequency+min2.frequency, "temp", min1, min2)
            self.nodes.append(node)
            self.nodes = sorted(self.nodes, key=lambda x: x.frequency)
        
        self.root = node

    def get_codes(self, node, code='', code_dict={}):
        if node.is_leaf():
            code_dict.update({node.symbol:code})
            return code_dict
        left = node.left
        right = node.right
        self.get_codes(left, code+'1', code_dict)
        self.get_codes(right, code+'0', code_dict)
        return code_dict


# Example usage
if __name__ == "__main__":
    # Input frequencies as per Table 9.1.2
    frequencies = {
        '!': 2,
        '@': 3,
        '#': 7,
        '$': 8,
        '%': 12
    }

    # Create HuffmanCoding instance and get the codes
    huffman_coding = HuffmanCoding(frequencies)
    codes = huffman_coding.get_codes(huffman_coding.root)

    # Output the resulting Huffman codes
    print("Huffman Codes for the given frequencies:")
    for symbol, code in codes.items():
        print(f"{symbol}: {code}")

