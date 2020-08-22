import base64

incoming = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"


def convert(inc_str):
    byte_string = bytes.fromhex(inc_str)
    return base64.b64encode(byte_string)


convert(incoming)
