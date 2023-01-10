from data_reader import fasta_reader
from math import ceil

def find_start(data):
    for seq1 in data:
        found = True
        for seq2 in data:
            if seq1 == seq2 : continue
            counter = len(seq1)
            while counter > ceil(len(seq1)/2):
                if seq1[:counter] == seq2[-counter:] :
                    found = False
                    break
                
                counter -= 1
            if not found: break
        if found : return seq1
            


data = fasta_reader("rosalind_long.txt")
superstr = find_start(data)
print(superstr, "\n\n\n")
data.remove(superstr)
bong = True

while len(data) != 0 :
    for seq in data :
        index = ceil(3/4*len(seq))
        while index > ceil(len(seq)/2):
            if superstr[-index:] == seq[:index]:
                superstr = superstr + seq[index:]
                data.remove(seq)
                break
            index -= 1
        
print(superstr)
