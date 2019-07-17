#python3

import hashlib

#Character list for decryption
chrList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
            'O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b',
            'c','d','e','f','g','h','i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x','y','z',' ','1','2','3',
            '4','5','6','7','8','9','0']

#Variables for user input
prgFunction = ''
encryptType = ''
inputMsg = ''

#Variables for encryption
currentLetterNum = 0
currentLetter = ''

#Variable for decryption
currentBlock = 0
currentLetterNum = 0
currentBlockList = ''
chrListCheck = 0
chrCheck = ''

#Variable for output
finalMessage = ''

print('Would you like to encrypt or decrypt?')
prgFunction = input(str(':'))
print('What form of encryption would you like to do?')
encryptType = input(str(':'))
print('What is the message?')
inputMsg = input(str(':'))

if prgFunction == 'encrypt':
    while currentLetterNum +1 <= len(inputMsg):
        if encryptType =='md5':
            currentLetter = inputMsg[currentLetterNum]
            currentLetter = hashlib.md5(currentLetter.encode()).hexdigest()
        elif encryptType == 'sha1':
            currentLetter = inputMsg[currentLetterNum]
            currentLetter = hashlib.sha1(currentLetter.encode()).hexdigest()
        elif encryptType == 'sha224':
            currentLetter = inputMsg[currentLetterNum]
            currentLetter = hashlib.sha224(currentLetter.encode()).hexdigest()
        elif encryptType == 'sha256':
            currentLetter = inputMsg[currentLetterNum]
            currentLetter = hashlib.sha256(currentLetter.encode()).hexdigest()
        elif encryptType == 'sha384':
            currentLetter = inputMsg[currentLetterNum]
            currentLetter = hashlib.sha384(currentLetter.encode()).hexdigest()
        elif encryptType == 'sha512':
            currentLetter = inputMsg[currentLetterNum]
            currentLetter = hashlib.sha512(currentLetter.encode()).hexdigest()
        else:
            print('ERROR: Invalid Type')
            break
        finalMessage += currentLetter
        currentLetterNum += 1
elif prgFunction == 'decrypt':
    if encryptType == 'md5':
        while currentBlock+currentLetterNum <= len(inputMsg):
            while currentBlock+currentLetterNum <= currentLetterNum+31:
                currentBlockList += inputMsg[currentBlock + currentLetterNum]
                currentLetterNum += 1
            while chrListCheck <= 62:
                chrCheck = chrList[chrListCheck]
                chrCheck = hashlib.md5(chrCheck.encode()).hexdigest()
                if chrCheck == currentBlockList:
                    finalMessage += chrList[chrListCheck]
                    chrListCheck = 1000
                    print(finalMessage)
                else:
                    chrListCheck += 1
            currentLetterNum = 0
            currentBlock += 32
            chrListCheck = 0
else:
    print('ERROR: Invalid program function')
print(finalMessage)
