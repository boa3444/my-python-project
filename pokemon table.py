from prettytable import PrettyTable , HRuleStyle
table = PrettyTable()
table.border= True
table.align= "r"


table.add_column("Pokemon Names",[
    "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise",
    "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot",
    "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash",
    "Nidoran♀", "Nidorina", "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable",
    "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect",
    "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape",
    "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop",
    "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler",
    "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio",
    "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno",
    "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan",
    "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra",
    "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros",
    "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte",
    "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite",
    "Mewtwo", "Mew"
])
table.add_column("Type", ["Grass, Poison", "Grass, Poison", "Grass, Poison", "Fire", "Fire", "Fire, Flying",
    "Water", "Water", "Water", "Bug", "Bug", "Bug, Flying", "Bug, Poison", "Bug, Poison",
    "Bug, Poison", "Normal, Flying", "Normal, Flying", "Normal, Flying", "Normal", "Normal",
    "Normal, Flying", "Normal, Flying", "Poison", "Poison", "Electric", "Electric", "Ground",
    "Ground", "Poison", "Poison", "Poison", "Poison", "Poison", "Poison", "Fairy", "Fairy",
    "Fire", "Fire", "Normal, Fairy", "Normal, Fairy", "Grass, Poison", "Grass, Poison",
    "Grass, Poison", "Bug, Grass", "Bug, Grass", "Bug, Poison", "Bug, Poison", "Ground",
    "Ground", "Normal", "Normal", "Water", "Water", "Fighting", "Fighting", "Fire", "Fire",
    "Water", "Water", "Water, Fighting", "Psychic", "Psychic", "Psychic", "Fighting", "Fighting",
    "Fighting", "Grass, Poison", "Grass, Poison", "Grass, Poison", "Water", "Water", "Rock, Ground",
    "Rock, Ground", "Rock, Ground", "Fire", "Fire", "Water, Psychic", "Water, Psychic",
    "Electric", "Electric", "Normal, Flying", "Normal, Flying", "Normal, Flying", "Water", "Water",
    "Poison", "Poison", "Water", "Water, Ice", "Ghost, Poison", "Ghost, Poison", "Ghost, Poison",
    "Rock, Ground", "Psychic", "Psychic", "Water", "Water", "Electric", "Electric", "Grass, Psychic",
    "Grass, Psychic", "Ground", "Ground", "Fighting", "Fighting", "Normal", "Poison", "Poison",
    "Ground, Rock", "Ground, Rock", "Normal", "Grass", "Normal", "Water", "Water", "Water", "Water",
    "Water", "Water, Psychic", "Psychic", "Bug, Flying", "Ice, Psychic", "Electric", "Fire", "Bug",
    "Normal", "Water", "Water, Flying", "Water, Ice", "Normal", "Normal", "Water", "Electric", "Fire",
    "Normal", "Rock, Water", "Rock, Water", "Rock, Water", "Rock, Water", "Rock, Flying", "Normal",
    "Ice, Flying", "Electric, Flying", "Fire, Flying", "Dragon", "Dragon", "Dragon", "Psychic", "Psychic"])
print(table)