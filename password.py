import random
s = "bcdefghijkl\
    mnopqrstuvwxyz1234\
        567890ABCDEFGHIJKLM\
        NOPQRSTUVWXYZ!@$%^&\
        ()_-+[]{};/';.,"

passwordlen = 16
password = ''.join(random.sample(s, passwordlen))
print(password)
