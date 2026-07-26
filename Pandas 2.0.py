import pandas as SketchingIsCool

Dictionary = {"Star Wars":["A New Hope", "The Empire Strikes Back", "Return of the Jedi", "The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],
              "Ratings": ["5", "4", "2", "3", "6", "1"]}

print(type(Dictionary))

Star_Wars = SketchingIsCool.DataFrame(Dictionary)
print(Star_Wars)
print(type(Star_Wars))
Star_Wars = Star_Wars.sort_values(by = "Ratings")
print(Star_Wars)
That_One_Weird_Sad_Thing = SketchingIsCool.read_csv("/Users/puspendra/Data Science/That_One_weird-Sad_Thing.csv")
print(That_One_Weird_Sad_Thing)
print(That_One_Weird_Sad_Thing.head(5))
print(That_One_Weird_Sad_Thing.tail(5))
That_One_Weird_Sad_Thing.info()
print(That_One_Weird_Sad_Thing.describe())
print(That_One_Weird_Sad_Thing.shape)
print(That_One_Weird_Sad_Thing["Age"].mean())