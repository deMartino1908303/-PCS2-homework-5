import re
from data_reader import read_data
import urllib.request

data = read_data("rosalind_mprt.txt").split("\n")
pattern = re.compile(r'(?=(N[^P][ST][^P]))')
for protein_name in data :
    if "_" in protein_name:
        index = protein_name.index("_")
    else:
        index = 6
        
    url = "http://www.uniprot.org/uniprot/{}.fasta".format(protein_name[:index])
    with urllib.request.urlopen(url) as response:
        protein_code = str(response.read().decode("utf-8", "ignore"))
    
    protein_code = protein_code[protein_code.find("SV=")+4:].replace("\n","")
    
    if not protein_code.isalnum() : continue
    
    while not protein_code.isalpha():
        if protein_code == "": break
        protein_code = protein_code[1:]

        
    motifs = []
    
    for match in re.finditer(pattern, protein_code):
        motifs.append(match.start() + 1)
    
    if " ".join(map(str, motifs)) != "" :
        print(protein_name)
        print(" ".join(map(str, motifs)))
