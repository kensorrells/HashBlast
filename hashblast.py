import hashlib


def input_hash():
    
    #I created the variable md, beauase later I will be converting these hashes back to English

    md = input("Encode your data: ")

    
    print(" \n             MD5                     ")
    print("________________________________________")
    print(hashlib.md5(md.encode()).hexdigest())
    print("________________________________________")

    print(" \n            Sha256                   ")
    print("____________________________________________________________________")
    print(hashlib.sha256(md.encode()).hexdigest())
    print("____________________________________________________________________")

    print(" \n            Sha512                   ")
    print("____________________________________________________________________________________________")
    print(hashlib.sha512(md.encode()).hexdigest())
    print("____________________________________________________________________________________________")
    

input_hash()



