from prettytable import PrettyTable


poke_table = PrettyTable()

poke_table.add_column("Pokemon Name",["Pikachu", "Raichu", "Onyx"])

poke_table.add_column("Skill Type", ["Electric","Electric","Fire"])

poke_table.add_autoindex()
poke_table.align = "l"

print(poke_table)