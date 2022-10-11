import random

letterArray = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numberArray =['1','2','3','4','5','6','7','8','9','0']
specCharArray =['(',')','{','}','[',']','|','`','!','"','$','%','^','&','*','"','<','>',':',';','#','~','_','-','+','=',',','@',']']
str = ''
saveQuery = input('save to passwords.txt? yes/no')
if saveQuery == 'yes':
    passUse = input('what is this password for?')
letters = input('do you want letters? yes/no')
if letters == 'yes':
    caps = input('do you want random caps? yes/no')
numbers = input('do you want numbers? yes/no')
specChar = input('do you want special characters? yes/no')
length = input('How long do you want your password')
for i in range(0, int(length)):
    ranFloat = random.random()
    if letters == 'yes':
        if ranFloat <= 0.33:
            newLetter = letterArray[random.randrange(0,26,1)]
            if caps == 'yes':
            #checks if caps is 'yes'
                if random.random() <= 0.5:
                    newLetter = newLetter.upper()
            str = str + newLetter
    if numbers == 'yes':
        if ranFloat < 0.66 and ranFloat > 0.33:
            newNumber = numberArray[random.randrange(0,10,1)]
            str = str + newNumber
    if specChar == 'yes':
        if ranFloat >= 0.66:
            newSpecChar = specCharArray[random.randrange(0,29,1)]
            str = str + newSpecChar
if saveQuery == 'yes':
    file_object = open('passwords.txt', 'a')
    file_object.write(passUse + ': ' + str + '\n')
    file_object.close()
print(str)
