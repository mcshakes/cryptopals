import crypt


def test_pass(crypt_pass):
    salt = crypt_pass[0:2]

    dictFile = open("dictionary.txt", "r")

    for word in dictFile.readlines():
        word = word.strip("\n")
        crypt_word = crypt.crypt(word, salt)

        if (crypt_word == crypt_pass):
            print(f"[+] Found Password: {word}\n")
            return

    print("[-] Password Not Found.\n")
    return


def main():
    pass_file = open("passwords.txt")

    for line in pass_file.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptPass = line.split(":")[1].strip(" ")
            print("[*] Cracking Password For: ", user)
            test_pass(cryptPass)


if __name__ == "__main__":
    main()
