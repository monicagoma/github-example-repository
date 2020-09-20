def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if len(dna1) > len(dna2):
        return True
    elif len(dna1) < len(dna2):
        return False 

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if DNA sequence is valid.

    >>> is_valid_sequence ('ATCGGC')
    True
    >>> is_valid_sequence ('aTCGGC')
    False
    """
    is_valid_sequence = False 
    for char in dna:
        if char in 'ATCG':
            return True
        if char in 'atcg':
            return False
        
def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str
    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index.

    >>> insert_sequence ('ATCG', 'GCA', 2)
    ATCGCAG
    >>> insert_sequence ('ATGGC', 'ATC', 0)
    ATCATGGC
    """
    return dna1[:index] + dna2 + dna1[index:]

def get_complement (nucleotide):
    """ (str)-> str
    Return the nucleotide's complement

    >>> get_complement ('A')
    T
    >>> get_complement ('C')
    G
    """
    if nucleotide == 'A':
       return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
def get_complementary_sequence(dna):

    '''(str) -> str
    Return the DNA sequence that is complimentary to the given
    DNA sequence.
    Precondition A complements T, C complements G
    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('TAGC')
    'ATCG'
    >>> get_complementary_sequence('ATCGA')
    'TAGCT'
    '''
    dna_complement = ''
    
    for char in dna:
        if char in 'ATCG':
            dna_complement = dna_complement + get_complement(char)
    return dna_complement
