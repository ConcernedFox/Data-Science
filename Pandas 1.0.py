import pandas as pd

Vihaan_Ratings = [4, 3, 5, 4, 4, 4]
print(Vihaan_Ratings)
Public_Ratings = [2, 3, 4, 5, 5, 5, 2, 1, 1]
print(Public_Ratings)
Box_Office = [4, 3, 3, 2, 2, 2, 5, 5, 5]


Series1 = pd.Series(Vihaan_Ratings, index = ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith", "A New Hope", "The Empire Strikes Back", "Return of the Jedi"])
Series2 = pd.Series(Public_Ratings, index = ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith", "A New Hope", "The Empire Strikes Back", "Return of the Jedi", "The Force Awakens", "The Last Jedi", "The Rise of Skywalker"])
Series3 = pd.Series(Box_Office, index = ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith", "A New Hope", "The Empire Strikes Back", "Return of the Jedi", "The Force Awakens", "The Last Jedi", "The Rise of Skywalker"])

print(Series1)

print(Series1.mean())
print(Series1.sum())
print(Series1.median())
print(Series1.count())
print(Series1.min())
print(Series1.max())
print(Series1.mode())
print(Series1.sort_values())
print(Series1.sort_values(ascending = False))
print(Series1.value_counts())
