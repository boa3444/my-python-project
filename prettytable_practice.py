import prettytable

table_creator = prettytable.PrettyTable()

table_creator.field_names = ["col1" , "col2", "col3"]
table_creator.add_row(["a00", "a01", "ahah"])

# table_creator.add_row(["a10", "a11"])

print(table_creator)