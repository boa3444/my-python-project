print("Perfect song for the moment!")
print("For what occasion or moment do you want the music to be suited...\n"
"1. Fantasy vibes\n"
"2. Classical music\n"
"3. Rap beats")
user_input1= input("Press Enter to continue")

Fantasy_vibes =  [
    {"song": "abcdefu", "artist": "GAYLE", "vibe": "Rebellious enchantment, like a curse breaking"},
    {"song": "good 4 u", "artist": "Olivia Rodrigo", "vibe": "Dark fairy tale revenge, a witch's ballad"},
    {"song": "drivers license", "artist": "Olivia Rodrigo", "vibe": "Melancholy journey through a haunted forest"},
    {"song": "Happier Than Ever", "artist": "Billie Eilish", "vibe": "Unleashing a powerful, dragon-like roar"},
    {"song": "Therefore I Am", "artist": "Billie Eilish", "vibe": "Shadowy, mysterious, lurking in the castle shadows"},
    {"song": "Watermelon Sugar", "artist": "Harry Styles", "vibe": "Sun-drenched, whimsical meadow dance"},
    {"song": "As It Was", "artist": "Harry Styles", "vibe": "Nostalgic echo from a forgotten kingdom"},
    {"song": "Heat Waves", "artist": "Glass Animals", "vibe": "Dreamy, ethereal journey through a shimmering landscape"},
    {"song": "Levitating (feat. DaBaby)", "artist": "Dua Lipa", "vibe": "Soaring through the starlit sky on a magical steed"},
    {"song": "Blinding Lights", "artist": "The Weeknd", "vibe": "Fast-paced quest through a neon-lit fantasy city"},
    {"song": "Save Your Tears", "artist": "The Weeknd", "vibe": "Masked ball in a bewitched palace"},
    {"song": "Stay (with Justin Bieber)", "artist": "The Kid LAROI, Justin Bieber", "vibe": "A desperate plea echoing in an enchanted maze"},
    {"song": "Peaches (feat. Daniel Caesar & Giveon)", "artist": "Justin Bieber", "vibe": "Golden hour in a mythical garden"},
    {"song": "MONTERO (Call Me By Your Name)", "artist": "Lil Nas X", "vibe": "A descent into a vibrant, underworld realm"},
    {"song": "Industry Baby (feat. Jack Harlow)", "artist": "Lil Nas X, Jack Harlow", "vibe": "Triumphant march through a fantastical industrial landscape"},
    {"song": "Kiss Me More (feat. SZA)", "artist": "Doja Cat", "vibe": "Playful, enchanting encounter in a hidden grove"},
    {"song": "Say So", "artist": "Doja Cat", "vibe": "Groovy exploration of a magical marketplace"},
    {"song": "good boy gone bad", "artist": "TXT", "vibe": "A fallen angel's lament in a twilight realm"},
    {"song": "Anti-Romantic", "artist": "TXT", "vibe": "Yearning gaze from a lonely tower window"},
    {"song": "0X1=LOVESONG (I Know I Love You) feat. Seori", "artist": "TXT", "vibe": "A desperate cry across a desolate, frozen land"},
    {"song": "FEARLESS", "artist": "LE SSERAFIM", "vibe": "Confident stride through a field of magical blossoms"},
    {"song": "ANTIFRAGILE", "artist": "LE SSERAFIM", "vibe": "Growing stronger amidst shattered crystal shards"},
    {"song": "Hype Boy", "artist": "NewJeans", "vibe": "Energetic frolic through a whimsical dreamscape"},
    {"song": "Ditto", "artist": "NewJeans", "vibe": "Nostalgic longing in a snow-covered, timeless village"},
    {"song": "OMG", "artist": "NewJeans", "vibe": "Bewildered wonder in a surreal, shifting reality"},
    {"song": "Cupid - Twin Ver.", "artist": "FIFTY FIFTY", "vibe": "Sweet enchantment and whispered secrets in a moonlit garden"},
    {"song": "I AM", "artist": "IVE", "vibe": "Majestic ascent towards a celestial throne"},
    {"song": "Kitsch", "artist": "IVE", "vibe": "Stylish gathering in a uniquely decorated, otherworldly space"},
    {"song": "Super Shy", "artist": "NewJeans", "vibe": "Bashful encounter in a sparkling, hidden cove"},
    {"song": "ETA", "artist": "NewJeans", "vibe": "Urgent message carried by swift, mythical messengers"},
    {"song": "Seven (feat. Latto) - Clean Ver.", "artist": "Jung Kook", "vibe": "Devotion echoing through ancient temple ruins"},
    {"song": "Standing Next to You", "artist": "Jung Kook", "vibe": "Loyal guardian standing steadfast in a magical war"},
    {"song": " गुलाबी शरारा (Gulabi Sharara)", "artist": "Indeep Bakshi", "vibe": "Vibrant celebration in a royal, fantasy court (Note: This includes a popular Indian song that resonates with Gen Z and can have a fantasy aesthetic in its visuals and cultural context)"},
    {"song": "Bijlee Bijlee", "artist": "Harrdy Sandhu", "vibe": "Electric energy surging through a mystical landscape (Note: Another popular Indian song with potential for fantasy interpretation)"},
    {"song": "Kesariya", "artist": "Arijit Singh", "vibe": "Warm, glowing love like a magical sunrise (Note: A popular Bollywood song often associated with romantic, fairytale-like settings)"},
    {"song": "Calm Down (with Selena Gomez)", "artist": "Rema & Selena Gomez", "vibe": "Hypnotic rhythm drawing you into an enchanted dance"},
    {"song": "People", "artist": "Libianca", "vibe": "Searching for connection in a world filled with mystical beings"},
    {"song": "Flowers", "artist": "Miley Cyrus", "vibe": "Independent bloom in a resilient, magical garden"},
    {"song": "Kill Bill", "artist": "SZA", "vibe": "A vengeful spirit's elegant and deadly pursuit"},
    {"song": "Creepin' (with The Weeknd & 21 Savage)", "artist": "Metro Boomin, The Weeknd & 21 Savage", "vibe": "Shadowy figures lurking in a haunted, opulent setting"},
    {"song": "Unholy (feat. Kim Petras)", "artist": "Sam Smith & Kim Petras", "vibe": "Secret rituals in a decadent, hidden sanctuary"},
    {"song": "Die For You", "artist": "The Weeknd", "vibe": "Timeless devotion echoing through the ages"},
    {"song": "Golden", "artist": "Harry Styles", "vibe": "Radiant warmth spreading through a mystical dawn"},
    {"song": "Falling", "artist": "Harry Styles", "vibe": "Vulnerable moment in a grand, decaying castle"},
    {"song": "Adore You", "artist": "Harry Styles", "vibe": "Captivating gaze under a bewitching moonlight"},
    {"song": "Water", "artist": "Tyla", "vibe": "Fluid movements like a mystical water spirit"},
    {"song": "Paint The Town Red", "artist": "Doja Cat", "vibe": "Bold declaration in a vividly colored, fantastical town"},
    {"song": "Attention", "artist": "Doja Cat", "vibe": "Alluring presence in a mysterious, spotlighted realm"},
    {"song": "Vampire", "artist": "Olivia Rodrigo", "vibe": "A tale of draining enchantment and lost magic"},
    {"song": "Bad Habit", "artist": "Steve Lacy", "vibe": "A yearning echo in a dreamlike, hazy landscape"},
    {"song": "Late Night Talking", "artist": "Harry Styles", "vibe": "Whispered secrets under a canopy of stars"},
    {"song": "Daylight", "artist": "Harry Styles", "vibe": "Hopeful emergence into a bright, new fantasy world"},
    {"song": "Satellite", "artist": "Harry Styles", "vibe": "Orbiting with longing around a distant, radiant being"},
    {"song": "Boy's a liar Pt. 2 (feat. Ice Spice)"}]

