def ubah_huruf(sentence):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_bob = "KLMNOPQRSTUVWXYZABCDEFGHIJ"
    
    pattern = ""    
    for i in range(len(sentence)):
        for j, alp in enumerate(alphabet):
            if sentence[i]==alp:
                for k, alp_bob in enumerate(alphabet_bob):
                    if j==k:
                        pattern+=alp_bob
        if sentence[i]== " ":
            pattern+=" "
            
    return pattern

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB