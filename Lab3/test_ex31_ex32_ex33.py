import pytest
from ex31 import DNASequence
from ex32 import RNASequence
from ex33 import ProteinSequence

"""
Outsource:
- Claude Haiku 4.5
"""

class TestDNASequence:
    """Tests for DNASequence class from ex31.py"""
    
    def test_dna_creation_valid(self):
        """Test creating a DNA sequence with valid bases"""
        dna = DNASequence("dna1", "ATGCATGC")
        assert dna.identifier == "dna1"
        assert dna.data == "ATGCATGC"
    
    def test_dna_creation_lowercase(self):
        """Test creating a DNA sequence converts lowercase to uppercase"""
        dna = DNASequence("dna1", "atgcatgc")
        assert dna.data == "ATGCATGC"
    
    def test_dna_creation_invalid_chars(self):
        """Test creating a DNA sequence with invalid characters"""
        with pytest.raises(ValueError, match="DNA sequence can only contain A, T, G, C characters"):
            DNASequence("dna1", "AUGC")
    
    def test_dna_len(self):
        """Test DNA sequence length"""
        dna = DNASequence("dna1", "ATGC")
        assert len(dna) == 4
    
    def test_dna_str(self):
        """Test DNA string representation in FASTA format"""
        dna = DNASequence("dna1", "ATGC")
        result = str(dna)
        assert ">dna1" in result
        assert "ATGC" in result
    
    def test_dna_mutate_valid(self):
        """Test mutating a DNA base"""
        dna = DNASequence("dna1", "ATGC")
        dna.mutate(0, "C")
        assert dna.data == "CTGC"
    
    def test_dna_mutate_invalid_base(self):
        """Test mutating with invalid base"""
        dna = DNASequence("dna1", "ATGC")
        with pytest.raises(ValueError, match="Invalid base for mutation"):
            dna.mutate(0, "U")
    
    def test_dna_mutate_out_of_range(self):
        """Test mutating at out of range position"""
        dna = DNASequence("dna1", "ATGC")
        with pytest.raises(IndexError):
            dna.mutate(10, "A")
    
    def test_dna_find_motif_single(self):
        """Test finding a motif in DNA sequence"""
        dna = DNASequence("dna1", "ATGCATGC")
        positions = dna.find_motif("ATG")
        assert positions == [0, 4]
    
    def test_dna_find_motif_not_found(self):
        """Test finding a motif that doesn't exist"""
        dna = DNASequence("dna1", "AAAA")
        positions = dna.find_motif("GGG")
        assert positions == []
    
    def test_dna_find_motif_case_insensitive(self):
        """Test that motif search is case-insensitive"""
        dna = DNASequence("dna1", "ATGCATGC")
        positions = dna.find_motif("atg")
        assert positions == [0, 4]
    
    def test_dna_complement(self):
        """Test DNA complement strand generation"""
        dna = DNASequence("dna1", "ATG")
        comp = dna.complement()
        assert comp.identifier == "dna1_comp"
        assert comp.data == "TAC"
    
    def test_dna_complement_all_bases(self):
        """Test complement for all bases"""
        dna = DNASequence("dna1", "ATGC")
        comp = dna.complement()
        assert comp.data == "TACG"
    
    def test_dna_transcribe(self):
        """Test DNA to RNA transcription"""
        dna = DNASequence("dna1", "ATGC")
        rna = dna.transcribe()
        assert isinstance(rna, RNASequence)
        assert rna.identifier == "dna1_RNA"
        assert rna.data == "AUGC"
    
    def test_dna_transcribe_multiple_t(self):
        """Test RNA transcription replaces all T with U"""
        dna = DNASequence("dna1", "TTTTAAAA")
        rna = dna.transcribe()
        assert rna.data == "UUUUAAAA"


