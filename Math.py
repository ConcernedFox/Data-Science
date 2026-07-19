import math

print("Give me a Permutation in this format.#P#")
A = int(input("What is the first Number. It must be bigger than the next number."))
B = int(input("What is the second Number. It must be snaller than the previous number."))

Permutation = math.factorial(A)/math.factorial(A-B)

print("Give me a Combination in this format.#C#")

C = int(input("What is the first Number. It must be bigger than the next number."))
D = int(input("What is the second Number. It must be snaller than the previous number."))

Combination = math.factorial(C)/(math.factorial(D) * math.factorial(C-D))

print(int(Permutation))
print("This is the permutation")


print(int(Combination))
print("This is the combination")