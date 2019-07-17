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
alphaCounter = 0
conversionHolder = 0
block = ''
i = 0
x = 0
currentAlpha = 0

#Variable for output
finalMessage = ''

print('Would you like to encrypt or decrypt?')
prgFunction = input(str(':'))

if prgFunction == 'encrypt':
    print('What form of encryption would you like to do?')
    encryptType = input(str(':'))
    print('What is the message?')
    inputMsg = input(str(':'))
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
    print('What format is your message encrypted in?')
    encryptType = input(str(':'))
    print('What is the secret code?')
    inputMsg = input(str(':'))
    while x <= len(inputMsg):
        if encryptType == 'md5':
            while i+x <= x+31:
                currentAlpha = x + i
                block += inputMsg[currentAlpha]
                i += 1
            i = 0
            while alphaCounter <= 62:
                conversionHolder = chrList[alphaCounter]
                conversionHolder = hashlib.md5(conversionHolder.encode()).hexdigest()
                if block == conversionHolder:
                    finalMessage += chrList[alphaCounter]
                    alphaCounter = 100
                else:
                    alphaCounter += 1
            alphaCounter = 0
            block = ''
            x += 32
            if x >= len(inputMsg):
                print(finalMessage)
        elif encryptType == 'sha1':
            while i+x <= x+39:
                currentAlpha = x + i
                block += inputMsg[currentAlpha]
                i += 1
            i = 0
            while alphaCounter <= 62:
                conversionHolder = chrList[alphaCounter]
                conversionHolder = hashlib.sha1(conversionHolder.encode()).hexdigest()
                if block == conversionHolder:
                    finalMessage += chrList[alphaCounter]
                    alphaCounter = 100
                else:
                    alphaCounter += 1
            alphaCounter = 0
            block = ''
            x += 40
            if x >= len(inputMsg):
                print(finalMessage)
        elif encryptType == 'sha224':
            while i+x <= x+55:
                currentAlpha = x + i
                block += inputMsg[currentAlpha]
                i += 1
            i = 0
            while alphaCounter <= 62:
                conversionHolder = chrList[alphaCounter]
                conversionHolder = hashlib.sha224(conversionHolder.encode()).hexdigest()
                if block == conversionHolder:
                    finalMessage += chrList[alphaCounter]
                    alphaCounter = 100
                else:
                    alphaCounter += 1
            alphaCounter = 0
            block = ''
            x += 56
            if x >= len(inputMsg):
                print(finalMessage)
        elif encryptType == 'sha256':
            while i+x <= x+63:
                currentAlpha = x + i
                block += inputMsg[currentAlpha]
                i += 1
            i = 0
            while alphaCounter <= 62:
                conversionHolder = chrList[alphaCounter]
                conversionHolder = hashlib.sha256(conversionHolder.encode()).hexdigest()
                if block == conversionHolder:
                    finalMessage += chrList[alphaCounter]
                    alphaCounter = 100
                else:
                    alphaCounter += 1
            alphaCounter = 0
            block = ''
            x += 64
            if x >= len(inputMsg):
                print(finalMessage)
        elif encryptType == 'sha384':
            while i+x <= x+95:
                currentAlpha = x + i
                block += inputMsg[currentAlpha]
                i += 1
            i = 0
            while alphaCounter <= 62:
                conversionHolder = chrList[alphaCounter]
                conversionHolder = hashlib.sha224(conversionHolder.encode()).hexdigest()
                if block == conversionHolder:
                    finalMessage += chrList[alphaCounter]
                    alphaCounter = 100
                else:
                    alphaCounter += 1
            alphaCounter = 0
            block = ''
            x += 96
            if x >= len(inputMsg):
                print(finalMessage)
        elif encryptType == 'sha512':
            while i+x <= x+127:
                currentAlpha = x + i
                block += inputMsg[currentAlpha]
                i += 1
            i = 0
            while alphaCounter <= 62:
                conversionHolder = chrList[alphaCounter]
                conversionHolder = hashlib.sha256(conversionHolder.encode()).hexdigest()
                if block == conversionHolder:
                    finalMessage += chrList[alphaCounter]
                    alphaCounter = 100
                else:
                    alphaCounter += 1
            alphaCounter = 0
            block = ''
            x += 128
            if x >= len(inputMsg):
                print(finalMessage)
else:
    print('ERROR: Invalid program function')
print(finalMessage)
