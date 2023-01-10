from data_reader import fasta_reader

sequence = fasta_reader("rosalind_sseq.txt")
seq1 = str(sequence[0])
seq2 = str(sequence[1])
index = [0]
for char in seq2:
    index.append(seq1[sum(index):].find(char))
    with open("zzzzresult.txt", "a") as done:
        done.write(str(sum(index)+1))
        done.write(" ")
