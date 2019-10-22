# Adding odd integers exercise

a = int(input("Input lower bound: "))
b = int(input("Input upper bound: "))
sum = 0

for i in range(a, b+1):
        if i % 2 != 0:
            sum += i

print("The sum of odd integers between", a, "and", b, "is", str(sum))
