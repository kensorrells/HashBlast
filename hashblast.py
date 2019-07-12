#python3

import hashlib

txt_ent = 1
fun_type = 1
hsh_format = 1
run_cont = True
run_turns = 0
chr_num = 0
cur_chr = 0
msg_aft = ''
x=0
i=0
a=0
cant = ''
while run_cont == True:
 print("Please choose your format.")
 hsh_format = input("Format: ")
 print("Would you like to encrypt or decrypt?")
 fun_type = input("Function: ")
 print("Please enter the text.")
 txt_ent = input("Text: ")
 chr_num = len(txt_ent)
 print("_______________________________________________")
 while run_turns +1 <= chr_num:
  cur_chr = txt_ent[run_turns]
  if fun_type == 'encrypt':
   txtsha1 = hashlib.sha1(cur_chr.encode()).hexdigest()
   txtsha224 = hashlib.sha224(cur_chr.encode()).hexdigest()
   txtsha256 = hashlib.sha256(cur_chr.encode()).hexdigest()
   txtsha384 = hashlib.sha384(cur_chr.encode()).hexdigest()
   txtsha512 = hashlib.sha512(cur_chr.encode()).hexdigest()
   txtmd5 = hashlib.md5(cur_chr.encode()).hexdigest()
   if hsh_format == 'sha1':
    msg_aft += txtsha1
   elif hsh_format == 'sha224':
    msg_aft += txtsha224
   elif hsh_format == 'sha256':
    msg_aft += txtsha256
   elif hsh_format == 'sha384':
    msg_aft += txtsha384
   elif hsh_format == 'sha512':
    msg_aft += txtsha512
   else:
    msg_aft += txtmd5
    run_turns += 1
  else:
    chrlist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           ' ','1','2','3','4','5','6','7','8','9','0']
    fnl_msg = ''
    cent = txt_ent
    if hsh_format == 'sha1':
      while x <= len(cent):
        while i+x <= x+39:
         y = x + i
         cant += cent[y]
         print(cant)
         i += 1
        i = 0
        while a <= 62:
          b = chrlist[a]
          b =  hashlib.sha1(b.encode()).hexdigest()
          if cant == b:
            fnl_msg += chrlist[a]
            print(fnl_msg)
            a = 100
          else:
            a += 1
        a = 0
        cant = ''
        x += 40
        print(fnl_msg)
  run_turns += 1
 print(msg_aft)
 print("_______________________________________________")
 print("Would you like to do anything else?")
 cont = input("   : ")
 cont.lower
 if cont != 'no' or 'n':
     run_cont = False
 else:
     run_cont = True
