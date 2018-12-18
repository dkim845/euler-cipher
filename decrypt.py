# Script to decrypt the Message
# Daniel Kim 11/28/2018


def parse_message(message):
    array = []
    temp = ''
    for x in message:
        # End of a character
        if x == ']':
            array.append(temp)
            temp = ''
        # Case of any character besides the start
        elif x != '[':
            temp += x
    return array


def decrypt_adj_matrix(matrix):
    letter = ''
    for x in matrix:
        letter += '1'
        if x != '1':
            for y in range(0, int(x)-1):
                letter += '0'
    return chr(int(letter, 2))


# Main method
word = input('Ok super hacker, what is the message you want to decrypt: ')
arr = parse_message(word)
decrypted = ''
for element in arr:
    decrypted += decrypt_adj_matrix(element)
print("Here is the decrypted message!!!")
print(decrypted)

