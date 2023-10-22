'''
recursion
'''

def reverse_string(myString):
    if len(myString)==1:
        return myString[0]
    else:
        return reverse_string(myString[1:]) + myString[0]


def palindrome(myString):   
    first = myString[0]
    last = myString[-1]
    if len(myString)==1:
        return True
    elif first == last:
        if len(myString)==2:
            return True
        return palindrome(myString[1:-1])
    else:
        return False

def check_char(char):       #returns true if alpha character
    condition = ((chr(char)>=65) and (chr(char)<=90)) or ((chr(char)>=97) and (chr(char)<=122))
    return condition

def palindromews(val):       #removes spaces and other characters and ignore case
    myString = ''
    for ch in val:
        if ((ord(ch)>=65) and (ord(ch)<=90)) or ((ord(ch)>=97) and (ord(ch)<=122)):
            myString = myString+ch.lower()
    print('myString is: ',myString)
    first = myString[0]
    last = myString[-1]
    if len(myString)==1:
        return True
    elif first == last:
        if len(myString)==2:
            return True
        return palindrome(myString[1:-1])
    else:
        return False



mystr = "bantab"
print(palindrome(mystr))