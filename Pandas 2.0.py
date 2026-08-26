import pandas as SketchingIsCool

Dictionary = {"Star Wars":["A New Hope", "The Empire Strikes Back", "Return of the Jedi", "The Phantom Menace", "Attack of the Clones", "Revenge of the Sith", "The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
              "Ratings": ["5", "4", "2", "3", "6", "1", "7", "9", "8"]}

print(type(Dictionary))

Star_Wars = SketchingIsCool.DataFrame(Dictionary)
print(Star_Wars)
print(type(Star_Wars))
Star_Wars = Star_Wars.sort_values(by = "Ratings")
print(Star_Wars)
