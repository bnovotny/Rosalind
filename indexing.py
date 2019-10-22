#Take a slice of a string based on 4 indices

input_str = input("Input string to slice: ")

first_int = int(input("Input first integer: "))
second_int = int(input("Input second integer: "))
third_int = int(input("Input third integer: "))
fourth_int = int(input("Input fourth integer: "))

print(input_str[first_int:second_int+1] + " " + input_str[third_int:fourth_int+1])