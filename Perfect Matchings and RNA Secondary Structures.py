from data_reader import fasta_reader
from math import factorial

string = str(fasta_reader("rosalind_pmch.txt"))
a = string.count('A')
c = string.count('C')

print(factorial(a) * factorial(c))
