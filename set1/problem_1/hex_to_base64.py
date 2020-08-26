import codecs
import base64

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

# Convert hexadecimal string units to bits or binary


def hex_string_to_binary(hex_str: str) -> str:
    collection = []

    for idx in range(0, len(hex_str)):
        char = hex_str[idx]
        binary_str = HEX_MAP[char]
        collection.append(binary_str)

    return "".join(collection)

# split to 6 bits


def split_binary(bin_str: str) -> str:
    x = [bin_str[i:i+6] for i in range(0, len(bin_str), 6)]
    return "".join(x)

# Split the binary string into 4 pieces of 6 bits each
# ASCII format that follows a Radix-64 representation. Each character is picked from a set of 64 characters, which means that I'll only need 6 bits represent each character because 26 = 64 characters.


x = hex_string_to_binary(incoming)

z = split_binary(x)
# ans = base64.b64encode(z)
print(z)
# base64_convert(p)
