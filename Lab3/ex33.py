class ProteinSequence:
    """
    Represents a protein sequence with methods for manipulation and analysis.
    
    Protein sequences consist of amino acids represented by single-letter codes
    (A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y) plus '*' for stop codon.
    
    Attributes:
        valid_chars (set): Set of valid amino acid characters
        identifier (str): Unique identifier for the protein sequence
        data (str): The protein sequence data in uppercase
    
    Raises:
        ValueError: If the sequence contains invalid amino acid characters
    
    Outsource:
    - docstrings
    """
    valid_chars = set("ACDEFGHIKLMNPQRSTVWY*")

    def __init__(self, identifier: str, data: str):
        """
        Initialize a protein sequence.
        
        Args:
            identifier (str): Unique identifier for the sequence
            data (str): Protein sequence string (case-insensitive, will be converted to uppercase)
        
        Raises:
            ValueError: If data contains invalid amino acid characters
        
        Outsource:
        - docstrings
        """
        self.identifier = identifier
        self.data = data.upper()
        invalid_chars = set(self.data) - self.valid_chars
        if invalid_chars:
            raise ValueError(f"Invalid protein sequence — contains: {invalid_chars}")

    def __len__(self):
        """
        Return the length of the protein sequence.
        
        Returns:
            int: Number of amino acids in the sequence
        
        Outsource:
        - docstrings
        """
        return len(self.data)

    def __str__(self):
        """
        Return a formatted string representation of the protein sequence.
        
        Returns:
            str: Sequence in FASTA format (identifier on first line, sequence on second line)
        
        Outsource:
        - docstrings
        """
        return f">{self.identifier}\n{self.data}"

    def mutate(self, position: int, value: str):
        """
        Replace an amino acid at a specific position with a new residue.
        
        Args:
            position (int): 0-based index of the amino acid to replace
            value (str): New amino acid (single-letter code, case-insensitive)
        
        Raises:
            ValueError: If value is not a valid amino acid character
            IndexError: If position is out of range
        
        Outsource:
        - docstrings
        - lines: 83, 85, 86
        """
        if value.upper() not in self.valid_chars:
            raise ValueError("Invalid amino acid.")
        if not (0 <= position < len(self.data)):
            raise IndexError("Position out of range.")
        before = self.data[:position]
        after = self.data[position + 1:]
        new_residue = value.upper()
        self.data = before + new_residue + after

    def find_motif(self, motif: str):
        """
        Find all occurrences of a motif sequence within the protein sequence.
        
        Args:
            motif (str): Amino acid pattern to search for (case-insensitive)
        
        Returns:
            list: List of 0-based positions where the motif starts, empty list if not found
        
        Outsource:
        - docstrings
        - lines: 108, 110
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
