import matplotlib.pyplot as plots

x = ["The Prophecies Begin","The New Prophecy", "Power of Three", "Omen of the Stars", "Dawn of the Clans", "A Vision of Shadows", "The Broken Code", "A Starless Clan"]
y = [9, 1, 7, 7.5, 2, 8, 10, 9]
x2 = [0,10,20,30,40,50,60,70,80,90,100]
y2 = [13, 18, 24, 42, 37, 19, 11, 9, 4, 1, 73, 21, 86, 24, 82]
plots.bar(x, y)
plots.xticks(rotation = 45)

plots.show()
plots.pie(y, labels = x, autopct = "%1.1f%%")
plots.show()

plots.hist(y2, x2, rwidth = .00099999999999999999999999999)
plots.show()