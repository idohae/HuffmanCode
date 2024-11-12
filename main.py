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
