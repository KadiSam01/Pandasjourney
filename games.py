import pandas as pd 
games_list = "unit3/android-games.csv"
df = pd.read_csv(games_list)

def convert_number(value):
    val, amt = value.split(' ')
    val = float(val)
    if amt == 'M':
        val *= 10**6
    elif amt == 'k':
        val *= 10**3
    else:
        print(amt)
    return val

df["installs"] = df["installs"].apply(convert_number)
print("the most install game")
most_installs = df["installs"].max()
print(df[df["installs"]==most_installs]) 


print("the game with least instals game")
least_installs = df["installs"].min()
print(df[df["installs"]==least_installs])

print("game that you are required to pay")

required = True
print(df[df["paid"]==required.count()])
print("the total amount of games that are free")
print("what gamne is the least popular, looking at the the rating")
less_rating = df["1 star ratings"].min()
print(df[df["1 star ratings"]==less_rating])

print("the most popular games, looking the 5 star ratings")

most_rating = df["5 star ratings"].max()
print(df[df["5 star ratings"]==most_rating])
