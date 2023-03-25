#!/usr/bin/env python3

import crypt

plain_pass = input("What is the password? ")
salt = input("What is the salt? ")

print("MD5       : {0}".format(crypt.crypt(plain_pass, "$1$" + salt)))
print("Blowfish  : {0}".format(crypt.crypt(plain_pass, "$2a$" + salt)))
print("eksblofish: {0}".format(crypt.crypt(plain_pass, "$2y$" + salt)))
print("SHA-256   : {0}".format(crypt.crypt(plain_pass, "$5$" + salt)))
print("SHA-512   : {0}".format(crypt.crypt(plain_pass, "$6$" + salt)))

