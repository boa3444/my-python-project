# receiver= "[name]"

with open(r".\Input\Names\invited_names.txt") as invited_names:
    for name in invited_names:
        name = name.strip()
        final_letter = f".\Output\ReadyToSend\Letter_To_{name}.txt"

        with open( final_letter, mode = 'w') as finalletter:
            salutation = f"Dear {name},"
            finalletter.write(salutation)
            finalletter.write('''\n
You are invited to my birthday this Saturday.

Hope you can make it!

~Divyanshi''')

        