import pandas as pd

squirrel_data= pd.read_csv(r"C:\Users\newon\Downloads\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250626.csv")
DF= pd.DataFrame(squirrel_data)

fur_color = []

for color in DF['Primary Fur Color']:
    # print(color)
    fur_color.append(color)

black= fur_color.count("Black")
gray= fur_color.count("Gray")
cinnamon = fur_color.count("Cinnamon")

final_count= {
    'black': black, 
    'gray':gray, 
    'cinnamon':cinnamon
    }


squirrel_color_data= pd.Series(final_count)
# print(squirrel_color)




squirrel_color_data.to_csv('squirrel_color.csv') 
    # sq.write()