Classical_music= [
    {"piece": "Clair de Lune", "composer": "Claude Debussy", "vibe": "Moonlit enchantment, shimmering ethereal beauty"},
    {"piece": "Gymnopédie No. 1", "composer": "Erik Satie", "vibe": "Ancient, serene landscape; timeless and slightly melancholic"},
    {"piece": "Peer Gynt Suite No. 1, Op. 46: I. Morning Mood", "composer": "Edvard Grieg", "vibe": "Dawn breaking over a mythical Nordic landscape"},
    {"piece": "Peer Gynt Suite No. 1, Op. 46: IV. In the Hall of the Mountain King", "composer": "Edvard Grieg", "vibe": "Grotesque and thrilling march of subterranean creatures"},
    {"piece": "Boléro", "composer": "Maurice Ravel", "vibe": "Hypnotic, growing intensity like a magical ritual unfolding"},
    {"piece": "Pavane pour une infante défunte", "composer": "Maurice Ravel", "vibe": "Regal and sorrowful dance for a departed princess of a mythical realm"},
    {"piece": "The Swan (from Carnival of the Animals)", "composer": "Camille Saint-Saëns", "vibe": "Graceful and serene movement of a mythical swan on a magical lake"},
    {"piece": "Arabesque No. 1", "composer": "Claude Debussy", "vibe": "Intricate and flowing patterns, like magical vines or water"},
    {"piece": "Gnossienne No. 1", "composer": "Erik Satie", "vibe": "Mysterious and introspective, evoking ancient secrets"},
    {"piece": "Adagio in G minor", "composer": "Remo Giazotto (attributed to Albinoni)", "vibe": "Profound sorrow and beauty, like a lament for a lost kingdom"},
    {"piece": "O Fortuna (from Carmina Burana)", "composer": "Carl Orff", "vibe": "Powerful and dramatic, like the turning wheel of fate in an epic saga"},
    {"piece": "Ride of the Valkyries (from Die Walküre)"}]