class TestRNASequence:
    """Tests for RNASequence class from ex32.py"""
    
    def test_rna_creation_valid(self):
        """Test creating an RNA sequence with valid bases"""
        rna = RNASequence("rna1", "AUGCAUGC")
        assert rna.identifier == "rna1"
        assert rna.data == "AUGCAUGC"
    
    def test_rna_creation_lowercase(self):
        """Test creating an RNA sequence converts lowercase to uppercase"""
        rna = RNASequence("rna1", "augcaugc")
        assert rna.data == "AUGCAUGC"
    
    def test_rna_creation_invalid_chars(self):
        """Test creating an RNA sequence with invalid characters"""
        with pytest.raises(ValueError, match="Invalid RNA sequence"):
            RNASequence("rna1", "ATGC")
    
    def test_rna_len(self):
        """Test RNA sequence length"""
        rna = RNASequence("rna1", "AUG")
        assert len(rna) == 3
    
    def test_rna_str(self):
        """Test RNA string representation in FASTA format"""
        rna = RNASequence("rna1", "AUG")
        result = str(rna)
        assert ">rna1" in result
        assert "AUG" in result
    
    def test_rna_mutate_valid(self):
        """Test mutating an RNA base"""
        rna = RNASequence("rna1", "AUGC")
        rna.mutate(0, "C")
        assert rna.data == "CUGC"
    
    def test_rna_mutate_invalid_base(self):
        """Test mutating with invalid base"""
        rna = RNASequence("rna1", "AUGC")
        with pytest.raises(ValueError, match="Invalid base"):
            rna.mutate(0, "T")
    
    def test_rna_mutate_out_of_range(self):
        """Test mutating at out of range position"""
        rna = RNASequence("rna1", "AUGC")
        with pytest.raises(IndexError):
            rna.mutate(10, "A")
    
    def test_rna_find_motif_single(self):
        """Test finding a motif in RNA sequence"""
        rna = RNASequence("rna1", "AUGCAUGC")
        positions = rna.find_motif("AUG")
        assert positions == [0, 4]
    
    def test_rna_find_motif_not_found(self):
        """Test finding a motif that doesn't exist"""
        rna = RNASequence("rna1", "AAAA")
        positions = rna.find_motif("UUU")
        assert positions == []
    
    def test_rna_find_motif_case_insensitive(self):
        """Test that motif search is case-insensitive"""
        rna = RNASequence("rna1", "AUGCAUGC")
        positions = rna.find_motif("aug")
        assert positions == [0, 4]
    
    def test_rna_complement(self):
        """Test RNA complement strand generation"""
        rna = RNASequence("rna1", "AUG")
        comp = rna.complement()
        assert comp.identifier == "rna1_comp"
        assert comp.data == "UAC"
    
    def test_rna_complement_all_bases(self):
        """Test RNA complement for all bases"""
        rna = RNASequence("rna1", "AUGC")
        comp = rna.complement()
        assert comp.data == "UACG"
    
    def test_rna_translate_start_codon(self):
        """Test RNA translation with start codon"""
        rna = RNASequence("rna1", "AUG")
        protein = rna.translate()
        assert isinstance(protein, ProteinSequence)
        assert protein.identifier == "rna1_PROT"
        assert protein.data == "M"
    
    def test_rna_translate_with_stop_codon(self):
        """Test RNA translation stops at stop codon"""
        rna = RNASequence("rna1", "AUGUAA")
        protein = rna.translate()
        assert protein.data == "M"
    
    def test_rna_translate_multiple_codons(self):
        """Test RNA translation with multiple codons"""
        rna = RNASequence("rna1", "AUGGCCGAA")
        protein = rna.translate()
        assert "M" in protein.data
        assert "A" in protein.data
        assert "E" in protein.data


