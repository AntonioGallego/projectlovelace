Amino2RNA = {
	"Ala":["GCU","GCC","GCA","GCG"],
	"Ile":["AUU","AUC","AUA"],
	"Arg":["CGU","CGC","CGA","CGG","AGA","AGG"],
	"Leu":["CUU","CUC","CUA","CUG","UUA","UUG"],
	"Asn":["AAU","AAC"],
	"Lys":["AAA","AAG"],
	"Asp":["GAU","GAC"],
	"Met":["AUG"],
	"Asn":["AAU","AAC","GAU","GAC"],
	"Phe":["UUU","UUC"],
	"Cys":["UGU","UGC"],
	"Pro":["CCU","CCC","CCA","CCG"],
	"Gln":["CAA","CAG"],
	"Ser":["UCU","UCC","UCA","UCG","AGU","AGC"],
	"Glu":["GAA","GAG"],
	"Thr":["ACU","ACC","ACA","ACG"],
	"Gln":["CAA","CAG","GAA","GAG"],
	"Trp":["UGG"],
	"Gly":["GGU","GGC","GGA","GGG"],
	"Tyr":["UAU","UAC"],
	"His":["CAU","CAC"],
	"Val":["GUU","GUC","GUA","GUG"],
	"STOP":["UAA","UGA","UAG"]
}

RNA2Amino={}
for amino in Amino2RNA:
	codons=Amino2RNA[amino]
	for codon in codons:
		RNA2Amino[codon]=amino

def amino_acid_sequence(RNASequence):
    amino_acids=""
    SPLASH="""
-. .-.   .-. .-.   .-. .-.   .
  \   \ /   \   \ /   \   \ /
 / \   \   / \   \   / \   \\
~   `-~ `-`   `-~ `-`   `-~ `-"""
    print(SPLASH)
    print("[+] Target RNA sequence ",RNASequence)
    for elem in range(0, len(RNASequence), 3):
        codon=RNASequence[elem:elem + 3]
        print("[+] Assembling codon",codon)
        amino=RNA2Amino[codon]
        if amino=="STOP":
            return amino_acids
        amino_acids+=amino
    return amino_acids


print(amino_acid_sequence("CCU"))
#Output: Pro

print(amino_acid_sequence("AUGCCAAAGGGUUGA"))
#Output: "MetProLysGly"

print(amino_acid_sequence("GCAAGAGAUAAUUGU"))
#Output: AlaArgAspAsnCys
