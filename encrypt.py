# Script to encrypt the Message
# Daniel Kim 11/28/2018


def create_xor_array(word):
    array = []
    # Make the word uppercase
    word = word.upper()
    # Compare against '32' using XOR and store in array
    for x in word:
        if x == ' ':
            array.append(ord(x))
        else:
            array.append(ord(x) ^ 32)
    return array


def create_adj_matrix(input_num):
    s = '['
    cur = 1
    base = format(input_num, 'b')
    flag = True
    for x in base:
        if flag:
            flag = False
        else:
            if x == '1':
                s = s + str(cur)
                cur = 1
            else:
                cur += 1
    # Case of ending with '0'
    s += str(cur)
    s += ']'
    return s


# Main Method
message = input('Enter the phrase you want to be encrypted in a super sneaky way: ')
xor_array = create_xor_array(message)
encrypt = ''
for element in xor_array:
    encrypt += create_adj_matrix(element)
print('Here is your super secret message.')
print(encrypt)
