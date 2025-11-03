from ex32 import RNASequence


class DNASequence:
    """
    Represents a DNA sequence with methods for manipulation and analysis.
    
    DNA sequences contain four nucleotide bases: A (Adenine), T (Thymine),
    G (Guanine), and C (Cytosine).
    
    Attributes:
        valid_chars (set): Set of valid DNA nucleotide bases {'A', 'T', 'G', 'C'}
        identifier (str): Unique identifier for the DNA sequence
        data (str): The DNA sequence data in uppercase
    
    Raises:
        ValueError: If the sequence contains invalid characters not in valid_chars
    
    Outsource:
    - docstrings
    """
    valid_chars = {'A', 'T', 'G', 'C'}

    def __init__(self, identifier: str, data: str):
        """
        Initialize a DNA sequence.
        
        Args:
            identifier (str): Unique identifier for the sequence
            data (str): DNA sequence string (case-insensitive, will be converted to uppercase)
        
        Raises:
            ValueError: If data contains characters other than A, T, G, C

        Outsource:
        - docstrings
        """
        self.identifier = identifier
        self.data = data.upper()
        if not all(char in self.valid_chars for char in self.data):
            raise ValueError("DNA sequence can only contain A, T, G, C characters.")
        
    def __len__(self):
        """
        Return the length of the DNA sequence.
        
        Returns:
            int: Number of nucleotides in the sequence

        Outsource:
        - docstrings
        """
        return len(self.data)

    def __str__(self):
        """
        Return a formatted string representation of the DNA sequence.
        
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
            value (str): New base (A, T, G, or C - case-insensitive)
        
        Raises:
            ValueError: If value is not a valid DNA base
            IndexError: If position is out of range
        
        Outsource:
        - docstrings
        - lines: 85, 87, 88
        """
        if value.upper() not in self.valid_chars:
            raise ValueError("Invalid base for mutation, must be one of A, T, G, C.")
        if not (0 <= position < len(self.data)):
            raise IndexError("Position out of range, my gene")
        before = self.data[:position]       
        after = self.data[position + 1:]    
        new_base = value.upper()            
        self.data = before + new_base + after

    def find_motif(self, motif: str):
        """
        Find all occurrences of a motif sequence within the DNA sequence.
        
        Args:
            motif (str): Sequence pattern to search for (case-insensitive)
        
        Returns:
            list: List of 0-based positions where the motif starts, empty list if not found
        
        Outsource:
        - docstrings
        - lines: 112, 113
        """
        motif = motif.upper()
        positions = []                                
        seq_length = len(self.data)
        motif_length = len(motif)
        search_limit = seq_length - motif_length + 1

        for i in range(search_limit):
            fragment = self.data[i:i + motif_length]
            if fragment == motif:
                positions.append(i)

        return positions
    
    def complement(self):
        """
        Generate the complementary DNA strand.
        
        Complement base pairing rules for DNA:
        - A pairs with T
        - T pairs with A
        - G pairs with C
        - C pairs with G
        
        Returns:
            DNASequence: New DNASequence object with complementary bases and "_comp" suffix in identifier
        
        Outsource:
        - docstrings
        - lines: 138, 139
        """
        bases = "ATGC"
        complements = "TACG"
        comp_map = str.maketrans(bases, complements)
        comp_data = self.data.translate(comp_map)
        new_identifier = self.identifier + "_comp"
        complementary_seq = DNASequence(new_identifier, comp_data)

        return complementary_seq


    def transcribe(self):
        """
        Transcribe DNA to RNA by replacing thymine (T) with uracil (U).
        
        This represents the biological process of transcription where DNA is converted
        to RNA with U replacing T.
        
        Returns:
            RNASequence: New RNASequence object with T replaced by U and "_RNA" suffix in identifier
        
        Outsource:
        - docstrings
        """
        dna_data = self.data
        rna_data = dna_data.replace("T", "U")
        new_identifier = self.identifier + "_RNA"
        rna_seq = RNASequence(new_identifier, rna_data)

        return rna_seq
