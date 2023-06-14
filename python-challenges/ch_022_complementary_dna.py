'''
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)
"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
'''


def DNA_strand(dna):
    # maketrans() creates a translation table, mapping each letter to be replaced by its corresponding substitute.
    mapping = dna.maketrans('ATCG', 'TAGC')
    # translate() apply the mapping.
    complementary_side = dna.translate(mapping)
    return complementary_side


print(DNA_strand('AAAA') == 'TTTT')
print(DNA_strand('ATTGC') == 'TAACG')
print(DNA_strand('GTAT') == 'CATA')
