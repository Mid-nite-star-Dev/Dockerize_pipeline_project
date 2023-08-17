import pandas as pd 

data = [
{"Country": "USA", "Population": 328200000, "GDP": 21439400, "Unemployment": 3.8},
{"Country": "China", "Population": 1393000000, "GDP": 14342920, "Unemployment": 3.6},
{"Country": "Japan", "Population": 126500000, "GDP": 5082465, "Unemployment": 2.4},
{"Country": "Germany", "Population": 82790000, "GDP": 3845481, "Unemployment": 3.4},
{"Country": "India", "Population": 1354000000, "GDP": 2956756, "Unemployment": 6.1},
{"Country": "France", "Population": 66990000, "GDP": 2930535, "Unemployment": 8.0},
{"Country": "United Kingdom", "Population": 66440000, "GDP": 2825208, "Unemployment": 4.1},
{"Country": "Italy", "Population": 60480000, "GDP": 2086911, "Unemployment": 9.9},
{"Country": "Brazil", "Population": 209300000, "GDP": 1868626, "Unemployment": 11.6},
{"Country": "Canada", "Population": 37590000, "GDP": 1673625, "Unemployment": 5.6},
{"Country": "South Korea", "Population": 51310000, "GDP": 1660119, "Unemployment": 3.9},
{"Country": "Australia", "Population": 25200000, "GDP": 1403313, "Unemployment": 5.2},
{"Country": "Russia", "Population": 144500000, "GDP": 1402081, "Unemployment": 4.8},
{"Country": "Spain", "Population": 46560000, "GDP": 1394215, "Unemployment": 14.1},
{"Country": "Mexico", "Population": 126200000, "GDP": 1212294, "Unemployment": 3.3},
{"Country": "Indonesia", "Population": 267700000, "GDP": 1075216, "Unemployment": 5.3},
{"Country": "Netherlands", "Population": 17430000, "GDP": 909887, "Unemployment": 3.6},
{"Country": "Saudi Arabia", "Population": 33699947, "GDP": 793697, "Unemployment": 12.9},
{"Country": "Turkey", "Population": 82003882, "GDP": 754605, "Unemployment": 11.1},
{"Country": "Switzerland", "Population": 8541000, "GDP": 703080, "Unemployment": 2.6},
{"Country": "Nigeria", "Population": 214000000, "GDP": 448120, "Unemployment": 23.1},
]

df = pd.DataFrame(data)

# To find the highest populated country
highest_population_country = df[df['Population'] == df['Population'].max()]['Country'].values[0]

# Calculate the Average GDP across all countries
Average = df['GDP'].mean()


# To find the Country with the lowest Unemployment rate
lowest_Unemployment = df[df['Unemployment']==df['Unemployment'].min()]['Country'].values[0]

df = df.sort_values(by="GDP", ascending=False)

# Get the top 5 countries by GDP
top_5_countries = df.head(5)

# Calculate the total population of the top 5 countries
total_population = top_5_countries["Population"].sum()

# To find the number of countries with a GDP higher than 5 million?
million = df[df['GDP']>5000000]
numbers_of_countries = million.shape[0]

# Adding a new column 'GDP per capita' to Calculate the GDP per capita: for each countries
df['GDP_per_capita'] = df['GDP'] / df['Population']

# Find the country with the lowest GDP per capita
lowest_gdp_per_capita = df['GDP_per_capita'].min()
lowest_gdp_per_capita_country = df[df['GDP_per_capita'] == lowest_gdp_per_capita]['Country'].values[0]

print('My Name is Collins, and here are my answers: \n')

print(f'1. Country with the highest population: {highest_population_country}.')

print(f'2. Average GDP across all countries: {Average}.')

print(f'3. Country with the lowest Unemployment rate: {lowest_Unemployment}.')

print(f'4. The total population of the top 5 countries by GDP is" {total_population}.')

print(f'5. Number of countries with a GDP higher than 5 million: {numbers_of_countries}.')

print(f'6. The country with the lowest GDP per capita: {lowest_gdp_per_capita_country}.')