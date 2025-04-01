print("Perfect song for the moment!")
print("For what occasion or moment do you want the music to be suited...\n"
"1. Fantasy vibes\n"
"2. Post breakup music\n"
"3. Classical music\n"
"4. Rap beats")
user_input1= input("Press Enter to continue")

Fantasy_vibes = ["'Lothlórien' by Howard Shore",
                 " 'Dragon Age: Inquisition Soundtrack' by Inon Zur",
                 "'The Shire' by Howard Shore",
                  "The Witcher 3: Wild Hunt Soundtrack by Marcin Przybyłowicz"]
Post_breakup_music= ["'Someone Like You' by Adele", 
"'Back to December' by Taylor Swift", 
"'Irreplaceable' by Beyoncé",
"'Let Her Go' by Passenger"]

Classical_music= ['"Clair de Lune" by Claude Debussy',
'"Symphony No. 5" by Ludwig van Beethoven',
'"The Four Seasons" by Antonio Vivaldi',
'"Nocturne in E-flat Major, Op. 9 No. 2" by Frédéric Chopin']

Rap_beats= ['"Sicko Mode" by Travis Scott',
"'God's Plan' by Drake" ,
'"HUMBLE." by Kendrick Lamar',
'"Juicy" by The Notorious B.I.G.']


import random

user_input2 = int(input("Choose (1) for Fantasy vibes\n"
"(2) for Post breakup music\n"
"(3) for Classical music\n"
"(4) for Rap beats \n"))


newlist= []
if user_input2 == 1:
    newlist.extend(Fantasy_vibes)
    print(f" Your music of the moment is : {random.choice(newlist)}")


if user_input2 == 2:
    newlist.extend(Post_breakup_music)
    print(f" Your music of the moment is : {random.choice(newlist)}")

if user_input2 == 3:
    newlist.extend(Classical_music)
    print(f" Your music of the moment is : {random.choice(newlist)}")

if user_input2 == 4:
    newlist.extend(Rap_beats)
    print(f" Your music of the moment is : {random.choice(newlist)}")




