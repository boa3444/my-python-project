import string
lowercase = list(string.ascii_lowercase)


    
def cryption():
    user_input1 = input("Type 'decode' to decrypt and 'encode' to encrypt.\n")
    if user_input1== 'encode':
        message =input("Type your message.\n")
        shift_number = int(input("Type your shift number.\n"))
        message_to_be_filled= ''
        for each_letter in message:
            if each_letter in lowercase:
                each_letter_index = lowercase.index(each_letter)
                new_each_letter_index = (each_letter_index-26) + shift_number
                message_to_be_filled += lowercase[new_each_letter_index]
        
        
        print(message_to_be_filled)        

    elif user_input1== 'decode':
        message =input("Type your message.\n")
        shift_number = int(input("Type your shift number.\n"))
        message_to_be_filled= ''
        for each_letter in message:
            if each_letter in lowercase:
                each_letter_index = lowercase.index(each_letter)
                new_each_letter_index =  (each_letter_index - 26)  - shift_number ###
                message_to_be_filled += lowercase[new_each_letter_index]
        print(message_to_be_filled) 
    else:
        print("***Invalid input***")

cryption()
to_continue= input("Type 'continue' to do this again or type 'end' to stop this.\n").lower()
    
while to_continue== 'continue':
    cryption()
    to_continue= input("Type 'continue' to do this again or type 'end' to stop this.\n").lower()

    

