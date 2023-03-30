# Caesar cipher

roladex = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

def getcharindex(char):
    for i in range(len(roladex)):
        if roladex[i] == char:
            indice = i
            break
    return indice

def encrypt() :
    message = input("What message would you like to encrypt? : ").lower()
    paradigm_shift = int(input("What paradigm shift would you like to use? : "))
    returnval = ""
    for char in message:
        if char not in roladex:
            returnval += char
        else:
            returnval = returnval + (roladex[getcharindex(char) - paradigm_shift])

    print(f"the encrypted version of your message is {returnval}\n")


def decrypt():
    message = input("What message would you like to decrypt? : ")
    paradigm_shift = int(input("What was the paradigm shift used for the encryption of this message? : "))
    returnval = ""
    for char in message:
        if char not in roladex:
            returnval += char
        else:
            correctIndex = getcharindex(char) + paradigm_shift
            if correctIndex >= len(roladex):
                correctIndex %= len(roladex)
            returnval = returnval + (roladex[correctIndex])

    print(f"the decrypted version of your message is {returnval}\n")


if __name__ == "__main__":
    print("Welcome to the Caesar Cypher encryption module.")

    validinput = False
    while not validinput:

        direction = input("Are you in need of an encryption or a decryption? : ").lower()
        if direction == "encryption":
            validinput = True
        elif direction == "decryption":
            validinput = True
        else:
            print("Your input is not valid")

    if direction == "encryption":
        encrypt()
    else:
        decrypt()
