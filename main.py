import hashlib

HASH_LENGTH = 256
SLICE_LENGTH = 32
NUMBER_OF_SLICES = HASH_LENGTH // SLICE_LENGTH
XOR_VALUE = bin(int("0x24d03294", 16))[2:]
BLOCK_SIZE = 4

def xor(s1:str, s2:str)->str:
    if(len(s1) < len(s2)):
        s1 = "0" * (len(s2) - len(s1)) + s1
    else:
        s2 = "0" * (len(s1) - len(s2)) + s2
    
    res = ""
    
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            res += "0"
        else:
            res += "1"
    return res

def main():
    '''
        Calculating the SHA-256 hash of the given string. 
    '''
    hashvalue = hashlib.sha256("DM Fall 2023 HW3".encode('utf-8'))
    hash_string = hashvalue.hexdigest()
    b = ""

    '''
        Converting the hash_string from hexadecimal system
        into binary.
    '''
    
    for digit in hash_string:
        temp = bin(int(digit, 16))[2:]
        b += "0" * (BLOCK_SIZE - len(temp)) + temp
    b = "0" * (HASH_LENGTH - len(b)) + b

    '''
        Cutting the resulting binary string into slices of
        SLICE_LENGTH length.
    '''
    r = []
    for i in range(0, 255, SLICE_LENGTH):
        r.append(b[i : i + SLICE_LENGTH])

    '''
        Calculating XOR of all resulting strings.
    '''
    d = "0" * SLICE_LENGTH
    for r_i in r:
        d = xor(d, r_i)

    '''
        Computing w.
    '''
    w = xor(d, XOR_VALUE)

    print(f"w = {w}")

if __name__ == "__main__":
    main()
