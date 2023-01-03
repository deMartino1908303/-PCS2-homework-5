from Bio import SeqIO

dna_strings = [seq for seq in SeqIO.parse("rosalind_grph.txt", "fasta")]

for fasta1 in dna_strings:
    
    seq1 = fasta1.seq
    
    for fasta2 in dna_strings:
        
        seq2 = fasta2.seq
        
        if seq1 == seq2 : continue
        
        if seq1[-3:] == seq2[:3]:
            
            new_edge = [fasta1.id, fasta2.id]
        
            print(" ".join(new_edge))
