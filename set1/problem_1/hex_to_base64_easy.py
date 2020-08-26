import codecs

hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

bytes_object = bytes.fromhex(hex_str)
ascii_string = bytes_object.decode("ASCII")

# ^ Gets you: I'm killing your brain like a poisonous mushroom

base64_str = codecs.encode(bytes_object, "base64")

return base64_str