Rap_beats= [
    {"song": "Power", "artist": "Kanye West", "vibe": "Epic and godlike, the soundtrack to a ruler surveying their dominion"},
    {"song": "Run This Town (feat. Rihanna & Kanye West)", "artist": "JAY-Z", "vibe": "Anthemic rise to power in a fantastical urban kingdom"},
    {"song": "Ni**as in Paris", "artist": "JAY-Z & Kanye West", "vibe": "Opulent and larger-than-life, like wandering through a gilded, dreamlike city"},
    {"song": "Dark Fantasy", "artist": "Kanye West", "vibe": "A twisted fairy tale unfolding in a decadent court"},
    {"song": "All of the Lights", "artist": "Kanye West", "vibe": "Blinding and overwhelming, like the sensory overload of a magical metropolis"},
    {"song": "Otis (feat. Otis Redding)", "artist": "JAY-Z & Kanye West", "vibe": "Joyful and triumphant ride through a whimsical landscape"},
    {"song": "Gold Digger (feat. Jamie Foxx)", "artist": "Kanye West", "vibe": "A cautionary tale with a touch of exaggerated, almost mythical character types"},
    {"song": "Stronger", "artist": "Kanye West", "vibe": "Becoming an unstoppable force, like a hero imbued with newfound power"},
    {"song": "Good Life (feat. T-Pain)", "artist": "Kanye West"}]
import random

user_input2 = int(input("Choose (1) for Fantasy vibes\n"
"(2) for Classical music\n"
"(3) for Rap beats \n"))


newlist= []
if user_input2 == 1:
    newlist.extend(Fantasy_vibes)
    print(f" Your music of the moment is : {random.choice(newlist)}")




if user_input2 == 2:
    newlist.extend(Classical_music)
    print(f" Your music of the moment is : {random.choice(newlist)}")

if user_input2 == 3:
    newlist.extend(Rap_beats)
    print(f" Your music of the moment is : {random.choice(newlist)}")




