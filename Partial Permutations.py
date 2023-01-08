from math import factorial
from data_reader import read_data

numbers= read_data("rosalind_pper.txt").split(" ")
numerator = factorial(int(numbers[0]))
deonominator = factorial(int(numbers[0])-int(numbers[1]))
print((numerator/deonominator)%1_000_000)
