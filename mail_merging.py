

with open(r".\Input\Names\invited_names.txt") as invited_names_txt:
    for name in invited_names_txt:
        name = name.strip()   #removed \n

        #letters to send to friends:
        final_letter = f".\Output\ReadyToSend\Letter_To_{name}.txt"

    
        with open( final_letter, mode = 'w') as finalletters:
            with open(r".\Input\Letters\starting_letter.txt") as blueprint_letter:
                bp_contents= blueprint_letter.read()
                with_correct_salutation = bp_contents.replace("[name]", name)
    
            finalletters.write(with_correct_salutation)