class TestProteinSequence:
    """Tests for ProteinSequence class from ex33.py"""
    
    def test_protein_creation_valid(self):
        """Test creating a protein sequence with valid amino acids"""
        protein = ProteinSequence("prot1", "MKLLVV")
        assert protein.identifier == "prot1"
        assert protein.data == "MKLLVV"
    
    def test_protein_creation_lowercase(self):
        """Test creating a protein sequence converts lowercase to uppercase"""
        protein = ProteinSequence("prot1", "mkllvv")
        assert protein.data == "MKLLVV"
    
    def test_protein_creation_invalid_chars(self):
        """Test creating a protein sequence with invalid characters"""
        with pytest.raises(ValueError, match="Invalid protein sequence"):
            ProteinSequence("prot1", "XYZ")
    
    def test_protein_creation_with_stop_codon(self):
        """Test creating a protein sequence with stop codon"""
        protein = ProteinSequence("prot1", "MKL*")
        assert protein.data == "MKL*"
    
    def test_protein_len(self):
        """Test protein sequence length"""
        protein = ProteinSequence("prot1", "MKLLVV")
        assert len(protein) == 6
    
    def test_protein_str(self):
        """Test protein string representation in FASTA format"""
        protein = ProteinSequence("prot1", "MKLLVV")
        result = str(protein)
        assert ">prot1" in result
        assert "MKLLVV" in result
    
    def test_protein_mutate_valid(self):
        """Test mutating an amino acid"""
        protein = ProteinSequence("prot1", "MKLLVV")
        protein.mutate(0, "A")
        assert protein.data == "AKLLVV"
    
    def test_protein_mutate_invalid_aa(self):
        """Test mutating with invalid amino acid"""
        protein = ProteinSequence("prot1", "MKLLVV")
        with pytest.raises(ValueError, match="Invalid amino acid"):
            protein.mutate(0, "X")
    
    def test_protein_mutate_out_of_range(self):
        """Test mutating at out of range position"""
        protein = ProteinSequence("prot1", "MKLLVV")
        with pytest.raises(IndexError):
            protein.mutate(10, "A")
    
    def test_protein_find_motif_single(self):
        """Test finding a motif in protein sequence"""
        protein = ProteinSequence("prot1", "MKLLVVMKLL")
        positions = protein.find_motif("MKL")
        assert positions == [0, 6]
    
    def test_protein_find_motif_not_found(self):
        """Test finding a motif that doesn't exist"""
        protein = ProteinSequence("prot1", "AAAA")
        positions = protein.find_motif("GGG")
        assert positions == []
    
    def test_protein_find_motif_case_insensitive(self):
        """Test that motif search is case-insensitive"""
        protein = ProteinSequence("prot1", "MKLLVVMKLL")
        positions = protein.find_motif("mkl")
        assert positions == [0, 6]
    
    def test_protein_find_motif_single_occurrence(self):
        """Test finding motif with single occurrence"""
        protein = ProteinSequence("prot1", "MKLLVV")
        positions = protein.find_motif("LLV")
        assert positions == [2]


class TestIntegration:
    """Integration tests across DNA, RNA, and Protein sequences"""
    
    def test_dna_to_rna_transcription(self):
        """Test converting DNA to RNA through transcription"""
        dna = DNASequence("gene1", "ATGAAATAG")
        rna = dna.transcribe()
        assert rna.data == "AUGAAAUAG"
    
    def test_rna_to_protein_translation(self):
        """Test converting RNA to protein through translation"""
        rna = RNASequence("rna1", "AUGUAA")
        protein = rna.translate()
        assert len(protein.data) > 0
    
    def test_dna_complement_then_transcribe(self):
        """Test getting complement DNA and then transcribing"""
        dna = DNASequence("dna1", "ATGC")
        comp = dna.complement()
        rna = comp.transcribe()
        assert rna.data == "UACG"
    
    def test_sequence_length_consistency(self):
        """Test that sequence lengths are consistent"""
        dna = DNASequence("dna1", "ATGCATGC")
        rna = dna.transcribe()
        assert len(dna) == len(rna)
    
    def test_motif_finding_across_sequences(self):
        """Test finding motifs in different sequence types"""
        dna = DNASequence("dna1", "ATGATGATG")
        positions_dna = dna.find_motif("ATG")
        
        rna = RNASequence("rna1", "UGUGUGU")
        positions_rna = rna.find_motif("UGU")
        
        assert len(positions_dna) == 3
        assert len(positions_rna) == 3
