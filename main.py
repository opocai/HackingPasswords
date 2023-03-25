#!/usr/bin/env python3

import crypt


plain_pass = input("What is the password? ")

print("MD5       : {0}".format(crypt.crypt(plain_pass, "$1$")))
print("Blowfish  : {0}".format(crypt.crypt(plain_pass, "$2a$")))
print("eksblofish: {0}".format(crypt.crypt(plain_pass, "$2y$")))
print("SHA-256   : {0}".format(crypt.crypt(plain_pass, "$5$")))
print("SHA-512   : {0}".format(crypt.crypt(plain_pass, "$6$")))

print(crypt.crypt("qwerty", "$6$Kf8H/YDaKaRxozUC$"))
