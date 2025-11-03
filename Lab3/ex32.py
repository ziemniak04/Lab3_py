from ex33 import ProteinSequence


class RNASequence:
    """
    Represents an RNA sequence with methods for manipulation and analysis.
    
    RNA sequences contain four nucleotide bases: A (Adenine), U (Uracil), 
    G (Guanine), and C (Cytosine).
    
    Attributes:
        valid_chars (set): Set of valid RNA nucleotide bases {'A', 'U', 'G', 'C'}
        identifier (str): Unique identifier for the RNA sequence
        data (str): The RNA sequence data in uppercase
    
    Raises:
        ValueError: If the sequence contains invalid characters not in valid_chars
    
    Outsource:
    - docstrings
    """
    valid_chars = {'A', 'U', 'G', 'C'}

    def __init__(self, identifier: str, data: str):
        """
        Initialize an RNA sequence.
        
        Args:
            identifier (str): Unique identifier for the sequence
            data (str): RNA sequence string (case-insensitive, will be converted to uppercase)
        
        Raises:
            ValueError: If data contains characters other than A, U, G, C
        
        Outsource:
        - docstrings
        """
        self.identifier = identifier
        self.data = data.upper()
        invalid_chars = set(self.data) - self.valid_chars
        if invalid_chars:
            raise ValueError(f"Invalid RNA sequence — contains: {invalid_chars}")

    def __len__(self):
        """
        Return the length of the RNA sequence.
        
        Returns:
            int: Number of nucleotides in the sequence

        Outsource:
        - docstrings
        """
        return len(self.data)

    def __str__(self):
        """
        Return a formatted string representation of the RNA sequence.
        
        Returns:
            str: Sequence in FASTA format (identifier on first line, sequence on second line)
        
        Outsource:
        - docstrings
        """
        return f">{self.identifier}\n{self.data}"

    def mutate(self, position: int, value: str):
        """
        Replace a nucleotide at a specific position with a new base.
        
        Args:
            position (int): 0-based index of the nucleotide to replace
            value (str): New base (A, U, G, or C - case-insensitive)
        
        Raises:
            ValueError: If value is not a valid RNA base
            IndexError: If position is out of range
        
        Outsource:
        - docstrings
        - lines: 86, 88,89
        """
        if value.upper() not in self.valid_chars:
            raise ValueError("Invalid base — must be one of A, U, G, C.")
        if not (0 <= position < len(self.data)):
            raise IndexError("Position out of range.")
        before = self.data[:position]
        after = self.data[position + 1:]
        new_base = value.upper()
        self.data = before + new_base + after

    def find_motif(self, motif: str):
        """
        Find all occurrences of a motif sequence within the RNA sequence.
        
        Args:
            motif (str): Sequence pattern to search for (case-insensitive)
        
        Returns:
            list: List of 0-based positions where the motif starts, empty list if not found
        
        Outsource:
        - docstrings
        - lines: 111-113
        """
        positions = []
        seq_length = len(self.data)
        motif = motif.upper()
        motif_length = len(motif)
        search_limit = seq_length - motif_length + 1
        for i in range(search_limit):
            fragment = self.data[i:i + motif_length]
            if fragment == motif:
                positions.append(i)
        return positions

    def complement(self):
        """
        Generate the complementary RNA sequence.
        
        Complement base pairing rules:
        - A pairs with U
        - U pairs with A
        - G pairs with C
        - C pairs with G
        
        Returns:
            RNASequence: New RNASequence object with complementary bases and "_comp" suffix in identifier
        
        Outsource:
        - docstrings
        - lines: 137, 138
        """
        bases = "AUGC"
        complements = "UACG"
        comp_map = str.maketrans(bases, complements)
        comp_data = self.data.translate(comp_map)
        new_identifier = self.identifier + "_comp"
        complementary_seq = RNASequence(new_identifier, comp_data)

        return complementary_seq

    def translate(self):
        """
        Translate the RNA sequence into a protein sequence using the genetic code.
        
        The translation starts at AUG (start codon) and continues until a stop codon
        (UAA, UAG, UGA) is encountered. Codons are read in triplets (3 nucleotides).
        
        Returns:
            ProteinSequence: New protein sequence with amino acids and "_PROT" suffix in identifier
        
        Note:
            - Only partial codon table is implemented (common codons)
            - Unknown codons are represented as '?'
            - Translation stops at stop codon
        
        Outsource:
        - docstrings
        - lines: codon_table (whole), for i in range... if amino_acid == '*': break
        """
        codon_table = {
            'AUG': 'M',
            'UUU': 'F', 'UUC': 'F',
            'UUA': 'L', 'UUG': 'L',
            'UAA': '*', 'UAG': '*', 'UGA': '*',
            'UGG': 'W', 'GCC': 'A', 'GAA': 'E', 'UAC': 'Y', 'UGC': 'C'
        }
        protein = ""
        seq_length = len(self.data)
        for i in range(0, seq_length - 2, 3):
            codon = self.data[i:i + 3]
            amino_acid = codon_table.get(codon, '?')
            if amino_acid == '*':
                break
            protein += amino_acid
        new_identifier = self.identifier + "_PROT"
        return ProteinSequence(new_identifier, protein)
