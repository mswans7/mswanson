#First Coding Exercise for Computational Phylogenetics
#Mark Swanson

#first i defined mySeq as the sequence i'll be manipulating
mySeq = "aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg"
print "The sequence is", len(mySeq), "base pairs long"
bases = len(mySeq)
#then I replaced the t's with u's in order to convert the sequence into RNA
RNAseq = mySeq.replace('t', 'u')
print "The RNA version of this sequence is:"
print RNAseq
#I used the replace function to change each base pair to its complement. I'm not sure how to do
#this without using placeholder characters, or if I can do all the replacements at once.
#what I have is a little clunky but it works
reversecomp = RNAseq.replace('a', 't')
reversecomp = reversecomp.replace('u', 'a')
reversecomp = reversecomp.replace('g', 'x')
reversecomp = reversecomp.replace('c', 'g')
reversecomp = reversecomp.replace('x', 'c')
print "The reverse complement is:"
#This code reverses the string
reversecomp = reversecomp[::-1]
print reversecomp
#printing the 13th and 14th codons to the screen by indexing
print "The 13th codon is: ", mySeq[36:39]
print "The 14th codon is: ", mySeq[40:43]

#the following is a function for translating codons into amino acids
def sample(a):
	#the following four lines define strings for the program to refer to
	baseone = "TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG"
	basetwo = "TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG"
	basethree = "TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG"
	aas = "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG"
	#the sequences need to be made lowercase so they are compatible with mySeq
	baseone = baseone.lower()
	basetwo = basetwo.lower()
	basethree = basethree.lower()
	#the following lines find the appropriate base from mySeq in the genetic code strings
	base = baseone.find(mySeq[a])
	#n will be the location in the first line of the key where the appropriate base from the given sequence is first encountered
	n = base
	#this next line looks within that range in the second line of the key to see where the second base of the codon from the given sequence is encountered
	second = basetwo[n:n+16].find(mySeq[a+1])
	c = second
	c = c + n
	third = basethree[c:c+4].find(mySeq[a+2])
	d = third
	d = d + c
	acid = aas[d]
	return(str(acid))
#the next lines set up how many times the function needs to be executed based on the length of the given sequence
times = len(mySeq)
times = times/3
#a defines the starting point in the sequence, which is then altered by the loop
a = 0
amino = "The translated sequence is:"
for i in range(times):
	acid = sample(a)
	amino = amino + acid
	a = a + 3 
print amino
	
