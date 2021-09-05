
# Import files and remove spaces

def import_seq(inputfile):
    with open(inputfile, "r") as f:
        seq = f.read()
    seq = seq.replace("/n", "")
    seq = seq.replace("\n", "")
    seq = seq.replace("/r", "")
    return seq

def translate_dna(seq):

    #Translation dictionary

    table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

    protein = ""

    #Check if is it possible to translate(can be divided by 3)

    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i : i+3]
            protein += table[codon]
    else:
        print("Invalid Sequence")

    return protein

protein = import_seq("protein.txt")
dna = import_seq("dna.txt")
translated_dna = translate_dna(dna[20:935]) #The slice is based on where in the DNA is that specific protein sequence 

#Compare already translated protein sequence with one this translator produced. Can be removed. 

if translated_dna == protein:
    print("Sucess")

