import hashlib
def sha256_to_qr():
    a=0
    
    for i in "abimbanaiskenceediyor@gmail.com":
        a+=1

        sha256 = hashlib.sha256()
        sha256.update(bytes(i,'utf8'))
        string_hash = sha256.hexdigest()
        
        txt = f"{a}_{string_hash}"
        print(txt)
        #qr_generator(create_name(),txt)

sha256_to_qr()
