#python3

import hashlib

txt_ent = 1
fun_type = 1
hsh_format = 1
run_cont = True

while run_cont == True:
 print("Please choose your format.")
 hsh_format = input("Format: ")
 print("Would you like to encrypt or decrypt?")
 fun_type = input("Function: ")
 print("Please enter the text.")
 txt_ent = input("Text: ")
 print("________________________________________")
 if hsh_format == 'SHA1':
  if fun_type == 'encrypt':
   print(hashlib.sha1(txt_ent.encode()).hexdigest())
  else:
   print("")
 elif hsh_format == 'SHA224':
  if fun_type == 'encrypt':
   print(hashlib.sha224(txt_ent.encode()).hexdigest())
  else:
   print("")
 elif hsh_format == 'SHA256':
  if fun_type == 'encrypt':
   print(hashlib.sha256(txt_ent.encode()).hexdigest())
  else:
   print("")
 elif hsh_format == 'SHA384':
  if fun_type == 'encrypt':
   print(hashlib.sha384(txt_ent.encode()).hexdigest())
  else:
   print("")
 elif hsh_format == 'SHA512':
  if fun_type == 'encrypt':
   print(hashlib.sha512(txt_ent.encode()).hexdigest())
  else:
   print("")
 elif hsh_format == 'MD5':
  if fun_type == 'encrypt':
   print(hashlib.md5(txt_ent.encode()).hexdigest())
  else:
   print("")
 else:
     print("ERROR")
     BREAK
 print("________________________________________")
 print("Would you like to do anything else?")
 cont = input("   : ")
 cont.lower
 if cont != 'no' or 'n':
     run_cont = False
 else:
     run_cont = True
