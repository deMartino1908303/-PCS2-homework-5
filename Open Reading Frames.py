from Bio import SeqIO

def reding_frame(amminoacid_sequence):
    AA = str(amminoacid_sequence).split("*")
    possible_protein = []

    AA.pop(-1)
    for seq in AA :
        indices = []
        index = seq.find("M")
        while index != -1:
            indices.append(index)
            index = seq.find("M", index + 1)
            
        for index in indices :
            possible_protein.append(seq[index:])
    
    return possible_protein
            
        


    
    
ff = SeqIO.read("rosalind_orf.txt", "fasta").seq

ammino_acid_list = [ff.translate(table="Standard", stop_symbol="*"),\
                    ff.reverse_complement().translate(table="Standard", stop_symbol="*"),\
                    ff[1:len(ff)-2].translate(table="Standard", stop_symbol="*"),\
                    ff[1:len(ff)-2].reverse_complement().translate(table="Standard", stop_symbol="*"),\
                    ff[2:len(ff)-1].translate(table="Standard", stop_symbol="*"),\
                    ff[2:len(ff)-1].reverse_complement().translate(table="Standard", stop_symbol="*"),]
orf = []
for a_a in ammino_acid_list :
    tmp = reding_frame(a_a)
    #print("--------------", tmp)
    if len(tmp) > 1 :
        for item in tmp:
            if item and item not in orf:
                orf.append(item)
    else :
        if tmp and tmp not in orf:
            orf.append(tmp)
#print(orf)
print("\n".join(orf))
