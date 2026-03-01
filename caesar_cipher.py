
letters=[chr(i) for i in range(ord('a'), ord('z') + 1)]

def find_ind_of_letter(letter):
    i=0
    for char in letters:
        if letter == char:
            return i 
        
        i += 1

# print(find_ind_of_letter("e"))

def encrypt( message , shift_num):

    encrypted_mess = []
    for char in message:
        index = find_ind_of_letter(char)
        new_index = index + shift_num  #shifting to right
        encrypted_mess.append(letters[new_index])

    return encrypted_mess


def decrypt(message , shift_num):
    decrypted_mess = []
    for char in message:
        index = find_ind_of_letter(char)
        new_index= index - shift_num   # shifting to left
        decrypted_mess.append(letters[new_index])

    return decrypted_mess


user_input = "y"

while user_input == "y":
    enc_dec = input ("You wanna encrypt or decrypt? ").lower()
    message = input("Type message: ").lower()
    shift_num = int(input("Shift number :"))
    if enc_dec == "encrypt":
        result = encrypt(message , shift_num)
        print(f"Encrypted result: {''.join(result)}")

    elif enc_dec == "decrypt":
        result = decrypt(message , shift_num)
        print(f"Decrypted result: {''.join(result)}")

    else:
        print("Input 'encrypt' or 'decrypt' only")

    user_input= input("You wanna do this again (y/n)?\n").lower()

    if user_input == "n":
        print("Sayonara...")