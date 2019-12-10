def encrypt(plaintext, key):
    l = len(plaintext)
    ciphertext = ''
    lk = len(key)
    for i in range(l):
            if(plaintext[i].isalpha()):
                ciphertext = ciphertext + chr((ord(plaintext[i]) + ord(key[i%lk]) - 2*ord('a'))%26 + ord('a'))
    
    return ciphertext

def decrypt_key(ciphertext, key):
    l = len(ciphertext)
    plaintext = ''
    lk = len(key)
    for i in range(l):
        if(ciphertext[i].isalpha()):
            code = ord(ciphertext[i]) - ord(key[i%lk])
            if(code < 0):
                code = code + 26
            plaintext = plaintext + chr(code + ord('a'))
        
    return plaintext

def collisions(s1, s2):
    l = len(s1)
    c = 0
    for i in range(l):
        if(s1[i] == s2[i]):
            c = c + 1
    return c

def decrypt(ciphertext):
    l = len(ciphertext)
    prev = 0
    shift = 0
    new = ciphertext
    c = new[l-1]
    new = new[:-1]
    new = c + new
    shift = 1
    prev = collisions(ciphertext, new)
    prev = prev/l
    cur = prev
    print(cur)
    while(abs(cur - prev) < 0.015):
        c = new[l-1]
        new = new[:-1]
        new = c + new
        shift = shift + 1
        cur = collisions(ciphertext, new)
        cur = cur/l
        print(cur)
    
    return shift
    
    