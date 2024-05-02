#DNA      = DeoxyriboNucleic Acid
#Function = Long term storage for genetic information; transmission of genetic information to make other cells and new organisms. 
#Structure= B-form double helix. DNA is a double-stranded molecule consisting of a long chain of nucleotides.

#RNA      = RiboNucleic Acid
#Function = Used to transfer the genetic code from the nucleus to the ribosomes to make proteins. RNA is used to transmit genetic information in some organisms and may have been the molecule used to store genetic blueprints in primitive organisms.
#Structure= A-form helix. RNA usually is a single-strand helix consisting of shorter chains of nucleotides.
#mRNA     = Messenger RNA will sent a message based of the DNA takes message to ribosomes
#rRNA     = Ribosomal RNA Ribosomes make protien
#tRNA     = Transfer RNA matches the correct mRNA codon

#DNA to RNA transcription
#G --> C

#C --> G

#T --> A

#A --> U
A = 'Adenine'
U = 'Uracil'
G = 'Guanine'
C = 'Cylosine'
T = 'Thymine'
Cy= 'Cytosine'

print("When the transcrpition happens from DNA to RNA the " + A + " turns into " + U + ". " + G + " turns into " + C + "and vice versa. " +  T + " turns into " + A + ". " )

dna = input("Please input the dna strand that you would like to transcribe ")
rna = ""

for i in dna:
    if i not in "ATGC":
        rna= "invalid input"
        break
    if i == 'A':
        rna +='U'
    elif i == 'C':
        rna += 'G'
    elif i == 'T':
        rna += 'A'
    else:
        rna += 'C'

print(rna)