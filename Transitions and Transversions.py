from data_reader import fasta_reader

sequence = fasta_reader("rosalind_tran.txt")
seq1 = sequence[0]
seq2 = sequence[1]
counter = 0
T_sition = 0 #same type
T_version = 0 #diffrent type
while counter < len(seq1):
    if seq1[counter] == seq2[counter] :
        counter += 1
        continue
    
    base_1 = seq1[counter]
    base_2 = seq2[counter]
    if base_1 == "A" and base_2 == "G" : T_sition += 1
    elif base_1 == "G" and base_2 == "A" : T_sition += 1
    elif base_1 == "C" and base_2 == "T" : T_sition += 1
    elif base_1 == "T" and base_2 == "C" : T_sition += 1
    else : T_version += 1
    counter += 1
    #print ("-")

print(T_sition/T_version)
