#python3

import hashlib

txt_ent = 1
fun_type = 1
hsh_format = 1
run_cont = True
run_turns = 0
chr_num = 0
cur_chr = 0

while run_cont == True:
 print("Please choose your format.")
 hsh_format = input("Format: ")
 print("Would you like to encrypt or decrypt?")
 fun_type = input("Function: ")
 print("Please enter the text.")
 txt_ent = input("Text: ")
 chr_num = len(txt_ent)
 print("________________________________________")
 while run_turns +1 <= chr_num:
  cur_chr = txt_ent[run_turns]
  if hsh_format == 'SHA1':
   if fun_type == 'encrypt':
    print(hashlib.sha1(cur_chr.encode()).hexdigest())
   else:
    print("")
  elif hsh_format == 'SHA224':
   if fun_type == 'encrypt':
    print(hashlib.sha224(cur_chr.encode()).hexdigest())
   else:
    print("")
  elif hsh_format == 'SHA256':
   if fun_type == 'encrypt':
    print(hashlib.sha256(cur_chr.encode()).hexdigest())
   else:
    print("")
  elif hsh_format == 'SHA384':
    if fun_type == 'encrypt':
      print(hashlib.sha384(cur_chr.encode()).hexdigest())
    else:
      print("")
  elif hsh_format == 'SHA512':
    if fun_type == 'encrypt':
      print(hashlib.sha512(cur_chr.encode()).hexdigest())
    else:
      print("")
  elif hsh_format == 'MD5':
    if fun_type == 'encrypt':
      print(hashlib.md5(cur_chr.encode()).hexdigest())
    else:
      print("")
  else:
    print("ERROR:")
    break
  run_turns += 1
 print("________________________________________")
 print("Would you like to do anything else?")
 cont = input("   : ")
 cont.lower
 if cont != 'no' or 'n':
     run_cont = False
 else:
     run_cont = True
