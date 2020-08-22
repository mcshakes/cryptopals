string = "1c0111001f010100061a024b53535009181c"
cyphertext = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


def hex_decode(inc_str):
    byte_string = bytes.fromhex(inc_str)
    return byte_string


def byte_xor(ba1, ba2):
    # x = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(ba1,s2))
    print(x)


x = hex_decode(string)
byte_xor(x, cyphertext)
