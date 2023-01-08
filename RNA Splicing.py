from Bio.Seq import Seq
from data_reader import fasta_reader

def remove_introns(dna, introns):
    for intron in introns:
        dna = dna.replace(intron, "")
    return dna

def transcribe_and_translate(dna):
    rna = dna.replace("T", "U")
    protein = Seq(rna).translate(stop_symbol="")
    return protein

dna = fasta_reader("rosalind_splc.txt")
introns = []

clean_dna = remove_introns(dna[0], dna[1:])
protein = transcribe_and_translate(clean_dna)
print(protein)
