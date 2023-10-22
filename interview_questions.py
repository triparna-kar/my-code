"""
General Programs at interviews.
"""

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "()[]{}"
# Output: true
# Example 3:
# Input: s = "(]"
# Output: false

def bracket(mystr):
    """
    verify bracket validity
    """
    mystring = mystr
    validity = True
    stack = list()
    open_strings = ['(', '{', '[']
    close_strings = [')', '}', ']']

    for item in mystring:
        if item in open_strings:
            stack.append(item)
        elif item in close_strings:
            get_top_stack = stack[-1]
            if close_strings.index(item) == open_strings.index(get_top_stack):
                stack.pop()
                validity = validity and True
            else:
                validity = validity and False
                break
        else:
            print("Incorrect string")
    if len(stack) != 0:
        validity = validity and False
    print("String {} is {}".format(mystr, validity))
    return validity


mystr = "[()]{}{[()()]()}"
bracket(mystr)

###################################################################################################################3

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. 
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false

def anagram(str1, str2):
    """
    Check string is anagram
    """
    anagram = True
    str_stack = list(str1)
    for char in str2:
        if char in str_stack:
            anagram = anagram and True
            str_stack.remove(char)
        else:
            anagram = anagram and False
            break
    if len(str_stack) != 0:
        anagram = anagram and False
    return anagram

str1 = "anagram"
str2 = "nagaram"
print("String Anagram: " + str(anagram(str1, str2)))


###################################################################################################################

# Mirror this matrix -

# [1, 0, 0]
# [0, 1, 0]
# [0, 0, 1]

# Into 

# [0, 0, 1]
# [0, 1, 0]
# [1, 0, 0]


def mirror(matrix):
    """
    mirror matrix
    """
    new_matrix = list()
    for row in matrix:
        reverse = row[::-1]
        new_matrix.append(reverse)
    
    print ("*** Mirrored Matrix ***")
    for row in new_matrix:
        print(str(row))

    return new_matrix


matrix = [[1,0,0],[0,1,0],[0,0,1]]

mirror(matrix)

#################################################################

# Transpose this matrix - 
# [2, 3, 4] 
# [5, 8, 5]
# Into 
# [2, 5]
# [3, 8]
# [4, 5]

# [00, 01, 02]
# [10, 11, 12]

# [00, 01]
# [10, 11]
# [20, 21]


def transpose(matrix):
    """
    Transpose Matrix
    """
    
    row_length = len(matrix)
    print("row_length: " + str(row_length))
    col_length = len(matrix[0])
    print("col_length: " + str(col_length))
    new_matrix = list()

    for i in range(col_length):
        new_matrix.append(list())
        for j in range(row_length):
            new_matrix[i].append(None)

    for i in range(row_length):        
        for j in range(col_length):
            new_matrix[j][i] = matrix[i][j]            
             

matrix = [[2,3,4], [5,8,5]]
transpose(matrix)

#################################################################

# Password: max length 8, 1 cap, 1 small, 1 spcl char, alphanumeric
# Return if password is valid or invalid

def check_password(password):
    status = True
    if len(password) >= 8:
        status = status and True
    else:
        status = status and False
    
    cap_found = False
    small_found = False
    num_found = False
    spl_found = False

    for character in password:
        if ord(character) >= 97 and ord(character) <= 122:
            small_found = True
        if ord(character) >=65 and ord(character) <= 90:
            cap_found = True
        if character in ['0','1','2','3','4','5','6','7','8','9']:
            num_found = True
        
        # Check Special Characters:
        asc = ord(character)
        if asc in range(32, 48) or asc in range(58,65) or asc in range(91,97) or asc in range(123, 127):
            spl_found = True
    
    status = status and cap_found and small_found and num_found and spl_found
    return status

password = "             "
print(check_password(password))

#################################################################

