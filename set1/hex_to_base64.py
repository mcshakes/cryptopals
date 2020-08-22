import base64

# Base64 is used to encode binary information and Hexadecimal is used to view the raw bytes.

HEX_MAP = {
    '0': "0000",
    '1': "0001",
    '2': "0010",
    '3': "0011",
    '4': "0100",
    '5': "0101",
    '6': "0110",
    '7': "0111",
    '8': "1000",
    '9': "1001",
    'a': "1010",
    'b': "1011",
    'c': "1100",
    'd': "1101",
    'e': "1110",
    'f': "1111"
}

incoming = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# Convert hexadecimal string to binary string

# Split the binary string into 4 pieces of 6 bits each
# Convert the binary string to decimal
# Compare each decimal against each character in a reference string of 64 characters


def hex_string_to_binary(hex_str: str) -> str:
    collection = []

    for idx in range(0, len(hex_str)):
        char = hex_str[idx]
        binary_str = HEX_MAP[char]
        collection.append(binary_str)

    print("".join(collection))


hex_string_to_binary(incoming)
