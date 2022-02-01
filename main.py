# phrase = "The Zen of Python"
# sound = " ".join(list(map(lambda w: w + "!", phrase.split())))
# print(sound)

# from functools import reduce
# from statistics import mean, median
# nums = list(range(50))
# tenfold = list((n * 10 for n in nums))
# print(tenfold)
# div7 = list((n for n in nums if n % 7 == 0))
# print(div7)
# squares = list((n **2 for n in nums))
# print(squares)
# sqsums = reduce(lambda x, y: x + y, squares)
# print(sqsums)
# print(min(squares))
# print(max(squares))
# print(mean(squares))
# print(median(squares))
# print(sorted(squares, reverse=True))

# mylist = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
# sumos = sum(x for x in mylist if type(x) == int or type(x) is float)
# print(sumos)
# strings = " ".join(w for w in mylist if type(w) == str)
# print(strings)
# num_of_booleans = sum(type(c) is bool for c in mylist)
# print(num_of_booleans)

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return (f"[{self.name}, {self.age}]")

# petras = Human("Petras", 45)
# antanas = Human("Antanas", 39)
# jonas = Human("Jonas", 42)

# kgb_files = []
# kgb_files.append(petras)
# kgb_files.append(antanas)
# kgb_files.append(jonas)

# print(kgb_files)

# from operator import attrgetter
# sort_by_name = sorted(kgb_files, key=attrgetter("name"), reverse=True)
# sort_by_age = sorted(kgb_files, key=attrgetter("age"), reverse=True)
# print(sort_by_name)
# print(sort_by_age)