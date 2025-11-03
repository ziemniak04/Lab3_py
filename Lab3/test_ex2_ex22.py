import pytest
from ex2 import Patient
from ex22 import Hospital

"""
Outsource:
- Claude Haiku 4.5
"""

class TestPatient:
    """Tests for Patient class from ex2.py"""
    
    def test_patient_creation_valid(self):
        """Test creating a patient with valid data"""
        patient = Patient("John Doe", "1990-05-15", "P001", "Hypertension")
        assert patient.name == "John Doe"
        assert patient.dob == "1990-05-15"
        assert patient.id == "P001"
        assert patient.diagnosis == "Hypertension"
        assert patient.admitted is False
    
    def test_patient_creation_with_admitted_true(self):
        """Test creating a patient with admitted=True"""
        patient = Patient("Jane Smith", "1985-03-20", "P002", "Asthma", admitted=True)
        assert patient.admitted is True
    
    def test_patient_admit(self):
        """Test admitting a patient"""
        patient = Patient("Anna Nowak", "2005-10-11", "P1", "Asthma")
        assert patient.admitted is False
        patient.admit()
        assert patient.admitted is True
    
    def test_patient_discharge(self):
        """Test discharging a patient"""
        patient = Patient("Jan Kowalski", "1985-09-30", "P2", "Type 1 Diabetes", admitted=True)
        assert patient.admitted is True
        patient.discharge()
        assert patient.admitted is False
    
    def test_patient_str_admitted(self):
        """Test string representation of admitted patient"""
        patient = Patient("Alice", "2000-12-02", "P3", "Type 2 Diabetes", admitted=True)
        result = str(patient)
        assert "Patient ID: P3" in result
        assert "Name: Alice" in result
        assert "Date of Birth: 2000-12-02" in result
        assert "Diagnosis: Type 2 Diabetes" in result
        assert "Status: Admitted" in result
    
    def test_patient_str_not_admitted(self):
        """Test string representation of non-admitted patient"""
        patient = Patient("Bob", "1995-07-10", "P4", "Cold")
        result = str(patient)
        assert "Patient ID: P4" in result
        assert "Name: Bob" in result
        assert "Status: Not Admitted" in result
    
    def test_patient_str_returns_string(self):
        """Test that __str__ returns a string, not a tuple"""
        patient = Patient("Test Patient", "2000-01-01", "P999", "Test Diagnosis")
        result = str(patient)
        assert isinstance(result, str)


class TestHospital:
    """Tests for Hospital class from ex22.py"""
    
    def test_hospital_creation_valid(self):
        """Test creating a hospital with valid name"""
        hospital = Hospital("City General Hospital")
        assert hospital.name == "City General Hospital"
        assert hospital.patients == []
    
    def test_hospital_creation_invalid_name(self):
        """Test creating a hospital with empty name"""
        with pytest.raises(ValueError, match="Name must be written"):
            Hospital("")
    
    def test_hospital_creation_none_name(self):
        """Test creating a hospital with None name"""
        with pytest.raises(ValueError, match="Name must be written"):
            Hospital(None)
    
    def test_add_patient(self):
        """Test adding a patient to the hospital"""
        hospital = Hospital("City General Hospital")
        patient = Patient("Anna Nowak", "2005-10-11", "P1", "Asthma")
        hospital.add_patient(patient)
        assert len(hospital.patients) == 1
        assert hospital.patients[0] == patient
    
    def test_add_multiple_patients(self):
        """Test adding multiple patients to the hospital"""
        hospital = Hospital("City General Hospital")
        p1 = Patient("Anna Nowak", "2005-10-11", "P1", "Asthma")
        p2 = Patient("Jan Kowalski", "1985-09-30", "P2", "Type 1 Diabetes")
        p3 = Patient("Alicja Mazurek", "2000-12-02", "P3", "Type 2 Diabetes")
        
        hospital.add_patient(p1)
        hospital.add_patient(p2)
        hospital.add_patient(p3)
        
        assert len(hospital.patients) == 3
        assert p1 in hospital.patients
        assert p2 in hospital.patients
        assert p3 in hospital.patients
    
    def test_discharge_patient_exists(self):
        """Test discharging a patient that exists"""
        hospital = Hospital("City General Hospital")
        patient = Patient("Anna Nowak", "2005-10-11", "P1", "Asthma")
        hospital.add_patient(patient)
        
        result = hospital.discharge_patient("P1")
        assert result == "Patient P1 is discharged."
        assert patient not in hospital.patients
    
    def test_discharge_patient_not_exists(self):
        """Test discharging a patient that doesn't exist"""
        hospital = Hospital("City General Hospital")
        result = hospital.discharge_patient("P999")
        assert result == "Patient P999 not found."
    
    def test_get_patient_list_empty(self):
        """Test getting patient list when no patients are admitted"""
        hospital = Hospital("City General Hospital")
        p1 = Patient("Anna Nowak", "2005-10-11", "P1", "Asthma")
        p2 = Patient("Jan Kowalski", "1985-09-30", "P2", "Type 1 Diabetes")
        
        hospital.add_patient(p1)
        hospital.add_patient(p2)
        
        admitted_patients = hospital.get_patient_list()
        assert admitted_patients == []
    
    def test_get_patient_list_with_admitted(self):
        """Test getting list of admitted patients"""
        hospital = Hospital("City General Hospital")
        p1 = Patient("Anna Nowak", "2005-10-11", "P1", "Asthma")
        p2 = Patient("Jan Kowalski", "1985-09-30", "P2", "Type 1 Diabetes")
        p3 = Patient("Alicja Mazurek", "2000-12-02", "P3", "Type 2 Diabetes")
        
        hospital.add_patient(p1)
        hospital.add_patient(p2)
        hospital.add_patient(p3)
        
        p1.admit()
        p3.admit()
        
        admitted_patients = hospital.get_patient_list()
        assert len(admitted_patients) == 2
        assert p1 in admitted_patients
        assert p3 in admitted_patients
        assert p2 not in admitted_patients
    
    def test_hospital_integration(self):
        """Integration test: hospital operations with patients"""
        hospital = Hospital("City General Hospital")
        
        p1 = Patient("Anna Nowak", "2005-10-11", "P1", "Asthma")
        p2 = Patient("Jan Kowalski", "1985-09-30", "P2", "Type 1 Diabetes")
        
        hospital.add_patient(p1)
        hospital.add_patient(p2)
        
        assert len(hospital.patients) == 2
        
        p1.admit()
        admitted_list = hospital.get_patient_list()
        assert len(admitted_list) == 1
        
        hospital.discharge_patient("P1")
        assert len(hospital.patients) == 1
        assert p1 not in hospital.patients
